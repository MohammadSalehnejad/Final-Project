from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# تابع تبدیل تصویر به آرایه
def image_to_array(image_path):
    image = Image.open(image_path).convert('L')  # تبدیل به خاکستری
    return np.array(image)

# تابع کانولوشن برای آرایه دو بعدی
def convolution2d(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    output = np.zeros_like(image)

    # افزودن صفر در لبه‌های تصویر ورودی
    padded_image = np.pad(image, ((kernel_height // 2, kernel_height // 2), (kernel_width // 2, kernel_width // 2)), mode='constant')

    for y in range(image_height):
        for x in range(image_width):
            output[y, x] = np.sum(kernel * padded_image[y:y + kernel_height, x:x + kernel_width])
    
    return output

# تابع تشخیص لبه
def edge_detection(image_array):
    edge_filter = np.array([[-1, -1, -1],
                            [-1,  8, -1],
                            [-1, -1, -1]])
    return convolution2d(image_array, edge_filter)

# استفاده نمونه
image_path = 'path/to/image.jpg'
image_array = image_to_array(image_path)
edges = edge_detection(image_array)

# ذخیره نتیجه تشخیص لبه به فایل
with open('edges.txt', 'w') as f:
    np.savetxt(f, [edges])

plt.imshow(edges, cmap='gray')
plt.savefig('edges.png')  # ذخیره تصویر لبه‌ها به فایل
plt.show()
