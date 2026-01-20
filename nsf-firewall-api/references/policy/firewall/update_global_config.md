# 6.1.12 防火墙策略全局配置更新

## 简要描述
防火墙策略全局配置更新。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/global_config/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| defaultAction | 是 | int | 默认阻断是否开启：1-关闭/2-开启，默认1 |
| isDnatOrgIp | 是 | int | 策略匹配DNAT设置：0-内部IP地址/1-外部IP地址，默认0 |
| isSnatOrgIp | 是 | int | 策略匹配SNAT设置：0-转换后地址/1-转换前地址，默认0 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/global_config/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"isSnatOrgIp": 0, "isDnatOrgIp": 0, "defaultAction": 2}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {}
}
```

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
- 修改默认动作（放行/阻断）
- 配置NAT策略匹配方式
- 全局策略配置调整
