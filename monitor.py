import requests
import time
import subprocess
import logging

PROMETHEUS_URL = "http://127.0.0.1:9090/api/v1/query"

CPU_THRESHOLD = 80.0

logging.basicConfig(
    filename="auto_ops.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def get_cpu_usage():
    query = '100 - (avg by(instance) (irate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)'

    try:
        response = requests.get(PROMETHEUS_URL, params={'query': query}, timeout=3)
        data = response.json()

        if data['data']['result']:
            value = float(data['data']['result'][0]['value'][1])
            return round(value, 2)

    except Exception as e:
        logging.error(f"Prometheus query failed: {e}")

    return 0.0


def restart_container(name):
    try:
        subprocess.run(["docker", "restart", name])
        logging.warning(f"Container restarted: {name}")
    except Exception as e:
        logging.error(f"Restart failed: {e}")


def auto_heal(cpu):
    logging.warning(f"High CPU detected: {cpu}%")

    # 示例自动处理
    restart_container("cadvisor")


def main():

    print("Auto Ops Monitor Started...")

    while True:

        cpu = get_cpu_usage()

        print(f"CPU Usage: {cpu}%")

        if cpu > CPU_THRESHOLD:
            auto_heal(cpu)

        time.sleep(10)


if __name__ == "__main__":
    main()