# 4.1.4 设置联动地址

## 简要描述
设置防火墙的联动地址，用于与安全管理平台通信。

## 请求URL
```
POST https://{{host}}/north/nf/collaboration/security_platform/set/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| local_addr | 是 | string | 本地IP地址（IPv4地址不带掩码） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/collaboration/security_platform/set/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"local_addr": "192.168.1.1"}'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "联动地址设置成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误: 联动地址设置失败"
}
```

## 使用场景
- 配置本地联动IP地址
- 建立与管理平台的通信基础
