import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np

class SignalProcessorApp:
    def __init__(self, master):
        self.master = master
        master.title("Signal Processor")

        self.label = tk.Label(master, text="Signal Processor")
        self.label.pack()

        self.plot_button = tk.Button(master, text="Plot Signals", command=self.plot_signals)
        self.plot_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    # تابع رسم سیگنال‌ها
    def plot_signals(self):
        t = np.linspace(0, 1, 400)
        signal1 = np.cos(2 * np.pi * 50 * t)
        signal2 = np.cos(2 * np.pi * 10 * t)
        combined_signal = signal1 + signal2

        # ذخیره سیگنال‌ها در فایل
        with open('signal1.txt', 'w') as f:
            np.savetxt(f, [signal1])
        with open('signal2.txt', 'w') as f:
            np.savetxt(f, [signal2])
        with open('combined_signal.txt', 'w') as f:
            np.savetxt(f, [combined_signal])

        plt.figure()
        plt.subplot(3, 1, 1)
        plt.plot(t, signal1, label="Signal 1 (50Hz)")
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(t, signal2, label="Signal 2 (10Hz)")
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(t, combined_signal, label="Combined Signal")
        plt.legend()

        plt.savefig('signals.png')  # ذخیره نمودارها به فایل تصویر
        plt.show()

root = tk.Tk()
app = SignalProcessorApp(root)
root.mainloop()
