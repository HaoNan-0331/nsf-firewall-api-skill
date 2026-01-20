# 6.4.7 清空NAT策略

## 简要描述
清空所有NAT策略。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/nat/clear_nat/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/nat/clear_nat/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "清空 NAT 策略成功",
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
- 清空所有NAT策略
- 重置NAT配置
