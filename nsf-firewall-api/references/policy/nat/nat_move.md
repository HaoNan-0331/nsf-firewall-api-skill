# 6.4.9 移动NAT策略

## 简要描述
移动NAT策略（调整优先级）。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/nat/move/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| move_type | 否 | string | 移动类型：top(置顶)/bottom(置底) |
| transfer_nat1 | 是 | int | 源策略id |
| transfer_nat2 | 否 | int | 目标策略id（move_type和transfer_nat2不能同时为空或同时存在） |
| type | 是 | string | 类型 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/nat/move/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"transfer_nat1": 1, "transfer_nat2": "2", "type": "snat"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "移动：test12345->test2222 成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：移动 NAT 错误",
  "result": {}
}
```

## 使用场景
- 调整NAT策略优先级顺序
- 将策略置顶或置底
- 移动策略到指定位置
