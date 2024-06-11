import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import unittest

# تابع کانولوشن


def convolution(signal, kernel):
    signal_len = len(signal)
    kernel_len = len(kernel)
    conv_len = signal_len + kernel_len - 1
    result = np.zeros(conv_len)

    for i in range(conv_len):
        for j in range(kernel_len):
            if i - j >= 0 and i - j < signal_len:
                result[i] += signal[i - j] * kernel[j]

    return result

# تابع طراحی فیلتر پایین گذر


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# تابع طراحی فیلتر بالا گذر


def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

# تابع اعمال فیلتر پایین گذر


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# تابع اعمال فیلتر بالا گذر


def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y


# تنظیمات نمونه برداری
fs = 100.0  # نرخ نمونه برداری
t = np.arange(0, 10, 1/fs)  # بردار زمان

# سیگنال ترکیبی
signal = np.cos(0.2 * np.pi * t) + np.cos(0.02 * np.pi * t)

# ذخیره سیگنال ترکیبی در فایل
with open('combined_signal.txt', 'w') as f:
    np.savetxt(f, [signal])

# فیلتر کردن سیگنال
low_cutoff = 0.1  # فرکانس قطع پایین
high_cutoff = 0.15  # فرکانس قطع بالا

low_passed = butter_lowpass_filter(signal, low_cutoff, fs)
high_passed = butter_highpass_filter(signal, high_cutoff, fs)

# ذخیره سیگنال‌های فیلتر شده در فایل‌ها
with open('low_frequency_signal.txt', 'w') as f:
    np.savetxt(f, [low_passed])
with open('high_frequency_signal.txt', 'w') as f:
    np.savetxt(f, [high_passed])

# نمایش نتایج
plt.subplot(3, 1, 1)
plt.plot(t, signal, label='Combined Signal')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, low_passed, label='Low Frequency Signal (Filtered)')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, high_passed, label='High Frequency Signal (Filtered)')
plt.legend()

plt.savefig('signal_separation.png')  # ذخیره نمودارها به فایل تصویر
plt.show()



class TestSignalProcessing(unittest.TestCase):
    # تابع تست کانولوشن
    def test_convolution(self):
        signal = [1, 2, 3]
        kernel = [0, 1, 0.5]
        expected = [0, 1, 2.5, 4, 1.5]
        result = convolution(signal, kernel)
        np.testing.assert_array_almost_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
