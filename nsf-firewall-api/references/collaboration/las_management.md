# 4.1.3 创建/编辑/连接/断开日志审计系统(LAS)

## 简要描述
创建、编辑、连接或断开日志审计系统(LAS)。

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
| type | 是 | string | 管理中心类型：las（日志审计系统） |
| addr | 是 | string | 服务器地址（IPv4地址不带掩码） |
| port | 是 | string | 端口号（0~65535） |
| enable | 是 | bool | 是否连接（true：启用，false：禁用） |
| log_switch | 是 | array | 日志发送模板，1和2为必选项：<br>1. heart_beats（设备心跳信息）<br>2. dev_status（设备状态信息）<br>3. fw_log（防火墙日志）<br>4. ips_log（入侵防护日志）<br>5. av_log（防病毒日志）<br>6. scm_log（内容过滤日志）<br>7. url_log（URL过滤日志）<br>8. vpn_log（VPN日志）<br>9. auth_log（认证日志）<br>10. sys_log（系统日志） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/collaboration/security_platform/update/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": -1,
    "type": "las",
    "addr": "12.22.2.2",
    "port": "443",
    "enable": true,
    "log_switch": ["heart_beats", "dev_status"]
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
- 新增LAS日志审计系统配置
- 修改已有LAS平台的连接参数
- 启用/禁用LAS连接
- 配置日志上报类型
