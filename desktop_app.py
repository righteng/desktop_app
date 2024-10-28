import tkinter

class Application(tkinter.Frame):
    def __init__(self, root = None):
        super().__init__(root,
            width = 380, height = 280,
            borderwidth = 1, relief = 'groove')
        self.root = root
        #表示位置
        self.pack()
        #サイズ調整
        self.pack_propagate(0)
        self.create_widgets()
    
    #閉じるボタン
    def create_widgets(self):
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side = 'bottom')

root = tkinter.Tk()

#表示ウィンドウの名称
root.title('test app')

#表示ウィンドウの大きさ
root.geometry('400x300')

app = Application(root = root)

app.mainloop()