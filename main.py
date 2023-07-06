import sys
import os
from PIL import Image

# Ensuring initial command line input is proper

try:
    target = sys.argv[1]
    mode = sys.argv[2]
except:
    print("Not all args supplied")
    print("Format: py .\main.py [path] [i/t]")
    exit()

if not (os.path.isdir(target) or os.path.isfile(target)):
    print("The path is not a valid folder or file.")
    exit()

if not (mode == 'i' or mode == 't'):
    print("The mode must be either i or t.")
    # exit()

# Processing

gif = Image.open(target)
frames = []

try:
    while True:
        current = gif.copy()
        frames.append(current)
        gif.seek(gif.tell() + 1)
except EOFError:
    pass

width, height = gif.size
finalWidth = width * len(frames)
toSave = Image.new("RGBA", (finalWidth, height))
offset = 0

for frame in frames:
    toSave.paste(frame, (offset, 0))
    offset += width

toSave.save("./output.png")