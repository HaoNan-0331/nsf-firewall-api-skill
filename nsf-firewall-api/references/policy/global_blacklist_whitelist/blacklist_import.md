# 6.2.5 导入黑名单

## 简要描述
导入黑名单。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/blist/upload/
```

## 请求方式
```
POST
```

## 请求Body参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| file | 是 | file | 文件名，.csv格式，大小≤2.5M |
| ipv6 | 否 | string | ipv6：true(ipv6)/false(ipv4)，默认ipv4 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/blist/upload/" \
  -H "Authorization: <your-token>" \
  -F "file=@blacklist.csv" \
  -F "ipv6=false"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "导入 1 条黑名单成功"
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "导入黑名单失败"
}
```

## 使用场景
- 批量导入黑名单
- 从备份文件恢复黑名单
