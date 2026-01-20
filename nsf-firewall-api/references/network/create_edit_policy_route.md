# 新建/编辑策略路由

## 简要描述
新建或编辑策略路由配置。

## 请求URL
```
POST https://{{host}}/north/nf/network/route/policy/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| action | 是 | string | 新建/编辑（create：新建，edit：编辑） |
| name | 是 | string | 路由名称（长度1-64字符，特殊字符只支持-_\.，名称唯一，不能以特殊字符开头） |
| enabled | 是 | bool | 状态（false：禁用，true：开启） |
| source_ip | 是 | string | 源IP地址 |
| dst_ip | 否 | string | 目的IP地址 |
| dst_obj_type | 是 | string | 目的对象（ip：ip地址，domain_object：域名对象） |
| dst_domain_obj | 否 | string | 目的域名对象（域名对象ID，dst_obj_type为domain_object时必填，最多8个） |
| is_app_route | 是 | bool | 基于应用还是服务（false：服务，true：应用） |
| service | 否 | string | 服务（is_app_route为false时必填，服务名称，多个以逗号分隔） |
| application | 否 | string | 应用（is_app_route为true时必填，应用名称，多个以逗号分隔） |
| src_interface | 是 | string | 源接口（物理接口：SUB_INTERFACE、LOOPBACK_INTERFACE、L3_INTERFACE、VLAN_INTERFACE；逻辑接口：BOND_L3_INTERFACE等） |
| export_type | 是 | string | 出接口类型（single：单出口，many：多出口） |
| loadbalanceMode | 否 | int | 负载方式（0：仅单出口选择，1：源目ip模式，2：逐包模式，3：用户模式） |
| fib_path | 是 | array | 出接口（export_type为many时可多个，single时只能一个） |
| fib_path[].dst_interface | 是 | string | 目的接口 |
| fib_path[].gateway | 否 | string | 网关地址（目的接口为GRE、PPPOE时可选，IPSEC_INTERFACE时自动赋值） |
| fib_path[].preference | 是 | int | 管理距离（1-255） |
| fib_path[].weight | 是 | int | 权值（single时为1，many时为1-255） |
| fib_path[].linkdection | 否 | int | 链路探测id |
| id | 否 | int | 策略id（编辑时必填） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/route/policy/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "test1234",
    "action": "edit",
    "id": 1,
    "source_ip": "3.3.3.0/24",
    "export_type": "single",
    "dst_ip": "4.4.4.0/24",
    "dst_obj_type": "ip",
    "dst_domain_obj": "",
    "linkdection": 0,
    "is_app_route": false,
    "service": "any",
    "application": "any",
    "fib_path": [
      {
        "dst_interface": "G1/1",
        "gateway": "3.3.3.3",
        "preference": 1,
        "linkdection": 0,
        "weight": 1
      }
    ],
    "src_interface": "G1/1",
    "enabled": false,
    "loadbalanceMode": 0
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：下发不成功",
  "result": {}
}
```

## 使用场景
- 创建基于源地址的策略路由
- 配置多出口负载均衡
- 配置应用路由
- 编辑已有策略路由
