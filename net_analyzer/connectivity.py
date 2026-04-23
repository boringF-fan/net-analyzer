"""外网连通性检测模块"""
import socket
import time
import urllib.request


DNS_SERVER = "114.114.114.114"
DNS_PORT = 53
DNS_TIMEOUT = 5


def test_internet_connectivity(timeout=DNS_TIMEOUT):
    """
    测试外网连通性
    :param timeout: 超时时间(秒)
    :return: tuple (rtt_ms, status)
    """
    try:
        start = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((DNS_SERVER, DNS_PORT))
        sock.close()
        elapsed = (time.time() - start) * 1000
        return round(elapsed, 2), "OK"
    except Exception:
        return -1, "FAIL"


def test_dns_resolution(hostname="www.baidu.com", timeout=DNS_TIMEOUT):
    """
    测试DNS解析
    :param hostname: 目标域名
    :param timeout: 超时时间(秒)
    :return: tuple (resolved_ip, status)
    """
    try:
        ip = socket.gethostbyname(hostname)
        return ip, "OK"
    except Exception:
        return "N/A", "FAIL"


def get_public_ip(timeout=10):
    """
    获取公网IP (使用标准库urllib)
    :param timeout: 超时时间(秒)
    :return: str 公网IP
    """
    try:
        req = urllib.request.Request("https://ipinfo.io/ip", headers={"User-Agent": "Mozilla/5.0"})
        response = urllib.request.urlopen(req, timeout=timeout)
        return response.read().decode('utf-8').strip()
    except Exception:
        return "N/A"
