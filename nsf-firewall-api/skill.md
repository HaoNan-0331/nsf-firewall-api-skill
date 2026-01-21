---
name: nsf-firewall-api
description: 绿盟NF防火墙REST API管理技能。此技能应在需要对绿盟NF防火墙进行自动化运维操作时使用，包括接口管理、路由配置、策略管理、地址/服务对象、应用层控制、VPN、网络诊断和系统管理等。支持单次和批量操作，自动记录操作日志。需要用户提供从Web界面生成的Token进行认证。
---

# 绿盟NF防火墙REST API管理技能

本技能提供绿盟NF防火墙的自动化运维能力，支持通过REST API进行全面管理。

## 技能用途

本技能用于绿盟NF防火墙的自动化运维操作，包括但不限于：
- 网络接口配置和状态查询
- 静态路由管理
- NAT策略和访问控制策略管理
- 地址对象和服务对象管理
- 应用层控制
- VPN配置（IPSec/SSL）
- 高可用性配置
- 网络诊断（Ping/Traceroute/路径分析）
- 系统管理（主机名/DNS/NTP/管理员/证书）

## 认证方式

本技能使用Token认证，Token需从防火墙Web界面生成：

1. 登录防火墙Web管理界面
2. 进入"系统管理"->"API管理"或类似位置
3. 生成新的API Token
4. 复制Token供本技能使用

**重要提示**: 每次用户提出需求时，必须向用户索取Token。

### API地址格式

```
{schema}://{host}:{port}/{prefix}/{resource}
```

- **schema**: https 或 http
- **host**: 防火墙IP地址
- **port**: 服务端口（默认8081）
- **prefix**: 固定为 `/north/nf`
- **resource**: 资源路径（如 `strategy/firewall/info/`）

**示例**: `https://192.168.1.1:8081/north/nf/strategy/firewall/info/`

### 请求头设置

```
Authorization: <your-token>
Content-Type: application/json
```

## 使用工作流程

### 1. 获取认证信息

当用户提出需求时，首先询问以下信息：

```
请提供以下信息：
1. 防火墙地址 (例如: https://183.67.91.142:8081)
2. API Token (从Web界面生成)
```

### 2. 单次操作流程

针对简单的单个操作需求：

1. 根据用户需求，确定要调用的API端点和参数
2. 使用 `scripts/nsf_api_client.py` 执行操作
3. 返回原始JSON结果给用户

**执行示例:**
```bash
python scripts/nsf_api_client.py https://192.168.1.1 YOUR_TOKEN get_interfaces
```

### 3. 批量操作流程

针对需要执行多个操作的场景：

1. 根据用户需求，生成批量操作请求
2. 创建批量操作文件（JSON或YAML格式）
3. 使用 `scripts/nsf_batch_operations.py` 执行批量操作
4. 返回所有操作的结果

**执行示例:**
```bash
python scripts/nsf_batch_operations.py https://192.168.1.1 YOUR_TOKEN batch_ops.json
```

### 4. 日志查看流程

查看操作历史日志：

```bash
# 查看今天的日志
python scripts/nsf_log_viewer.py

# 查看指定日期的日志
python scripts/nsf_log_viewer.py --date 20250118

# 只查看失败的请求
python scripts/nsf_log_viewer.py --failed-only

# 统计信息
python scripts/nsf_log_viewer.py --stats
```

## 支持的操作

### 防火墙策略
- `get_firewall_policies` - 获取防火墙策略列表
- `add_firewall_policy` - 添加防火墙策略
- `update_firewall_policy` - 更新防火墙策略
- `delete_firewall_policy` - 删除防火墙策略

### 网络接口管理
- `get_interfaces` - 获取所有接口
- `get_interface <if_name>` - 获取指定接口
- `update_interface <if_name> <data>` - 更新接口配置

### 静态路由
- `get_routes` - 获取所有路由
- `add_route <data>` - 添加路由
- `update_route <route_id> <data>` - 更新路由
- `delete_route <route_id>` - 删除路由

