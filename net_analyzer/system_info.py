"""系统信息模块"""
import platform


def get_system_info():
    """
    获取系统信息
    :return: dict 包含 OS, VERSION, ARCH
    """
    return {
        "OS": platform.system(),
        "VERSION": platform.version(),
        "ARCH": platform.machine()
    }
