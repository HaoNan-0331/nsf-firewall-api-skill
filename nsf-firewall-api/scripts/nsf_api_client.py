#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
绿盟NF防火墙REST API客户端
支持单次和批量操作，自动记录操作日志
"""

import requests
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class NSFApiClient:
    """绿盟NF防火墙API客户端"""

    def __init__(self, host: str, token: str, verify_ssl: bool = False, log_dir: str = None):
        """
        初始化API客户端

        Args:
            host: 防火墙IP地址，格式: https://<IP> 或 http://<IP>
            token: 从Web界面生成的认证Token
            verify_ssl: 是否验证SSL证书，默认False
            log_dir: 日志目录路径，默认为logs/
        """
        self.host = host.rstrip('/')
        self.token = token
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': token,
            'Content-Type': 'application/json'
        })
        self.api_prefix = '/north/nf'  # 绿盟NF防火墙API前缀

        # 设置日志目录
        if log_dir is None:
            log_dir = Path(__file__).parent.parent / 'logs'
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def _log_operation(self, method: str, endpoint: str, params: Dict = None,
                       data: Dict = None, response: Any = None):
        """记录操作日志"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'method': method,
            'endpoint': endpoint,
            'params': params,
            'data': data,
            'response': response if isinstance(response, dict) else str(response)[:1000]
        }

        log_file = self.log_dir / f'api_log_{datetime.now().strftime("%Y%m%d")}.json'
        with open(log_file, 'a', encoding='utf-8') as f:
            json.dump(log_entry, f, ensure_ascii=False)
            f.write('\n')

    def request(self, method: str, endpoint: str, params: Dict = None,
                data: Dict = None) -> Dict:
        """
        发送API请求

        Args:
            method: HTTP方法 (GET, POST, PUT, DELETE)
            endpoint: API端点路径
            params: URL查询参数
            data: 请求体数据

        Returns:
            API响应JSON数据
        """
        url = f"{self.host}{self.api_prefix}/{endpoint.lstrip('/')}"
        response_data = None

        try:
            if method.upper() == 'GET':
                response = self.session.get(
                    url,
                    params=params,
                    verify=self.verify_ssl,
                    timeout=30
                )
            elif method.upper() == 'POST':
                response = self.session.post(
                    url,
                    params=params,
                    json=data,
                    verify=self.verify_ssl,
                    timeout=30
                )
            elif method.upper() == 'PUT':
                response = self.session.put(
                    url,
                    params=params,
                    json=data,
                    verify=self.verify_ssl,
                    timeout=30
                )
            elif method.upper() == 'DELETE':
                response = self.session.delete(
                    url,
                    params=params,
                    json=data,
                    verify=self.verify_ssl,
                    timeout=30
                )
            else:
                return {'error': f'不支持的HTTP方法: {method}'}

            response_data = response.json()

            # 记录日志
            self._log_operation(method, endpoint, params, data, response_data)

            return response_data

        except requests.exceptions.SSLError:
            return {'error': 'SSL证书验证失败，请设置verify_ssl=False或使用http://'}
        except requests.exceptions.Timeout:
            return {'error': '请求超时，请检查网络连接'}
        except requests.exceptions.ConnectionError:
            return {'error': '连接失败，请检查防火墙地址是否正确'}
        except json.JSONDecodeError:
            return {'error': f'响应解析失败: {response.text[:500]}'}
        except Exception as e:
            return {'error': f'未知错误: {str(e)}'}

    def batch_request(self, requests_list: List[Dict]) -> List[Dict]:
        """
        批量发送API请求

        Args:
            requests_list: 请求列表，每个元素包含 {method, endpoint, params, data}

        Returns:
            响应列表
        """
        results = []
        for req in requests_list:
            result = self.request(
                method=req.get('method', 'GET'),
                endpoint=req.get('endpoint', ''),
                params=req.get('params'),
                data=req.get('data')
            )
            results.append({
                'request': req,
                'response': result
            })
        return results

    # ==================== 网络接口模块 ====================

    def get_interfaces(self) -> Dict:
        """获取所有网络接口信息"""
        return self.request('GET', '/interface/interfaces')

    def get_interface(self, if_name: str) -> Dict:
        """获取指定接口信息"""
        return self.request('GET', f'/interface/interfaces/{if_name}')

    def update_interface(self, if_name: str, data: Dict) -> Dict:
        """更新接口配置"""
        return self.request('PUT', f'/interface/interfaces/{if_name}', data=data)

    # ==================== 静态路由模块 ====================

    def get_routes(self) -> Dict:
        """获取所有静态路由"""
        return self.request('GET', '/route/static/routes')

    def add_route(self, data: Dict) -> Dict:
        """添加静态路由"""
        return self.request('POST', '/route/static/routes', data=data)

    def update_route(self, route_id: str, data: Dict) -> Dict:
        """更新静态路由"""
        return self.request('PUT', f'/route/static/routes/{route_id}', data=data)

    def delete_route(self, route_id: str) -> Dict:
        """删除静态路由"""
        return self.request('DELETE', f'/route/static/routes/{route_id}')

    # ==================== NAT策略模块 ====================

    def get_nat_policies(self) -> Dict:
        """获取所有NAT策略"""
        return self.request('GET', '/policy/nat/policies')

    def add_nat_policy(self, data: Dict) -> Dict:
        """添加NAT策略"""
        return self.request('POST', '/policy/nat/policies', data=data)

    def update_nat_policy(self, policy_id: str, data: Dict) -> Dict:
        """更新NAT策略"""
        return self.request('PUT', f'/policy/nat/policies/{policy_id}', data=data)

    def delete_nat_policy(self, policy_id: str) -> Dict:
        """删除NAT策略"""
        return self.request('DELETE', f'/policy/nat/policies/{policy_id}')

    # ==================== 访问控制策略模块 ====================

    def get_firewall_policies(self, size: int = -1, page: int = 1, **kwargs) -> Dict:
        """
        获取防火墙策略

        Args:
            size: 分页大小，-1表示获取所有
            page: 页数
            **kwargs: 其他可选参数 (search, type, is_v6, searchType, name, zone, action)
        """
        params = {'size': size, 'page': 1}
        params.update(kwargs)
        return self.request('GET', '/strategy/firewall/info/', params=params)

    def get_acl_policies(self) -> Dict:
        """获取所有访问控制策略"""
        return self.request('GET', '/policy/acl/policies')

    def add_acl_policy(self, data: Dict) -> Dict:
        """添加访问控制策略"""
        return self.request('POST', '/policy/acl/policies', data=data)

    def update_acl_policy(self, policy_id: str, data: Dict) -> Dict:
        """更新访问控制策略"""
        return self.request('PUT', f'/policy/acl/policies/{policy_id}', data=data)

    def delete_acl_policy(self, policy_id: str) -> Dict:
        """删除访问控制策略"""
        return self.request('DELETE', f'/policy/acl/policies/{policy_id}')

    # ==================== 地址对象模块 ====================

    def get_address_objects(self) -> Dict:
        """获取所有地址对象"""
        return self.request('GET', '/objects/addresses')

    def add_address_object(self, data: Dict) -> Dict:
        """添加地址对象"""
        return self.request('POST', '/objects/addresses', data=data)

    def update_address_object(self, obj_id: str, data: Dict) -> Dict:
        """更新地址对象"""
        return self.request('PUT', f'/objects/addresses/{obj_id}', data=data)

    def delete_address_object(self, obj_id: str) -> Dict:
        """删除地址对象"""
        return self.request('DELETE', f'/objects/addresses/{obj_id}')

    # ==================== 服务对象模块 ====================

    def get_service_objects(self) -> Dict:
        """获取所有服务对象"""
        return self.request('GET', '/objects/services')

    def add_service_object(self, data: Dict) -> Dict:
        """添加服务对象"""
        return self.request('POST', '/objects/services', data=data)

    def update_service_object(self, obj_id: str, data: Dict) -> Dict:
        """更新服务对象"""
        return self.request('PUT', f'/objects/services/{obj_id}', data=data)

    def delete_service_object(self, obj_id: str) -> Dict:
        """删除服务对象"""
        return self.request('DELETE', f'/objects/services/{obj_id}')

    # ==================== 应用层模块 ====================

    def get_applications(self) -> Dict:
        """获取应用列表"""
        return self.request('GET', '/application/applications')

    def get_app_policies(self) -> Dict:
        """获取应用控制策略"""
        return self.request('GET', '/application/policies')

    def add_app_policy(self, data: Dict) -> Dict:
        """添加应用控制策略"""
        return self.request('POST', '/application/policies', data=data)

    # ==================== VPN模块 ====================

    def get_ipsec_vpn(self) -> Dict:
        """获取IPSec VPN配置"""
        return self.request('GET', '/vpn/ipsec/configs')

    def get_ssl_vpn(self) -> Dict:
        """获取SSL VPN配置"""
        return self.request('GET', '/vpn/ssl/configs')

    def add_ipsec_vpn(self, data: Dict) -> Dict:
        """添加IPSec VPN配置"""
        return self.request('POST', '/vpn/ipsec/configs', data=data)

    # ==================== 高可用性模块 ====================

    def get_ha_status(self) -> Dict:
        """获取HA状态"""
        return self.request('GET', '/ha/status')

    def get_ha_config(self) -> Dict:
        """获取HA配置"""
        return self.request('GET', '/ha/config')

    def update_ha_config(self, data: Dict) -> Dict:
        """更新HA配置"""
        return self.request('PUT', '/ha/config', data=data)

    # ==================== 网络诊断模块 ====================

    def ping(self, data: Dict) -> Dict:
        """Ping测试"""
        return self.request('POST', '/diagnostics/ping', data=data)

    def traceroute(self, data: Dict) -> Dict:
        """路径追踪"""
        return self.request('POST', '/diagnostics/traceroute', data=data)

    def get_path(self, data: Dict) -> Dict:
        """路径分析"""
        return self.request('POST', '/diagnostics/path', data=data)

    # ==================== 系统管理模块 ====================

    def get_system_info(self) -> Dict:
        """获取系统信息"""
        return self.request('GET', '/system/info')

    def get_hostname(self) -> Dict:
        """获取主机名"""
        return self.request('GET', '/system/hostname')

    def set_hostname(self, hostname: str) -> Dict:
        """设置主机名"""
        return self.request('PUT', '/system/hostname', data={'hostname': hostname})

    def get_dns(self) -> Dict:
        """获取DNS配置"""
        return self.request('GET', '/system/dns')

    def set_dns(self, data: Dict) -> Dict:
        """设置DNS配置"""
        return self.request('PUT', '/system/dns', data=data)

    def get_ntp(self) -> Dict:
        """获取NTP配置"""
        return self.request('GET', '/system/ntp')

    def set_ntp(self, data: Dict) -> Dict:
        """设置NTP配置"""
        return self.request('PUT', '/system/ntp', data=data)

    def get_admins(self) -> Dict:
        """获取管理员列表"""
        return self.request('GET', '/system/admins')

    def add_admin(self, data: Dict) -> Dict:
        """添加管理员"""
        return self.request('POST', '/system/admins', data=data)

    def update_admin(self, admin_id: str, data: Dict) -> Dict:
        """更新管理员"""
        return self.request('PUT', f'/system/admins/{admin_id}', data=data)

    def delete_admin(self, admin_id: str) -> Dict:
        """删除管理员"""
        return self.request('DELETE', f'/system/admins/{admin_id}')

    def get_certificates(self) -> Dict:
        """获取证书列表"""
        return self.request('GET', '/system/certificates')

    def import_certificate(self, data: Dict) -> Dict:
        """导入证书"""
        return self.request('POST', '/system/certificates/import', data=data)


