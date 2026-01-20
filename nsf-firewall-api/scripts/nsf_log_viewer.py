#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
绿盟NF防火墙操作日志查看工具
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime


def load_logs(log_dir: str, date: str = None) -> list:
    """
    加载日志文件

    Args:
        log_dir: 日志目录路径
        date: 日期字符串 (YYYYMMDD)，默认为今天
    """
    log_path = Path(log_dir)

    if date is None:
        date = datetime.now().strftime("%Y%m%d")

    log_file = log_path / f'api_log_{date}.json'

    if not log_file.exists():
        return []

    logs = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                logs.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue

    return logs


def filter_logs(logs: list, **filters) -> list:
    """根据条件过滤日志"""
    filtered = logs

    if 'method' in filters:
        filtered = [log for log in filtered if log['method'] == filters['method']]

    if 'endpoint' in filters:
        filtered = [log for log in filtered if filters['endpoint'] in log['endpoint']]

    if 'success' in filters:
        is_success = filters['success']
        filtered = [
            log for log in filtered
            if ('error' not in log.get('response', {})) == is_success
        ]

    if 'start_time' in filters:
        filtered = [
            log for log in filtered
            if log['timestamp'] >= filters['start_time']
        ]

    if 'end_time' in filters:
        filtered = [
            log for log in filtered
            if log['timestamp'] <= filters['end_time']
        ]

    return filtered


def main():
    parser = argparse.ArgumentParser(
        description='绿盟NF防火墙操作日志查看工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 查看今天的所有日志
  python nsf_log_viewer.py

  # 查看指定日期的日志
  python nsf_log_viewer.py --date 20250118

  # 只查看失败的请求
  python nsf_log_viewer.py --failed-only

  # 只看POST请求
  python nsf_log_viewer.py --method POST

  # 查看特定端点的请求
  python nsf_log_viewer.py --endpoint /policy/acl/policies

  # 统计请求类型
  python nsf_log_viewer.py --stats

  # 导出为CSV
  python nsf_log_viewer.py --export operations.csv
        '''
    )

    parser.add_argument('--log-dir', default='./logs',
                        help='日志目录路径 (默认: ./logs)')
    parser.add_argument('--date', help='日期 (YYYYMMDD格式，默认为今天)')
    parser.add_argument('--method', help='过滤HTTP方法 (GET/POST/PUT/DELETE)')
    parser.add_argument('--endpoint', help='过滤端点 (支持部分匹配)')
    parser.add_argument('--success-only', action='store_true',
                        help='只显示成功的请求')
    parser.add_argument('--failed-only', action='store_true',
                        help='只显示失败的请求')
    parser.add_argument('--stats', action='store_true',
                        help='显示统计信息')
    parser.add_argument('--export', help='导出为CSV文件')
    parser.add_argument('--limit', type=int, help='限制输出条数')

    args = parser.parse_args()

    # 加载日志
    logs = load_logs(args.log_dir, args.date)

    if not logs:
        print("没有找到日志记录")
        return

    # 过滤日志
    filters = {}
    if args.method:
        filters['method'] = args.method.upper()
    if args.endpoint:
        filters['endpoint'] = args.endpoint
    if args.success_only:
        filters['success'] = True
    if args.failed_only:
        filters['success'] = False

    if filters:
        logs = filter_logs(logs, **filters)

    if args.limit:
        logs = logs[:args.limit]

    # 统计信息
    if args.stats:
        print("=== 操作统计 ===")
        print(f"总请求数: {len(logs)}")

        # 按方法统计
        method_counts = {}
        for log in logs:
            method = log['method']
            method_counts[method] = method_counts.get(method, 0) + 1

        print("\n按HTTP方法统计:")
        for method, count in sorted(method_counts.items()):
            print(f"  {method}: {count}")

        # 按端点统计
        endpoint_counts = {}
        for log in logs:
            endpoint = log['endpoint']
            endpoint_counts[endpoint] = endpoint_counts.get(endpoint, 0) + 1

        print("\n按端点统计 (Top 10):")
        for endpoint, count in sorted(endpoint_counts.items(),
                                      key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {endpoint}: {count}")

        # 成功/失败统计
        success_count = sum(1 for log in logs
                           if 'error' not in log.get('response', {}))
        print(f"\n成功: {success_count}, 失败: {len(logs) - success_count}")

    # 导出CSV
    if args.export:
        import csv
        with open(args.export, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['时间', '方法', '端点', '参数', '数据', '响应'])
            for log in logs:
                writer.writerow([
                    log['timestamp'],
                    log['method'],
                    log['endpoint'],
                    json.dumps(log.get('params'), ensure_ascii=False),
                    json.dumps(log.get('data'), ensure_ascii=False),
                    json.dumps(log.get('response'), ensure_ascii=False)[:500]
                ])
        print(f"已导出 {len(logs)} 条记录到 {args.export}")
        return

    # 输出日志
    print(f"=== 找到 {len(logs)} 条日志记录 ===")
    print()

    for i, log in enumerate(logs, 1):
        print(f"[{i}] {log['timestamp']}")
        print(f"    方法: {log['method']}")
        print(f"    端点: {log['endpoint']}")

        if log.get('params'):
            print(f"    参数: {json.dumps(log['params'], ensure_ascii=False)}")

        if log.get('data'):
            data_str = json.dumps(log['data'], ensure_ascii=False)
            if len(data_str) > 200:
                data_str = data_str[:200] + '...'
            print(f"    数据: {data_str}")

        response = log.get('response', {})
        if 'error' in response:
            print(f"    响应: ERROR - {response['error']}")
        else:
            resp_str = json.dumps(response, ensure_ascii=False)
            if len(resp_str) > 200:
                resp_str = resp_str[:200] + '...'
            print(f"    响应: {resp_str}")

        print()


if __name__ == '__main__':
    main()
