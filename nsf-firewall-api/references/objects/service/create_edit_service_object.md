# 7.6.2 新建/编辑服务对象

## 简要描述
新建或编辑服务对象。

## 请求URL
```
POST https://{{host}}/north/nf/object/serviceobj/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| action | 是 | string | 新建/编辑：create(新建)/edit(编辑)，新建时不能超过规格(默认5000) |
| d_port | 否 | string | 目的端口，0~65535，单个端口号或以-连接的端口号范围（协议为TCP/UDP时必填） |
| ip_protocol_type | 否 | string | IP协议类型：ip/esp/ah/gre（协议等于IP时必填） |
| name | 是 | string | 名称，长度1-64字节，名称唯一，特殊字符只支持_-\.:/，不能以特殊字符开头 |
| note | 否 | string | 备注，长度0-64字符，特殊字符支持~!#$%^*()-_{}:;/.和@ |
| protocol | 否 | string | 协议：TCP/UDP/IP（类型为custom时必填） |
| s_port | 否 | string | 源端口，0~65535，单个端口号或以-连接的端口号范围（协议为TCP/UDP时必填） |
| type | 是 | string | 类型：custom(自定义服务)/group(服务组) |
| contain_object | 否 | string | 服务对象，最多引用128个服务对象，多个以逗号隔开（类型为group时必填） |
| id | 否 | string | 对象ID（action='edit'时必填） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/object/serviceobj/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "create",
    "type": "custom",
    "name": "wewe",
    "protocol": "TCP",
    "s_port": "54",
    "d_port": "67",
    "ip_protocol_type": "ip",
    "note": "dd",
    "contain_object": "",
    "id": ""
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "新建自定义服务对象 wdwdw 成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8204,
  "module": "NF",
  "message": "范围不合规: action参数值有误"
}
```

## 使用场景
- 创建自定义服务对象
- 创建服务组
- 编辑已有服务对象
