from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


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

        layout_vertical_1 = BoxLayout(orientation='vertical', padding=10)
        input_elev = TextInput(text='Introduceti numele elevului', multiline=False)
        layout_vertical_1.add_widget(input_elev)

        layout_vertical_2 = BoxLayout(orientation='vertical', padding=10)
        layout_vertical_2.add_widget(input_elev)
        layout_vertical_2.add_widget(Label(text='Editare elevi 1'))
        layout_vertical_2.add_widget(Label(text=citire_elevi()))


        tab3.add_widget(layout_vertical_1)
        tab3.add_widget(layout_vertical_2)


        self.add_widget(tab1)
        self.add_widget(tab2)
        self.add_widget(tab3)


class MyApp(App):
    def build(self):
        return MyTabbedPanel()


if __name__ == '__main__':
    MyApp().run()
