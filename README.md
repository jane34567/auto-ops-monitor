# Auto-Ops Monitor

基于 Docker 和 Prometheus 生态的轻量级自动化监控与故障采集方案。

## 项目简介

本项目基于 `dockprom` 基础架构，重点实现并扩展了 `monitor.py` 自动化诊断逻辑，提供了一套开箱即用的容器化监控栈，并结合 Python 自动化脚本，实现了从指标采集、可视化展示到异常自动抓取的完整闭环。适用于本地开发环境或轻量级虚拟机的日常运维监控。

**架构图**

![构](D:\my\dockprom\架构图.jpg)

## 核心组件

- **指标采集**: 使用 NodeExporter 采集宿主机硬件指标，cAdvisor 采集 Docker 容器运行状态。
- **数据存储与查询**: Prometheus 定期拉取并存储时序数据，数据默认保留 200 小时。
- **可视化**: 集成 Grafana 12.0.2，支持通过配置文件自动加载 Dashboard 和数据源。
- **告警通知**: Alertmanager 结合配置的 Slack Webhook 实现告警的实时推送。
- **自动化运维**: 独立的 `monitor.py` 脚本，通过 Prometheus API 实时监听 CPU 负载。当 CPU 超过 80% 阈值时，自动触发宿主机 Docker 状态快照，保留故障现场。

## 快速开始

### 1. 启动监控栈

确保宿主机已安装 Docker 和 Docker Compose。在项目根目录下执行：

Bash`docker-compose up -d`

主要服务端口说明：

- Prometheus: `9090`
- Grafana: `3000` (默认账号/密码通过环境变量注入，默认为 admin/admin)
- Alertmanager: `9093`

### 2. 配置告警通道 (可选)

修改 `config.yml` 中的 `api_url` 为你自己的 Slack Webhook 地址，并替换 Channel 名称，以接收实时告警推送。

### 3. 启动自动化脚本

在宿主机运行自动化监控脚本（需确保 Python 环境已安装 `requests` 库）：

Bash`pip install requestspython monitor.py`

脚本将持续守护，并在触发告警规则时自动通过 Docker CLI 抓取资源占用明细。

## 告警规则说明

目前内置的核心告警规则包括：

- **服务器高负载**: CPU 或内存使用率超过 80% 的安全阈值。
- **核心服务宕机**: 监控目标服务或关键容器意外退出运行超过 60 秒。