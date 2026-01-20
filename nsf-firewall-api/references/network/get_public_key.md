# 获取加密公钥

## 简要描述
获取PPPOE接口用户名和密码加密公钥。

## 请求URL
```
GET https://{{host}}/north/nf/network/public_key/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/network/public_key/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "操作成功",
  "result": {
    "type": "RSA",
    "public_key": "",
    "encryption_logic": ""
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| type | string | 加密方式 |
| public_key | string | 公钥 |
| encryption_logic | string | 加密逻辑 |

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
- 配置PPPOE接口前获取公钥
- 加密PPPOE用户名和密码
- 安全传输凭据信息
