# 获取所有接口列表

## 简要描述
获取所有接口列表。

## 请求URL
```
GET https://{{host}}/north/nf/network/interface/all/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/network/interface/all/" \
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
| userName | string | 用户名 |
| passWord | string | 密码 |
| lacp_state | string | 汇聚口lacp协商状态 |
| enable | bool | 是否启用 |

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
- 一次性获取所有接口信息
- 接口配置导出
- 接口状态巡检
