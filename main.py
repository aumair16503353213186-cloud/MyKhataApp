from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class KhataApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="Umair Khata Project", font_size=25)
        self.layout.add_widget(self.label)
        
        self.pass_input = TextInput(hint_text="Password Dalein (Umar 786)", password=True, multiline=False)
        self.layout.add_widget(self.pass_input)
        
        self.btn = Button(text="Login", background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.verify_password)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def verify_password(self, instance):
        if self.pass_input.text == "Umar 786":
            self.label.text = "Khushamdeed Umair! Vault Khul Gaya."
        else:
            self.label.text = "Galt Password! Dobara Koshish Karein."

if __name__ == "__main__":
    KhataApp().run()
