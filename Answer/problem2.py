import numpy as np
import unittest

# تابع محاسبه میدان الکتریکی در یک نقطه مشخص


def electric_field(charge_pos, charge_val, point):
    k = 8.99e9  # N*m^2/C^2
    r = np.array(point) - np.array(charge_pos)
    r_mag = np.linalg.norm(r)
    r_hat = r / r_mag
    E = (k * charge_val / r_mag**2) * r_hat
    return E

# تابع محاسبه میدان الکتریکی کل در یک نقطه مشخص


def total_electric_field(charges, point):
    E_total = np.array([0.0, 0.0])
    for charge in charges:
        E_total += electric_field(charge['pos'], charge['val'], point)
    return E_total

# تابع محاسبه میدان الکتریکی از یک خط بار یکنواخت


def electric_field_line(charge_density, line_length, point):
    k = 8.99e9  # N*m^2/C^2
    E_total = np.array([0.0, 0.0])
    num_segments = 100  # تعداد بخش‌ها برای تقریب خط بار
    dl = line_length / num_segments
    for i in range(num_segments + 1):
        charge_pos = np.array([i * dl, 0])
        charge_val = charge_density * dl
        E_total += electric_field(charge_pos, charge_val, point)
    return E_total


# استفاده نمونه
charges = [{'pos': [0, 0], 'val': 1e-9}, {'pos': [1, 0], 'val': -1e-9}]
point = [0.5, 0.5]

E_total = total_electric_field(charges, point)
# ذخیره میدان الکتریکی کل به فایل
with open('total_electric_field.txt', 'w') as f:
    np.savetxt(f, [E_total])

charge_density = 1e-9
line_length = 1.0
E_line = electric_field_line(charge_density, line_length, point)
# ذخیره میدان الکتریکی از خط به فایل
with open('electric_field_line.txt', 'w') as f:
    np.savetxt(f, [E_line])

print("Total Electric Field at {}: {}".format(point, E_total))
print("Electric Field from Line at {}: {}".format(point, E_line))


class TestElectricField(unittest.TestCase):

    def test_electric_field(self):
        charge_pos = [0, 0]
        charge_val = 1e-9
        point = [1, 0]

        expected_E = np.array([8.99e9 * charge_val, 0])

        E = electric_field(charge_pos, charge_val, point)

        self.assertTrue(np.allclose(E, expected_E))


if __name__ == '__main__':
    unittest.main()
