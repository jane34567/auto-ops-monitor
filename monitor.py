import requests
import time
import json
import random

# --- 配置区域 ---
# 127.0.0.1 避免 Windows DNS 问题
PROMETHEUS_URL = "http://127.0.0.1:9090/api/v1/query"
# 告警阈值 (CPU > 1% 就报警)
CPU_THRESHOLD = 1.0 
# 这里是钥匙！dockprom 默认账号密码
AUTH_KEYS = ('admin', 'admin')

def get_cpu_usage():
    """带密码验证向 Prometheus 查询 CPU 使用率"""
    # 查询语句：计算 CPU 使用率
    query = '100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)'
    
    try:
        # 注意：这里加了 auth=AUTH_KEYS 参数
        response = requests.get(PROMETHEUS_URL, params={'query': query}, auth=AUTH_KEYS, timeout=2)
        
        # 调试：如果你想看服务器到底回了什么，可以把下面这行注释取消
        # print(f"[DEBUG] Status: {response.status_code}")

        if response.status_code != 200:
            print(f"[ERROR] 登录失败或服务器错误 (代码: {response.status_code})")
            return 0.0

        try:
            data = response.json()
        except json.JSONDecodeError:
            print(f"[ERROR] 返回的不是 JSON 数据")
            return 0.0
            
        if data['status'] == 'success' and data['data']['result']:
            value = float(data['data']['result'][0]['value'][1])
            return round(value, 2)
        else:
            return 0.0
            
    except requests.exceptions.ConnectionError:
        print("[ERROR] 无法连接监控系统，请检查 Docker 是否运行。")
        return 0.0
    except Exception as e:
        print(f"[ERROR] 发生未知错误: {e}")
        return 0.0

def ai_diagnosis(cpu_val):
    """模拟 AI 诊断"""
    advices = [
        "Check for infinite loops in Docker containers.",
        "Resource contention detected. Suggest scaling up.",
        "Abnormal network traffic spike detected."
    ]
    print("\n" + "="*45)
    print(f" [AI-Ops Agent] Analyzing System Logs...")
    print(f" [ALERT] CPU Usage Spike Detected: {cpu_val}%")
    print(f" [AI Suggestion] {random.choice(advices)}")
    print("="*45 + "\n")

def main():
    print(f">>> Auto-Ops Monitor Script Started (Authenticated)...")
    print(f"--- Target: Local Docker Host | Threshold: CPU > {CPU_THRESHOLD}% ---")
    print("-" * 55)

    while True:
        cpu_usage = get_cpu_usage()
        current_time = time.strftime("%H:%M:%S", time.localtime())
        
        if cpu_usage > CPU_THRESHOLD:
            # 只有这里会触发 AI 报警
            print(f"[{current_time}] FAILED! [CRITICAL] CPU: {cpu_usage}% (Threshold Exceeded)")
            ai_diagnosis(cpu_usage)
        else:
            # 正常情况
            print(f"[{current_time}] OK!  [NORMAL] CPU: {cpu_usage}%")
            
        time.sleep(5)

if __name__ == "__main__":
    main()