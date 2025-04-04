import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def shader(x, y):
    r1 = 1 - int((x * 3 - 1.5) ** 2 + (y * 3 - 1.5) ** 2)
    r2 = 1 - int((x * 3 - 1.5) ** 2 + (y * 3 - 1.5) ** 2)
    if(x > 0.5 and y < x):
        r1 = 0
        r2 = 0
    r3 = 1 - int((x * 20 - 7) ** 2 + (y * 20 - 7) ** 2)
    return r1, r2, r3


main(shader)