# AI-Driven Auto-Ops Monitor (AI 智能自动化巡检系统)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED) ![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C)

## 项目简介
本项目是一个基于 **Prometheus + Grafana** 的企业级服务器监控与自动化运维系统。集成了 Python 自动化巡检脚本，能够通过 REST API 实时抓取系统核心指标（CPU、内存、I/O），并在检测到异常时触发 **AI 辅助诊断逻辑**，模拟生成故障排查建议。

## 技术栈 (Tech Stack)
* **核心监控**: Prometheus (时序数据库) + Node Exporter (数据采集)
* **可视化**: Grafana (配置 Docker Host / System 仪表盘)
* **容器化**: Docker Compose 全栈编排
* **自动化运维**: Python (Requests, JSON处理, 异常告警算法)

## 核心功能
1.  **全栈监控部署**: 一键拉起监控集群，实现秒级数据采集。
2.  **自动化巡检**: Python 脚本实现 24/7 无人值守巡检，替代人工轮询。
3.  **智能告警 (AI-Ops)**:
    * 实时计算 CPU 负载阈值。
    * 异常触发时，自动输出故障日志并提供优化建议（如资源扩容、死循环排查）。

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