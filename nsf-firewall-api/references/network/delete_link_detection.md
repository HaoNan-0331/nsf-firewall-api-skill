# 删除链路探测信息

## 简要描述
删除指定的链路探测配置。

## 请求URL
```
POST https://{{host}}/north/nf/network/linkdection/delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | string | 链路id（一个或多个整数以逗号隔开，存在的链路探测ID值） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/linkdection/delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": "1"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "删除链路探测 test1 成功",
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
- 删除不再使用的链路探测配置
- 批量删除链路探测规则
- 清理无效的链路探测
