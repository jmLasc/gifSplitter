import sys
import os
from PIL import Image

# Check that initial command line input is proper
try:
    target = sys.argv[1]
except:
    print("Not all args supplied")
    print("Format: py .\main.py [target]")
    exit()

if not (os.path.isfile(target)):
    print("The target is a file that does not exist.")
    exit()

if (os.path.splitext(target)[1].lower() != ".gif"):
    print("Target file is not a gif")
    exit()

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

#Image Creation
width, height = gif.size
finalWidth = width * len(frames)
toSave = Image.new("RGBA", (finalWidth, height))
offset = 0

for frame in frames:
    toSave.paste(frame, (offset, 0))
    offset += width

#Saving Output
destination = "./output"
if not os.path.exists(destination):
    os.makedirs(destination)
    print("Output directory not found, making folder 'output'.")

#Checking for duplicates
output = "output.png"
if os.path.exists("output/output.png"):
    suffix=1
    name, extension = os.path.splitext(output)
    while os.path.exists("{0}/{1}-{2}{3}".format(destination, name, suffix, extension)):
        suffix += 1
    output = "{0}-{1}{2}".format(name, suffix, extension)

toSave.save("{0}/{1}".format(destination, output))

print("Operation complete.")