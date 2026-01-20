# 6.1.2 新建/编辑防火墙策略

## 简要描述
新建或编辑防火墙策略。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/configuration/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| command | 是 | string | 命令：create(新建)/edit(编辑) |
| id | 否 | int | 策略id（编辑时必填） |
| backend_id | 否 | string | 后端id |
| name | 是 | string | 防火墙策略名称，长度1-64字符，特殊字符只支持-_，名称唯一，不能以特殊字符开头 |
| group | 否 | string | 策略分组（参数是策略组id） |
| s_safety_zone | 是 | array | 源安全区，支持最大64个对象（参数是对象名称） |
| d_safety_zone | 是 | array | 目的安全区，支持最大64个对象（参数是对象名称） |
| s_address | 是 | array | 源地址对象，支持最多32个对象或对象组，参数是对象id |
| d_address | 是 | array | 目的地址对象，支持最多32个对象或对象组，参数是对象id |
| service | 是 | array | 服务对象，支持最多32个服务或服务组，参数是对象id |
| application | 否 | array | 应用对象，支持最多128个应用对象或应用组，参数是对象id |
| time | 是 | array | 生效时间，支持最多32个时间对象或对象组，参数是对象id |
| action | 是 | string | 动作：1-放行/2-阻断 |
| log | 否 | string | 日志记录：0-关闭/1-开启，默认0 |
| ipv6Enable | 否 | int | 配置ipv6策略：0-ipv4/1-ipv6，不传参根据源目的对象类型确定 |
| longLinkEnable | 是 | bool | 开启长连接：false(关闭)/true(开启) |
| longLinkAgeTime | 否 | int | 长连接老化时间，1-24000(分钟)，longLinkEnable=true时必填 |
| isForbidden | 是 | int | 是否禁用：0-启用/1-禁用 |
| ips | 否 | string | IPS模板（模板数字id，证书具有对应功能） |
| obmModule | 否 | string | 上网行为管理（模板数字id，证书具有对应功能） |
| sdModule | 否 | string | 敏感数据（模板数字id，证书具有对应功能） |
| mailModule | 否 | string | 邮件安全（模板数字id，证书具有对应功能） |
| url_filter | 否 | string | URL过滤模板（模板数字id，证书具有对应功能） |
| antivirus | 否 | string | 防病毒模板（模板数字id，证书具有对应功能，需开启防病毒引擎） |
| wafModule | 否 | string | WEB应用通用防护模板（模板数字id，证书具有对应功能） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/configuration/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "create",
    "name": "testdoc",
    "group": "",
    "s_safety_zone": ["TRUST"],
    "d_safety_zone": ["TRUST"],
    "s_address": ["100000"],
    "d_address": ["100000"],
    "user": [],
    "service": ["600000"],
    "application": [],
    "time": ["800000"],
    "action": "1",
    "log": "0",
    "ipv6Enable": 0,
    "longLinkEnable": false,
    "session_time": null,
    "safety_protect": "0",
    "hit_count": null,
    "broadband": null,
    "isForbidden": 0,
    "ips": "",
    "obmModule": "",
    "sdModule": "",
    "mailModule": "",
    "url_filter": "",
    "antivirus": "",
    "wafModule": ""
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "新建防火墙策略 xxx 成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：异常错误",
  "result": {}
}
```

## 使用场景
- 创建新的防火墙访问策略
- 修改已有策略的配置
- 配置策略的安全功能模块（IPS、防病毒、URL过滤等）
