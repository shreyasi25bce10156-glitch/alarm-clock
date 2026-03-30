"""
Python Alarm Clock GUI (Tkinter)
Save as: alarm_gui.py

Features:
- Enter alarm time in HH:MM:SS or HH:MM format
- Set and Stop alarm
- Live clock display
- Plays Windows beep when alarm triggers, falls back to system bell on other OS

No external libraries required.
"""

import tkinter as tk
from tkinter import messagebox
import datetime
import time
import platform
import threading

try:
    import winsound
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False


class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("360x200")
        self.root.resizable(False, False)

        self.alarm_time = None
        self.alarm_set = False

        # UI
        self.time_label = tk.Label(root, text="--:--:--", font=(None, 28))
        self.time_label.pack(pady=(10, 5))

        frm = tk.Frame(root)
        frm.pack(pady=5)

        tk.Label(frm, text="Alarm (HH:MM or HH:MM:SS):").grid(row=0, column=0, padx=5)
        self.entry = tk.Entry(frm, width=12)
        self.entry.grid(row=0, column=1)

        btn_set = tk.Button(frm, text="Set Alarm", command=self.set_alarm)
        btn_set.grid(row=0, column=2, padx=5)

        btn_stop = tk.Button(frm, text="Stop Alarm", command=self.stop_alarm)
        btn_stop.grid(row=1, column=2, padx=5, pady=(8,0))

        self.status_label = tk.Label(root, text="No alarm set.", fg="gray")
        self.status_label.pack(pady=(8,0))

        # start the clock update loop
        self.update_clock()

    def update_clock(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=now)

        # check alarm
        if self.alarm_set and self.alarm_time is not None:
            # compare only the provided precision
            if len(self.alarm_time.split(':')) == 2:
                compare_now = now[:5]  # HH:MM
            else:
                compare_now = now  # HH:MM:SS

            if compare_now == self.alarm_time:
                self.trigger_alarm()

        # schedule next update
        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        raw = self.entry.get().strip()
        if not raw:
            messagebox.showwarning("Invalid", "Please enter alarm time.")
            return

        parts = raw.split(':')
        if len(parts) not in (2,3):
            messagebox.showwarning("Invalid", "Use HH:MM or HH:MM:SS format.")
            return

        try:
            if len(parts) == 2:
                hh = int(parts[0]); mm = int(parts[1]); ss = 0
            else:
                hh = int(parts[0]); mm = int(parts[1]); ss = int(parts[2])

            # validate
            if not (0 <= hh <= 23 and 0 <= mm <= 59 and 0 <= ss <= 59):
                raise ValueError()

            # store normalized string
            if len(parts) == 2:
                self.alarm_time = f"{hh:02d}:{mm:02d}"
            else:
                self.alarm_time = f"{hh:02d}:{mm:02d}:{ss:02d}"

            self.alarm_set = True
            self.status_label.config(text=f"Alarm set for {self.alarm_time}", fg="green")
            messagebox.showinfo("Alarm Set", f"Alarm set for {self.alarm_time}")

        except ValueError:
            messagebox.showwarning("Invalid", "Invalid time values. Use numbers in proper ranges.")

    def stop_alarm(self):
        if self.alarm_set:
            self.alarm_set = False
            self.alarm_time = None
            self.status_label.config(text="No alarm set.", fg="gray")
            messagebox.showinfo("Stopped", "Alarm cancelled.")
        else:
            messagebox.showinfo("Info", "No alarm to stop.")

    def trigger_alarm(self):
        # prevent retriggering
        self.alarm_set = False
        self.status_label.config(text="RINGING!", fg="red")

        # play sound in a separate thread so UI doesn't freeze
        t = threading.Thread(target=self.play_sound_and_notify, daemon=True)
        t.start()

    def play_sound_and_notify(self):
        try:
            for i in range(10):
                if HAS_WINSOUND and platform.system() == 'Windows':
                    winsound.Beep(1000, 700)
                else:
                    # fallback: system bell
                    print('\a', end='')
                time.sleep(0.3)
        finally:
            # after ringing, show a dialog on the main thread
            self.root.after(0, lambda: messagebox.showinfo("Alarm", "Time's up!"))
            self.root.after(0, lambda: self.status_label.config(text="No alarm set.", fg="gray"))


if __name__ == '__main__':
    root = tk.Tk()
    app = AlarmApp(root)
    root.mainloop()