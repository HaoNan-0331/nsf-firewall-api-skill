# 4.1.6 删除安全管理平台

## 简要描述
删除指定的安全管理平台配置。

## 请求URL
```
POST https://{{host}}/north/nf/collaboration/security_platform/delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | int | 安全管理平台id |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/collaboration/security_platform/delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "安全管理中心删除联动配置（10.1.1.1:：443）成功",
  "result": {
    "errorCode": 0,
    "errMsg": "Command Success.",
    "status": "Success",
    "id": ""
  }
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误: 安全管理中心配置失败"
}
```

## 使用场景
- 删除不再使用的安全管理平台配置
- 清理无效的联动配置
