from kivymd.app import MDApp
from kivy.lang import Builder
import webbrowser

KV = """

Screen:
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout: 
        orientation: 'vertical'
        BoxLayout: 
            orientation: 'horizontal'
            MDTextField:
                hint_text: "Search here..."
                text_color: (1, 1, 1, 1)
                theme_text_color: "Custom"
                background_color: "#ffffff88"
                mode: "fill"
                id: 'searchfield'
                user_font_size: '12dp'
            MDIconButton:
                icon: "magnify"
                text_color: (1, 1, 1, 1)
                theme_text_color: "Custom"
                md_bg_color: "#ffffff88"
                md_bg_normal: ""
                user_font_size: '48dp'
                size_hint: None, None
                on_press:
                    app.search()
        Label:
            text: ' '
            text_size: self.size
            halign: 'center'
            valign: 'top'
     """
class Main(MDApp):
    def search(self):
        text = self.root.children[0].children[1].children[1].text
        query = text.replace(" ", "+")
        webbrowser.open(f'https://www.google.com/search?q={query}')
        
    def build(self):
        return Builder.load_string(KV)


Main().run()