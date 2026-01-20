# 6.2.15 获取黑白名单全局控制是否记录class日志

## 简要描述
获取黑白名单全局控制是否记录class日志。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/info/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/info/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "关闭配置",
  "result": {
    "enable": 0
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| enable | int | 配置开关(0:关闭/1:开启) |

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "配置获取失败"
}
```

## 使用场景
- 查看class日志记录状态
