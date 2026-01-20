# 4.1.2 创建/编辑/连接/断开智能安全运营平台(ISOP)

## 简要描述
创建、编辑、连接或断开智能安全运营平台(ISOP)。

## 请求URL
```
POST https://{{host}}/north/nf/collaboration/security_platform/update/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | int | 管理平台id，-1时为新增 |
| type | 是 | string | 管理中心类型：isop（智能安全运营平台） |
| addr | 是 | string | 服务器地址（IPv4地址不带掩码） |
| port | 是 | string | 端口号（0~65535） |
| enable | 是 | bool | 是否连接（true：启用，false：禁用） |
| isop_block | 是 | string | 一键封堵开关（true：开，false：关） |
| log_switch | 是 | array | 日志发送模板，1-4为必选：<br>1. heart_beats（设备心跳信息）<br>2. dev_status（设备状态信息）<br>3. dev_version（设备版本信息）<br>4. dev_license（设备证书信息）<br>5. fw_log（防火墙日志）<br>6. ips_log（入侵防护日志）<br>7. av_log（防病毒日志）<br>8. scm_log（内容过滤日志）<br>9. url_log（URL过滤日志）<br>10. vpn_log（VPN日志）<br>11. auth_log（认证日志）<br>12. sys_log（系统日志） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/collaboration/security_platform/update/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": -1,
    "type": "isop",
    "addr": "12.1.1.1",
    "port": "443",
    "enable": true,
    "isop_block": "false",
    "log_switch": ["heart_beats", "dev_status", "dev_version", "dev_license"]
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "安全管理中心配置成功",
  "result": {
    "errorCode": 0,
    "errMsg": "Command Success.",
    "status": "Success",
    "id": "0"
  }
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误: 安全管理中心配置失败"
}
```

## 使用场景
- 新增ISOP管理平台配置
- 修改已有ISOP平台的连接参数
- 启用/禁用ISOP连接和一键封堵功能
- 配置设备信息上报
