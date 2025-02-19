from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creăm primul tab
        tab1 = TabbedPanelItem(text='Tab 1')
        tab1.add_widget(Label(text='Acesta este primul tab'))

        # Creăm al doilea tab
        tab2 = TabbedPanelItem(text='Tab 2')
        tab2.add_widget(Label(text='Acesta este al doilea tab'))

        # Creăm al treilea tab
        tab3 = TabbedPanelItem(text='Tab 3')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Acesta este al treilea tab'))
        layout.add_widget(Label(text='Un alt label în tabul al treilea'))
        tab3.add_widget(layout)

        # Adăugăm tab-urile în interfață
        self.add_widget(tab1)
        self.add_widget(tab2)
        self.add_widget(tab3)


class MyApp(App):
    def build(self):
        return MyTabbedPanel()


if __name__ == '__main__':
    MyApp().run()
