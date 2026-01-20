# 6.4.4 获取NAT策略总览

## 简要描述
获取NAT策略总览（树形结构）。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/nat/tree/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/nat/tree/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "获取成功",
  "result": [
    {
      "id": 1,
      "name": "test1234",
      "nat_type": 0
    },
    {
      "id": 2,
      "name": "test2222",
      "nat_type": 1
    },
    {
      "id": 3,
      "name": "tt3333",
      "nat_type": 2
    }
  ]
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 策略ID |
| name | string | 策略名称 |
| nat_type | int | 策略类型(0:源NAT策略/1:目的NAT策略/2:双向NAT策略) |

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
- 获取所有NAT策略列表
- 查看策略类型分布
- 快速浏览策略总览
