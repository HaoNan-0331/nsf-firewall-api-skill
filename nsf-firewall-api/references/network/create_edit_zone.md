# 创建/编辑安全区

## 简要描述
创建或编辑安全区。

## 请求URL
```
POST https://{{host}}/north/nf/network/zone/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| name | 是 | string | 名称（长度1-32字符，支持中英文、数字及特殊字符-_.，不能以特殊字符开头，编辑时不允许修改） |
| comment | 是 | string | 备注（长度0-128字符，支持中英文、数字及特殊字符-_.，不能以特殊字符开头） |
| action | 是 | string | 动作：create（创建）/edit（编辑） |
| zone_type | 否 | int | 安全区编号（存在的安全区编号，编辑时必选） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/zone/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "testddd",
    "comment": "11113ddds",
    "type": "customize",
    "action": "edit",
    "zone_type": 6
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "编辑安全区 testddd 成功",
  "result": {}
}
```

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
- 创建自定义安全区
- 编辑安全区描述信息
- 修改安全区关联配置
