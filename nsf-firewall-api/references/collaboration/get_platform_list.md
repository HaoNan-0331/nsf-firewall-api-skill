# 4.1.5 获取联动安全管理平台列表

## 简要描述
获取已配置的联动安全管理平台列表。

## 请求URL
```
GET https://{{host}}/north/nf/collaboration/security_platform/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/collaboration/security_platform/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {
    "config": [
      {
        "id": 0,
        "type": "espc",
        "addr": "192.168.100.12",
        "port": "443",
        "enable": true,
        "status": 2,
        "err_msg": "",
        "isop_block": "false",
        "takeover_status": false,
        "is_caa_auth": false,
        "log_switch": ["heart_beats", "dev_status", "fw_log", "url_log"],
        "isopBlockParams": {
          "token": "",
          "name": "",
          "expire": "",
          "port": "8081"
        }
      }
    ],
    "local_addr": "192.168.1.1",
    "npai": {
      "version": "3.2.0.91240513",
      "update_time": "2024-05-14 18:22:22"
    }
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| config | list | 联动安全管理平台列表 |
| config[].id | int | 对象ID值 |
| config[].type | string | 类型（espc/isop/las） |
| config[].addr | string | 安全管理平台地址 |
| config[].port | string | 端口 |
| config[].enable | boolean | 连接/断开状态 |
| config[].status | int | 状态 |
| config[].err_msg | string | 错误信息 |
| config[].isop_block | string | ISOP封堵状态 |
| config[].takeover_status | boolean | 统一管理 |
| config[].is_caa_auth | boolean | 集中授权的联动配置 |
| config[].log_switch | list | 日志发送类型 |
| config[].isopBlockParams | object | ISOP封堵信息 |
| local_addr | string | 本地IP地址 |
| npai | object | 接口信息 |
| npai.version | string | 接口版本 |
| npai.update_time | string | 接口升级时间 |

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误: 安全管理中心数据获取失败"
}
```

## 使用场景
- 查看已配置的所有安全管理平台
- 检查平台连接状态
- 获取本地联动地址配置
