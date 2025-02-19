from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def citire_elevi():
    with open("elevi.dat", "r") as f:
        citire = f.read()
        # citire.replace("\n", " ")
    return citire


class MyTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False  # Disable default tab

        # Creăm primul tab
        tab1 = TabbedPanelItem(text='Prezență')
        tab1.add_widget(Label(text='Prezență'))

        # Creăm al doilea tab
        tab2 = TabbedPanelItem(text='Raport')
        tab2.add_widget(Label(text='Raport'))

        # Creăm al treilea tab
        tab3 = TabbedPanelItem(text='Editare elevi')
        layout_principal=BoxLayout(orientation='vertical',padding=10)
        layout_orizontal=BoxLayout(orientation='horizontal',padding=10)
        input_elev = TextInput(text='', multiline=False,size_hint=(.5,.25))
        buton_adaugare=Button(text='Adaugare',size_hint=(.5,.25))


        layout_orizontal.add_widget(input_elev)
        layout_orizontal.add_widget(buton_adaugare)

        layout_vertical=BoxLayout(orientation='vertical',padding=10)
        lista_elevi = Label(text=citire_elevi(),font_size='20')
        layout_vertical.add_widget(lista_elevi)
        layout_principal.add_widget(layout_orizontal)
        layout_principal.add_widget(layout_vertical)
        tab3.add_widget(layout_principal)









        self.add_widget(tab1)
        self.add_widget(tab2)
        self.add_widget(tab3)


class MyApp(App):
    def build(self):
        return MyTabbedPanel()


if __name__ == '__main__':
    MyApp().run()
