from kivymd.app import MDApp
from kivy.lang import Builder
import webbrowser

class Main(MDApp):
    def search(self):
        text = self.root.children[0].children[1].children[1].text
        query = text.replace(" ", "+")
        webbrowser.open(f'https://www.google.com/search?q={query}')

    def build(self):
        return Builder.load_file('window.kv')


Main().run()