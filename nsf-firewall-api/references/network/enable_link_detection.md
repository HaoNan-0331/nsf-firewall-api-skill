# 启用/禁用链路探测

## 简要描述
启用或禁用指定的链路探测。

## 请求URL
```
POST https://{{host}}/north/nf/network/linkdection_status/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | array | 链路id列表（存在的链路探测对象ID） |
| enable | 是 | bool | 是否启用（True、False） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/linkdection_status/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "enable": false,
    "id": [1]
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
  "status": 8302,
  "module": "NF",
  "message": "资源未找到：链路探测不存在"
}
```

## 使用场景
- 批量启用链路探测
- 批量禁用链路探测
- 临时关闭链路探测用于维护
