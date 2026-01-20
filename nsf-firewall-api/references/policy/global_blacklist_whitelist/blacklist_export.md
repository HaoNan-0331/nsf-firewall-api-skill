# 6.2.4 导出黑名单

## 简要描述
导出黑名单。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/globalWb/blist/export/
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
curl -X GET "https://{{host}}/north/nf/strategy/globalWb/blist/export/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "导出黑名单失败"
}
```

## 使用场景
- 导出黑名单到文件
- 备份黑名单配置
