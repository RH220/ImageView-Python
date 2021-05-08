from tkinter import *
import tkinter.ttk as ttk

class ProgressBarSampleApp(ttk.Frame):

    def __init__(self, app):
        super().__init__(app)
        self.pack()

        label = ttk.Label(self,text="Progressbar")
        label.pack(side="left")


        self.pbDeterminateVer = ttk.Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
        self.pbDeterminateVer.pack(side="left")

        startbutton = ttk.Button(self,text="start",command = self.startDeterminateVer)
        startbutton.place(x=100, y=10)
        startbutton.pack(side="left")

        stopbutton = ttk.Button(self,text="stop",command = self.stopDeterminateVer)
        stopbutton.pack(side="left")


    #stepを実行する
    def startDeterminateVer(self):
        self.step()
    #stopを実行することで初期化される
    def stopDeterminateVer(self):
        self.pbDeterminateVer.stop()

    #stepの引数にどれだけ進捗を進めるかを指定する
    def step(self):
        self.pbDeterminateVer.step(10)


if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅400横幅300に画面サイズを変更します。
    app.geometry("600x300")
    #タイトルを指定
    app.title("ProgressBar Sample Program")
    # #フレームを作成する
    frame = ProgressBarSampleApp(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()