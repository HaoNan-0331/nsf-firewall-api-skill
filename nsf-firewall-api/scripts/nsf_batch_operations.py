#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
绿盟NF防火墙批量操作脚本
支持从JSON或YAML文件读取批量操作请求
"""

import json
import sys
import argparse
from pathlib import Path
from typing import List, Dict

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

from nsf_api_client import NSFApiClient


def load_batch_file(file_path: str) -> List[Dict]:
    """
    从文件加载批量操作

    支持的格式:
    - JSON: .json
    - YAML: .yaml, .yml (需要PyYAML)
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {file_path}")

    suffix = path.suffix.lower()

    if suffix == '.json':
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif suffix in ['.yaml', '.yml']:
        if not YAML_AVAILABLE:
            raise ImportError("YAML支持需要安装PyYAML: pip install pyyaml")
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    else:
        raise ValueError(f"不支持的文件格式: {suffix}")


def main():
    parser = argparse.ArgumentParser(
        description='绿盟NF防火墙批量操作工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 从JSON文件执行批量操作
  python nsf_batch_operations.py https://192.168.1.1 YOUR_TOKEN batch_ops.json

  # 从YAML文件执行批量操作
  python nsf_batch_operations.py https://192.168.1.1 YOUR_TOKEN batch_ops.yaml

批量操作文件格式 (JSON):
[
  {
    "method": "POST",
    "endpoint": "/route/static/routes",
    "data": {
      "destination": "192.168.100.0/24",
      "gateway": "192.168.1.254",
      "interface": "eth1"
    }
  },
  {
    "method": "GET",
    "endpoint": "/interface/interfaces"
  }
]

批量操作文件格式 (YAML):
- method: POST
  endpoint: /policy/acl/policies
  data:
    name: "允许内网访问"
    source: "192.168.1.0/24"
    destination: "any"
    service: "any"
    action: "accept"

- method: GET
  endpoint: /policy/acl/policies
        '''
    )

    parser.add_argument('host', help='防火墙地址 (如: https://192.168.1.1)')
    parser.add_argument('token', help='认证Token')
    parser.add_argument('file', help='批量操作文件路径 (.json/.yaml/.yml)')
    parser.add_argument('--verify-ssl', action='store_true', help='验证SSL证书')

    args = parser.parse_args()

    # 加载批量操作文件
    try:
        requests_list = load_batch_file(args.file)
    except Exception as e:
        print(f"错误: 无法加载批量操作文件: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(requests_list, list):
        print("错误: 批量操作文件必须包含一个操作列表", file=sys.stderr)
        sys.exit(1)

    print(f"加载了 {len(requests_list)} 个操作")
    print()

    # 创建客户端并执行批量操作
    client = NSFApiClient(
        host=args.host,
        token=args.token,
        verify_ssl=args.verify_ssl
    )

    results = client.batch_request(requests_list)

    # 输出结果
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
