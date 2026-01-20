# 6.2.14 清空白名单

## 简要描述
清空所有白名单。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/globalWb/wlist/clear/
```

## 请求方式
```
GET
```

## 请求Query参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| ipv6 | 否 | string | ipv6：true(ipv6)/false(ipv4)，默认ipv4 |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/globalWb/wlist/clear/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "操作成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "[后台]-操作失败"
}
```

## 使用场景
- 清空所有白名单规则
- 重置白名单配置
