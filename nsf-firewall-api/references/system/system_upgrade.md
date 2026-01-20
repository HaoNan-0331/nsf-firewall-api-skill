# 3.3 系统升级

## 3.3.1 系统升级上传文件

### 简要描述
上传系统升级包文件，支持多种类型的升级包。

### 请求URL
```
POST https://{{host}}/north/nf/system/system_offine_update
```

### 请求方式
```
POST
```

### 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| type | 是 | string | 升级包类型：<br>- `local.eng`：系统升级文件<br>- `local.app`：应用特征库<br>- `ips_rule`：入侵防护<br>- `av`：病毒特征库<br>- `local.urllib`：URL分类库<br>- `waf_rule`：WEB防护规则库<br>- `nti_api_v2`：情报威胁库 |
| file | 是 | file | 文件类型限制：<br>- type='local.eng'：.bin<br>- type='local.app'：.rule<br>- type='ips_rule'：.rule<br>- type='av'：.av<br>- type='local.urllib'：.urlib<br>- type='waf_rule'：.rule<br>- type='nti_api_v2'：.gz<br>文件大小不超过1.5GB |

### 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/system/system_offine_update" \
  -H "Authorization: <your-token>" \
  -F "type=local.eng" \
  -F "file=@update.bin"
```

### 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "系统升级系统升级文件升级成功",
  "result": []
}
```

### 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：系统升级-升级包导入失败"
}
```

---

## 3.3.2 获取系统版本信息

### 简要描述
获取系统中各组件的当前版本信息。

### 请求URL
```
GET https://{{host}}/north/nf/system/system_update_version/
```

### 请求方式
```
GET
```

### 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/system/system_update_version/" \
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
    "res": [
      {
        "type": "local.eng",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "引擎版本",
        "version": "6.0.5.168",
        "is_over": false
      },
      {
        "type": "local.app",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "应用特征库",
        "version": "2.0.0.36871",
        "is_over": false
      },
      {
        "type": "av",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "病毒特征库",
        "version": "6.0.1.1329",
        "is_over": false
      },
      {
        "type": "local.urllib",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "URL分类库",
        "version": "6.0.0.259",
        "is_over": false
      },
      {
        "type": "ips_rule",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "入侵防护特征库",
        "version": "2.0.0.36871",
        "is_over": false
      },
      {
        "type": "waf_rule",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "WEB防护规则库",
        "version": "2.0.0.36871",
        "is_over": false
      },
      {
        "type": "nti_threat_actor",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "APT检测",
        "version": "20240908.0001",
        "is_over": false
      },
      {
        "type": "nti_miner_ioc",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "挖矿检测情报",
        "version": "20240908.0001",
        "is_over": false
      },
      {
        "type": "nti_ransomware",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "勒索检测",
        "version": "20240908.0001",
        "is_over": false
      },
      {
        "type": "nti_b",
        "id": "",
        "md5": "",
        "current": "true",
        "time": "",
        "file_name": "",
        "type_name": "B包(通用)",
        "version": "20240907.0001",
        "is_over": false
      }
    ],
    "is_sse": false
  }
}
```

### 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| type | string | 类型标识 |
| id | string | 对象ID |
| md5 | string | MD5值 |
| current | string | 是否为当前版本 |
| time | string | 更新时间 |
| file_name | string | 文件名称 |
| type_name | string | 类型名称 |
| version | string | 当前版本号 |
| is_over | boolean | 是否有升级版本 |

### 失败返回示例
```json
{
  "status": 8302,
  "module": "NF",
  "message": "资源未找到：系统版本信息获取失败"
}
```

---

## 3.3.3 系统升级

### 简要描述
执行系统版本升级操作。

### 请求URL
```
POST https://{{host}}/north/nf/system/system_update_version/update/
```

### 请求方式
```
POST
```

### 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| type | 是 | string | 系统版本类型（如：local.eng） |
| id | 是 | string | 系统版本类型ID值，长度限制0~32个字符 |

### 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/system/system_update_version/update/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"type": "local.eng", "id": "<upgrade-id>"}'
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
  "status": 8601,
  "module": "NF",
  "message": "未知错误：升级失败"
}
```

---

## 3.3.4 获取在线升级配置

### 简要描述
获取系统在线升级的配置信息。

### 请求URL
```
GET https://{{host}}/north/nf/system/system_online_config/
```

### 请求方式
```
GET
```

### 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/system/system_online_config/" \
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
    "date": "0",
    "download_only": "false",
    "enabled": "true",
    "mode": "sched",
    "time": "02:00",
    "type": "day",
    "update_engine": "false",
    "url": "update.nsfocus.com",
    "update_type": "all",
    "update_time_type": "false"
  }
}
```

### 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| date | string | 升级天数 |
| download_only | string | 升级包通知开关 |
| enabled | string | 定时升级开关 |
| mode | string | 模式 |
| time | string | 升级具体时间 |
| type | string | 升级时间类型（day/week） |
| update_engine | string | 升级包含引擎 |
| url | string | 升级地址 |
| update_type | string | 升级包类型 |
| update_time_type | string | 升级时间 |

### 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "在线升级配置获取失败"
}
```

---

## 3.3.5 编辑在线升级配置

### 简要描述
修改系统在线升级的配置信息。

### 请求URL
```
POST https://{{host}}/north/nf/system/save_system_online_config/
```

### 请求方式
```
POST
```

### 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| url | 是 | string | 升级地址（update.nsfocus.com） |
| update_time_type | 是 | string | 升级时间（true/false） |
| update_type | 否 | string | 升级包类型（all/eng），当update_time_type='true'时必填 |
| update_engine | 否 | string | 升级包含引擎（true/false），当update_time_type='false'时必填 |
| download_only | 否 | string | 升级包通知开关（true/false），当update_time_type='false'时必填 |
| enabled | 否 | string | 定时升级开关（true/false），当update_time_type='false'时必填 |
| time | 否 | string | 升级具体时间（%H:%M:%S或%H:%M），当update_time_type='false'时必填 |
| type | 否 | string | 升级时间类型（day/week），当update_time_type='false'时必填 |
| date | 否 | string | 升级天数：<br>- type='day'时，date='0'<br>- type='week'时，date='1'~'7'<br>当update_time_type='false'时必填 |

### 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/system/save_system_online_config/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "update.nsfocus.com",
    "update_engine": "false",
    "update_type": "all",
    "download_only": "false",
    "enabled": "true",
    "time": "02:00",
    "type": "day",
    "date": "0",
    "update_time_type": "false"
  }'
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
  "status": 8601,
  "module": "NF",
  "message": "未知错误：在线升级配置失败"
}
```

---

## 使用场景
- **版本升级**：定期更新系统版本和特征库以获取最新功能和安全防护
- **在线升级**：配置定时自动升级，确保系统始终使用最新版本
- **离线升级**：在无网络环境下上传升级包进行系统升级
