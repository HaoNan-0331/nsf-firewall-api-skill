# 6.2.2 新建/编辑黑名单

## 简要描述
新建或编辑黑名单。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/blist/configuration/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 否 | string | 对象ID（action='edit'时必填） |
| action | 是 | string | 新建/编辑：create(新建)/edit(编辑) |
| ip | 否 | string | IP地址（objectType=ip时必填） |
| type | 是 | string | 类型：sourceIp(源地址)/destIp(目的地址)，编辑时不可修改 |
| protocol | 是 | string | 协议：any/TCP/UDP/ICMP/IP |
| port | 否 | string | 端口：any或1-65535 |
| objectType | 是 | string | 对象类型：ip(ip地址)/object(对象)，ipv6时只能为ip |
| zone | 否 | string | 地理对象ID（objectType='object'时必填，长度≤526） |
| ipv6 | 否 | string | ipv6类型：true(ipv6)/false(ipv4)，默认ipv4 |
| time | 否 | string | 开始时间，格式yyyy-mm-dd hh:mm:ss（is_time='t'时必填） |
| endtime | 否 | string | 结束时间，格式yyyy-mm-dd hh:mm:ss（is_time='t'时必填） |
| is_time | 是 | string | 时间段：t(开启)/f(关闭) |
| status | 否 | boolean | 启用状态：True(开启)/False(关闭) |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/blist/configuration/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "sourceIp",
    "ip": "12.12.1.2",
    "protocol": "any",
    "objectType": "ip",
    "port": "any",
    "is_time": "f",
    "time": 0,
    "endtime": 0,
    "action": "create",
    "source": "user"
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "新建黑名单 [12.12.1.3] 成功",
  "result": [10001]
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
- 添加IP地址到黑名单
- 编辑已有黑名单规则
- 配置带时间限制的黑名单
