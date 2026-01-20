# 6.1.7 禁用启用防火墙策略

## 简要描述
禁用或启用防火墙策略。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/status/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | string | 策略id |
| status | 是 | int | 状态：0-启用/1-禁用 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/status/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": "1", "status": 1}'
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
- 临时禁用某条策略
- 重新启用已禁用的策略
