# 新建三层子接口

## 简要描述
新建三层子接口。

## 请求URL
```
POST https://{{host}}/north/nf/network/interfacedetail/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| type | 是 | string | 接口类型：SUB_INTERFACE |
| id | 是 | string | 接口id，新增时为空 |
| parent_name | 是 | string | 父接口（有效的三层物理口名称） |
| name | 是 | string | 接口名称（父接口.vlanid组合，长度1-15字符） |
| vlan_id | 是 | int | VLANID（1-4094） |
| zone | 是 | string | 接口安全区（存在的安全区名称） |
| attribute | 是 | string | 接口属性：logic（逻辑接口） |
| manage | 是 | int | 管理属性（存在的管理属性id） |
| ipv4 | 是 | string | IPv4地址（ipv4格式，地址唯一） |
| sub_ipv4 | 否 | string | 从属IPv4地址（ipv4格式，最多32个） |
| status | 是 | string | 状态：up/down |
| ipv6 | 否 | string | IPv6地址（ipv6格式，地址唯一） |
| ipv6_method | 是 | string | IPv6配置方式：auto/manual |
| router_message | 否 | int | 是否发送路由通告（0：否，1：是） |
| ipv4_mtu | 否 | int | IPv4 MTU（未开启巨帧128-1600，开启巨帧128-9216） |
| tcp_mss | 否 | int | TCP MSS（78-1560，不启用时可传null或空） |
| ipv6_mtu | 是 | int | IPv6 MTU（未开启巨帧1280-1600，开启巨帧1280-9216） |
| label | 否 | string | 标签（长度0-64字节，中文3字节） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/interfacedetail/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "SUB_INTERFACE",
    "id": "",
    "parent_name": "G1/3",
    "name": "G1/3.1",
    "vlan_id": 1,
    "zone": "TRUST",
    "attribute": "logic",
    "manage": 1,
    "ipv4": "0.0.0.0/0",
    "sub_ipv4": "",
    "status": "down",
    "ipv6": "",
    "ipv6_method": "manual",
    "router_message": 0,
    "ipv4_mtu": 1500,
    "tcp_mss": 1460,
    "ipv6_mtu": 1500,
    "label": "ddd"
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "新建三层子接口 G1/3.1 成功",
  "result": [
    {
      "id": 25,
      "interface_id": 0,
      "type": "SUB_INTERFACE",
      "name": "G1/3.1",
      "attribute": "logic",
      "vlan_id": 1,
      "vsys": 0,
      "manage": 1,
      "parent_name": "G1/3",
      "ipv4": "0.0.0.0/0",
      "sub_ipv4": "",
      "status": "down",
      "ipv6": "",
      "ipv6_method": "manual",
      "router_message": 0,
      "ipv4_mtu": 1500,
      "ipv6_mtu": 1500,
      "port_type": "",
      "zone": "TRUST",
      "mac": "",
      "label": "ddd",
      "tcp_mss": 1460
    }
  ]
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：下发失败",
  "result": {}
}
```

## 使用场景
- 在物理接口上创建VLAN子接口
- 实现基于VLAN的网络隔离
- 扩展网络接口数量
