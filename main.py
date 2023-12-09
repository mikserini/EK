from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


code = {'a': '1', 'A': '2', 'ą': '3', 'Ą': '4', 'b': '5', 'B': '6', 'c': '7', 'C': '8', 'ć': '9', 'Ć': '10',
        'd': '11', 'D': '12', 'e': '13', 'E': '14', 'ę': '15', 'Ę': '16', 'f': '17', 'F': '18', 'g': '19', 'G': '20',
        'h': '21', 'H': '22', 'i': '23', 'I': '24', 'j': '25', 'J': '26', 'k': '27', 'K': '28', 'l': '29', 'L': '30',
        'ł': '31', 'Ł': '32', 'm': '33', 'M': '34', 'n': '35', 'N': '36', 'ń': '37', 'Ń': '38', 'o': '39', 'O': '40',
        'ó': '41', 'Ó': '42', 'p': '43', 'P': '44', 'q': '45', 'Q': '46', 'r': '47', 'R': '48', 's': '49', 'S': '50',
        'ś': '51', 'Ś': '52', 't': '53', 'T': '54', 'u': '55', 'U': '56', 'v': '57', 'V': '58', 'w': '59', 'W': '60',
        'x': '61', 'X': '62', 'y': '63', 'Y': '64', 'z': '65', 'Z': '66', 'ź': '67', 'Ź': '68', 'ż': '69', 'Ż': '70',
        ' ': '71', '1': 'a', '2': 'A', '3': 'ą', '4': 'Ą', '5': 'b', '6': 'B', '7': 'c', '8': 'C', '9': 'ć',
        '10': 'Ć', '11': 'd', '12': 'D', '13': 'e', '14': 'E', '15': 'ę', '16': 'Ę', '17': 'f', '18': 'F', '19': 'g',
        '20': 'G', '21': 'h', '22': 'H', '23': 'i', '24': 'I', '25': 'j', '26': 'J', '27': 'k', '28': 'K', '29': 'l',
        '30': 'L', '31': 'ł', '32': 'Ł', '33': 'm', '34': 'M', '35': 'n', '36': 'N', '37': 'ń', '38': 'Ń', '39': 'o',
        '40': 'O', '41': 'ó', '42': 'Ó', '43': 'p', '44': 'P', '45': 'q', '46': 'Q', '47': 'r', '48': 'R', '49': 's',
        '50': 'S', '51': 'ś', '52': 'Ś', '53': 't', '54': 'T', '55': 'u', '56': 'U', '57': 'v', '58': 'V', '59': 'w',
        '60': 'W', '61': 'x', '62': 'X', '63': 'y', '64': 'Y', '65': 'z', '66': 'Z', '67': 'ź', '68': 'Ź', '69': 'ż',
        '70': 'Ż', '71': ' ', '!': '!', '"': '"', '#': '#', '$': '$', '%': '%', '&': '&', "'": "'", '(': '(',
        ')': ')', '*': '*', '+': '+', ',': ',', '-': '-', '.': '.', '/': '/', ':': ':', ';': ';', '<': '<', '=': '=',
        '>': '>', '?': '?', '@': '@', '[': '[', '\\': '\\', ']': ']', '^': '^', '_': '_', '`': '`', '{': '{', '|': '|', '}': '}', '~': '~'}

