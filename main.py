import sys
import os
import struct
import brotli
import tkinter as tk
from PIL import Image
from colorama import Fore, Style, init

init(autoreset=True)

def convert_to_th(input_path, output_path):
    image = Image.open(input_path).convert("RGBA")
    width, height = image.size
    rgba_data = bytearray(pixel for pixel in image.getdata() for pixel in pixel)
    
    compressed_data = brotli.compress(rgba_data)
    
    with open(output_path, 'wb') as f:
        f.write(b'THIMG')
        f.write(struct.pack('I', width))
        f.write(struct.pack('I', height))
        f.write(struct.pack('B', 32))
        f.write(struct.pack('I', len(compressed_data)))
        f.write(compressed_data)
    
    print(Fore.GREEN + f"[SUCCESS] {input_path} converted to {output_path}")

def read_th(file_path):
    with open(file_path, 'rb') as f:
        if f.read(5) != b'THIMG':
            raise ValueError(Fore.RED + "[ERROR] Invalid .th file format.")
        
        width = struct.unpack('I', f.read(4))[0]
        height = struct.unpack('I', f.read(4))[0]
        color_depth = struct.unpack('B', f.read(1))[0]
        compressed_size = struct.unpack('I', f.read(4))[0]
        compressed_data = f.read(compressed_size)
        
        pixel_data = brotli.decompress(compressed_data)
        
    return width, height, pixel_data

def display_th(file_path):
    width, height, pixel_data = read_th(file_path)

    root = tk.Tk()
    root.title(file_path)
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    img = tk.PhotoImage(width=width, height=height)

    for y in range(height):
        for x in range(width):
            idx = (y * width + x) * 4
            r, g, b, a = pixel_data[idx:idx+4]
            color = f'#{r:02x}{g:02x}{b:02x}'
            img.put(color, (x, y))

    canvas.create_image((width // 2, height // 2), image=img, state="normal")
    root.mainloop()

def main():
    if len(sys.argv) < 3:
        print(Fore.CYAN + "Usage: python main.py <command> <input_image> [output_image.th]")
        print(Fore.YELLOW + "Commands:")
        print(Fore.YELLOW + "  convert - Convert an image to .th format")
        print(Fore.YELLOW + "  display - Display a .th image")
        return

    command = sys.argv[1]
    input_path = sys.argv[2]

    if command == "convert":
        if len(sys.argv) != 4:
            print(Fore.RED + "Usage: python main.py convert <input_image> <output_image.th>")
            return
        
        output_path = sys.argv[3]

        if not os.path.isfile(input_path):
            print(Fore.RED + f"[ERROR] {input_path} does not exist.")
            return
        
        if not output_path.endswith('.th'):
            print(Fore.RED + "[ERROR] Output file must have a .th extension.")
            return

        convert_to_th(input_path, output_path)

    elif command == "display":
        if not os.path.isfile(input_path):
            print(Fore.RED + f"[ERROR] {input_path} does not exist.")
            return
        
        display_th(input_path)

    else:
        print(Fore.RED + f"[ERROR] Unknown command: {command}")

if __name__ == "__main__":
    main()
