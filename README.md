

# 🌐 Basic Network Sniffing Tool

This project implements a basic network sniffing tool using Python, providing functionality to capture and log network traffic using the `scapy` library. Ensure to consider ethical implications and legal permissions when working on such projects.

## 📖 Overview

This network sniffing tool captures and logs network packets, displaying basic information about each packet. It saves the captured data to a text file (`network_sniffing_log.txt`).

## 🛠️ Features

- Capture and log network packets.
- Display basic information about each captured packet.
- Simple CLI interface built with Python.

## 🚀 How to Execute the Program

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Install necessary dependencies using pip:
   ```sh
   pip install scapy
   ```

3. **Run the Program:**
   ```sh
   python network_sniffer.py
   ```

## 📂 Code Overview

### File: `network_sniffer.py`

This file contains the main implementation of the network sniffing tool using the `scapy` library.

#### Imports
```python
from scapy.all import sniff, wrpcap
import os
```

#### Functions:

- **`start_sniffing(self):`** Starts capturing network packets.
- **`process_packet(self, packet):`** Processes each captured packet and logs basic information.
- **`write_to_file(self, packet):`** Writes captured packet information to `network_sniffing_log.txt`.

### Usage Instructions:

- Execute `python network_sniffer.py` to start capturing packets.
- View captured packet information in the console output.
- Logs are saved to `network_sniffing_log.txt` in the same directory as `network_sniffer.py`.

## 🙏 Contribution and Issues

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

### Ethical Considerations

- Ensure you have appropriate permissions and legal rights before using or distributing a network sniffing tool.
- Respect privacy and adhere to ethical standards when developing or using such software.

---

