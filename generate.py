import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def generate_video(text):
    width, height = 100, 100

    codec = cv2.VideoWriter.fourcc(*'MP4V')
    out = cv2.VideoWriter("output.mp4", codec, 24, (width, height))

    font_size = 70
    font_path = r"C:\Windows\Fonts\Arial.ttf"
    font = ImageFont.truetype(font_path, font_size)

    pil_image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(pil_image)
    text_size = draw.textbbox((0, 0), text, font=font)

    start_x = width
    end_x = -text_size[2]
    steps = 24 * 3
    step = (start_x - end_x) / steps

    for t in range(steps):
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        pil_image = Image.fromarray(frame)
        draw = ImageDraw.Draw(pil_image)

        current_x = start_x - step * t
        current_y = (height - (text_size[3] - text_size[1])) // 2 - 10
        draw.text((current_x, current_y), text, font=font, fill=(255, 255, 255))

        frame = np.array(pil_image)
        out.write(frame)

    out.release()
