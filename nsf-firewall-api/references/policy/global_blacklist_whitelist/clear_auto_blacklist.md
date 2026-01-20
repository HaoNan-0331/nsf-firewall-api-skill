# 6.2.20 清空黑名单中ips av自动加入的数据

## 简要描述
清空黑名单中ips av自动加入的数据。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/clear/configuration/
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
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/clear/configuration/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"ipv6": ""}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "清空 ips_auto 和 av_auto 黑名单成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "清空 ips_auto 和 av_auto 黑名单失败"
}
```

## 使用场景
- 清空自动加入的黑名单条目
- 重置IPS/AV自动黑名单
