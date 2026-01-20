# 7.6.5 删除服务对象

## 简要描述
删除服务对象。

## 请求URL
```
POST https://{{host}}/north/nf/object/serviceobj_delete/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | string | 对象ID，='all'时清除所有type指定类型的服务对象，或一个/多个整数以逗号隔开，不允许重复值 |
| type | 否 | string | 类型：custom(自定义服务)/group(服务组)/system(系统服务)，id='all'时必填 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/object/serviceobj_delete/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": "600099"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "删除服务对象成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8302,
  "module": "NF",
  "message": "资源未找到: 不存在该值为32的数据无法删除"
}
```

## 使用场景
- 删除单个服务对象
- 批量删除多个服务对象
- 清空指定类型的所有服务对象
