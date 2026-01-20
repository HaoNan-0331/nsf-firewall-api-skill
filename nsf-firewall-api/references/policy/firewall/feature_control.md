# 6.1.13 根据证书特性和订阅情况控制安全模板

## 简要描述
根据证书特性和订阅情况控制安全模板。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/firewall/feature_control/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/firewall/feature_control/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {
    "ips": true,
    "url_filter": true,
    "content_filter": true,
    "av": true,
    "waf_rule": true
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| ips | bool | IPS功能是否可用 |
| url_filter | bool | URL过滤功能是否可用 |
| content_filter | bool | 内容过滤功能是否可用 |
| av | bool | 防病毒功能是否可用 |
| waf_rule | bool | WAF功能是否可用 |

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：服务器错误",
  "result": {}
}
```

## 使用场景
- 查询设备授权的安全功能模块
- 检查证书支持的安全特性
- 验证订阅服务状态
