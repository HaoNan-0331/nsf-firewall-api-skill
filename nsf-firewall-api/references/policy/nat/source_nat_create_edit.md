# 6.4.1 新建/编辑源NAT策略

## 简要描述
新建或编辑源NAT策略。

## 请求URL
```
POST https://{{host}}/north/nf/strategy/nat/nat_action/
```

## 请求方式
```
POST
```

## 请求参数
| 字段名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| action | 是 | string | 动作：create(创建)/edit(编辑) |
| d_address | 是 | string | 目的地址对象，最多32个对象或对象组，参数为对象名称 |
| d_safety_zone | 是 | string | 目的安全区（目的安全区和出接口安全区必须一致，参数为对象名称） |
| dst_port | 是 | string | 出接口（三层主接口/三层子接口/vlan口/汇聚三层主接口/GRE接口，参数为对象名称） |
| enabled | 是 | bool | 状态：true(启用)/false(禁用) |
| id | 否 | string | 策略ID（编辑时必填） |
| name | 是 | string | 名称，长度1-64字符，名称唯一，特殊字符只支持-_. |
| nat_object | 是 | string | 转换后地址-源地址，参数为对象名称 |
| nat_type | 是 | int | 策略类型：0-源NAT策略/1-目的NAT策略/2-双向NAT策略 |
| s_address | 是 | string | 源地址对象，最多32个对象或对象组，参数为对象名称 |
| s_address_translation | 是 | int | 转换地址类型：1-接口地址/2-网络对象 |
| s_safety_zone | 是 | string | 源安全区，最大规格63，参数为对象名称 |
| service | 是 | string | 服务，支持32个服务或服务组，参数为服务名称 |
| HA | 否 | string | HA线路名称（存在的HA线路名称） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/nat/nat_action/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "test1234",
    "nat_type": 0,
    "action": "create",
    "id": "",
    "s_safety_zone": "DMZ",
    "d_safety_zone": "DMZ",
    "s_address": "any",
    "d_address": "any",
    "service": "any",
    "dst_port": "vlan1",
    "s_address_translation": 1,
    "nat_object": "interface_ip",
    "enabled": true
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "新建 NAT 策略 test1234 成功",
  "result": {}
}
```

## 失败返回示例
```json
{
  "status": 8601,
  "module": "NF",
  "message": "未知错误：xxx 策略新建失败",
  "result": {}
}
```

## 使用场景
- 创建源地址转换(SNAT)策略
- 编辑已有源NAT策略
- 配置出接口地址转换
