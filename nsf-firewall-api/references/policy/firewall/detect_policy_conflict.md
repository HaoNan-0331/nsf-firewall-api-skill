# 6.1.10 策略冲突检测

## 简要描述
策略冲突检测。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/firewall/detect_policy_conflict/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/firewall/detect_policy_conflict/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
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
- 检测策略之间的冲突
- 优化策略配置
