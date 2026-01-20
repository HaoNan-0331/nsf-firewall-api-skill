# 3.4 系统配置

## 3.4.1 基本配置

### 3.4.1.1 获取NTP配置信息

#### 简要描述
获取系统NTP时间同步配置。

#### 请求URL
```
GET https://{{host}}/north/nf/system/ntp/config/
```

#### 请求方式
```
GET
```

#### 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/system/ntp/config/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

#### 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {
    "syncSwitch": "off",
    "ntpServer": "0.0.0.0",
    "syncInterval": "3600",
    "authSwitch": "off",
    "authAlgorithm": "md5",
    "authKeyPath": "/opt/nsfocus/product/etc/ntp/"
  }
}
```

#### 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| syncSwitch | string | 同步NTP开关（on/off） |
| ntpServer | string | NTP服务器地址 |
| syncInterval | string | 同步间隔（秒） |
| authSwitch | string | NTP认证开关（on/off） |
| authAlgorithm | string | 认证算法（md5） |
| authKeyPath | string | NTP密钥目录 |

#### 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "ntp配置异常"
}
```

---

### 3.4.1.2 编辑NTP配置信息

#### 简要描述
修改系统NTP时间同步配置。

#### 请求URL
```
POST https://{{host}}/north/nf/system/ntp/config/
```

#### 请求方式
```
POST
```

#### 请求参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| syncSwitch | 是 | string | 同步NTP开关（on：开启，off：关闭） |
| ntpServer | 是 | string | NTP服务器（支持IPv4/IPv6不带掩码、域名） |
| syncInterval | 是 | int | 同步间隔（秒），范围0~86400 |
| authSwitch | 是 | string | NTP认证开关（on：开启，off：关闭） |
| authAlgorithm | 否 | string | 认证算法（md5） |
| file | 否 | file | NTP密钥文件，大小不超过1M |

#### 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/system/ntp/config/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "syncSwitch": "on",
    "ntpServer": "ntp.aliyun.com",
    "syncInterval": "3600",
    "authSwitch": "off"
  }'
```

#### 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "ntp配置成功",
  "result": {}
}
```

#### 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "ntp配置异常"
}
```

---

## 使用场景
- **NTP时间同步**：配置NTP服务器确保系统时间准确
- **时间管理**：统一管理多台设备的时间，避免时间漂移
