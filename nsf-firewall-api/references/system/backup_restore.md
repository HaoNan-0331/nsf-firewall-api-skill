# 3.1 备份恢复

## 3.1.1 下载配置备份文件

### 简要描述
下载防火墙配置备份文件。

### 请求URL
```
GET https://{{host}}/north/nf/system/backup/
```

### 请求方式
```
GET
```

### 请求参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| type | 是 | string | 备份类型，取值范围：all（全部备份文件） |

### 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/system/backup/?type=all" \
  -H "Authorization: <your-token>"
```

### 成功返回示例
```json
{}
```

### 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：备份全部配置文件失败"
}
```

---

## 3.1.2 上传配置文件

### 简要描述
上传配置文件以恢复系统配置。

### 请求URL
```
POST https://{{host}}/north/nf/system/_recover_package/
```

### 请求方式
```
POST
```

### 请求参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| file | 是 | file | 配置文件，限制：文件大小不超过50M，文件类型为.bak |

### 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/system/_recover_package/" \
  -H "Authorization: <your-token>" \
  -F "file=@backup.bak"
```

### 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "恢复系统文件校验成功",
  "result": {
    "check_code": 0
  }
}
```

### 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：系统备份恢复失败"
}
```

---

## 3.1.3 确认系统恢复

### 简要描述
确认执行系统恢复操作。

### 请求URL
```
GET https://{{host}}/north/nf/system/confirm_recover/
```

### 请求方式
```
GET
```

### 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/system/confirm_recover/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

### 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "系统恢复成功"
}
```

### 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：系统恢复失败"
}
```

---

## 3.1.4 获取数据恢复的进度数据

### 简要描述
获取系统数据恢复的实时进度信息。

### 请求URL
```
GET https://{{host}}/north/nf/system/recover_progress/
```

### 请求方式
```
GET
```

### 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/system/recover_progress/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

### 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {
    "status": 0,
    "percent": 0,
    "data": []
  }
}
```

### 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| result.status | int | 执行状态：1-恢复完成，2-进行中，3-恢复失败，0-未执行恢复 |
| result.percent | int | 完成进度（百分比） |
| result.data | object | 数据详细 |
| result.data[].msg | string | 提示信息 |
| result.data[].label | string | 同步时间 |
| result.data[].status | string | 状态信息 |

### 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：系统恢复失败"
}
```

---

## 使用场景
- **定期备份**：定期下载配置备份文件，防止配置丢失
- **配置迁移**：将配置从一台设备迁移到另一台设备
- **灾难恢复**：系统故障时通过备份文件快速恢复
- **恢复监控**：实时查看恢复进度，确保操作顺利完成
