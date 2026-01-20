# 7.5.3 获取网络对象总览

## 简要描述
获取网络对象总览（按类型统计）。

## 请求URL
```
GET https://{{host}}/north/nf/object/network_obj_referenced/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/object/network_obj_referenced/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": [
    {
      "title": "对象总览",
      "total": 3,
      "using": 1
    },
    {
      "title": "节点对象",
      "total": 0,
      "using": 0
    },
    {
      "title": "网络对象",
      "total": 3,
      "using": 1
    },
    {
      "title": "地址池",
      "total": 0,
      "using": 0
    },
    {
      "title": "MAC地址",
      "total": 0,
      "using": 0
    },
    {
      "title": "地址组",
      "total": 0,
      "using": 0
    },
    {
      "title": "域名组",
      "total": 0,
      "using": 0
    }
  ]
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| title | string | 名称 |
| total | int | 总数 |
| using | int | 使用中 |

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
- 查看各类型网络对象数量统计
- 查看对象使用情况
- 对象资源概览
