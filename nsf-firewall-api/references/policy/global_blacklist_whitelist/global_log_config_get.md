# 6.2.6 获取黑白名单全局控制是否记录日志

## 简要描述
获取黑白名单全局控制日志开关配置。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/globalWb/blist/global_config/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/globalWb/blist/global_config/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "获取成功",
  "result": {
    "white_log_enable": 0,
    "black_log_enable": 1
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| white_log_enable | int | 记录白名单(0:关闭/1:开启) |
| black_log_enable | int | 记录黑名单(0:关闭/1:开启) |

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "[后台]-获取失败"
}
```

## 使用场景
- 查看黑白名单日志记录状态
- 检查全局日志配置
