# 新建/编辑链路探测

## 简要描述
新建或编辑链路探测配置。

## 请求URL
```
POST https://{{host}}/north/nf/network/linkdection/action/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| action | 是 | string | 新建/编辑（create：新建，edit：编辑） |
| name | 是 | string | 链路名称（支持数字、字母和中文，特殊字符支持-_\.，长度≤32字符，名称唯一） |
| if_name | 是 | string | 出接口（接口类型支持三层接口、三层子接口、VLAN接口、汇聚三层接口） |
| send_state | 是 | bool | 启用状态（True/False） |
| con_failured_times | 是 | int | 探测失败次数（1-5） |
| detection_heart | 是 | int | 探测间隔（秒，1-3600） |
| linkdection_configs | 是 | dict | 探测目的主机信息（不能为空，最大长度不超过32） |
| linkdection_configs.src_addr | 是 | string | 源IP地址（合规的ipv4地址不带掩码，属于出接口） |
| linkdection_configs.dst_addr | 是 | string | 探测目的主机IP（合规的ipv4地址不带掩码，地址唯一） |
| linkdection_configs.method | 是 | int | 探测方式（1：icmp，2：tcp，3：udp） |
| linkdection_configs.dst_port | 否 | int | 探测端口（0-65535） |
| linkdection_configs.nexthopip | 否 | string | 下一跳（合规的ipv4地址不带掩码） |
| id | 否 | int | 链路id（存在的链路探测对象ID，action='edit'时必填） |
| source | 否 | string | 模块类型（['', 'ha']） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/linkdection/action/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "source": "",
    "action": "create",
    "id": "",
    "name": "test123",
    "if_name": "G1/1",
    "send_state": true,
    "con_failured_times": 3,
    "detection_heart": 5,
    "linkdection_configs": [
      {
        "src_addr": "0.0.0.0",
        "dst_addr": "192.168.3.3",
        "dst_port": 0,
        "nexthopip": "",
        "method": 1
      }
    ]
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误: 【链路探测模块】-【后台模块】配置异常"
}
```

## 使用场景
- 创建新的链路探测规则
- 修改已有链路探测配置
- 配置HA场景的链路健康检查
- 多目标探测配置
