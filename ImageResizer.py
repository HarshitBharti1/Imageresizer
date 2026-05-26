import cv2
import os

image_path = "Colors.jpg"
image = cv2.imread(image_path)

sizes = [
    (640, 480),
    (800, 600),
    (1024, 768)
]

base_name = os.path.splitext(os.path.basename(image_path))[0]

for i, (w, h) in enumerate(sizes, start=1):
    resized = cv2.resize(image, (w, h))
    window_name = f"{w}x{h}"
    cv2.imshow(window_name, resized)

    output_path = f"{base_name}_{w}x{h}.jpg"
    cv2.imwrite(output_path, resized)

cv2.waitKey(0)
cv2.destroyAllWindows()