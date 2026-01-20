# 3.2 证书信息

## 3.2.1 获取证书信息

### 简要描述
获取防火墙系统中的证书信息列表。

### 请求URL
```
GET https://{{host}}/north/nf/system/cert/info/
```

### 请求方式
```
GET
```

### 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/system/cert/info/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

### 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": []
}
```

### 失败返回示例
```json
{
  "status": 8302,
  "module": "NF",
  "message": "资源未找到：数据库不存在"
}
```

---

## 使用场景
- **证书查看**：查看系统中已安装的证书
- **证书管理**：检查证书有效期和状态
