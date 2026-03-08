# AI-Driven Auto-Ops Monitor (AI 智能自动化巡检系统)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED) ![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C)

## 项目简介
本项目是一个基于 **Prometheus + Grafana** 的服务器监控与自动化运维系统。集成了 Python 自动化巡检脚本，能够通过 REST API 实时抓取系统核心指标（CPU、内存、I/O），并在检测到异常时触发 **AI 辅助诊断逻辑**，模拟生成故障排查建议。

## 架构图
  graph TD
    A[Docker Host] --> B[NodeExporter / Host监控]
    A --> C[cAdvisor / 容器监控]
    B --> D[Prometheus 指标采集]
    C --> D
    D --> E[Alertmanager 告警管理]
    E --> F[monitor.py 自动化脚本]
    F --> G[自动诊断 / 日志处理]
    H[Grafana 监控可视化]
    I[Caddy 负责统一入口访问]

## 技术栈 (Tech Stack)
* **核心监控**: Prometheus (时序数据库) + Node Exporter (数据采集)
* **可视化**: Grafana (配置 Docker Host / System 仪表盘)
* **容器化**: Docker Compose 全栈编排
* **自动化运维**: Python (Requests, JSON处理, 异常告警算法)

## 核心功能
设计多维度告警规则（CPU、内存、磁盘、容器资源使用率），
并开发 Python 自动化脚本通过 Prometheus API 实现异常检测
与自动修复（容器重启、日志记录等），提升系统故障响应效率。

## 运行截图
![77003010225](C:\Users\JULIEM~1\AppData\Local\Temp\1770030102250.png)

![77003011046](C:\Users\JULIEM~1\AppData\Local\Temp\1770030110467.png)



## 快速开始
```bash
# 1. 启动监控服务
docker-compose up -d

# 2. 运行巡检脚本
python monitor.py
```
