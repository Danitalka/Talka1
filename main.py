from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard

class RootWidget(BoxLayout):
    def on_lang_select(self, text):
        pass

    def start_process(self):
        self.ids.output_label.text = "🎙️ Sto ascoltando..."
        self.ids.output_label.text = f"🎧 Traduzione: Hello, how are you?"

    def copia_traduzione(self):
        testo = self.ids.output_label.text
        if "Tradotto:" in testo or "Traduzione:" in testo:
            tradotto = testo.split(":", 1)[-1].strip()
            Clipboard.copy(tradotto)
        else:
            Clipboard.copy(testo)

    def mostra_copiato(self):
        pass

class TalkaApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    TalkaApp().run()