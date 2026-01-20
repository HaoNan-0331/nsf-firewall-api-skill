# 6.1.3 删除防火墙策略

## 简要描述
删除防火墙策略。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | string | 策略id号，多个id使用逗号隔开 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": "1,3,4"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "删除防火墙策略 ID【x】成功",
  "result": {}
}
```

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
- 删除单条防火墙策略
- 批量删除多条策略
