import os
import re

directory_path = os.path.abspath(os.curdir)

pts = 'v143'
wtpv = '10.0.22621.0'

for filename in os.listdir(directory_path):
    if filename.endswith(".vcxproj"):
        file_path = os.path.join(directory_path, filename)

        with open(file_path, 'r') as file:
            filedata = file.read()

        filedata = re.sub(r'<PlatformToolset>.*?</PlatformToolset>', f'<PlatformToolset>{pts}</PlatformToolset>', filedata, flags=re.DOTALL)
        filedata = re.sub(r'<WindowsTargetPlatformVersion>.*?</WindowsTargetPlatformVersion>', f'<WindowsTargetPlatformVersion>{wtpv}</WindowsTargetPlatformVersion>', filedata, flags=re.DOTALL)

        with open(file_path, 'w') as file:
            file.write(filedata)

print("Замена успешно выполнена.")
