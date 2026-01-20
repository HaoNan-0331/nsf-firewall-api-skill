# 总览 - API参考文档

## 获取系统状态信息

### 简要描述
获取防火墙系统的运行状态信息，包括CPU、内存、磁盘、风扇等硬件状态。

### 请求URL
```
GET https://{{host}}/north/nf/overview/info/
```

### 请求方式
```
GET
```

### 请求参数
| 参数 | 类型 | 必选 | 说明 |
|------|------|------|------|
| - | - | - | 无需参数 |

### 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/overview/info/" \
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
    "mode": "单机",
    "cpu_temperature": "42.0°C",
    "cpu_utilization": "13.33%",
    "disk_utilization": "23.4%",
    "disk_size": "128GB",
    "disk_employ": "30GB",
    "fan_speed": "3512RPM",
    "data_disk_utilization": "0.00%",
    "data_disk_size": "0.0KB",
    "data_disk_employ": "0.0KB",
    "memory_utilization": "50.00%",
    "disk_exists": false,
    "log_utilization": {
      "total": "500M",
      "use_size": "135.71M",
      "storage_rate": 80
    }
  }
}
```

### 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| mode | string | 部署模式（如：单机/集群） |
| cpu_temperature | string | CPU温度 |
| cpu_utilization | string | CPU使用率 |
| disk_utilization | string | 硬盘使用率 |
| disk_size | string | 磁盘容量大小 |
| disk_employ | string | 磁盘已使用容量 |
| fan_speed | string | 风扇转速 |
| data_disk_utilization | string | 数据盘使用率 |
| data_disk_size | string | 数据盘容量大小 |
| data_disk_employ | string | 数据盘已使用容量 |
| memory_utilization | string | 内存使用率 |
| disk_exists | boolean | 是否有硬盘 |
| log_utilization | object | 日志存储信息 |
| log_utilization.total | string | 日志存储总容量 |
| log_utilization.use_size | string | 日志存储已使用容量 |
| log_utilization.storage_rate | int | 日志存储使用率（百分比） |

### 失败返回示例
```json
{
  "status": 8302,
  "module": "NF",
  "message": "资源未找到: 数据库不存在"
}
```

### 状态码说明
| status | 说明 |
|--------|------|
| 2000 | 获取成功 |
| 8302 | 资源未找到 |

### 使用场景
- 系统健康状态监控
- 资源使用率巡检
- 故障诊断时查看系统状态
