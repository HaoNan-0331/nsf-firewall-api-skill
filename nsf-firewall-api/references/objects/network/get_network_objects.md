# 7.5.1 获取网络对象信息

## 简要描述
获取网络对象信息。

## 请求URL
```
GET https://{{host}}/north/nf/object/networkobj/
```

## 请求方式
```
GET
```

## 请求Query参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（>0或=-1，默认10） |
| page | 否 | int | 页数（>0，默认1） |
| search | 否 | string | 查询关键字，长度≤50 |
| type | 是 | string | 对象类型：segment(子网)/node(节点)/pool(地址池)/mac(mac地址)/group(地址组)/domain(域名组)/all(所有类型) |
| is_v6 | 否 | string | 是否ipv6：true(是)/false(否)/undefined(全部) |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/object/networkobj/?type=all&size=10&page=1" \
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
    "total": 3,
    "list": [
      {
        "id": 100000,
        "backend_id": "100000",
        "name": "any",
        "type": "segment",
        "ip_address": "0.0.0.0/0",
        "mac": "",
        "domain": "",
        "contain_object": "",
        "negation": false,
        "note": "Default",
        "is_ipv6": false
      }
    ]
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 对象id |
| backend_id | string | 后端id |
| name | string | 对象名称 |
| type | string | 对象类型 |
| ip_address | string | ip地址 |
| mac | string | mac地址 |
| domain | string | 域名 |
| contain_object | string | 包含对象 |
| negation | bool | 是否取反 |
| note | string | 备注 |
| is_ipv6 | bool | 是否ipv6 |

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
- 查询所有网络对象
- 按类型筛选对象（子网/节点/地址池/MAC/地址组/域名组）
- 分页浏览对象列表
- 搜索特定对象
