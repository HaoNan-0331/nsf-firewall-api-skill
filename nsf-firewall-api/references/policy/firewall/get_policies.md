# 6.1.1 获取防火墙策略

## 简要描述
获取防火墙策略。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/firewall/info/
```

## 请求方式
```
GET
```

## 请求Query参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（>0或=-1，默认为10） |
| page | 否 | int | 页数（>0，默认为1） |
| search | 否 | string | 查询关键字，长度≤50，查询范围为name,s_safety_zone,d_safety_zone,hit_count,group |
| type | 否 | string | 查看方式：match(匹配顺序)/group(策略分组)/zone(安全区)/create(新建顺序)，默认按匹配优先级查看 |
| is_v6 | 否 | string | 是否ipv6：true(ipv6策略)/false(ipv4策略)/为空(ipv4) |
| searchType | 否 | string | 查询条件：all(模糊查询)/group(条件查询) |
| name | 否 | string | 策略名称（1-64字符，仅searchType为group时生效） |
| zone | 否 | string | 安全区（仅searchType为group时生效） |
| action | 否 | string | 策略动作：1-放行/2-阻断（仅searchType为group时生效） |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/firewall/info/?size=10&page=1&type=match" \
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
    "total": 1,
    "list": [
      {
        "id": 1,
        "priority": 0,
        "name": "test13",
        "backend_id": "1",
        "group": {
          "backend_id": "",
          "name": "未分组"
        },
        "s_safety_zone": "TRUST",
        "d_safety_zone": "UNTRUST",
        "user": "",
        "action": "2",
        "ipv6Enable": false,
        "longLinkEnable": false,
        "longLinkAgeTime": null,
        "log": "0",
        "session_time": "",
        "safety_protect": "",
        "hit_count": 0,
        "isForbidden": 0,
        "broadband": "",
        "s_address": [
          {
            "id": 100000,
            "type": "segment",
            "backend_id": "100000",
            "name": "any"
          }
        ],
        "d_address": [
          {
            "id": 100000,
            "type": "segment",
            "backend_id": "100000",
            "name": "any"
          }
        ],
        "service": [
          {
            "id": 11453,
            "type": "system",
            "backend_id": "600001",
            "name": "echo[t]"
          }
        ],
        "application": [
          {
            "id": 610,
            "type": "system",
            "backend_id": "28191478136176642",
            "name": "Speedtest"
          }
        ],
        "time": [
          {
            "id": 800000,
            "type": "custom",
            "backend_id": "800000",
            "name": "any"
          }
        ],
        "ips": "",
        "obmModule": "",
        "mailModule": "",
        "sdModule": "",
        "wafModule": "",
        "url_filter": "",
        "antivirus": ""
      }
    ]
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 策略id |
| priority | int | 优先级 |
| name | string | 策略名称 |
| backend_id | string | 后端id |
| group | dict | 分组信息 |
| group.backend_id | string | 后端id |
| group.name | string | 分组名称 |
| s_safety_zone | string | 源安全区 |
| d_safety_zone | string | 目的安全区 |
| user | string | 用户 |
| action | string | 策略动作(1-放行,2-阻断) |
| ipv6Enable | bool | 是否ipv6 |
| longLinkEnable | bool | 是否长连接 |
| longLinkAgeTime | int | 长连接时间 |
| log | string | 是否记录(0-不记录,1-记录) |
| session_time | string | 会话时间 |
| safety_protect | string | 安全保护 |
| hit_count | int | 命中次数 |
| isForbidden | int | 是否禁用 |
| s_address | dict | 源地址 |
| s_address.id | int | 地址id |
| s_address.type | string | 地址类型 |
| s_address.backend_id | string | 后端id |
| s_address.name | string | 地址名称 |
| s_address.ip_address | string | 地址ip |
| d_address | dict | 目的地址 |
| d_address.id | int | 地址id |
| d_address.type | string | 地址类型 |
| d_address.backend_id | string | 后端id |
| d_address.name | string | 地址名称 |
| d_address.ip_address | string | 地址ip |
| service | dict | 服务 |
| service.id | int | 服务id |
| service.type | string | 服务类型 |
| service.backend_id | string | 后端id |
| service.name | string | 服务名称 |
| service.protocol | string | 服务协议 |
| service.s_port | string | 服务源端口 |
| service.d_port | string | 服务目的端口 |
| application | array | 应用 |
| time | array | 时间 |
| time.id | int | 时间id |
| time.type | strings | 时间类型 |
| time.backend_id | string | 后端id |
| time.name | string | 时间名称 |
| ips | string | 入侵防护 |
| obmModule | string | 上网行为管理 |
| mailModule | string | 邮件安全 |
| sdModule | string | 敏感数据 |
| wafModule | string | web应用通用防护 |
| url_filter | string | url过滤 |
| antivirus | string | 防病毒 |

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
- 查询防火墙所有策略
- 按条件筛选策略（安全区、动作、名称等）
- 分页浏览策略列表
- 查看策略命中次数
