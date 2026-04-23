"""输出格式化模块"""
import sys


def format_report(results):
    """
    格式化诊断报告
    :param results: 诊断结果字典
    :return: str 格式化后的报告
    """
    lines = []

    # 标题
    lines.append("=" * 50)
    lines.append("         NET DIAG (Network Diagnostic)")
    lines.append("=" * 50)

    # 系统信息
    lines.append("[ SYSTEM ]")
    system = results.get("system", {})
    lines.append(f"OS      : {system.get('OS', 'N/A')}")
    lines.append(f"VERSION : {system.get('VERSION', 'N/A')}")
    lines.append(f"ARCH    : {system.get('ARCH', 'N/A')}")

    # 分隔线
    lines.append("-" * 20)

    # 网卡信息
    lines.append("[ NETWORK ]")
    interfaces = results.get("interfaces", [])
    if interfaces:
        for iface in interfaces:
            name = iface.get("name", "Unknown")[:20]
            status = iface.get("status", "N/A")
            ip = iface.get("ip", "N/A")
            lines.append(f"{name:<20} {status} | {ip}")
    else:
        lines.append("No network interfaces found")

    # 分隔线
    lines.append("-" * 20)

    # 网关信息
    lines.append("[ GATEWAY ]")
    gateway = results.get("gateway", {})
    lines.append(f"ADDR    : {gateway.get('ADDR', 'N/A')}")
    lines.append(f"RTT     : {gateway.get('RTT', 'N/A')}")
    lines.append(f"STATUS  : {gateway.get('STATUS', 'N/A')}")

    # 分隔线
    lines.append("-" * 20)

    # 外网连通性
    lines.append("[ INTERNET ]")
    internet = results.get("internet", {})
    lines.append(f"TARGET  : {internet.get('TARGET', 'N/A')}")
    lines.append(f"RTT     : {internet.get('RTT', 'N/A')}")
    lines.append(f"STATUS  : {internet.get('STATUS', 'N/A')}")

    # 分隔线
    lines.append("-" * 20)

    # DNS信息
    lines.append("[ DNS ]")
    dns = results.get("dns", {})
    lines.append(f"TARGET  : {dns.get('TARGET', 'N/A')}")
    lines.append(f"RESOLVE : {dns.get('RESOLVE', 'N/A')}")
    lines.append(f"STATUS  : {dns.get('STATUS', 'N/A')}")

    # 分隔线
    lines.append("-" * 20)

    # 公网IP
    lines.append("[ PUBLIC ]")
    lines.append(f"IP      : {results.get('public_ip', 'N/A')}")

    # 分隔线
    lines.append("-" * 20)

    # 汇总
    lines.append("[ SUMMARY ]")
    summary = results.get("summary", {})
    dhcp = summary.get("DHCP", "N/A")
    gw = summary.get("GW", "N/A")
    wan = summary.get("WAN", "N/A")
    dns_status = summary.get("DNS", "N/A")
    summary_line = f"DHCP={dhcp} --- GW={gw} --- WAN={wan} --- DNS={dns_status}"
    lines.append(summary_line)

    # 页脚
    lines.append("=" * 50)

    return "\n".join(lines)
