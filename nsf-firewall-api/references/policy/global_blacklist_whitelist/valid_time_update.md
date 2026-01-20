# 6.2.19 提交黑白名单ips av有效时间

## 简要描述
提交黑白名单ips av有效时间。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/validTime/configuration/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| duration_time | 是 | int | 有效期，1~60分钟 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/validTime/configuration/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"duration_time": ""}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "配置下发成功",
  "result": {
    "duration_time": 32
  }
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "配置下发失败"
}
```

## 使用场景
- 设置黑白名单自动加入项的有效期
