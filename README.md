# ProtogenOS - Coming Soon

## 🚀 Features
- **LED Matrix Face**: Displays animated expressions and customizable visuals.
- **NFC Friend Storage**: Stores UID and basic details of other ProtogenOS users.
- **UDP Broadcast Sync**: Detects and syncs with nearby ProtogenOS devices.
- **Wi-Fi Web Control Surface (WWCS)**: Web-based interface for real-time customization.
- **OLED Status Screen**: Displays integration status and system info.
- **Ultrasonic Sensor (USS)**: Detects proximity and user interactions.
- **IMU (Gyroscope/Accelerometer) for Tail Movements**: Captures motion for expressions or responses.

## 🛠 Hardware Requirements
- **Raspberry Pi 2GB+** (for LED matrix processing)
- **ESP32 with Wi-Fi** (for MAC address sniffing and network communication)
- **NFC Module** (for storing friend details)
- **OLED Display** (for system status updates)
- **Ultrasonic Sensor** (for interactive detection)
- **IMU Sensor** (for tail movement tracking)

## 📦 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/mvoud/ProtogenOS.git
   cd ProtogenOS
   ```
2. Install dependencies on Raspberry Pi:
   ```sh
   sudo apt update && sudo apt install python3 python3-pip
   pip install -r requirements.txt
   ```
3. Flash the ESP32 firmware using Arduino IDE or PlatformIO.
4. Configure Wi-Fi and device settings in `config.json`.
5. Run the main script:
   ```sh
   python3 main.py
   ```

## 🔧 Configuration
Modify the `config.json` file to customize:
- Wi-Fi credentials
- LED matrix expressions
- UDP sync settings
- Tail movement thresholds

## 🤝 Contributing
Feel free to open issues or submit pull requests to improve ProtogenOS.

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for details.
