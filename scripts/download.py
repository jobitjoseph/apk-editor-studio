#!/usr/bin/env python3

import os
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile

def unzip(z, src, dst):
    dst = os.path.join(dst, os.path.basename(src))
    with open(dst, 'wb') as f:
        f.write(z.read(src))

def resolveExecutableName(path):
    return path if sys.platform != 'win32' else path + '.exe'

def resolvePath(path):
    return os.path.join(os.path.dirname(__file__), path)

def resolvePlatformPath():
    path = resolvePath('../res/deploy')
    if sys.platform == 'win32':
        return os.path.join(path, 'windows/tools')
    elif sys.platform == 'linux':
        return os.path.join(path, 'linux/bin')
    elif sys.platform == 'darwin':
        return os.path.join(path, 'macos/bundle/contents/MacOS')

def progress(blocknum, blocksize, totalsize):
    bytesdone = min(blocknum * blocksize, totalsize)
    percent = bytesdone * 1e2 / totalsize
    s = '\r%5.1f%% %*d / %d KB' % (percent, len(str(totalsize)), bytesdone / 1024, totalsize / 1024)
    sys.stderr.write(s)
    if bytesdone >= totalsize:
        sys.stderr.write('\n')

# Prepare

os.makedirs(resolvePath('../res/deploy/all/tools'), exist_ok=True)
os.makedirs(resolvePlatformPath(), exist_ok=True)

# Download Apktool

print('(1/3) Downloading Apktool...')
urlretrieve('https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.5.0.jar',
    resolvePath('../res/deploy/all/tools/apktool.jar'), progress)

# Download and unpack Android Build Tools

print('(2/3) Downloading Android Build Tools...')
buildToolsUrl = 'https://dl.google.com/android/repository/build-tools_r29.0.3-{}.zip'
if sys.platform == 'win32':
    buildToolsUrl = buildToolsUrl.format('windows')
elif sys.platform == 'linux':
    buildToolsUrl = buildToolsUrl.format('linux')
elif sys.platform == 'darwin':
    buildToolsUrl = buildToolsUrl.format('macosx')
urlretrieve(buildToolsUrl, 'build-tools.zip', progress)

with ZipFile('build-tools.zip') as z:
    unzip(z, 'android-10/lib/apksigner.jar', resolvePath('../res/deploy/all/tools/'))
    unzip(z, resolveExecutableName('android-10/zipalign'), resolvePlatformPath())
    if sys.platform == 'win32':
        unzip(z, 'android-10/libwinpthread-1.dll', resolvePlatformPath())
os.remove('build-tools.zip')

# Download and unpack Android SDK Platform Tools

print('(3/3) Downloading Android SDK Platform Tools...')
platformToolsUrl = 'https://dl.google.com/android/repository/platform-tools-latest-{}.zip'
if sys.platform == 'win32':
    platformToolsUrl = platformToolsUrl.format('windows')
elif sys.platform == 'linux':
    platformToolsUrl = platformToolsUrl.format('linux')
elif sys.platform == 'darwin':
    platformToolsUrl = platformToolsUrl.format('darwin')
urlretrieve(platformToolsUrl, 'platform-tools.zip', progress)

with ZipFile('platform-tools.zip') as z:
    unzip(z, resolveExecutableName('platform-tools/adb'), resolvePlatformPath())
    if sys.platform == 'win32':
        unzip(z, 'platform-tools/AdbWinApi.dll', resolvePlatformPath())
        unzip(z, 'platform-tools/AdbWinUsbApi.dll', resolvePlatformPath())
os.remove('platform-tools.zip')
