# 6.1.11 获取防火墙策略全局配置信息

## 简要描述
获取防火墙策略全局配置信息。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/firewall/global_info/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/firewall/global_info/" \
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
    "isDnatOrgIp": 0,
    "isSnatOrgIp": 0,
    "defaultAction": 2,
    "isHandleLocal": 1,
    "isHandleInnerIp": 1,
    "vsysId": 0
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| isDnatOrgIp | int | 策略匹配DNAT设置：0-内部IP地址/1-外部IP地址 |
| isSnatOrgIp | int | 策略匹配SNAT设置：0-转换后地址/1-转换前地址 |
| defaultAction | int | 默认阻断是否开启：1-关闭/2-开启 |
| isHandleLocal | int | 是否处理本地流量 |
| isHandleInnerIp | int | 是否处理内部IP |
| vsysId | int | 虚拟系统id |

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：获取失败",
  "result": {}
}
```

## 使用场景
- 查看防火墙策略全局配置
- 获取默认动作设置
- 查看NAT策略匹配设置
