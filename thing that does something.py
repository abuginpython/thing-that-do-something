# fucking headache
# test path: F:\nahidwin\The Legend of Korra (2012 - 2014) [1080p]\Book One - Air

import os

path = input('path: ')
targetExtension = input('Target Extension: ')
convertTo = input('Convert to: ')

files = os.listdir(path)

for things in files:
    if things.endswith(targetExtension): 
        print("-----------------Nah, i'd win--------------------")
        r = things.replace(targetExtension,convertTo)
        os.system(f'ffmpeg -i "{path}\{things}" "{path}\{r}"')
