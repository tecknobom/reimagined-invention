from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock


class ChatApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dest_ip = None
        self.username = None

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        self.root = Builder.load_string(
            '''
BoxLayout:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    MDTextField:
        id: username
        hint_text: "Kullanıcı adınızı girin"
        size_hint_x: None
        width: "200dp"
        on_text_validate: app.start_chat()

    MDRectangleFlatButton:
        text: "Başlat"
        size_hint: None, None
        size: "200dp", "50dp"
        on_release: app.start_chat()
'''
        )

    def start_chat(self):
        self.username = self.root.ids.username.text.strip()
        if not self.username:
            self.show_message("Hata", "Lütfen bir kullanıcı adı girin.")
            return
        Clock.schedule_once(self.find_and_connect_peers)

    def find_and_connect_peers(self, *args):
        # Diğer kullanıcıları bulma ve bağlanma kodunu buraya ekleyin
        # Örneğin:
        # self.dest_ip = find_peer_ip()
        # if self.dest_ip:
        #     self.show_message("Bilgi", f"Bağlantı kuruldu: {self.dest_ip}")
        # else:
        #     self.show_message("Hata", "Bağlantı kurulamadı.")
        self.show_message("Bilgi", "Diğer kullanıcılar bulunuyor ve bağlantı kuruluyor...")

    def show_message(self, title, message):
        dialog = MDDialog(title=title, text=message, size_hint=(0.8, 0.4))
        dialog.open()


if __name__ == "__main__":
    ChatApp().run()
