from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.graphics import Color, Line
from kivy.clock import Clock
from kivy.core.window import Window
import random

# إعدادات شاشة الويندوز والأندرويد
Window.clearcolor = (0.05, 0.05, 0.1, 1)

class FfUltraLouai(App):
    def build(self):
        self.title = "FF ULTRA PRO - LOUAI TIK42"
        self.lang = "AR"
        self.is_crosshair_on = False
        
        # الحاوية الرئيسية
        self.main_view = FloatLayout()

        # --- القائمة الجانبية للأدوات (Side Panel) ---
        self.panel = BoxLayout(orientation='vertical', padding=15, spacing=10,
                               size_hint=(0.45, 0.95), pos_hint={'x': 0, 'top': 0.98})
        
        # شعار المطور (Developer Branding)
        self.dev_label = Label(text="[b]LOUAI TIK42[/b]\n[size=12]TikTok: louaitik42[/size]",
                               markup=True, size_hint_y=None, height=80, color=(0, 1, 1, 1))
        self.panel.add_widget(self.dev_label)

        # مراقب الرام (RAM Monitoring)
        self.ram_info = Label(text="RAM: 0GB Free", font_size='14sp')
        self.panel.add_widget(self.ram_info)
        self.ram_bar = ProgressBar(max=100, value=70, size_hint_y=None, height=15)
        self.panel.add_widget(self.ram_bar)

        # أزرار الأدوات
        self.btn_boost = Button(text="BOOST PHONE", background_color=(0, 0.8, 0, 1))
        self.btn_boost.bind(on_press=self.boost_animation)
        self.panel.add_widget(self.btn_boost)

        self.btn_cross = Button(text="SHOW CROSSHAIR", background_color=(1, 0, 0, 1))
        self.btn_cross.bind(on_press=self.toggle_crosshair)
        self.panel.add_widget(self.btn_cross)

        self.btn_sensi = Button(text="AUTO SENSI", background_color=(0, 0.5, 1, 1))
        self.btn_sensi.bind(on_press=self.get_sensi)
        self.panel.add_widget(self.btn_sensi)

        # تبديل اللغات (Language Switch)
        lang_box = BoxLayout(spacing=5, size_hint_y=None, height=40)
        for l in ["AR", "EN", "FR"]:
            b = Button(text=l, font_size='10sp')
            b.bind(on_press=lambda x, lang=l: self.set_lang(lang))
            lang_box.add_widget(b)
        self.panel.add_widget(lang_box)

        self.main_view.add_widget(self.panel)

        # منطقة عرض الحالة (Status Display)
        self.status = Label(text="System Ready", pos_hint={'center_x': 0.7, 'y': 0.1}, color=(1,1,1,0.5))
        self.main_view.add_widget(self.status)

        # تحديث الرام تلقائياً
        Clock.schedule_interval(self.update_ram_visual, 3)
        return self.main_view

    def toggle_crosshair(self, instance):
        if not self.is_crosshair_on:
            with self.main_view.canvas.after:
                Color(1, 0, 0, 1) # أحمر
                # رسم الدائرة في منتصف الشاشة تماماً
                self.circle = Line(circle=(Window.width/2, Window.height/2, 6), width=2)
                self.h_line = Line(points=[Window.width/2-15, Window.height/2, Window.width/2+15, Window.height/2], width=1)
                self.v_line = Line(points=[Window.width/2, Window.height/2-15, Window.width/2, Window.height/2+15], width=1)
            self.is_crosshair_on = True
            instance.text = "HIDE CROSS"
        else:
            self.main_view.canvas.after.clear()
            self.is_crosshair_on = False
            instance.text = "SHOW CROSS"

    def update_ram_visual(self, dt):
        usage = random.randint(45, 88)
        self.ram_bar.value = usage
        self.ram_info.text = f"RAM Usage: {usage}%"

    def boost_animation(self, instance):
        self.status.text = "Optimizing... Lag Fixed!"
        self.ram_bar.value = 25
        def reset(dt): self.status.text = "System Ready"
        Clock.schedule_once(reset, 2)

    def get_sensi(self, instance):
        s = random.randint(95, 100)
        self.status.text = f"Sensi: Gen {s}, RedDot {s-4}"

    def set_lang(self, lang):
        self.lang = lang
        translations = {
            "AR": ("تم التطوير: LOUAI TIK42", "تسريع الهاتف", "إظهار الدائرة", "حساسية تلقائية"),
            "EN": ("Developed by: LOUAI TIK42", "BOOST PHONE", "SHOW CROSSHAIR", "AUTO SENSI"),
            "FR": ("Par: LOUAI TIK42", "BOOSTER TEL", "AFFICHER CERCLE", "SENSI AUTO")
        }
        self.dev_label.text = f"[b]{translations[lang][0]}[/b]\n[size=12]TikTok: louaitik42[/size]"
        self.btn_boost.text = translations[lang][1]
        self.btn_cross.text = translations[lang][2]
        self.btn_sensi.text = translations[lang][3]

if __name__ == '__main__':
    FfUltraLouai().run()
