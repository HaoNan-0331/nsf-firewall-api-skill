# 6.1.15 新建/编辑防火墙策略组

## 简要描述
新建或编辑防火墙策略组。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/group/configuration/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| command | 是 | string | 命令：create(创建)/edit(编辑) |
| id | 否 | int | 策略组id号（command为edit时必填） |
| name | 是 | string | 策略组名称，长度1-32字符，特殊字符只支持-_，名称唯一，不能以特殊字符开头 |
| comment | 否 | string | 备注，长度1-64字符，特殊字符支持~! |
| rule | 否 | array | 策略id列表，最多32条策略 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/group/configuration/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "create",
    "comment": "sdfasdf",
    "name": "group333",
    "rule": []
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "新建防火墙策略组 xx 成功",
  "result": {}
}
```

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
- 创建新的策略组
- 编辑已有策略组
- 将策略添加到策略组
