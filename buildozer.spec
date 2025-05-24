
[app]
title = Talka
package.name = talka
package.domain = org.danitalk
source.dir = .
source.include_exts = py,png,kv,atlas
version = 0.1
requirements = python3,kivy,pygame,requests,speechrecognition,googletrans==4.0.0rc1,gtts,pydub
orientation = portrait
icon.filename = icon.png
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.sdk_path = /root/.buildozer/android/platform/android-sdk
android.build_tools_version = 34.0.0
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET, RECORD_AUDIO
android.allow_backup = 1

[android.packaging]
presplash.filename = icon.png

[android.extra_packages]
android.use_android_native_audio = 1

[buildozer.plugins]
enabled = android

[hostpython]
version = 3.10
