from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.label import Label


class MyTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False  # Disable default tab

        # Create first tab
        tab1 = TabbedPanelHeader(text='Prezență')
        tab1.content = Label(text='Content for Tab 1')
        self.add_widget(tab1)

        # Create second tab
        tab2 = TabbedPanelHeader(text='Tab 2')
        tab2.content = Label(text='Content for Tab 2')
        self.add_widget(tab2)

        # Create third tab
        tab3 = TabbedPanelHeader(text='Editare elevi')
        tab3.content = Label(text='Content for Tab 3')
        self.add_widget(tab3)


class MyApp(App):
    def build(self):
        return MyTabbedPanel()


if __name__ == '__main__':
    MyApp().run()
