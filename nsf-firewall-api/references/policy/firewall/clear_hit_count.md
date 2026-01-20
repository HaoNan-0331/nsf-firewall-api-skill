# 6.1.4 清空防火墙策略命中次数

## 简要描述
清空防火墙策略命中次数。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/firewall/clear_hit_count/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | string | 策略id号，多个id使用逗号隔开 |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/firewall/clear_hit_count/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"id": "1,3,4"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "清空防火墙命中计数成功",
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
- 重置策略命中统计
- 清理历史命中数据
