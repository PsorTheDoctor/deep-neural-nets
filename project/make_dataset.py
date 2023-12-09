import cv2
from pathlib import Path

input_path = 'images/'
output_path = 'results/'
file_paths = list(Path(input_path).glob('*.jpg'))
window_id  = ''

for file_path in file_paths:
    file_name = str(file_path)[6:]
    img = cv2.imread(input_path + file_name)
    cv2.imshow(window_id, img)

    x, y, w, h = cv2.selectROI(
        window_id, img, fromCenter=False, showCrosshair=False
    )
    if (x, y, w, h) != (0, 0, 0, 0):
        cv2.imwrite(output_path + file_name, img[y: y + h, x: x + w])
