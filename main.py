from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class MangaApp(App):
    def __init__(self):
        super().__init__()

        self.lb = Label(text="0")
        self.answer = 0
        self.pre_res = Label(text='0')
        self.pre_res.color ="red"
        self.pre_res.font_size = 50
        self.lb.font_size = 50

        
    def btn_clic(self, instance):
        if self.lb.text == "0":
            self.lb.text = instance.text
        else:
            self.lb.text += instance.text
        try:
            self.pre_res.text = str(eval(self.lb.text))     
        except SyntaxError :
            self.pre_res.text ="None"

    def btn_clic_del(self, num=0):
        if self.lb.text == "0":
            pass
        else:
            self.lb.text = self.lb.text[:-1]
            if self.lb.text == "":
                self.lb.text = "0"

    def btn_clic_cler(self, instance):
        self.lb.text = '0'
        
    def res(self, instance):
        try:
            self.lb.text = str(eval(self.lb.text))
        except SyntaxError:
            pass        
    
    def build(self):
        
        btn_1  = Button(text='1', font_size=60, on_press=self.btn_clic)
        btn_2  = Button(text='2', font_size=60, on_press=self.btn_clic)
        btn_3  = Button(text='3', font_size=60, on_press=self.btn_clic)

        lan_btn_1 = BoxLayout()
        lan_btn_1.add_widget(btn_1)
        lan_btn_1.add_widget(btn_2)
        lan_btn_1.add_widget(btn_3)
        
        btn_4  = Button(text='4', font_size=60, on_press=self.btn_clic)
        btn_5  = Button(text='5', font_size=60, on_press=self.btn_clic)
        btn_6  = Button(text='6', font_size=60, on_press=self.btn_clic)

        lan_btn_2 = BoxLayout()
        lan_btn_2.add_widget(btn_4)
        lan_btn_2.add_widget(btn_5)
        lan_btn_2.add_widget(btn_6)
        
        btn_7  = Button(text='7', font_size=60, on_press=self.btn_clic)
        btn_8  = Button(text='8', font_size=60, on_press=self.btn_clic)
        btn_9  = Button(text='9', font_size=60, on_press=self.btn_clic)

        lan_btn_3 = BoxLayout()
        lan_btn_3.add_widget(btn_7)
        lan_btn_3.add_widget(btn_8)
        lan_btn_3.add_widget(btn_9)
        
        btn_0  = Button(text='0', font_size=60, on_press=self.btn_clic)
        btn_plus  = Button(text='+', font_size=60, on_press=self.btn_clic)
        btn_minus  = Button(text='-', font_size=60, on_press=self.btn_clic)
        
        lan_btn_4 = BoxLayout()
        lan_btn_4.add_widget(btn_0)
        lan_btn_4.add_widget(btn_plus)
        lan_btn_4.add_widget(btn_minus)
        
        btn_mul  = Button(text='*', font_size=60, on_press=self.btn_clic)
        btn_divis  = Button(text='/', font_size=60, on_press=self.btn_clic)
        btn_res = Button(text="=", font_size=60, on_press=self.res)

        lan_btn_5 = BoxLayout()
        lan_btn_5.add_widget(btn_mul)
        lan_btn_5.add_widget(btn_divis)
        lan_btn_5.add_widget(btn_res)

        btn_del = Button(text='C', font_size=60, on_press=self.btn_clic_del)
        btn_cler = Button(text='X', font_size=60, on_press=self.btn_clic_cler)
        
        lan_btn_6 = BoxLayout()
        lan_btn_6.add_widget(btn_del)
        lan_btn_6.add_widget(btn_cler)
                    
        kv = BoxLayout() 
        
        kv.add_widget(lan_btn_1)        
        kv.add_widget(lan_btn_2)        
        kv.add_widget(lan_btn_3)        
        kv.add_widget(lan_btn_4)
        kv.add_widget(lan_btn_5)
        kv.add_widget(lan_btn_6)
        kv.orientation = 'vertical'
             
        bl = BoxLayout()
        bl.orientation = 'vertical'
        
        bl.add_widget(self.lb)
        bl.add_widget(self.pre_res)
        bl.add_widget(kv)

        return bl

if __name__ == "__main__":
    MangaApp().run()

