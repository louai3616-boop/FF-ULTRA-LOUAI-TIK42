[app]
# (str) Title of your application
title = FF ULTRA LOUAI TIK42

# (str) Package name
package.name = ffultralouai

# (str) Package domain (needed for android packaging)
package.domain = org.louai.tik42

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# المهام المطلوبة لتشغيل الكود الخاص بك
requirements = python3,kivy,kivymd,pillow

# (str) Custom source for any requirements
# (str) Presplash of the application
# (str) Icon of the application (تأكد أن اسم الصورة في جيت هاب هو icon.png)
icon.filename = icon.png

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
# الصلاحيات اللازمة للظهور فوق الألعاب والاتصال بالانترنت
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (bool) indicates whether the screen should stay on
# Disable screen saver
android.skip_update = False

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) display warning on buildozer version
warn_on_root = 1
