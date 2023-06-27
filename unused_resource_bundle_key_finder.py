import os
import re
import json

# start dir 
rootDir = r'C:\my-codebase'

# resource bundle path
# has to be outside the rootdir/codebase, which probably isn't the case, so you should temporarily move it elsewhere for this script to work
bundle_path = r'C:\other-location\resource-bundle.ts'

# extract keys from resource bundle
# change encoding if necessary
with open(bundle_path, 'r', encoding='utf-8') as f:
    content = f.read()
    keys = re.findall(r"['\"](.*?)['\"]:", content)  # find all keys between single or double quotes followed by a colon

unused_keys = keys.copy()  # start by assuming all keys are unused

# iterate over entire codebase/whatever you defined as rootDir
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.endswith('.ts') or fname.endswith('.html'):  # only search through .ts and .html files
            with open(os.path.join(dirName, fname), 'r', encoding='utf-8') as f: # change encoding if necessary
                file_contents = f.read()
                for key in keys:
                    # check if key is used in file
                    if key in file_contents:
                        if key in unused_keys:
                            unused_keys.remove(key)

# print unused keys
print('Unused keys:')
for key in unused_keys:
    print(key)