### NAT策略
- `get_nat_policies` - 获取所有NAT策略
- `add_nat_policy <data>` - 添加NAT策略
- `update_nat_policy <policy_id> <data>` - 更新NAT策略
- `delete_nat_policy <policy_id>` - 删除NAT策略

### 访问控制策略
- `get_acl_policies` - 获取所有ACL策略
- `add_acl_policy <data>` - 添加ACL策略
- `update_acl_policy <policy_id> <data>` - 更新ACL策略
- `delete_acl_policy <policy_id>` - 删除ACL策略

### 地址对象
- `get_address_objects` - 获取所有地址对象
- `add_address_object <data>` - 添加地址对象
- `update_address_object <obj_id> <data>` - 更新地址对象
- `delete_address_object <obj_id>` - 删除地址对象

### 服务对象
- `get_service_objects` - 获取所有服务对象
- `add_service_object <data>` - 添加服务对象
- `update_service_object <obj_id> <data>` - 更新服务对象
- `delete_service_object <obj_id>` - 删除服务对象

### 网络诊断
- `ping <data>` - Ping测试
- `traceroute <data>` - 路径追踪
- `get_path <data>` - 路径分析

### 系统管理
- `get_system_info` - 获取系统信息
- `get_hostname` / `set_hostname` - 主机名管理
- `get_dns` / `set_dns` - DNS配置
- `get_ntp` / `set_ntp` - NTP配置
- `get_admins` / `add_admin` / `update_admin` / `delete_admin` - 管理员管理
- `get_certificates` - 证书管理

## 使用场景示例

### 场景1: 查看防火墙策略
```
用户: 查看防火墙当前配置的所有策略
操作: 获取防火墙地址和Token
     执行: python nsf_api_client.py <host> <token> get_firewall_policies
     返回原始JSON结果，包含策略列表
```

### 场景2: 查看接口状态
```
用户: 查看防火墙所有接口状态
操作: 获取防火墙IP和Token
     执行: python nsf_api_client.py <host> <token> get_interfaces
     返回原始JSON结果
```

### 场景3: 添加静态路由
```
用户: 添加一条静态路由，目标网段192.168.100.0/24，网关192.168.1.254，出接口eth1
操作: 获取防火墙IP和Token
     构造参数: {"destination": "192.168.100.0/24", "gateway": "192.168.1.254", "interface": "eth1"}
     执行: python nsf_api_client.py <host> <token> add_route '{"destination": "192.168.100.0/24", "gateway": "192.168.1.254", "interface": "eth1"}'
     返回原始JSON结果
```

### 场景4: 批量添加策略
```
用户: 批量添加访问控制策略，允许内网访问互联网
操作: 获取防火墙IP和Token
     创建批量操作文件
     执行: python nsf_batch_operations.py <host> <token> batch_policies.json
     返回所有操作的结果
```

### 场景5: 网络诊断
```
用户: 测试到8.8.8.8的连通性
操作: 获取防火墙IP和Token
     构造参数: {"host": "8.8.8.8", "count": 4}
     执行: python nsf_api_client.py <host> <token> ping '{"host": "8.8.8.8", "count": 4}'
     返回原始JSON结果
```

### 场景6: 配置巡检
```
用户: 对防火墙进行配置巡检
操作: 获取防火墙IP和Token
     批量执行: get_system_info, get_interfaces, get_routes, get_firewall_policies
     返回所有操作的原始JSON结果
```

### 场景7: 查看操作日志
```
用户: 查看今天的所有操作记录
操作: 执行 python nsf_log_viewer.py
     返回日志列表
```

## 批量操作模板

批量操作文件位于 `assets/templates/` 目录：
- `batch_template.json` - JSON格式模板
- `batch_template.yaml` - YAML格式模板

用户可以参考模板创建自己的批量操作文件。

## 技术依赖

