"""网关模块"""
import subprocess
import re
import socket
import time


def get_default_gateway():
    """
    获取默认网关IP（兼容Windows中文系统）
    :return: str 网关IP或None
    """
    try:
        result = subprocess.run(
            ["ipconfig"],
            capture_output=True,
            text=True,
            timeout=10
        )
        for line in result.stdout.split("\n"):
            if "默认网关" in line and ":" in line:
                parts = line.split(":")
                if len(parts) >= 2:
                    gw = parts[1].strip()
                    if re.match(r"^\d+\.\d+\.\d+\.\d+$", gw):
                        return gw
    except Exception:
        pass
    return None


def test_gateway_connectivity(gateway_ip, timeout=3):
    """
    测试网关连通性并获取RTT
    :param gateway_ip: 网关IP
    :param timeout: 超时时间(秒)
    :return: tuple (rtt_ms, status) RTT为-1表示失败
    """
    if not gateway_ip:
        return -1, "N/A"

    try:
        start = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((gateway_ip, 80))
        except:
            try:
                sock.connect((gateway_ip, 443))
            except:
                pass
        sock.close()
        elapsed = (time.time() - start) * 1000
        return round(elapsed, 2), "OK"
    except Exception:
        return -1, "FAIL"
