# 6.2.17 黑白名单规格数据统计

## 简要描述
黑白名单规格数据统计-获取。

## 请求URL
```
GET https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/spec_dashboard/
```

## 请求方式
```
GET
```

## 请求示例
```bash
curl -X GET "https://{{host}}/north/nf/strategy/globalWb/blist/logEnable/spec_dashboard/" \
  -H "Authorization: <your-token>" \
  -H "Content-Type: application/json"
```

## 成功返回示例
```json
{
  "status": 2000,
  "module": "NF",
  "message": "获取统计数据成功",
  "result": {
    "blackList": {
      "spec": 450000,
      "useSourceIp": 0,
      "useDestIp": 0
    },
    "whiteList": {
      "spec": 50000,
      "useSourceIp": 0,
      "useDestIp": 0
    }
  }
}
```

## 返回参数说明
| 参数名 | 类型 | 说明 |
|--------|------|------|
| blackList.spec | int | 黑名单总剩余 |
| blackList.useSourceIp | int | 黑名单源地址总个数 |
| blackList.useDestIp | int | 黑名单目的地址总个数 |
| whiteList.spec | int | 白名单总剩余 |
| whiteList.useSourceIp | int | 白名单源地址总个数 |
| whiteList.useDestIp | int | 白名单目的地址总个数 |

## 使用场景
- 查看黑白名单容量使用情况
- 统计黑白名单规格数据
