# 6.1.16 删除防火墙策略组

## 简要描述
删除防火墙策略组。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/group/delete/
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
curl -X POST "https://{{host}}/north/nf/strategy/firewall/group/delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": "1,3,4"}'
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
  "message": "未知错误：策略组删除失败",
  "result": {}
}
```

## 使用场景
- 删除单个策略组
- 批量删除多个策略组
