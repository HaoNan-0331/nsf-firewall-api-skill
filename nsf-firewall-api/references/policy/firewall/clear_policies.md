# 6.1.5 清空防火墙策略

## 简要描述
清空防火墙策略。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/firewall/clear/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/firewall/clear/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "清空防火墙策略成功",
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
- 清空所有防火墙策略
- 重置防火墙策略配置