所有脚本依赖以下Python库：
- **requests**: HTTP请求库
- **PyYAML**: YAML文件解析（可选，用于YAML格式批量操作）

安装依赖：
```bash
pip install requests pyyaml
```

## API参考文档

详细的API端点、参数格式和响应结构请参考各模块文档：

| 一级模块 | 二级模块 | 文件路径 | 说明 |
|----------|----------|----------|------|
| 应用配置 | - | `references/application_config/api_reference.md` | 应用配置下发 |
| 总览 | - | `references/overview/api_reference.md` | 系统状态信息获取 |
| 系统 | 备份恢复 | `references/system/backup_restore.md` | 配置备份/恢复/进度 |
| 系统 | 证书信息 | `references/system/certificate.md` | 证书管理 |
| 系统 | 系统升级 | `references/system/system_upgrade.md` | 版本管理/在线升级 |
| 系统 | 系统配置 | `references/system/system_config.md` | NTP等基本配置 |
| 协同联动 | ESP-C管理 | `references/collaboration/espc_management.md` | 企业安全中心配置 |
| 协同联动 | ISOP管理 | `references/collaboration/isop_management.md` | 智能安全运营平台配置 |
| 协同联动 | LAS管理 | `references/collaboration/las_management.md` | 日志审计系统配置 |
| 协同联动 | 联动地址 | `references/collaboration/set_linkage_address.md` | 设置联动地址 |
| 协同联动 | 平台列表 | `references/collaboration/get_platform_list.md` | 获取安全管理平台列表 |
| 协同联动 | 删除平台 | `references/collaboration/delete_platform.md` | 删除安全管理平台 |
| 网络管理 | 三层子接口-新建 | `references/network/create_sub_interface.md` | 新建三层子接口 |
| 网络管理 | 三层子接口-编辑 | `references/network/edit_sub_interface.md` | 编辑三层子接口 |
| 网络管理 | 虚拟线对-新建 | `references/network/create_vwire_pair.md` | 新建虚拟线对 |
| 网络管理 | 虚拟线对-编辑 | `references/network/edit_vwire_pair.md` | 编辑虚拟线对 |
| 网络管理 | 三层接口-编辑 | `references/network/edit_l3_interface.md` | 编辑三层接口 |
| 网络管理 | 接口列表 | `references/network/get_interface_list.md` | 获取接口列表 |
| 网络管理 | 所有接口 | `references/network/get_all_interfaces.md` | 获取所有接口列表 |
| 网络管理 | 加密公钥 | `references/network/get_public_key.md` | 获取PPPOE加密公钥 |
| 网络管理 | 安全区-查询 | `references/network/get_zone_info.md` | 获取安全区信息 |
| 网络管理 | 安全区-配置 | `references/network/create_edit_zone.md` | 创建/编辑安全区 |
| 网络管理 | 安全区-删除 | `references/network/delete_zone.md` | 删除安全区 |
| 网络管理 | 链路探测-查询 | `references/network/get_link_detection.md` | 获取链路探测信息 |
| 网络管理 | 链路探测-删除 | `references/network/delete_link_detection.md` | 删除链路探测 |
| 网络管理 | 链路探测-配置 | `references/network/create_edit_link_detection.md` | 新建/编辑链路探测 |
| 网络管理 | 链路探测-启用 | `references/network/enable_link_detection.md` | 启用/禁用链路探测 |
| 网络管理 | 策略路由-查询 | `references/network/get_policy_route.md` | 获取策略路由 |
| 网络管理 | 策略路由-配置 | `references/network/create_edit_policy_route.md` | 新建/编辑策略路由 |
| 网络管理 | 策略路由-删除 | `references/network/delete_policy_route.md` | 删除策略路由 |
| 策略 | 获取策略 | `references/policy/firewall/get_policies.md` | 获取防火墙策略列表（支持分页、搜索） |
| 策略 | 新建/编辑策略 | `references/policy/firewall/create_edit_policy.md` | 新建/编辑防火墙策略 |
| 策略 | 删除策略 | `references/policy/firewall/delete_policy.md` | 删除防火墙策略 |
| 策略 | 清空命中次数 | `references/policy/firewall/clear_hit_count.md` | 清空防火墙策略命中次数 |
| 策略 | 清空所有策略 | `references/policy/firewall/clear_policies.md` | 清空防火墙策略 |
| 策略 | 批量编辑策略 | `references/policy/firewall/batch_edit_policy.md` | 批量编辑防火墙策略 |
| 策略 | 启用/禁用策略 | `references/policy/firewall/enable_disable_policy.md` | 禁用启用防火墙策略 |
| 策略 | 移动策略 | `references/policy/firewall/move_policy.md` | 移动防火墙策略 |
| 策略 | 智能策略检测 | `references/policy/firewall/intelligent_policy_check.md` | 智能策略检测 |
| 策略 | 冲突检测 | `references/policy/firewall/detect_policy_conflict.md` | 策略冲突检测 |
| 策略 | 全局配置查询 | `references/policy/firewall/get_global_info.md` | 获取防火墙策略全局配置信息 |
| 策略 | 全局配置更新 | `references/policy/firewall/update_global_config.md` | 防火墙策略全局配置更新 |
| 策略 | 功能特性查询 | `references/policy/firewall/feature_control.md` | 根据证书特性控制安全模板 |
| 策略 | 获取策略组 | `references/policy/firewall/get_policy_groups.md` | 获取防火墙策略组 |
| 策略 | 新建/编辑策略组 | `references/policy/firewall/create_edit_policy_group.md` | 新建/编辑防火墙策略组 |
| 策略 | 删除策略组 | `references/policy/firewall/delete_policy_group.md` | 删除防火墙策略组 |
| 策略 | 清空策略组元素 | `references/policy/firewall/clear_policy_group_elements.md` | 批量删除防火墙策略组元素 |
| 策略 | 获取黑名单 | `references/policy/global_blacklist_whitelist/blacklist_get_info.md` | 获取黑名单列表 |
| 策略 | 新建/编辑黑名单 | `references/policy/global_blacklist_whitelist/blacklist_create_edit.md` | 新建/编辑黑名单 |
| 策略 | 删除黑名单 | `references/policy/global_blacklist_whitelist/blacklist_delete.md` | 删除黑名单 |
| 策略 | 导出黑名单 | `references/policy/global_blacklist_whitelist/blacklist_export.md` | 导出黑名单 |
| 策略 | 导入黑名单 | `references/policy/global_blacklist_whitelist/blacklist_import.md` | 导入黑名单 |
| 策略 | 日志配置查询 | `references/policy/global_blacklist_whitelist/global_log_config_get.md` | 获取黑白名单全局日志配置 |
| 策略 | 日志配置更新 | `references/policy/global_blacklist_whitelist/global_log_config_update.md` | 更新黑白名单全局日志配置 |
| 策略 | 清空黑名单 | `references/policy/global_blacklist_whitelist/blacklist_clear.md` | 清空所有黑名单 |
| 策略 | 获取白名单 | `references/policy/global_blacklist_whitelist/whitelist_get_info.md` | 获取白名单列表 |
| 策略 | 新建/编辑白名单 | `references/policy/global_blacklist_whitelist/whitelist_create_edit.md` | 新建/编辑白名单 |
| 策略 | 删除白名单 | `references/policy/global_blacklist_whitelist/whitelist_delete.md` | 删除白名单 |
| 策略 | 导出白名单 | `references/policy/global_blacklist_whitelist/whitelist_export.md` | 导出白名单 |
| 策略 | 导入白名单 | `references/policy/global_blacklist_whitelist/whitelist_import.md` | 导入白名单 |
| 策略 | 清空白名单 | `references/policy/global_blacklist_whitelist/whitelist_clear.md` | 清空所有白名单 |
| 策略 | Class日志查询 | `references/policy/global_blacklist_whitelist/class_log_enable_get.md` | 获取黑白名单class日志配置 |
| 策略 | Class日志更新 | `references/policy/global_blacklist_whitelist/class_log_enable_update.md` | 更新黑白名单class日志配置 |
| 策略 | 规格统计 | `references/policy/global_blacklist_whitelist/spec_dashboard.md` | 黑白名单规格数据统计 |
| 策略 | 有效时间查询 | `references/policy/global_blacklist_whitelist/valid_time_get.md` | 获取黑白名单ips av有效时间 |
| 策略 | 有效时间更新 | `references/policy/global_blacklist_whitelist/valid_time_update.md` | 更新黑白名单ips av有效时间 |
| 策略 | 清空自动黑名单 | `references/policy/global_blacklist_whitelist/clear_auto_blacklist.md` | 清空ips/av自动加入的黑名单 |
| 策略 | 超时数据处理 | `references/policy/global_blacklist_whitelist/overtime_data.md` | 下发ips av超时数据 |
| 策略 | 新建/编辑源NAT | `references/policy/nat/source_nat_create_edit.md` | 新建/编辑源NAT策略 |
| 策略 | 新建/编辑目的NAT | `references/policy/nat/destination_nat_create_edit.md` | 新建/编辑目的NAT策略 |
| 策略 | 新建/编辑双向NAT | `references/policy/nat/bidirectional_nat_create_edit.md` | 新建/编辑双向NAT策略 |
| 策略 | NAT策略总览 | `references/policy/nat/nat_tree_overview.md` | 获取NAT策略总览 |
| 策略 | 获取NAT策略 | `references/policy/nat/nat_get_info.md` | 获取NAT策略详细信息 |
| 策略 | 删除NAT策略 | `references/policy/nat/nat_delete.md` | 删除NAT策略 |
| 策略 | 清空NAT策略 | `references/policy/nat/nat_clear.md` | 清空所有NAT策略 |
| 策略 | 启用/禁用NAT | `references/policy/nat/nat_enable_disable.md` | 启用/禁用NAT策略 |
| 策略 | 移动NAT策略 | `references/policy/nat/nat_move.md` | 移动NAT策略 |
| 对象 | 获取网络对象 | `references/objects/network/get_network_objects.md` | 获取网络对象信息 |
| 对象 | 新建/编辑网络对象 | `references/objects/network/create_edit_network_object.md` | 新建/编辑网络对象 |
| 对象 | 网络对象总览 | `references/objects/network/network_objects_overview.md` | 获取网络对象总览 |
| 对象 | 删除网络对象 | `references/objects/network/delete_network_object.md` | 删除网络对象 |
| 对象 | 获取域名配置 | `references/objects/network/get_domain_config.md` | 获取域名策略域名解析层数 |
| 对象 | 设置域名配置 | `references/objects/network/set_domain_config.md` | 设置域名策略域名解析层数 |
| 对象 | 获取服务对象 | `references/objects/service/get_service_objects.md` | 获取服务对象列表 |
| 对象 | 新建/编辑服务对象 | `references/objects/service/create_edit_service_object.md` | 新建/编辑服务对象 |
| 对象 | 获取服务对象ID | `references/objects/service/get_service_object_ids.md` | 获取服务对象名称ID |
| 对象 | 服务对象总览 | `references/objects/service/service_objects_overview.md` | 获取服务对象总览 |
| 对象 | 删除服务对象 | `references/objects/service/delete_service_object.md` | 删除服务对象 |
| 对象 | - | `references/objects/api_reference.md` | 其他对象管理（防病毒、地理位置、应用等） |
| 附录 | - | `references/appendix/api_reference.md` | REST API配置、响应码、错误码、参考文档 |

