# 6.1.9 智能策略检测

## 简要描述
智能策略检测。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/intelligent_policy_check/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| dstIpAddr | 是 | string | 目的地址，取值范围0.0.0.0~255.255.255.255 |
| dstPortOrIcmpType | 是 | string | 目的端口，取值范围0~65535 |
| dstZone | 否 | string | 目的安全区（参数是对象名称） |
| isUsePri | 否 | string | 是否匹配优先级：0-否/1-是，默认0 |
| protocol | 是 | string | 服务协议：1-icmp/6-tcp/17-udp |
| srcIpAddr | 是 | string | 源地址，取值范围0.0.0.0~255.255.255.255 |
| srcPortOrIcmpType | 是 | string | 源端口，取值范围0~65535 |
| srcZone | 否 | string | 源安全区（参数是对象名称） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/intelligent_policy_check/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "srcZone": "TRUST",
    "dstZone": "TRUST",
    "srcIpAddr": "192.168.1.1",
    "dstIpAddr": "192.168.1.1",
    "protocol": 6,
    "srcPortOrIcmpType": 122,
    "dstPortOrIcmpType": 122,
    "isUsePri": 0
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
  "message": "未知错误：获取失败",
  "result": {}
}
```

## 使用场景
- 检测指定流量会命中哪条策略
- 策略调试验证
- 策略优先级分析
