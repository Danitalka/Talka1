[app]
title = Talka
package.name = talka
package.domain = org.danitalka
source.dir = .
source.include_exts = py,kv,png,ttf,mp3
version = 1.0
requirements = python3,kivy,speechrecognition,pygame,translate
orientation = portrait
fullscreen = 1
icon.filename = logo.png

[buildozer]
log_level = 2
warn_on_root = 1

[python]
android_private_storage = 1

[android]
android.api = 31
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET,RECORD_AUDIO
android.ndk = 23b
android.gradle_dependencies = 
android.gradle_plugins = 
android.add_src = 
android.add_jars = 
android.add_aars = 
android.copy_libs = 1

[android.packaging_options]
# leave empty

[android.sign]
# leave empty unless signing manually

[android.xpermissions]
# leave empty

[ios]
# Not relevant

[buildozer.android]
# enable Android builds
