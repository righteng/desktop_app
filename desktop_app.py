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
    
    def create_widgets(self):
        # 閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side = 'bottom')

        # テキストボックス
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 10
        self.text_box.pack()

        # 実行ボタン
        submit_btn = tkinter.Button(self, text = '実行', command = self.input_handler)
        submit_btn['text'] = '実行'
#        submit_btn['command'] = self.input_handler
        submit_btn.pack()

        # メッセージ出力
        self.message = tkinter.Message(self)
        self.message.pack()

        #ラジオボタン
        self.selected_radio = tkinter.StringVar()
        radio_1 = tkinter.Radiobutton(self, text = 'A', value = 'A', variable = self.selected_radio)
        radio_2 = tkinter.Radiobutton(self, text = 'B', value = 'B', variable = self.selected_radio)
        radio_3 = tkinter.Radiobutton(self, text = 'C', value = 'C', variable = self.selected_radio)
        radio_4 = tkinter.Radiobutton(self, text = 'D', value = 'D', variable = self.selected_radio)
        radio_1.pack()
        radio_2.pack()
        radio_3.pack()
        radio_4.pack()

        #チェックボタン
        self.is_student = tkinter.BooleanVar()
        chk_btn = tkinter.Checkbutton(self, text = '同意しますか', variable = self.is_student)
        chk_btn.pack()

    #実行ボタン押下時にプロンプト上に文字表示
    def input_handler(self):
        print('「実行」が押されました')
        text = self.text_box.get()
        self.message['text'] = '回答：' + text
        print(f'入力値： {text}')
        print(self.selected_radio.get())

root = tkinter.Tk()

#表示ウィンドウの名称
root.title('test app')

#表示ウィンドウの大きさ
root.geometry('400x300')

app = Application(root = root)

app.mainloop()