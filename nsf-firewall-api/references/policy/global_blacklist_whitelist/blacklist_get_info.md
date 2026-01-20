# 6.2.1 获取黑名单

## 简要描述
获取黑名单列表。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/globalWb/blist/info/
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
| ipv6 | 否 | string | ipv6类型：true(ipv6)/false(ipv4)/默认ipv4 |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/globalWb/blist/info/?size=10&page=1" \
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
    "total": 2,
    "list": [
      {
        "id": 10004,
        "ip": "2.4.5.7",
        "type": "destIp",
        "protocol": "UDP",
        "port": "any",
        "is_time": "f",
        "time": "0",
        "source": "user",
        "hit_count": 0,
        "status": false,
        "config_update_time": "2024-07-03T08:49:20.331617",
        "endtime": "0",
        "ip_type": 1
      }
    ]
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 对象ID |
| ip | string | IP地址 |
| type | string | 类型(sourceIp:源地址/destIp:目的地址) |
| protocol | string | 协议(any/TCP/UDP/ICMP/IP) |
| port | string | 端口 |
| is_time | string | 时间限制类型(t:开启/f:关闭) |
| time | string | 生效时间 |
| source | string | 来源 |
| hit_count | int | 命中次数 |
| status | boolean | 启用状态 |
| config_update_time | string | 创建时间 |
| endtime | string | 结束时间 |
| ip_type | int | IP地址类型(1:网段/2:地址池/3:子网) |

## 失败返回示例
```json
{
  "status": 8201,
  "module": "NF",
  "message": "数据类型不合规: page参数必须为数字"
}
```

## 使用场景
- 查询所有黑名单规则
- 分页浏览黑名单
- 搜索特定IP的黑名单
- 查看黑名单命中统计
