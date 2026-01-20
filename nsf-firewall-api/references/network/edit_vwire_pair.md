# 编辑虚拟线对

## 简要描述
编辑已存在的虚拟线对配置。

## 请求URL
```
POST https://{{host}}/north/nf/network/interfacedetail/edit/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| id | 是 | int | 接口id（存在的接口id） |
| type | 是 | string | 接口类型：XCONNECT_INTERFACE |
| name | 是 | string | 接口名称（长度1-15字节，支持英文和数字） |
| vm_first_id | 是 | int | 虚拟线接口1（接口类型是未配置物理口和汇聚接口） |
| vm_second_id | 是 | int | 虚拟线接口2（接口类型是未配置物理口和汇聚接口） |
| vwire_first_zone | 是 | string | 虚拟线接口1安全区（存在的安全区名称） |
| vwire_second_zone | 是 | string | 虚拟线接口2安全区（存在的安全区名称） |
| linkmode1 | 是 | string | 虚拟线接口1双工模式：[auto, half, full] |
| linkmode2 | 是 | string | 虚拟线接口2双工模式：[auto, half, full] |
| linkspeed1 | 是 | string | 虚拟线接口1连接速率：[auto, 10, 100, 1000, 10000, 40000] |
| linkspeed2 | 是 | string | 虚拟线接口2连接速率：[auto, 10, 100, 1000, 10000, 40000] |
| ipv4_mtu1 | 是 | int | 虚拟线接口1 IPv4 MTU（未开启巨帧128-1600，开启巨帧128-9216） |
| ipv4_mtu2 | 是 | int | 虚拟线接口2 IPv4 MTU（未开启巨帧128-1600，开启巨帧128-9216） |
| linkstatus | 是 | bool | 链路状态是否同步 |
| label | 否 | string | 标签（长度0-64字节，中文3字节） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/network/interfacedetail/edit/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "XCONNECT_INTERFACE",
    "id": 5,
    "name": "tdcdeqqwq",
    "vm_first_id": 5,
    "vm_second_id": 7,
    "vwire_first_zone": "TRUST",
    "vwire_second_zone": "TRUST",
    "linkmode1": "auto",
    "linkmode2": "auto",
    "linkspeed1": "auto",
    "linkspeed2": "auto",
    "ipv4_mtu1": 1500,
    "ipv4_mtu2": 1500,
    "linkstatus": true,
    "label": "dds"
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "success",
  "result": {
    "id": 3,
    "interface_id": 0,
    "name": "dtesew",
    "vsys": 0,
    "linkstatus": true,
    "port_type": "电口",
    "type": "XCONNECT_INTERFACES",
    "zone": "",
    "label": "dd",
    "attribute": "logic",
    "role": "虚拟线接口"
  }
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：下发失败",
  "result": {}
}
```

## 使用场景
- 修改虚拟线对的接口配置
- 调整虚拟线对的MTU值
- 更改虚拟线对的链路模式
