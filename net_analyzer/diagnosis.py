"""诊断逻辑模块"""
from system_info import get_system_info
from network_info import get_network_interfaces, is_dhcp_failed
from gateway import get_default_gateway, test_gateway_connectivity
from connectivity import (
    test_internet_connectivity,
    test_dns_resolution,
    get_public_ip
)
from formatter import format_report


class NetworkDiagnosis:
    def __init__(self):
        self.results = {
            "system": {},
            "interfaces": [],
            "gateway": {},
            "internet": {},
            "dns": {},
            "public_ip": "",
            "summary": {}
        }

    def collect(self):
        self.results["system"] = get_system_info()
        self.results["interfaces"] = get_network_interfaces()
        
        dhcp_failed = is_dhcp_failed(self.results["interfaces"])
        self.results["summary"]["DHCP"] = 0 if dhcp_failed else 1

        gateway_ip = get_default_gateway()
        rtt, status = test_gateway_connectivity(gateway_ip) if gateway_ip else (-1, "N/A")
        self.results["gateway"] = {"ADDR": gateway_ip or "N/A", "RTT": f"{rtt} ms" if rtt >= 0 else "N/A", "STATUS": status}
        self.results["summary"]["GW"] = 1 if status == "OK" else 0

        rtt, status = test_internet_connectivity()
        self.results["internet"] = {"TARGET": "114.114.114.114:53", "RTT": f"{rtt} ms" if rtt >= 0 else "N/A", "STATUS": status}
        self.results["summary"]["WAN"] = 1 if status == "OK" else 0

        resolved_ip, status = test_dns_resolution()
        self.results["dns"] = {"TARGET": "www.baidu.com", "RESOLVE": resolved_ip, "STATUS": status}
        self.results["summary"]["DNS"] = 1 if status == "OK" else 0

        self.results["public_ip"] = get_public_ip()

    def run(self):
        self.collect()
        print(format_report(self.results))
