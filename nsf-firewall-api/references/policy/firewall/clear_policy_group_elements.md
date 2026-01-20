# 6.1.17 批量删除防火墙策略组元素

## 简要描述
批量删除防火墙策略组元素。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/group/clear_attr/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | array | 策略id号 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/group/clear_attr/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": [1, 2, 3]}'
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
  "message": "未知错误：删除策略失败",
  "result": {}
}
```

## 使用场景
- 从策略组中移除策略
- 批量清理策略组中的策略
