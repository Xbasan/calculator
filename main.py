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

        
    def btn_clic_1(self, instance):
        if self.lb.text == "0":
            self.lb.text = '1'
        else:
            self.lb.text += '1'    
    
    def btn_clic_2(self, instance):
        if self.lb.text == "0":
            self.lb.text = '2'
        else:
            self.lb.text += '2'
            
    def btn_clic_3(self, instance):
        if self.lb.text == "0":
            self.lb.text = '3'
        else:
            self.lb.text += '3'

            
    def btn_clic_4(self, instance):
        if self.lb.text == "0":
            self.lb.text = '4'
        else:
            self.lb.text += '4'
            
    def btn_clic_5(self, instance):
        if self.lb.text == "0":
            self.lb.text = '5'
        else:
            self.lb.text += '5'


    def btn_clic_6(self, instance):
        if self.lb.text == "0":
            self.lb.text = '6'
        else:
            self.lb.text += '6'

    def btn_clic_7(self, instance):
        if self.lb.text == "0":
            self.lb.text = '7'
        else:
            self.lb.text += '7'

    def btn_clic_8(self, instance):
        if self.lb.text == "0":
            self.lb.text = '8'
        else:
            self.lb.text += '8'
            
    def btn_clic_9(self, instance):
        if self.lb.text == "0":
            self.lb.text = '9'
        else:
            self.lb.text += '9'
    

    def btn_clic_0(self, instance):
        if self.lb.text == "0":
            pass
        else:
            self.lb.text += '0'

    def btn_clic_mul(self, instance):
        if self.lb.text == "0":
            pass
        else:
            self.lb.text += '*'

    def btn_clic_divis(self, instance):
        if self.lb.text == "0":
            pass
        else:
            self.lb.text += '/'
            
    def btn_clic_minus(self, instance):
        if self.lb.text == "0":
            pass
        else:
            self.lb.text += '-'
            
    def btn_clic_plus(self, instance):
        if self.lb.text == "0":
            pass
        else:
            self.lb.text += '+'

    def btn_clic_del(self, num=0):
        if self.lb.text == "0":
            pass
        else:
            self.lb.text = self.lb.text[:-1]

    def btn_clic_cler(self, instance):
        self.lb.text = '0'

        
    def res(self, instance):
        try:
            self.lb.text = str(eval(self.lb.text))
        except SyntaxError:
            pass        
    
    def build(self):
        
        btn_1  = Button(text='1', on_press=self.btn_clic_1)
        btn_2  = Button(text='2', on_press=self.btn_clic_2)
        btn_3  = Button(text='3', on_press=self.btn_clic_3)

        lan_btn_1 = BoxLayout()
        lan_btn_1.add_widget(btn_1)
        lan_btn_1.add_widget(btn_2)
        lan_btn_1.add_widget(btn_3)
        
        btn_4  = Button(text='4', on_press=self.btn_clic_4)
        btn_5  = Button(text='5', on_press=self.btn_clic_5)
        btn_6  = Button(text='6', on_press=self.btn_clic_6)

        lan_btn_2 = BoxLayout()
        lan_btn_2.add_widget(btn_4)
        lan_btn_2.add_widget(btn_5)
        lan_btn_2.add_widget(btn_6)
        
        btn_7  = Button(text='7', on_press=self.btn_clic_7)
        btn_8  = Button(text='8', on_press=self.btn_clic_8)
        btn_9  = Button(text='9', on_press=self.btn_clic_9)

        lan_btn_3 = BoxLayout()
        lan_btn_3.add_widget(btn_7)
        lan_btn_3.add_widget(btn_8)
        lan_btn_3.add_widget(btn_9)
        
        btn_0  = Button(text='0', on_press=self.btn_clic_0)
        btn_plus  = Button(text='+', on_press=self.btn_clic_plus)
        btn_minus  = Button(text='-', on_press=self.btn_clic_minus)

        lan_btn_4 = BoxLayout()
        lan_btn_4.add_widget(btn_0)
        lan_btn_4.add_widget(btn_plus)
        lan_btn_4.add_widget(btn_minus)
        
        btn_mul  = Button(text='*', on_press=self.btn_clic_mul)
        btn_divis  = Button(text='/', on_press=self.btn_clic_divis)
        btn_res = Button(text="=", on_press=self.res)

        lan_btn_5 = BoxLayout()
        lan_btn_5.add_widget(btn_mul)
        lan_btn_5.add_widget(btn_divis)
        lan_btn_5.add_widget(btn_res)

        btn_del = Button(text='C', on_press=self.btn_clic_del)
        btn_cler = Button(text='X', on_press=self.btn_clic_cler)
        
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
        bl.add_widget(kv)

        return bl

if __name__ == "__main__":
    MangaApp().run()

