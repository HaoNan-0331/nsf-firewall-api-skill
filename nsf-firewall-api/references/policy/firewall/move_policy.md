# 6.1.8 移动防火墙策略

## 简要描述
移动防火墙策略。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/move/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| dstRuleId | 是 | string | 现在的位置（type和dstRuleId不能同时为空，也不能同时存在） |
| srcRuleId | 是 | string | 原来的位置（srcRuleId和dstRuleId不能相同） |
| type | 否 | string | 移动类型：top(置顶)/bottom(置底)（type和dstRuleId不能同时为空，也不能同时存在） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/move/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"srcRuleId": "2", "dstRuleId": "1"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：移动防火墙策略 xxx 失败",
  "result": {}
}
```

## 使用场景
- 调整策略优先级顺序
- 将策略置顶或置底
- 移动策略到指定位置
