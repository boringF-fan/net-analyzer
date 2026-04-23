#!/usr/bin/env python3
"""
NetAnalyer - Network Diagnostic Tool
快速采集 PC 网络状态，输出结构化结果供工程师远程判断
"""

import os
import time
import sys

# 设置控制台编码 (Windows)
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 确保当前包路径
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, bundle_dir)

from diagnosis import NetworkDiagnosis


def main():
    diag = NetworkDiagnosis()
    diag.run()
    sys.stdout.flush()
    print("\nPress Ctrl+C to exit...")
    sys.stdout.flush()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
