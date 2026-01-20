# 删除安全区

## 简要描述
删除指定的安全区。

## 请求URL
```
POST https://{{host}}/north/nf/network/zone/delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 否 | int | 安全区编号（只能是数字，存在的安全区id） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/zone/delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": 6}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "删除安全区 testddd 成功",
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
- 删除不再使用的自定义安全区
- 清理无效的安全区配置
- 注意：系统默认安全区不可删除
