# 编辑三层接口

## 简要描述
编辑已存在的三层物理接口配置。

## 请求URL
```
POST https://{{host}}/north/nf/network/interfacedetail/edit/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | int | 接口id（存在的接口id） |
| type | 是 | string | 接口类型：L3_INTERFACE |
| name | 是 | string | 接口名称（不能修改） |
| zone | 是 | string | 接口安全区（存在的安全区名称） |
| attribute | 是 | string | 接口属性：physical（物理接口） |
| manage | 是 | int | 管理属性（存在的管理属性id） |
| ipv4 | 是 | string | IPv4地址（ipv4格式，地址唯一） |
| sub_ipv4 | 否 | string | 从属IPv4地址（ipv4格式，最多32个） |
| status | 是 | string | 状态：up/down |
| ipv6 | 否 | string | IPv6地址（ipv6格式，地址唯一） |
| ipv6_method | 是 | string | IPv6配置方式：auto/manual |
| router_message | 否 | int | 是否发送路由通告（0：否，1：是） |
| mac | 否 | string | MAC地址（合法的6段式mac地址，以:或者-为分割符） |
| ipv4_mtu | 是 | int | IPv4 MTU（未开启巨帧128-1600，开启巨帧128-9216） |
| tcp_mss | 否 | int | TCP MSS（78-1560，不启用时可传null或空） |
| ipv6_mtu | 是 | int | IPv6 MTU（未开启巨帧1280-1600，开启巨帧1280-9216） |
| linkspeed | 是 | string | 连接速率：[auto, 10, 100, 1000, 10000, 40000] |
| linkmode | 是 | string | 双工模式：[auto, half, full] |
| multicast | 是 | string | 组播：true/false |
| label | 否 | string | 标签（长度0-64字节，中文3字节） |
| ip4_method | 是 | string | IPv4配置方式：static/pppoe |
| userName | 否 | string | 用户名（长度1-128字符，ipv4_method为pppoe时必填） |
| passWord | 否 | string | 密码（长度1-128字符，ipv4_method为pppoe时必填） |
| isGenerateRoute | 否 | string | 自动生成默认路由：true/false |
| HandShakeInterval | 否 | int | 心跳间隔（只能是数字） |
| Reconnects | 否 | int | 重连次数（只能是数字） |
| onlineMethod | 否 | string | 在线方式：true/false |
| ipGetMethod | 否 | string | IP获取方式：true/false |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/interfacedetail/edit/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 2,
    "type": "L3_INTERFACE",
    "name": "G1/2",
    "zone": "TRUST",
    "attribute": "physical",
    "manage": 1,
    "ipv4": "0.0.0.0/0",
    "status": "down",
    "ipv6_method": "manual",
    "router_message": 0,
    "mac": "00:0d:48:72:b3:7c",
    "ipv4_mtu": 1500,
    "ipv6_mtu": 1500,
    "linkspeed": "auto",
    "linkmode": "auto",
    "ip4_method": "static",
    "isGenerateRoute": "true",
    "HandShakeInterval": 20,
    "Reconnects": 5,
    "onlineMethod": "true",
    "ipGetMethod": "true"
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": [
    {
      "id": 3,
      "interface_id": 3,
      "type": "L3_INTERFACE",
      "name": "G1/3",
      "zone": "TRUST",
      "label": "tteeeww",
      "attribute": "physical",
      "role": "三层接口",
      "ipv4": "0.0.0.0/0",
      "sub_ipv4": "",
      "manage": "1",
      "vsys": 0,
      "status": "down",
      "ipv6": "",
      "ipv6_method": "manual",
      "router_message": 1,
      "mac": "00:0d:48:7d:64:1f",
      "linkmode": "half",
      "linkspeed": "auto",
      "ipv4_mtu": 1500,
      "ipv6_mtu": 1500,
      "port_type": "电口"
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
- 修改三层接口的IP地址
- 配置PPPoE拨号参数
- 调整接口的MTU和链路参数
- 修改接口所属的安全区
