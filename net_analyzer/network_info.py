"""网卡信息模块"""
import subprocess
import re
import platform


def get_network_interfaces():
    """
    获取所有网卡信息（兼容Windows中文系统）
    :return: list of dict 每个网卡包含 name, status, ip
    """
    interfaces = []
    
    if platform.system() != "Windows":
        return [{"name": "Unknown", "status": "N/A", "ip": "N/A"}]
    
    try:
        result = subprocess.run(
            ["ipconfig"],
            capture_output=True,
            text=True,
            timeout=10
        )
        output = result.stdout
        
        current_name = None
        current_ip = "N/A"
        
        for line in output.split("\n"):
            line_stripped = line.strip()
            
            # 检测适配器名称行 (中文: "以太网适配器 以太网" 或 "未知适配器 本地连接")
            # 匹配模式: 适配器关键字后面跟着具体名称，然后是冒号
            if re.match(r'^(以太网|无线|本地|Wi-Fi|VMware|未知|蓝牙|USB|Cellular).*[^:]$', line_stripped):
                # 保存上一个适配器
                if current_name:
                    interfaces.append({
                        "name": current_name,
                        "status": "UP" if current_ip != "N/A" else "DOWN",
                        "ip": current_ip
                    })
                
                # 提取适配器名称
                current_name = line_stripped
                current_ip = "N/A"
                
            # 检测IPv4地址行 (中文: "IPv4 地址 . . . . . . . . . . . . . : 192.168.1.1")
            elif "IPv4" in line_stripped and ":" in line_stripped:
                parts = line_stripped.split(":")
                if len(parts) >= 2:
                    potential_ip = parts[1].strip()
                    if re.match(r"^\d+\.\d+\.\d+\.\d+$", potential_ip):
                        current_ip = potential_ip
                            
        # 保存最后一个适配器
        if current_name:
            interfaces.append({
                "name": current_name,
                "status": "UP" if current_ip != "N/A" else "DOWN",
                "ip": current_ip
            })
        
        # 如果没有找到，返回至少一个虚拟适配器
        if not interfaces:
            interfaces.append({
                "name": "Unknown",
                "status": "N/A",
                "ip": "N/A"
            })
            
    except Exception as e:
        interfaces.append({
            "name": "Error",
            "status": "N/A",
            "ip": "N/A"
        })
    
    return interfaces


def is_dhcp_failed(interfaces):
    """
    判断DHCP是否失败
    无IP -> DHCP失败
    169.254.x.x -> DHCP失败
    正常IP -> DHCP正常
    """
    for iface in interfaces:
        if iface["status"] == "UP" and iface["ip"] != "N/A":
            ip = iface["ip"]
            if ip.startswith("169.254."):
                return True
            return False
    return True
