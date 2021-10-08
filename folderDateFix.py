import os

dirPath = os.path.join(os.path.expanduser("~"), "Downloads")

files = []
dirs = []
for r, d, f in os.walk(dirPath):
    files = f
    dirs = d
    break

zips = [file for file in files if file.endswith(".zip")]

zipDirMap = {}
for zipFile in zips:
    zipName = zipFile[:-4]
    if zipName in dirs:
        zipDir = dirs[dirs.index(zipName)]
        zipDirMap[zipFile] = zipDir

for zipFile in zipDirMap:
    zipAccessTime = os.path.getatime(os.path.join(dirPath, zipFile))
    zipModifiedTime = os.path.getmtime(os.path.join(dirPath, zipFile))
    os.utime(os.path.join(dirPath, zipDirMap[zipFile]), (zipAccessTime, zipModifiedTime))

orphanFolders = []
for folder in dirs:
    if folder not in zipDirMap.values():
        orphanFolders.append(folder)

for orphanFolder in orphanFolders:
    filesInFolder = []
    referenceFilePath = ""
    for r, d, f in os.walk(os.path.join(dirPath, orphanFolder)):
        filesInFolder = f
        referenceFilePath = r
        if len(filesInFolder) > 0:
            break
    fileAccessTime = os.path.getatime(os.path.join(referenceFilePath, filesInFolder[0]))
    fileModifiedTime = os.path.getmtime(os.path.join(referenceFilePath, filesInFolder[0]))
    os.utime(os.path.join(dirPath, orphanFolder), (fileAccessTime, fileModifiedTime))
