# 6.2.16 提交黑白名单全局控制是否记录class日志

## 简要描述
提交黑白名单全局控制是否记录class日志。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/configuration/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| enable | 是 | int | 启用：1(开启)/0(关闭) |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/configuration/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"enable": 1}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "配置下发成功",
  "result": {
    "enable": 0
  }
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "配置下发失败"
}
```

## 使用场景
- 开启/关闭class日志记录
