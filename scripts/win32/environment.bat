rem The following lines set the paths to the tools required for build.
rem Feel free to change them to correspond the paths on your system.

set QTDIR=C:\Qt\Qt5.13.2\5.13.2\msvc2017
set MAKE=C:\Qt\Qt5.13.2\Tools\QtCreator\bin\jom.exe
set VCVARS=C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat
set VCREDIST_DLL=C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Redist\MSVC\14.16.27012\x86\Microsoft.VC141.CRT
set VCREDIST_MSM=C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Redist\MSVC\14.16.27012\MergeModules\Microsoft_VC141_CRT_x86.msm
set OPENSSL=C:\Program Files (x86)\OpenSSL\bin
set WIXDIR=C:\Program Files (x86)\WiX Toolset v3.11\bin
set SEVENZIP=C:\Program Files\7-Zip\7z.exe

rem The following line sets the application version number variable. Don't change it.

set /p VERSION=<%0\..\..\..\VERSION
