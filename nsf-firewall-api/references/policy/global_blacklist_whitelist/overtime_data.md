# 6.2.21 下发ips av超时数据

## 简要描述
下发ips av超时数据。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/overtime/configuration/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| ipv6 | 否 | string | ipv6：true(ipv6)/false(ipv4)，默认ipv4 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/overtime/configuration/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"ipv6": ""}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "ipv4 黑名单无超时数据",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "未知错误"
}
```

## 使用场景
- 处理黑白名单超时数据
- 清理过期的自动黑名单
