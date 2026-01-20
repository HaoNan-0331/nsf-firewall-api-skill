# 6.2.11 删除白名单

## 简要描述
删除白名单。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/wlist/delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | string | 对象ID，多个ID以逗号隔开，不允许重复 |
| ipv6 | 否 | string | ipv6：true(ipv6)/false(ipv4)，默认ipv4 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/wlist/delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": "1", "ipv6": "false"}'
```

## 成功返回示例
```json
{
  "status": "2000",
  "module": "NF",
  "message": "白名单配置 IP地址：[2.4.5.7]、删除成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "白名单配置删除失败"
}
```

## 使用场景
- 删除单条白名单规则
- 批量删除多条白名单
