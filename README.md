# ⏰ Python Alarm Clock (GUI Version)

A clean and simple **Tkinter-based Alarm Clock** created in Python. This project includes a live digital clock display, alarm input field, alarm notifications, and beep sound alerts.

---

## 🚀 Features

* Live digital clock (HH:MM:SS)
* Set alarm in **HH:MM** or **HH:MM:SS** format
* Alarm popup notification
* Alarm beep sound (Windows) or system bell (other OS)
* Stop/Cancel alarm anytime
* No external libraries required

---

## 🛠 Technologies Used

* **Python 3.x**
* **Tkinter** (built‑in GUI library)
* **datetime**, **time** (time management)
* **winsound** (Windows sound module)
* **threading** (for non‑blocking alarm sound)

---

## 📂 Project Structure

```
alarm_gui.py
README.md
```

---

## 💻 How to Run

1. Save the script as `alarm_gui.py`
2. Run using:

```
python alarm_gui.py
```

3. A window will open showing:

   * Digital clock
   * Alarm input box
   * Buttons: Set Alarm / Stop Alarm

---

## 📌 How to Use

1. Enter time in **HH:MM** or **HH:MM:SS** format
2. Click **Set Alarm**
3. When time matches:

   * Alarm beeps
   * Popup appears
4. To cancel alarm, click **Stop Alarm**

---

## 🔊 Sound Behavior

* **Windows:** Uses `winsound.Beep()`
* **Linux/macOS:** Falls back to system bell (`print("\a")`)

---

## 📦 Full Source Code

The complete source code is available inside `alarm_gui.py` in this project.

---

## ⚙️ Future Upgrades

* Add MP3 ringtone support
* Add multiple alarms
* Add snooze button
* Add dark/light theme
* Add calendar-based scheduling

---

## 📝 License

Free to use, modify, and upgrade as needed.
