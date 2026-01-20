# 删除策略路由

## 简要描述
删除指定的策略路由。

## 请求URL
```
POST https://{{host}}/north/nf/network/route/policy/delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | string | 策略路由id号（多个id使用逗号隔开，all时清空路由） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/route/policy/delete/" \
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
  "message": "未知错误：下发不成功",
  "result": {}
}
```

## 使用场景
- 删除指定的策略路由
- 批量删除策略路由
- 清空所有策略路由（id="all"）