def main():
    """命令行入口"""
    if len(sys.argv) < 3:
        print("用法: python nsf_api_client.py <host> <token> [操作] [参数...]")
        print("\n示例:")
        print("  查看接口: python nsf_api_client.py https://192.168.1.1 YOUR_TOKEN get_interfaces")
        print("  添加路由: python nsf_api_client.py https://192.168.1.1 YOUR_TOKEN add_route '{...}'")
        print("\n支持的操作:")
        print("  get_firewall_policies - 获取防火墙策略")
        print("  get_interfaces, get_routes, add_route, delete_route")
        print("  get_nat_policies, add_nat_policy, delete_nat_policy")
        print("  get_acl_policies, add_acl_policy, delete_acl_policy")
        print("  get_address_objects, add_address_object")
        print("  get_service_objects, add_service_object")
        print("  ping, traceroute, get_path")
        print("  get_system_info, get_hostname, set_hostname")
        print("  get_dns, set_dns, get_ntp, set_ntp")
        print("  get_admins, add_admin, update_admin, delete_admin")
        print("  get_certificates")
        sys.exit(1)

    host = sys.argv[1]
    token = sys.argv[2]

    client = NSFApiClient(host, token, verify_ssl=False)

    if len(sys.argv) < 4:
        # 默认获取系统信息
        result = client.get_system_info()
    else:
        operation = sys.argv[3]
        params = json.loads(sys.argv[4]) if len(sys.argv) > 4 else None

        # 操作映射
        operations = {
            'get_firewall_policies': lambda: client.get_firewall_policies(),
            'get_interfaces': lambda: client.get_interfaces(),
            'get_routes': lambda: client.get_routes(),
            'add_route': lambda: client.add_route(params),
            'update_route': lambda: client.update_route(params.get('id'), params),
            'delete_route': lambda: client.delete_route(params),
            'get_nat_policies': lambda: client.get_nat_policies(),
            'add_nat_policy': lambda: client.add_nat_policy(params),
            'update_nat_policy': lambda: client.update_nat_policy(params.get('id'), params),
            'delete_nat_policy': lambda: client.delete_nat_policy(params),
            'get_acl_policies': lambda: client.get_acl_policies(),
            'add_acl_policy': lambda: client.add_acl_policy(params),
            'update_acl_policy': lambda: client.update_acl_policy(params.get('id'), params),
            'delete_acl_policy': lambda: client.delete_acl_policy(params),
            'get_address_objects': lambda: client.get_address_objects(),
            'add_address_object': lambda: client.add_address_object(params),
            'update_address_object': lambda: client.update_address_object(params.get('id'), params),
            'delete_address_object': lambda: client.delete_address_object(params),
            'get_service_objects': lambda: client.get_service_objects(),
            'add_service_object': lambda: client.add_service_object(params),
            'update_service_object': lambda: client.update_service_object(params.get('id'), params),
            'delete_service_object': lambda: client.delete_service_object(params),
            'get_applications': lambda: client.get_applications(),
            'get_app_policies': lambda: client.get_app_policies(),
            'add_app_policy': lambda: client.add_app_policy(params),
            'get_ipsec_vpn': lambda: client.get_ipsec_vpn(),
            'get_ssl_vpn': lambda: client.get_ssl_vpn(),
            'add_ipsec_vpn': lambda: client.add_ipsec_vpn(params),
            'get_ha_status': lambda: client.get_ha_status(),
            'get_ha_config': lambda: client.get_ha_config(),
            'update_ha_config': lambda: client.update_ha_config(params),
            'ping': lambda: client.ping(params),
            'traceroute': lambda: client.traceroute(params),
            'get_path': lambda: client.get_path(params),
            'get_system_info': lambda: client.get_system_info(),
            'get_hostname': lambda: client.get_hostname(),
            'set_hostname': lambda: client.set_hostname(params.get('hostname')),
            'get_dns': lambda: client.get_dns(),
            'set_dns': lambda: client.set_dns(params),
            'get_ntp': lambda: client.get_ntp(),
            'set_ntp': lambda: client.set_ntp(params),
            'get_admins': lambda: client.get_admins(),
            'add_admin': lambda: client.add_admin(params),
            'update_admin': lambda: client.update_admin(params.get('id'), params),
            'delete_admin': lambda: client.delete_admin(params),
            'get_certificates': lambda: client.get_certificates(),
        }

        if operation in operations:
            result = operations[operation]()
        else:
            result = {'error': f'不支持的操作: {operation}'}

    # 输出结果（原始JSON）
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
