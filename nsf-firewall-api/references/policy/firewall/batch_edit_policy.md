# 6.1.6 批量编辑防火墙策略

## 简要描述
批量编辑防火墙策略。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/batch/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | array | 策略id号 |
| service | 否 | array | 服务对象，支持最多32个服务或服务组，参数是对象id |
| application | 否 | array | 应用对象，支持最多128个应用对象或应用组，参数是对象id |
| s_safety_zone | 否 | array | 源安全区，支持最大64个对象，参数是对象名称 |
| s_address | 否 | array | 源地址对象，支持最多32个对象或对象组，参数是对象id |
| d_safety_zone | 否 | string | 目的安全区，支持最大64个对象，参数是对象名称，参数的ipv6属性必须和d_address的ipv6属性保持一致，参数的ipv6属性必须和策略的ipv6属性保持一致 |
| d_address | 否 | array | 目的地址对象，支持最多32个对象或对象组，参数是对象id |
| time | 否 | array | 生效时间，支持最多32个时间对象或对象组，参数是对象id |
| action | 否 | string | 动作：1-放行/2-阻断 |
| log | 否 | string | 日志记录：0-关闭/1-开启 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/batch/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": ["1", "2"],
    "s_safety_zone": ["UNTRUST"],
    "d_safety_zone": ["DMZ"],
    "action": "1",
    "log": "0"
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
  "message": "未知错误：服务器错误",
  "result": {}
}
```

## 使用场景
- 批量修改多条策略的安全区
- 批量修改策略动作
- 批量更新策略的服务或地址对象
