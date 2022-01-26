import os
import subprocess
import sys

sourcedir = "/home/sadi/Documents/MyTask-main"
for file in os.listdir(sourcedir):
    
    name = file[:file.rfind(".")]
    
    if not name.startswith("converted_"):
        subprocess.call(["ffmpeg", "-i", name+".wav", "-acodec", "pcm_s16le", "-ac",
                     "1", "-ar", "16000", "converted_" + name+ ".wav"])

for file2 in os.listdir(sourcedir):
    
    name2 = file2[:file2.rfind(".")]
   
    if name2.startswith("filtered_") :
        print(name2)
        subprocess.call(["python", "vad_nosi.py", "1", name2 +".wav"])
        