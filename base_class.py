import tkinter as tk

class Bit(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.run = False
        
    def create_widgets(self):
        self.run = False
        for widget in self.winfo_children():
            widget.grid_forget()
        self.label_bit = tk.Label(self, text = 'Enter bit').grid(row = 0)
        self.label_base = tk.Label(self, text = 'Enter base').grid(row = 1)
        self.entry_bit = tk.Entry(self)
        self.entry_bit.grid(row = 0, column = 1)
        self.entry_base = tk.Entry(self)
        self.entry_base.grid(row = 1, column = 1)
        self.decimal_repr = tk.Button(self, text = 'find decimal representation', command = self.find_decimal_representation).grid(row = 3, column = 1)
        self.cb = tk.Button(self, text = 'Change base', command = self.set_up_cb).grid(row = 3, column = 0)
        
    def error(self):
        for widget in self.winfo_children():
            widget.grid_forget()
        self.error_message = tk.Label(self,text = 'Error occur, please change input').grid(row = 0)
        self.reset = tk.Button(self, text = 'reset', command = self.create_widgets).grid(row = 1, column = 0)
    
    def create_bit(self):
        self.setup_num(self.entry_bit.get(),self.entry_base.get())

    
    def setup_num(self,bit,base):
        
        try:
            assert all([i.isdigit() for i in base])
            for i in bit:
                assert (i.isdigit() and int(base) > int(i)) or ((ord(i) >= 65 and ord(i) <=90) and ord(i)- 55 < int(base))
            self.bit = bit
            self.base = base
            self.answer = None
            self.run = True
        except AssertionError:
            pass

    def set_up_cb(self): #cb refers to change base
        self.create_bit()
        if not self.run:
            self.error()
        else:
            for widget in self.winfo_children():
                widget.grid_forget()
            self.label_cb = tk.Label(self, text = 'Enter what bit you want to change to').grid(row = 0)
            self.entry_cb = tk.Entry(self)
            self.entry_cb.grid(row = 0, column = 1)
            self.continue_calculation = tk.Button(self, text = 'Continue',command = lambda: self.change_base(int(self.entry_cb.get()))).grid(row = 1)

    def change_base(self,new_base):
        total = 0
        power = 0
        return_str = ''
        for i in self.bit[::-1]:
            if i.isdigit():
                total += int(i) * int(self.base) ** power
            else:
                total += (ord(i) - 55) * int(self.base) ** power
            power += 1
        while total > 0:                
            if total % new_base < 10:
                return_str += str(total % new_base)
            else:
                return_str += chr(55+ total % new_base)
            total = total // new_base
        for widget in self.winfo_children():
            widget.grid_forget()
        self.answer_label = tk.Label(self,text = return_str[::-1]).grid(row = 2)
        self.reset = tk.Button(self, text = 'reset', command = self.create_widgets).grid(row = 3)
        
        
    def find_decimal_representation(self):
        self.create_bit()
        total = 0
        power = 0
        for i in self.bit[::-1]:
            if i.isdigit():
                total += int(i) * int(self.base) ** power
            else:
                total += (ord(i) - 55) * int(self.base) ** power
            power += 1
        for widget in self.winfo_children():
            widget.grid_forget()
        self.answer_label = tk.Label(self, text = str(total)).grid(row = 0)
        self.reset = tk.Button(self, text = 'reset', command = self.create_widgets).grid(row = 1, column = 0)


root = tk.Tk()
root.title('Bit calculator')
mainBit = Bit(master=root)
mainBit.mainloop()    
        