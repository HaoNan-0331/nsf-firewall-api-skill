# 7.6.3 获取服务对象名称ID

## 简要描述
获取服务对象名称ID列表。

## 请求URL
```
GET https://{{host}}/north/nf/object/serviceobj/get_app_obj_ids/
```

## 请求方式
```
GET
```

## 请求Query参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| type | 是 | string | 对象类型：system/custom |
| name | 否 | string | 服务名称，长度0-30字符，特殊字符只支持_-\.:/和空格 |
| protocol | 否 | string | 服务协议：TCP/UDP/IP/ICMPV6/ICMP |
| port | 否 | string | 服务端口，范围1-65535，多个用逗号隔开，长度不超过10 |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/object/serviceobj/get_app_obj_ids/?type=system" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": [
    "echo[t]",
    "discard[t]"
  ]
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "操作失败"
}
```

## 使用场景
- 根据名称查询服务对象ID
- 批量获取服务对象标识
- 服务对象名称解析
