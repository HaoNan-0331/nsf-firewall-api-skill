# 6.4.6 删除NAT策略

## 简要描述
删除NAT策略。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/nat/delete_nat/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| ids | 是 | string | 策略id，多个用逗号隔开 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/nat/delete_nat/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"ids": "3"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "删除 NAT 策略成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：删除 NAT 错误",
  "result": {}
}
```

## 使用场景
- 删除单条NAT策略
- 批量删除多条NAT策略
