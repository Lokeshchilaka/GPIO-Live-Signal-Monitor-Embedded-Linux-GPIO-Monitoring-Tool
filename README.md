# 🚀 GPIO Live Signal Monitor — Embedded Linux GPIO Monitoring Tool

![GPIO Monitor](images/banner.png)

> ⚡ Detect • Monitor • Analyze  
> A Python-based Embedded Linux GPIO monitoring tool using `libgpiod` utilities for real-time signal observation.

---

# 📌 Project Overview

Modern Embedded Linux systems interact with hardware using:

- ⚡ GPIO pins  
- 🔌 Sensors  
- 📡 External signals  
- 🤖 Embedded peripherals  

This project demonstrates a **real-time GPIO signal monitoring system** built using Python and Linux GPIO interfaces.

The tool continuously monitors GPIO pin state changes and detects:

- 🟢 HIGH signal events  
- 🔴 LOW signal events  
- ⚡ Real-time hardware transitions  

---

# 🧠 Core Concept

Linux exposes GPIO devices through:

```bash
/dev/gpiochipX
```

Using:

```bash
gpioget
```

This project reads live GPIO states from the Linux GPIO subsystem and performs event detection in real time.

---

# 🗂️ Project Structure

![Project Files](images/files.png)

---

# 🔄 System Workflow

```text
GPIO Hardware Signal
          ↓
Linux GPIO Driver
          ↓
/dev/gpiochipX
          ↓
gpioget (libgpiod)
          ↓
Python subprocess
          ↓
Signal Monitoring Logic
          ↓
Real-Time Event Detection
```

---

# ⚙️ Version 1 — Basic GPIO Monitoring

![V1 Output](images/v1.png)

### ⚡ Features

- Reads GPIO values continuously  
- Supports dynamic GPIO chip selection  
- Supports dynamic GPIO pin selection  
- Detects signal state changes  
- Displays HIGH and LOW events  

---

# 🧠 Internal Working

### 🔹 User Input

```python
chip = input("Enter GPIO chip: ")
pin = input("Enter GPIO pin: ")
```

Allows dynamic monitoring of different GPIO devices.

---

### 🔹 GPIO Reading

```python
result = subprocess.getoutput(
    f"sudo gpioget {chip} {pin}"
)
```

Uses Linux `gpioget` utility to fetch live GPIO state.

---

### 🔹 State Monitoring

```python
if current_state != previous_state:
```

Detects signal transitions.

---

### 🔹 HIGH Signal Detection

```python
if current_state == "1":
```

Indicates:

- 🟢 HIGH voltage detected  
- ⚡ Active GPIO signal  

---

### 🔹 LOW Signal Detection

```python
elif current_state == "0":
```

Indicates:

- 🔴 LOW voltage detected  
- ⚡ Signal inactive  

---

### 🔹 Continuous Monitoring

```python
while True:
```

Creates a real-time monitoring loop.

---

### 🔹 Refresh Timing

```python
time.sleep(1)
```

Monitors GPIO state every 1 second.

---

# 🖥️ Example Output

![Live Monitoring](images/v2.png)

```text
===== LIVE GPIO MONITOR =====

GPIO 5 changed to: 1
EVENT: SIGNAL HIGH DETECTED

GPIO 5 changed to: 0
EVENT: SIGNAL LOW DETECTED
```

---

# 🧠 Linux GPIO Internals

This project indirectly interacts with:

- 🐧 Linux GPIO subsystem  
- 🔧 GPIO drivers  
- ⚡ Hardware registers  
- 📡 Character device interfaces  

---

# 🔄 Internal Linux GPIO Flow

```text
Python Script
      ↓
subprocess
      ↓
gpioget
      ↓
libgpiod
      ↓
ioctl() System Call
      ↓
/dev/gpiochipX
      ↓
Linux GPIO Subsystem
      ↓
GPIO Driver
      ↓
Hardware Registers
      ↓
Electrical Signal
```

---

# 🎯 Key Learning Outcomes

- 🐧 Embedded Linux GPIO subsystem  
- ⚡ Real-time GPIO monitoring  
- 🧠 Event-driven system observation  
- 🔧 Linux hardware interfaces  
- 📡 GPIO signal handling  
- 🖥️ Python subprocess communication  
- ⚙️ Embedded system debugging concepts  

---

# 🚀 Real-World Applications

- 🤖 Robotics systems  
- 📡 Sensor monitoring  
- 🏭 Industrial automation  
- 🚗 Automotive embedded systems  
- 🛸 Embedded hardware debugging  
- ⚡ Signal event detection systems  

---

# 🧩 Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Monitoring logic |
| 🐧 Linux | Embedded operating system |
| ⚡ GPIO | Hardware signal interface |
| 🔧 libgpiod | GPIO user-space utilities |
| 🖥️ subprocess | Command execution |
| ⏱️ time | Monitoring intervals |

---

# ▶️ How to Run

### 🔹 Install GPIO Utilities

```bash
sudo apt install gpiod
```

---

### 🔹 Run the Monitor

```bash
python3 gpio_monitor.py
```

👉 [View Code](./files/gpio_monitor.py)

---

# 📋 Requirements

- 🐧 Linux system  
- ⚡ GPIO-supported hardware  
- 🔧 libgpiod installed  
- 🔑 sudo permissions  

---

# 🔮 Future Improvements

- ⚡ Interrupt-based GPIO monitoring  
- 📊 GPIO activity dashboard  
- 🟢 Colored terminal UI  
- 📈 Signal logging system  
- 🔔 GPIO alert notifications  
- 🌐 Web-based monitoring interface  

---

# 🏁 Final Note

This project demonstrates how Embedded Linux systems monitor and interact with real hardware signals through the Linux GPIO subsystem.

It provides hands-on understanding of:

- 🐧 Linux GPIO architecture  
- ⚡ Hardware-software interaction  
- 🔧 Embedded debugging workflows  
- 📡 Real-time signal monitoring systems  

---

# 👨‍💻 Author

## Lokesh Jaya Rao
Embedded Systems Engineer ⚙️  
Embedded Linux Developer 🐧
