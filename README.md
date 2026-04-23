# NetAnalyer

A lightweight Python network diagnostic tool that collects PC network status and outputs structured results for remote troubleshooting.

## Features

- **System Info**: OS, version, architecture
- **Network Interfaces**: List all adapters with status and IPv4 address
- **DHCP Detection**: Identifies DHCP failures (169.254.x.x APIPA addresses)
- **Gateway Check**: Default gateway detection and connectivity test
- **Internet Connectivity**: Tests connection to 114.114.114.114:53
- **DNS Resolution**: Resolves www.baidu.com
- **Public IP**: Retrieves external IP address

## Requirements

- Python 3.7+
- **No external dependencies!** (uses standard library only)

## Usage

```bash
python net_analyzer/main.py
```

## Build Executable (PyInstaller)

For non-technical users, build a standalone `.exe` file (~15MB):

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Build

```bash
cd net_analyzer
pyinstaller --onefile --name net_analyzer --console --hidden-import=urllib.request main.py
```

### 3. Run

The executable will be in `net_analyzer/dist/net_analyzer.exe`.

```
dist\net_analyzer.exe
```

The output is designed to fit in a standard console window for easy screenshot sharing with network engineers.

## Output Example

```
==================================================
         NET DIAG (Network Diagnostic)
==================================================
[ SYSTEM ]
OS      : Windows
VERSION : 10.0.19041
ARCH    : AMD64
--------------------
[ NETWORK ]
以太网适配器 以太网  UP | 192.168.11.83
--------------------
[ GATEWAY ]
ADDR    : 192.168.11.1
RTT     : 1.15 ms
STATUS  : OK
--------------------
[ INTERNET ]
TARGET  : 114.114.114.114:53
RTT     : 9.99 ms
STATUS  : OK
--------------------
[ DNS ]
TARGET  : www.baidu.com
RESOLVE : 180.101.50.188
STATUS  : OK
--------------------
[ PUBLIC ]
IP      : 203.0.113.1
--------------------
[ SUMMARY ]
DHCP=1 --- GW=1 --- WAN=1 --- DNS=1
==================================================
```

## Troubleshooting Guide

| DHCP | GW  | WAN  | DNS  | Meaning                     |
|------|-----|------|------|-----------------------------|
| 1    | 1   | 1    | 1    | Network is OK               |
| 0    | -   | -    | -    | DHCP failed (APIPA address) |
| 1    | 0   | -    | -    | Gateway unreachable         |
| 1    | 1   | 0    | -    | Internet connection failed   |
| 1    | 1   | 1    | 0    | DNS resolution failed       |

## Project Structure

```
net_analyzer/
├── main.py           # Entry point
├── system_info.py    # System information
├── network_info.py   # Network interface info
├── gateway.py        # Gateway detection
├── connectivity.py   # Internet/DNS tests
├── diagnosis.py      # Main diagnosis logic
└── formatter.py      # Output formatting
```

## License

MIT