class TextExploder(App):
    def __init__(self, **kwargs):
        super(TextExploder, self).__init__(**kwargs)
        self.entered_text = ""
        self.info_label = Label(text="")

    def build(self):
        layout = BoxLayout(orientation="vertical")

        powitanie = Label(
            text="Witaj w eksploderze tekstu na części pierwsze",
            font_size=24,
            size_hint_y=None,
            height=400,
            halign='center')
        powitanie.bind(size=lambda instance, value: setattr(powitanie, 'text_size', (value[0], None)))

        btn_wprowadz_tekst = Button(
            text="Wprowadź tekst lub ciąg znaków",
            font_size=16,
            on_press=self.btn_wprowadz_tekst)

        layout.add_widget(powitanie)
        layout.add_widget(btn_wprowadz_tekst)

        return layout

    def btn_wprowadz_tekst(self, instance):
        popup = Popup(title="Wprowadź tekst lub ciąg znaków", size_hint=(None, None), size=(600, 600))

        layout = BoxLayout(orientation="vertical")
        text_input = TextInput()
        text_input.bind(text=self.check_enter)

        layout.add_widget(text_input)

        btn_close = Button(text="OK", size_hint_y=None, height=100)
        btn_close.bind(on_press=lambda btn: self.on_text_input_entered(popup, text_input))
        layout.add_widget(btn_close)

        popup.content = layout
        popup.open()

    def on_text_input_entered(self, popup, text_input):
        self.entered_text = text_input.text
        self.informacje_tekstowe(None)
        popup.dismiss()
        self.root.clear_widgets()
        self.root.add_widget(self.menu())

    def on_text_input_entered(self, popup, text_input):
        self.entered_text = text_input.text
        self.informacje_tekstowe(None)
        popup.dismiss()
        self.root.clear_widgets()
        self.root.add_widget(self.menu())

    def show_text_info(self, instance):
        self.informacje_tekstowe(instance)
        
        def load_new_text(instance):
            self.entered_text = ""
            self.btn_wprowadz_tekst(instance)
            popup.dismiss()
        
        confirmation_label = Label(text="Chcesz załadować kolejny tekst?")
        btn_yes = Button(text="Tak", size_hint_y=None, height=100, on_press=load_new_text)
        btn_no = Button(text="Nie", size_hint_y=None, height=100, on_release=App.get_running_app().stop)
        
        new_info_text = self.info_label.text
        
        info_text_input = TextInput(text=new_info_text, readonly=True, size_hint_y=None, height=400)
        
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None, height=500)
        layout.add_widget(info_text_input)
        
        btns_layout = GridLayout(cols=2, size_hint_y=None, height=100)
        btns_layout.add_widget(btn_yes)
        btns_layout.add_widget(btn_no)
        
        layout.add_widget(confirmation_label)
        layout.add_widget(btns_layout)
        
        popup_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(575, 475), padding=25, spacing=10)
        popup_layout.add_widget(layout)
        
        popup = Popup(title="Informacje o tekście", content=popup_layout, size_hint=(None, None), size=(600, 600))
        popup.open()

    def enter_text_again(self, instance):
        popup = Popup(title="Wprowadź tekst ponownie", size_hint=(None, None), size=(600, 600))

        layout = BoxLayout(orientation="vertical")
        text_input = TextInput()
        text_input.bind(text=self.check_enter)

        layout.add_widget(text_input)

        btn_close = Button(text="OK", size_hint_y=None, height=100)
        btn_close.bind(on_press=lambda btn: self.on_text_input_entered(popup, text_input))
        layout.add_widget(btn_close)

        popup.content = layout
        popup.open()

    def on_text_input_entered(self, popup, text_input):
        self.entered_text = text_input.text
        popup.dismiss()
        self.root.clear_widgets()
        self.root.add_widget(self.menu())
 
    def informacje_tekstowe(self, instance):
        def count_sentences(text_input):
            sentences_end = [".", "!", "?"]
            count = 0
            for char in self.entered_text:
                if char in sentences_end:
                    count += 1
            return count

        words = self.entered_text.split()
        D_letters = sum(1 for char in self.entered_text if char.isupper())
        m_letters = sum(1 for char in self.entered_text if char.islower())
        space = self.entered_text.count(" ")
        pol_char = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
        pol_positions = [i for i, char in enumerate(self.entered_text) if char in pol_char]
        count_pol_char = len(pol_positions)
        vis_characters = sum(1 for char in self.entered_text if char.isalnum() or char.isspace())
        hid_characters = len(self.entered_text) - vis_characters
        hid_positions = [i for i, char in enumerate(self.entered_text) if not char.isalnum() and not char.isspace()]
        letters_A = [i for i, char in enumerate(self.entered_text) if char.lower() == "a"]
        count_let = self.entered_text.count("a") + self.entered_text.count("b")
        some_letters = [i for i, char in enumerate(self.entered_text) if char.lower() in ['a', 'b']]

        info_text = f"Dane dotyczące tekstu:\nZnaki: {len(self.entered_text)}\nLitery: {len([letter for letter in self.entered_text if letter.isalpha()])}\nLiczby: {len([num for num in self.entered_text if num.isdigit()])}\nSymbole: {self.count_symbols(self.entered_text)}\nWyrazy: {len(words)}\nZdania: {count_sentences(self.entered_text)}\nDuże znaki: {D_letters}\nMałe znaki: {m_letters}\nSpacje (przerwy między wyrazami): {space}\nPolskie znaki: {count_pol_char} i znajdują się na pozycjach: {pol_positions}\nUkryte znaki: {hid_characters} i znajdują się na tych pozycjach: {hid_positions}\nPozycje, na których znajduje się litera 'A': {letters_A}\nIlość liter 'A' i 'B' w tekście wynosi: {count_let} i znajdują się na pozycjach: {some_letters}"

        self.info_label.text = info_text

    def count_symbols(self, text):
        symbol_count = sum(not char.isalnum() and not char.isspace() for char in text)
        return symbol_count

    def check_enter(self, instance, value):
        if "\n" in value:
            if isinstance(instance.parent, Popup):
                instance.parent.dismiss()
                self.menu()

    def menu(self):
        layout = BoxLayout(orientation="vertical")

        btn_show_info = Button(text="Pokaż informacje o tekście")
        btn_show_info.bind(on_press=self.show_text_info)

        btn_enter_text = Button(text="Wprowadź tekst ponownie")
        btn_enter_text.bind(on_press=self.enter_text_again)

        btn_encrypt = Button(text="Zaszyfruj tekst")
        btn_encrypt.bind(on_press=self.encrypt_text)

        btn_decrypt = Button(text="Odszyfruj tekst")
        btn_decrypt.bind(on_press=self.decrypt_text)

        btn_close = Button(text="Zamknij program")
        btn_close.bind(on_press=self.close_program)

        layout.add_widget(btn_show_info)
        layout.add_widget(btn_enter_text)
        layout.add_widget(btn_encrypt)
        layout.add_widget(btn_decrypt)
        layout.add_widget(btn_close)
        return layout

    def encrypt_text(self, instance):
        encrypted_text = self.text_to_numbers(self.entered_text)
        
        popup = Popup(title="Zaszyfrowany tekst", size_hint=(None, None), size=(600, 600))
        layout = BoxLayout(orientation="vertical")
        
        encrypted_text_input = TextInput(text=f'{encrypted_text}', font_size=16, readonly=True)
        layout.add_widget(encrypted_text_input)
        
        btn_ok = Button(text="OK", size_hint_y=None, height=100)
        btn_ok.bind(on_press=popup.dismiss)
        layout.add_widget(btn_ok)
        
        popup.content = layout
        popup.open()

    def decrypt_text(self, instance):
        decrypted_text = self.numb_to_text(self.entered_text)
        self.show_decrypted_text(decrypted_text)

    def show_decrypted_text(self, decrypted_text):
        popup = Popup(title="Odszyfrowany tekst", size_hint=(None, None), size=(600, 600))

        layout = BoxLayout(orientation="vertical")
        text_output = TextInput(text=decrypted_text, readonly=True)
        layout.add_widget(text_output)

        btn_ok = Button(text="OK", size_hint_y=None, height=100)
        btn_ok.bind(on_press=self.show_menu)
        layout.add_widget(btn_ok)

        popup.content = layout
        popup.open()

    def numb_to_text(self, name):
        decrypted_text = [code.get(num, num) for num in name.split()]
        return ''.join(decrypted_text)

    def close_program(self, instance):
        App.get_running_app().stop()

    def text_to_numbers(self, name):
        encrypted_text = [code[letter] if letter in code else letter for letter in name]
        return ' '.join(encrypted_text)

    def show_menu(self, instance):
        parent = instance.parent
        while not isinstance(parent, Popup):
            parent = parent.parent
            if not parent:
                return

        parent.dismiss()
        self.root.clear_widgets()
        self.root.add_widget(self.menu())

if __name__ == "__main__":
    TextExploder().run()
