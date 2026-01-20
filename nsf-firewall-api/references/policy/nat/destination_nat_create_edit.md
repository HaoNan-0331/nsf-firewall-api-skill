# 6.4.2 新建/编辑目的NAT策略

## 简要描述
新建或编辑目的NAT策略。

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
| enabled | 是 | bool | 状态：true(启用)/false(禁用) |
| external_address | 是 | string | 外部地址，单选，只支持ipv4，参数为对象名称 |
| external_port | 否 | string | 外部端口，0~65535，端口组最大规格16组 |
| health_check | 否 | string | 服务器健康检测，最大规格32个 |
| id | 否 | string | 策略ID（编辑时必填） |
| interface | 是 | string | 外部接口，最多接口数64个，参数为对象名称 |
| interface_type | 是 | string | 接口类型：normal(普通接口)/pppoe(动态接口) |
| internal_address | 是 | string | 内部IP地址，单选，只支持ipv4，参数为对象名称 |
| internal_port | 否 | string | 内部端口，0~65535，端口组最大规格16组 |
| name | 是 | string | 名称，长度1-64字符，名称唯一，特殊字符只支持-_. |
| nat_type | 是 | int | 策略类型：0-源NAT策略/1-目的NAT策略/2-双向NAT策略 |
| protocol | 是 | string | 协议：tcp/udp/icmp（port_map_type==1时必填） |
| port_map_type | 是 | string | 端口映射类型：1-映射部分端口/2-映射所有端口 |
| load_balance | 是 | string | 负载均衡：random(随机)/round_robin(轮询)/hash(哈希) |
| HA | 否 | string | HA线路名称（存在的HA线路名称） |

## 请求示例
```bash
curl -X POST "https://{{host}}/north/nf/strategy/nat/nat_action/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "test2222",
    "nat_type": 1,
    "action": "create",
    "id": "",
    "interface_type": "normal",
    "interface": "G1/2",
    "port_map_type": "1",
    "internal_address": "test1232",
    "external_address": "test1232",
    "internal_port": "33",
    "external_port": "22",
    "health_check": "",
    "load_balance": "random",
    "protocol": "tcp",
    "enabled": true
  }'
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "新建 NAT 策略 test2222 成功",
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
- 创建目的地址转换(DNAT)策略
- 配置端口映射（端口转发）
- 配置内部服务器映射
