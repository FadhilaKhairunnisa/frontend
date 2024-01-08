import cv2
import matplotlib.pyplot as plt

# Baca citra
image_path = 'CitraA.jpg'  # Ganti dengan path citra Anda
image = cv2.imread(image_path)

# Konversi citra ke format HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Tampilkan citra asli dan citra dalam format HSV
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Citra Asli')

plt.subplot(1, 2, 2)
plt.imshow(hsv_image)
plt.title('Citra HSV')

plt.show()