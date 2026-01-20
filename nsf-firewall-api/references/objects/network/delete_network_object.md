# 7.5.4 删除网络对象

## 简要描述
删除网络对象。

## 请求URL
```
POST https://{{host}}/north/nf/object/networkobj_delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | string | 网络对象id号，多个id使用逗号隔开（all表示清空所有对象，需和type一起使用） |
| type | 否 | string | 网络对象类型：segment(子网)/node(节点)/pool(地址池)/mac(mac地址)/group(地址组)/domain(域名组) |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/object/networkobj_delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": "1,3,4"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "删除 xx 对象成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 4000,
  "module": "NF",
  "message": "底层错误：删除 xx 对象失败",
  "result": {}
}
```

## 使用场景
- 删除单个网络对象
- 批量删除多个对象
- 清空指定类型的所有对象
