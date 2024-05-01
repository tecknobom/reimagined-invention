[app]
title = ChatApp
icon.filename = icon.png
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
osx.python_version = 3.8.10
android.python_version = 3.8.10
requirements = kivy==2.0.0, kivymd==0.104.2
source.main_entry = main.py
android.permissions = INTERNET

# APK paket adını belirtin
package.name = com.example.chatapp

# APK sürüm numarasını belirtin
version = 1.0
