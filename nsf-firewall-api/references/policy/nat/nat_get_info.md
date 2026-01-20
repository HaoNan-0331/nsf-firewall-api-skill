# 6.4.5 获取NAT策略

## 简要描述
获取NAT策略详细信息（支持分页和条件查询）。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/nat/info/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（>0或=-1，默认10） |
| page | 否 | int | 页数（>0，默认1） |
| type | 是 | string | 类型：create(按新建顺序)/priority(按匹配顺序) |
| where | 是 | string | 查询方式：AND(精确查找)/OR(模糊查询) |
| d_address | 否 | string | 原始数据包-目的地址，长度≤50 |
| d_safety_zone | 否 | string | 目的安全区，长度≤50 |
| dst_port | 否 | string | 入接口，长度≤50 |
| enabled | 否 | bool | 状态：true(启用)/false(禁用) |
| external_address | 否 | string | 外部地址，长度≤50 |
| external_port | 否 | string | 外部端口，长度≤50 |
| health_check | 否 | string | 服务器健康检测，长度≤50 |
| id | 否 | string | 策略ID，长度≤50 |
| interface | 否 | string | 出接口，长度≤50 |
| internal_address | 否 | string | 转换后地址-目的地址，长度≤50 |
| internal_port | 否 | string | 内部端口，长度≤50 |
| name | 否 | string | 名称，长度≤50 |
| nat_object | 否 | string | 转换后地址-源地址，长度≤50 |
| nat_type | 否 | int | 策略类型：1-snat/2-dnat/3-双向nat |
| protocol | 否 | string | 协议，长度≤50 |
| s_address | 否 | string | 原始数据包-源地址，长度≤50 |
| s_safety_zone | 否 | string | 源安全区，长度≤50 |
| service | 否 | string | 服务，长度≤50 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/nat/info/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"page": 1, "size": 10, "where": "AND", "type": "priority"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "获取成功",
  "result": {
    "total": 3,
    "list": [
      {
        "id": 1,
        "name": "test1234",
        "nat_type": 0,
        "interface_type": "normal",
        "interface": "",
        "port_map_type": 2,
        "internal_address": "",
        "external_address": "",
        "protocol": "",
        "internal_port": "",
        "external_port": "",
        "health_check": [],
        "load_balance": "",
        "HA": "",
        "enabled": true,
        "backend_id": "1",
        "priority": 0,
        "timestamp": "2024-08-14T09:45:41",
        "s_safety_zone": "DMZ",
        "d_safety_zone": "DMZ",
        "s_address": [
          {
            "name": "any",
            "id": 100000,
            "type": "segment",
            "is_ipv6": false,
            "backend_id": "100000"
          }
        ],
        "service": [
          {
            "backend_id": "600000"
          }
        ],
        "dst_port": "vlan1",
        "nat_object": [
          {
            "name": "interface_ip",
            "id": "",
            "type": "",
            "is_ipv6": "",
            "backend_id": ""
          }
        ],
        "s_address_translation": 1,
        "port_map": {
          "port_map_type": 2,
          "internal_address": "",
          "external_address": "",
          "protocol": "",
          "internal_port": "",
          "external_port": ""
        }
      }
    ]
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 策略ID |
| name | string | 策略名称 |
| nat_type | int | 策略类型(0:源NAT策略/1:目的NAT策略/2:双向NAT策略) |
| interface_type | string | 接口类型 |
| interface | string | 出接口 |
| internal_address | string | 转换后地址-目的地址 |
| external_address | string | 原始数据包-目的地址 |
| protocol | string | 协议 |
| internal_port | string | 内部端口 |
| external_port | string | 外部端口 |
| health_check | array | 服务器健康检测 |
| load_balance | string | 负载均衡 |
| HA | string | HA线路 |
| enabled | bool | 状态 |
| backend_id | int | 后端ID |
| priority | int | 优先级 |
| timestamp | string | 创建时间 |
| s_safety_zone | string | 源安全区 |
| d_safety_zone | string | 目的安全区 |
| s_address | array | 源地址 |
| d_address | array | 目的地址 |
| service | array | 服务 |
| dst_port | string | 入接口 |
| nat_object | array | 转换后地址对象 |
| s_address_translation | int | 地址转换方式(1:接口地址/2:网络对象) |
| port_map_type | int | 端口映射类型(1:映射部分端口/2:映射全部端口) |
| port_map | dict | 端口映射配置 |

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：获取失败",
  "result": {}
}
```

## 使用场景
- 查询NAT策略详细信息
- 按条件筛选策略
- 分页浏览策略列表
