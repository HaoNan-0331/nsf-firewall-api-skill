# 7.5.6 设置域名策略域名解析层数

## 简要描述
设置域名策略域名解析层数。

## 请求URL
```
POST https://{{host}}/north/nf/object/domain_config/config/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| maxLevel | 是 | int | 域名策略域名解析层数，取值范围1-1024 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/object/domain_config/config/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"maxLevel": 32}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "域名对象全局配置成功",
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
- 配置域名解析深度
- 控制域名解析的最大层级数
