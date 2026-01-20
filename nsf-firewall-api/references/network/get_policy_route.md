# 获取策略路由

## 简要描述
获取策略路由列表，支持分页和搜索。

## 请求URL
```
GET https://{{host}}/north/nf/network/route/policy/
```

## 请求方式
```
GET
```

## 请求参数
| 参数名 | 必选 | 类型 | 说明 |
|--------|------|------|------|
| size | 否 | int | 分页大小（>0或=-1，默认为10） |
| page | 否 | int | 页数（>0，默认为1） |
| search | 否 | string | 查询关键字（长度≤50） |

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/network/route/policy/?size=10&page=1" \
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
    "enabled_num": 1,
    "list": [
      {
        "id": 1,
        "name": "test123",
        "source_ip": "3.3.3.0/24",
        "dst_ip": "4.4.4.0/24",
        "dst_obj_type": "ip",
        "dst_domain_obj": "",
        "dst_domain_obj_name": [],
        "src_interface": [
          {
            "name": "G1/1",
            "status": "down",
            "linkspeed": "auto",
            "attribute": "physical",
            "ipv4": "0.0.0.0/0"
          }
        ],
        "service": [
          {
            "backend_id": "600000",
            "name": "any",
            "type": "system",
            "id": 99
          }
        ],
        "is_app_route": false,
        "application": [
          {
            "backend_id": "0",
            "id": 0,
            "name": "any",
            "type": "system"
          }
        ],
        "fib_path": [
          {
            "id": 2,
            "gateway": "3.3.3.3",
            "dst_interface": {
              "name": "G1/1",
              "status": "down",
              "linkspeed": "auto",
              "attribute": "physical",
              "ipv4": "0.0.0.0/0"
            },
            "weight": 1,
            "preference": 1
          }
        ],
        "enabled": true,
        "export_type": "single",
        "flag": "-1",
        "linkdection": [
          {
            "id": 0,
            "name": "test34455"
          }
        ],
        "loadbalance_mode": 0
      }
    ]
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | int | 策略路由id |
| name | string | 策略路由名称 |
| source_ip | string | 源IP地址 |
| dst_ip | string | 目的IP地址 |
| src_interface | array | 源接口 |
| service | array | 服务 |
| is_app_route | bool | 基于应用还是服务 |
| application | array | 应用 |
| export_type | string | 出接口类型 |
| loadbalance_mode | int | 负载方式 |
| enabled | bool | 状态 |
| linkdection | array | 链路探测 |
| fib_path | array | 出接口 |
| fib_path[].gateway | string | 网关 |
| fib_path[].weight | int | 权值 |
| fib_path[].preference | int | 管理距离 |

## 失败返回示例
```json
{
  "status": 8201,
  "module": "NF",
  "message": "数据类型不合规:page参数必须为数字",
  "result": {}
}
```

## 使用场景
- 查看所有策略路由配置
- 查询特定策略路由
- 策略路由巡检
