# 7.5.5 获取域名策略域名解析层数

## 简要描述
获取域名策略域名解析层数。

## 请求URL
```
GET https://{{host}}/north/nf/object/domain_config/info/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/object/domain_config/info/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "操作成功",
  "result": {
    "maxLevel": 32
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| maxLevel | int | 域名解析层数 |

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
- 查看域名解析配置
- 获取域名解析深度限制
