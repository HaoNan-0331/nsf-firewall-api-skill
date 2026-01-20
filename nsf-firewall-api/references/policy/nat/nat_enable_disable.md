# 6.4.8 启用/禁用NAT策略

## 简要描述
启用或禁用NAT策略。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/nat/enable_nat/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| ids | 是 | string | 策略id，多个用逗号隔开 |
| enabled | 是 | bool | 是否启用 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/nat/enable_nat/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"ids": 2, "enabled": true}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {
    "id": "2"
  }
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
- 临时禁用某条NAT策略
- 批量启用/禁用策略
- 重新启用已禁用的策略
