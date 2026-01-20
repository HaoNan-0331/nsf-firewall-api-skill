# 获取安全区信息

## 简要描述
获取安全区信息，支持分页和搜索。

## 请求URL
```
GET https://{{host}}/north/nf/network/zone/
```

## 请求方式
```
GET
```

## 请求参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（>0或=-1，=-1时查询全部数据，默认为10） |
| page | 否 | int | 页数（>0，默认为1） |
| search | 否 | string | 查询内容（字符串长度≤50） |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/network/zone/?size=10&page=1" \
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
    "total": 6,
    "list": [
      {
        "id": 0,
        "name": "TRUST",
        "message": "",
        "type": "default",
        "interface": [
          "G1/1",
          "G1/2",
          "G1/1.1"
        ]
      }
    ],
    "ha": false
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 安全区编号 |
| name | string | 安全区名称 |
| message | string | 描述 |
| type | string | 安全区类型（default：系统，customize：自定义） |
| interface | array | 安全区关联接口 |

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：异常错误",
  "result": {}
}
```

## 使用场景
- 查看所有安全区配置
- 查询安全区关联的接口
- 安全区信息巡检
