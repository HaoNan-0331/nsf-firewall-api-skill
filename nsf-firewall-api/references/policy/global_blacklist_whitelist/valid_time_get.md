# 6.2.18 获取黑白名单ips av有效时间

## 简要描述
获取黑白名单ips av有效时间。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/validTime/info/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/validTime/info/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "获取有效时间成功",
  "result": {
    "duration_time": 30
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| duration_time | int | 有效时间 |

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "获取有效时间失败"
}
```

## 使用场景
- 查看黑白名单自动加入项的有效期配置
