# 获取链路探测信息

## 简要描述
获取链路探测信息，支持分页和搜索。

## 请求URL
```
GET https://{{host}}/north/nf/network/linkdection/
```

## 请求方式
```
GET
```

## 请求参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（默认为10，>0的正整数或=-1查看全部数据） |
| page | 否 | int | 页数（默认为1，>0的正整数） |
| search | 否 | string | 查询关键字（长度不超过50个字符） |
| source | 否 | string | 来源（['ha']） |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/network/linkdection/?size=10&page=1" \
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
    "total": 1,
    "list": [
      {
        "id": 0,
        "backend_id": 0,
        "name": "xadqwc",
        "if_name": "G1/1",
        "send_state": false,
        "con_failured_times": 3,
        "detection_heart": 5,
        "linkdection_configs": [
          {
            "id": 34,
            "method": 2,
            "dst_port": 10,
            "src_addr": "0.0.0.0",
            "dst_addr": "2.3.4.5",
            "mcurstatus": 2,
            "finally_status": 1,
            "nexthopip": "",
            "link": 0
          }
        ],
        "source": "ha",
        "ref": ["HA_VRRP"]
      }
    ],
    "host_total": 0,
    "host_live": 0
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 对象ID |
| backend_id | int | 后台ID |
| name | string | 名称 |
| if_name | string | 出接口 |
| send_state | boolean | 启用状态 |
| con_failured_times | int | 探测失败次数 |
| detection_heart | int | 探测间隔（秒） |
| source | string | 模块类型（ha：高可用） |
| ref | list | 引用模块 |
| linkdection_configs | list | 探测目的主机IP |
| linkdection_configs[].id | int | 探测目的主机对象ID |
| linkdection_configs[].method | int | 探测方式（1：ICMP，2：TCP，3：UDP） |
| linkdection_configs[].dst_port | int | 探测端口 |
| linkdection_configs[].src_addr | string | 源IP地址 |
| linkdection_configs[].dst_addr | string | 探测目的主机IP |
| linkdection_configs[].mcurstatus | int | 主机状态 |
| linkdection_configs[].finally_status | int | 最终状态 |
| linkdection_configs[].nexthopip | string | 下一跳 |
| linkdection_configs[].link | int | 链路探测连接个数 |

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误:获取链路探测数据失败"
}
```

## 使用场景
- 查看链路探测配置
- 监控链路状态
- HA场景下的链路健康检查
