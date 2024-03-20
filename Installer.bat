@echo off
echo WorkFlowToolkit Installing...
if not exist WorkFlowToolkit mkdir WorkFlowToolkit\Installer
cd WorkFlowToolkit\Installer
echo Downloading Python...
if not exist py.exe curl https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe -o py.exe -s
echo Installing Python...
if not exist %USERPROFILE%\AppData\Local\Programs\Python\Python311 py.exe /s
echo Downloading Git...
if not exist git.exe curl https://dl.freesoftru.net/apps/22/215/21407/Git-2.36.1-64-bit.exe -o git.exe -s
echo Installing Git...
if not exist C:\Program Files\Git git.exe /VERYSILENT
cd ..
if not exist workflow-toolkit git clone https://github.com/vo1dspir1t/workflow-toolkit.git
cd workflow-toolkit
echo WorkFlowToolkit was installed!
pause
py main.py