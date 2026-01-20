# 7.6.1 获取服务对象

## 简要描述
获取服务对象列表。

## 请求URL
```
GET https://{{host}}/north/nf/object/serviceobj/
```

## 请求方式
```
GET
```

## 请求Query参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（默认10，>0或=-1查看全部） |
| page | 否 | int | 页数（默认1，>0） |
| search | 否 | string | 查询关键字，长度≤50 |
| type | 是 | string | 对象类型：all(全部)/custom(自定义服务)/group(服务组)/system(系统服务) |
| exact_fit | 否 | string | 精准查询：true/false |
| name | 否 | string | 服务名称，长度0-30字符，特殊字符只支持_-\.:/和空格 |
| protocol | 否 | string | 服务协议：TCP/UDP/IP/ICMPV6/ICMP |
| port | 否 | string | 服务端口，范围1-65535，多个用逗号隔开，长度不超过10 |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/object/serviceobj/?type=all&size=10&page=1" \
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
    "total": 0,
    "list": []
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| contain_object | string | 服务对象（对象名称，多个以逗号隔开） |
| d_port | string | 目的端口 |
| id | int | 对象ID |
| ip_protocol_type | string | IP协议类型 |
| name | string | 名称 |
| note | string | 备注 |
| protocol | string | 协议 |
| s_port | string | 源端口 |
| type | string | 类型（system:系统/custom:自定义/group:服务组） |

## 失败返回示例
```json
{
  "status": 8201,
  "module": "NF",
  "message": "数据类型不合规: page参数必须为数字"
}
```

## 使用场景
- 查询所有服务对象
- 按类型筛选服务（自定义/服务组/系统服务）
- 按协议和端口筛选
- 分页浏览服务对象列表
