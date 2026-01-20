# 应用配置 - API参考文档

## 应用配置

### 简要描述
应用配置接口，用于触发防火墙配置的下发和应用。

### 请求URL
```
POST https://{{host}}/north/nf/strategy/apply/application/
```

### 请求方式
```
POST
```

### 请求参数
| 参数 | 类型 | 必选 | 说明 |
|------|------|------|------|
| - | - | - | 无需参数 |

### 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/apply/application/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

### 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "应用配置成功",
  "result": {}
}
```

### 失败返回示例
```json
{
  "status": 2001,
  "module": "NF",
  "message": "操作失败：应用配置失败",
  "result": {}
}
```

### 状态码说明
| status | 说明 |
|--------|------|
| 2000 | 应用配置成功 |
| 2001 | 应用配置失败 |

### 使用场景
- 在完成策略、对象等配置修改后，需要调用此接口使配置生效
- 批量配置操作完成后统一应用配置
