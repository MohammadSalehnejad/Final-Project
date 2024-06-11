# تابع محاسبه مساحت مقطع هسته
def compute_transformer_area(power, voltage_primary, current_density):
    area = power / (voltage_primary * current_density)
    return area

# تابع محاسبه تعداد دورهای سیم‌پیچ
def compute_winding_turns(voltage_primary, voltage_secondary, turns_primary):
    turns_secondary = (voltage_secondary / voltage_primary) * turns_primary
    return turns_primary, turns_secondary

# استفاده نمونه
power = 1000  # توان در وات
voltage_primary = 220  # ولتاژ اولیه در ولت
current_density = 5  # چگالی جریان در A/mm^2

area = compute_transformer_area(power, voltage_primary, current_density)
turns_primary = 100  # تعداد دورهای اولیه به عنوان مثال
voltage_secondary = 110  # ولتاژ ثانویه در ولت

primary_turns, secondary_turns = compute_winding_turns(voltage_primary, voltage_secondary, turns_primary)

# ذخیره مساحت مقطع و تعداد دورهای سیم‌پیچ به فایل
with open('transformer_parameters.txt', 'w') as f:
    f.write(f"Core Cross-Sectional Area: {area} mm^2\n")
    f.write(f"Primary Turns: {primary_turns}, Secondary Turns: {secondary_turns}\n")

print(f"Core Cross-Sectional Area: {area} mm^2")
print(f"Primary Turns: {primary_turns}, Secondary Turns: {secondary_turns}")
