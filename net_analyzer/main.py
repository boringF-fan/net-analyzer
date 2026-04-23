#!/usr/bin/env python3
"""
NetAnalyer - Network Diagnostic Tool
快速采集 PC 网络状态，输出结构化结果供工程师远程判断
"""

import sys
import os

# 设置控制台编码 (Windows)
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# 确保当前包路径
if getattr(sys, 'frozen', False):
    # PyInstaller 打包后
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, bundle_dir)

from diagnosis import NetworkDiagnosis


def main():
    """主入口"""
    diag = NetworkDiagnosis()
    diag.run()


if __name__ == "__main__":
    main()
