# 6.1.14 获取防火墙策略组

## 简要描述
获取防火墙策略组。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/firewall/group/info/
```

## 请求方式
```
GET
```

## 请求Query参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（>0或=-1，默认为10） |
| page | 否 | int | 页数（>0，默认为1） |
| search | 否 | string | 查询关键字，长度≤50 |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/firewall/group/info/?size=10&page=1" \
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
    "total": 2,
    "list": [
      {
        "id": 4,
        "name": "group2",
        "backend_id": 0,
        "comment": "test123",
        "rule": []
      },
      {
        "id": 5,
        "name": "group3",
        "backend_id": 1,
        "comment": "test1232",
        "rule": []
      }
    ]
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 策略组id |
| name | string | 策略组名称 |
| backend_id | int | 后端id |
| comment | string | 备注 |
| rule | array | 策略列表 |
| rule.backend_id | int | 后端id |
| rule.name | string | 策略名称 |
| rule.action | string | 策略动作 |
| rule.s_safety_zone | string | 策略源安全区域 |
| rule.d_safety_zone | string | 策略目的安全区域 |

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
- 查询所有策略组
- 分页浏览策略组列表
- 搜索特定策略组
