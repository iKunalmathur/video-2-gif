# Import everything needed to edit video clips
from moviepy.editor import *
from datetime import datetime


# User Input Start/End
filepath = input("📼 Video File Path ? : ") # or "./data/video-sample.mp4"

if filepath == "":
    print("❌ Invalid File Path")
    exit()

start = input("🏁 Start (in seconds) ? [default=0] : ") or 0
end = input("🚧 End (in seconds) ? [default=10] : ") or 10
resize = input("🔍 Resize (between 1 - 0) ? [default=0.3] : ") or 0.3 # reduce its size (to 30% of the original)
speed = input("🐢 Speed (between 1 - 0) ? [default=0.5] : ") or 0.5 # Play at half speed
fps = input("⏲  FPS (Higher FPS higher build time) ? [default=5] : ") or 5 # 5 frames per second

# Load Video File
videoFile = VideoFileClip(filepath)

# Edit videoFile

# Select the subclip(from/start, to/end) in seconds
subclip = videoFile.subclip(start,end)

# Resize 
print(f"Resize Value Is {float(resize)} Type Of {type(float(resize))}")
subclip = subclip.resize(float(resize)) 

# Speed 
print(f"Speed Value Is {float(speed)} Type Of {type(float(speed))}")
subclip = subclip.speedx(float(speed)) 

# Write the result to a file (many options available !)
filename = "./out/output_"+datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

# subclip.write_videofile(filename+".mp4")

print(f"FPS Value Is {fps} Type Of {type(int(fps))}")
subclip.write_gif(filename+".gif",fps=int(fps))
