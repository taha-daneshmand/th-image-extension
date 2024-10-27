# TH Image Extension

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat)
![Pillow](https://img.shields.io/badge/Pillow-9.x-yellow?style=flat)
![Brotli](https://img.shields.io/badge/Brotli-1.x-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat)

A simple custom image format (`.th`) designed to compress and display RGBA images using Python, Brotli compression, and the Pillow library. This project provides the tools to convert standard images to `.th` format, as well as load and display `.th` images in a Tkinter GUI. The `.th` format is compact, efficient, and ideal for applications where file size and display simplicity are priorities.

## Features
- **Custom Format**: Save images in `.th` format with Brotli compression.
- **Compact Storage**: Smaller file sizes due to Brotli’s efficient compression.
- **Easy Display**: Display `.th` images with Tkinter, making it simple to integrate into Python applications.

## How It Works
The `.th` file structure consists of:
1. **Header**: 
   - Signature (`THIMG`) to verify file integrity.
   - Image width, height, and color depth.
2. **Compressed Data**:
   - RGBA pixel data compressed using Brotli.

## Installation
Ensure the following libraries are installed:
```bash
pip install pillow brotli colorama
```

## Usage

### 1. Convert an Image to `.th` Format
To convert an image to `.th` format:
```bash
python main.py convert <input_image> <output_image.th>
```

### 2. Display a `.th` Image
To display a `.th` image:
```bash
python main.py display <file.th>
```

### Example
```bash
# Convert example.png to example.th
python main.py convert example.png example.th

# Display example.th
python main.py display example.th
```

## Code Overview
- **convert_to_th**: Converts a standard image to `.th` format, compressing RGBA data using Brotli.
- **read_th**: Reads a `.th` file, decompresses pixel data, and returns width, height, and pixel data.
- **display_th**: Uses Tkinter to display the decompressed image.

## File Structure of `.th`
```
- Signature: 5 bytes (THIMG)
- Width: 4 bytes (unsigned int)
- Height: 4 bytes (unsigned int)
- Color Depth: 1 byte (always 32 for RGBA)
- Compressed Size: 4 bytes (unsigned int)
- Compressed Pixel Data: variable size (Brotli-compressed RGBA data)
```

## Requirements
- **Python** 3.x
- **Pillow** 9.x
- **Brotli** 1.x
- **Tkinter** (for image display)

## License
This project is licensed under the MIT License.
