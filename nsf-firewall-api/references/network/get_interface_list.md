# 获取接口列表

## 简要描述
获取接口列表，支持分页和搜索。

## 请求URL
```
GET https://{{host}}/north/nf/network/interface/
```

## 请求方式
```
GET
```

## 请求参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（>0或=-1，默认为10） |
| page | 否 | int | 页数（>0，默认为1） |
| search | 否 | string | 查询内容（字符串长度≤50） |
| type | 否 | string | 类型：create_ipsec_vpn（过滤L3_INTERFACE、SUB_INTERFACE等类型接口） |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/network/interface/?size=10&page=1" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "操作成功",
  "result": {
    "total": 8,
    "list": {
      "physical": [],
      "logic": [],
      "page": 1
    },
    "ha": false,
    "vsys_enable": false
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | ID，删改标识 |
| interface_id | int | 接口id，可忽略 |
| type | string | 接口类型 |
| name | string | 接口名称 |
| zone | string | 安全区 |
| label | string | 标签 |
| attribute | string | 接口属性（physical：物理，logic：逻辑） |
| role | string | 接口角色 |
| ipv4 | string | IPv4地址 |
| sub_ipv4 | string | 从属IPv4地址 |
| vlan_id | string | VLANID |
| manage | string | 管理属性 |
| parent_name | string | 父接口名称 |
| vsys | int | 所属虚拟系统id |
| status | string | 接口状态 |
| ipv6 | string | IPv6地址 |
| ipv6_method | string | IPv6地址配置方式 |
| router_message | int | 发送路由通告（1：是，0：否） |
| mac | string | MAC地址 |
| linkmode | string | 双工模式 |
| linkspeed | string | 连接速率 |
| ipv4_mtu | int | IPv4_MTU |
| ipv6_mtu | int | IPv6_MTU |
| port_type | string | 接口类型（光口、电口、空） |
| multicast | string | 组播 |
| tcp_mss | int | TCP_MSS |
| ip4_method | string | IPv4配置方式（static：静态，pppoe：PPPOE） |

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：异常错误",
  "result": {}
}
```

## 使用场景
- 查看所有接口的配置信息
- 搜索特定接口
- 分页浏览接口列表
