# 6.2.7 更新黑白名单全局控制是否记录日志

## 简要描述
更新黑白名单全局控制日志开关配置。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/globalWb/blist/global_config_update/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| black_log_enable | 是 | int | 启用黑名单日志：1(开启)/0(关闭) |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/globalWb/blist/global_config_update/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"black_log_enable": "1"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "全局配置成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "[后台]-全局配置失败"
}
```

## 使用场景
- 开启/关闭黑名单日志记录
- 全局日志配置管理