## 最佳实践

1. **安全性**
   - Token应妥善保管，不要在脚本中硬编码
   - 敏感操作前先备份配置
   - 生产环境变更操作前务必在测试环境验证

2. **可靠性**
   - 执行变更前先获取当前配置
   - 批量操作前先在单条操作测试
   - 注意操作顺序（如先添加对象，再引用对象）

3. **可追溯性**
   - 所有操作自动记录日志
   - 日志文件按日期归档在 `logs/` 目录
   - 使用日志查看工具查询历史操作

4. **错误处理**
   - 检查响应中的错误信息
   - 失败操作会记录在日志中
   - 使用 `--failed-only` 筛选失败的操作

## 目录结构

```
nsf-firewall-api/
├── skill.md                    # 本文件
├── scripts/                    # 执行脚本
│   ├── nsf_api_client.py       # API客户端（单次操作）
│   ├── nsf_batch_operations.py # 批量操作脚本
│   └── nsf_log_viewer.py       # 日志查看工具
├── references/                 # 参考文档（按模块分类）
│   ├── application_config/     # 应用配置
│   │   └── api_reference.md
│   ├── overview/               # 总览
│   │   └── api_reference.md
│   ├── system/                 # 系统（按二级目录分类）
│   │   ├── backup_restore.md   # 备份恢复
│   │   ├── certificate.md      # 证书信息
│   │   ├── system_upgrade.md   # 系统升级
│   │   └── system_config.md    # 系统配置
│   ├── collaboration/          # 协同联动（按三级目录分类）
│   │   ├── espc_management.md       # ESP-C管理
│   │   ├── isop_management.md       # ISOP管理
│   │   ├── las_management.md        # LAS管理
│   │   ├── set_linkage_address.md   # 联动地址
│   │   ├── get_platform_list.md     # 平台列表
│   │   └── delete_platform.md       # 删除平台
│   ├── network/                # 网络管理（按具体功能分类）
│   │   ├── create_sub_interface.md        # 新建三层子接口
│   │   ├── edit_sub_interface.md          # 编辑三层子接口
│   │   ├── create_vwire_pair.md          # 新建虚拟线对
│   │   ├── edit_vwire_pair.md            # 编辑虚拟线对
│   │   ├── edit_l3_interface.md          # 编辑三层接口
│   │   ├── get_interface_list.md         # 获取接口列表
│   │   ├── get_all_interfaces.md         # 获取所有接口列表
│   │   ├── get_public_key.md             # 获取加密公钥
│   │   ├── get_zone_info.md              # 获取安全区信息
│   │   ├── create_edit_zone.md           # 创建/编辑安全区
│   │   ├── delete_zone.md                # 删除安全区
│   │   ├── get_link_detection.md         # 获取链路探测信息
│   │   ├── delete_link_detection.md      # 删除链路探测
│   │   ├── create_edit_link_detection.md # 新建/编辑链路探测
│   │   ├── enable_link_detection.md      # 启用/禁用链路探测
│   │   ├── get_policy_route.md           # 获取策略路由
│   │   ├── create_edit_policy_route.md   # 新建/编辑策略路由
│   │   └── delete_policy_route.md        # 删除策略路由
│   ├── policy/                 # 策略
│   │   └── api_reference.md
│   ├── objects/                # 对象
│   │   └── api_reference.md
│   └── appendix/               # 附录
│       └── api_reference.md
├── assets/                     # 资产文件
│   └── templates/              # 批量操作模板
│       ├── batch_template.json # JSON格式模板
│       └── batch_template.yaml # YAML格式模板
└── logs/                       # 操作日志目录
    └── api_log_YYYYMMDD.json   # 按日期归档的日志
```

## 常见问题

### Q: Token在哪里获取？
A: 登录防火墙Web界面，在"系统管理"->"API管理"中生成Token。

### Q: 如何处理SSL证书验证失败？
A: 脚本默认禁用SSL验证，如需启用请设置 `verify_ssl=True`。

### Q: 批量操作中某条失败会影响其他操作吗？
A: 不会，批量操作会依次执行所有请求，每个操作的结果独立记录。

### Q: 日志文件会无限增长吗？
A: 日志按日期分割，建议定期清理旧的日志文件。
