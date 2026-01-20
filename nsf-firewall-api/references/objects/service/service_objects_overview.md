# 7.6.4 获取服务对象总览

## 简要描述
获取服务对象总览（按类型统计）。

## 请求URL
```
GET https://{{host}}/north/nf/object/service_obj_referenced/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/object/service_obj_referenced/" \
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
    "overview": {
      "total_num": 100,
      "total_reference_num": 0,
      "system_num": 98,
      "system_reference_num": 0,
      "custom_num": 2,
      "custom_reference_num": 0,
      "group_num": 0,
      "group_reference_num": 0
    }
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| total_num | int | 服务总数 |
| total_reference_num | int | 服务引用总数 |
| system_num | int | 系统服务总数 |
| system_reference_num | int | 系统服务引用数 |
| custom_num | int | 自定义服务总数 |
| custom_reference_num | int | 自定义服务引用数 |
| group_num | int | 服务组总数 |
| group_reference_num | int | 服务组引用数 |

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "数据库不存在"
}
```

## 使用场景
- 查看各类型服务对象数量统计
- 查看服务对象使用情况
- 服务资源概览
