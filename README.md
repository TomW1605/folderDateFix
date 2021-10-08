# folderDateFix
Basically, I tried moving my downloads folder to a secondary drive to save space and that messed up the dates on all the folders in there and reset them to the date I did the move.

Most of the folders were extracted from ZIP files. So, this script goes through the downloads folder and makes a list of all the ZIP files and all the folders. Then it matches the ZIPs and folders based on name. Then it uses the ZIP file as a reference to set the last access and last modified date on the folder. If there are any folders that do not match a ZIP file, then it uses a file inside the folder as a reference.

# WARNING
This scrip will not change the “Date Created” tag on the file. This means that it may be that some folders will have last modified dates that are earlier than the created date. I don’t think that will cause issues, but it might. USE AT YOUR OWN RISK.

Also, I only tested on windows.
