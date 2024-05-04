import json
import os 
sl= os.listdir(r'C:\Users\DELL\Desktop\lab\Dhruv\msc_palyer\music')
# a=json.dumps(sl, indent=4,separators=('',''))
b=json.dumps(sl)
print(b)