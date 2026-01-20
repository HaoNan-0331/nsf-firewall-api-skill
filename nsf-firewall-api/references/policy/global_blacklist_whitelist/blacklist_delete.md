# 6.2.3 删除黑名单

## 简要描述
删除黑名单。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/blist/delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | list | 对象ID列表，不允许重复值 |
| ipv6 | 否 | string | ipv6：true(ipv6)/false(ipv4)，默认ipv4 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/blist/delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": [1], "ipv6": "false"}'
```

## 成功返回示例
```json
{
  "status": "2000",
  "module": "NF",
  "message": "黑名单配置 IP地址：[2.4.5.7]、删除成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "黑名单配置删除失败"
}
```

## 使用场景
- 删除单条黑名单规则
- 批量删除多条黑名单
