# 7.5.2 新建/编辑网络对象

## 简要描述
新建或编辑网络对象。

## 请求URL
```
POST https://{{host}}/north/nf/object/networkobj/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| action | 是 | string | 动作：create(创建)/edit(编辑) |
| id | 否 | number | 网络对象id（编辑时必填） |
| name | 是 | string | 名称，长度1-64字符，特殊字符只支持-_，名称唯一，不能以特殊字符开头 |
| note | 否 | string | 备注，长度0-64字符，首尾不能有空格 |
| type | 是 | string | 网络对象类型：segment(子网)/node(节点)/pool(地址池)/mac(mac地址)/group(地址组)/domain(域名组) |
| ip_address | 否 | string | IP地址（type为node/segment/pool时必选） |
| mac | 否 | string | MAC地址（合法的6段式mac地址，以:或-为分割符，分割符不能混用） |
| domain | 否 | string | 域名（支持多个域名用回车分割，最多128个域名，支持通配符*） |
| contain_object | 否 | string | 包含对象，支持多个用逗号分隔（合法的节点/子网/地址池/mac地址名称，不能重复） |
| is_ipv6 | 否 | boolean | 是否ipv6（与group参数联合使用） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/object/networkobj/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "create",
    "id": 1,
    "name": "test",
    "note": "test",
    "type": "segment",
    "ip_address": "192.168.1.0/24",
    "mac": "AC:19:8E:F8:AD:73",
    "domain": "*.ip.com",
    "contain_object": "test1,test2",
    "is_ipv6": false
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {
    "id": 1,
    "type": "segment",
    "name": "test112",
    "ip_address": "192.122.1.0/24",
    "negation": false,
    "note": "ippdee",
    "backend_id": "1"
  }
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
- 创建新的网络对象（子网/节点/地址池/MAC/地址组/域名组）
- 编辑已有网络对象
- 配置地址对象用于策略引用
