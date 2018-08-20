TEMPLATE = app

QT += core gui widgets xml network
CONFIG += c++11

TARGET = apk-editor-studio
VERSION = 0.1.0

QMAKE_TARGET_PRODUCT = APK Editor Studio
QMAKE_TARGET_COMPANY = Alexander Gorishnyak
QMAKE_TARGET_DESCRIPTION = APK Editor Studio v$$VERSION
QMAKE_TARGET_COPYRIGHT = Copyright (C) 2018

DEFINES += APPLICATION='"\\\"$$QMAKE_TARGET_PRODUCT\\\""'
DEFINES += VERSION=\\\"$$VERSION\\\"
#DEFINES += PORTABLE

include($$PWD/src/apk-editor-studio.pri)
include($$PWD/lib/qtkeychain/qt5keychain.pri)
include($$PWD/deploy.pri)
