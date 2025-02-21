from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.button = Button(text="Apasă-mă", size_hint=(1, None), height=50)
        self.button.bind(on_press=lambda instance: self.show_message(instance, "Mesaj personalizat"))
        self.button.bind(on_release=lambda instance: print("Butonul a fost eliberat!"))
        layout.add_widget(self.button)
        return layout

    def show_message(self, instance, message):
        print(f"Butonul a fost apăsat! {message}")

if __name__ == "__main__":
    MyApp().run()
