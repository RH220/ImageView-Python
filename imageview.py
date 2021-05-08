import sys
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
import glob
import PIL.Image
from tkinter import filedialog as tkFileDialog
import tkinter as tk
# import Image as I
from PIL import Image as I, ImageTk as Itk
from PIL import ImageFile
import RH.slice_list as SList
from functools import partial
from pathlib import Path
ImageFile.LOAD_TRUNCATED_IMAGES = True
class CA(tk.Frame):
# クラス初期設定
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # クラスウィジェット作成
        f=tk.Frame(master, bg="red",
        relief="groove",borderwidth=3)
        
        # キャンバス作成
        self.c=tk.Canvas(f,width=1550,
        height=850,bg = "cyan",
        scrollregion=(0,0,1113400,1113400))
        # self.title('スクロール')
        # self.geometry(100+100)
        self.c.grid(column=0, row=0,
        sticky='nsew')
    
        # X 軸 スクロールバー作成
        sx=tk.Scrollbar(f,
        orient='horizontal',
        command=self.c.xview,width=10)
        self.c["xscrollcommand"]=sx.set
        sx.grid(column=0, row=1,
        sticky='ew')
        # Y 軸 スクロールバー作成
        sy=tk.Scrollbar(f,
        orient='vertical',
        command=self.c.yview, width=200)
        self.c["yscrollcommand"]=sy.set
        sy.grid(column=1, row=0,
        sticky='ns')
        f.grid_columnconfigure(0,weight=1)
        f.grid_rowconfigure(0,weight=1)
        f.pack(fill=tk.BOTH,expand=1)
    # var = StringVar()
    # var.set('normal')
    var = 'who'
    def print_varsize(self):
        import types
        print("{}{: >15}{}{: >10}{}".format('|','Variable Name','|','  Size','|'))
        print(" -------------------------- ")
        for k, v in globals().items():
            if hasattr(v, 'size') and not k.startswith('_') and not isinstance(v,types.ModuleType):
                print("{}{: >15}{}{: >10}{}".format('|',k,'|',str(v.size),'|'))
            elif hasattr(v, '__len__') and not k.startswith('_') and not isinstance(v,types.ModuleType):
                print("{}{: >15}{}{: >10}{}".format('|',k,'|',str(len(v)),'|'))
        
    def button1_clicked(self): 
        global filenames #クラスを超えて利用可能な変数です
        global ff #クラスを超えて利用可能な変数です
        fTyp = [('', '*')]
        # iDir = os.path.abspath(os.path.dirname(__file__))#現在のディレクトリで開く
        iDir = os.path.abspath(os.path.dirname('R:/Install/xampp/htdocs/Python/scraip/jpg4/'))
        filenames = tkFileDialog.askopenfilenames(filetypes=fTyp, initialdir=iDir)
        # print (filenames)#デバッグ用
        c.c.delete("window")
        
        page =0
        # c=CA()
        # y=0

        ff=len(filenames)
        # if(ff>=50):
        # print('分割')
        # for i in filenames:
            # print(i)\
        # # # test用
        a = filenames
        s = SList.Slice_list(a,50)
        s.cut_list()
        y=40 #最初の表示する位置
        if(rdo_var.get()== 0 ):
            print('3枚表示')
        # サムネイルの表示する大きさ
            viewCount = 2
            imWidth=480
            imHeight=524
            xWidth = 10
            x = xWidth
            # 1425
            # 1536
        else:
            print('2枚表示')
            viewCount = 1
            imWidth=712
            imHeight=772
            xWidth = 20
            x = xWidth
            
          
        # enumerate関数を使うと、要素のインデックスと要素を同時に取り出す事が出来ます。
        for index, i in enumerate(SList.slice_list_file):
            
            #!! 終わった後にしか表示されない
            lbl['text']='{0}/{1}'.format(index*50, ff)
            print('{0}/{1}'.format(index*50, ff))
            # print(index*50+'/'+ff)#取り込み状況を表示
            for index, j in enumerate(i):
                # print('Jdesu'+str(j))
        # print(SList.slice_list_file)
    
            # for n in filenames:
                print(index)
                print(j)
                img = PIL.Image.open(j)
                
                img =img.resize((imWidth,imHeight),PIL.Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                imgs.append(img)
                buttons = [None]*ff
                buttons[index] = tk.Button(c.c,image=img,
                    command=partial(c.button3_clicked,j,buttons[index],index))
                    # y command=partial(メソッド名,引数),text = index, font = '100')
                c.c.create_window(x, y,
                anchor=tk.NW, window = buttons[index])
                # c.c.create_image(x, y,
                # anchor=tk.NW, image=img)
                # yield c.c.create_image(x, y,
                # anchor=tk.NW, image=img)
                
                if(page<viewCount):
                    page+=1
                    x += imWidth+5
                    # print('true')
                    
                else:
                    page=0
                    x=xWidth
                    y+=imHeight+5
                    # print('no')
            else:
                # imgs = []
                print(buttons)
                print('done')
                # del filenames
                

        print('ファイル数 : '+str(ff))
# yリセット用ボタン
    def button3_clicked(self,num,buttons,index): 
        print(num)
        print(buttons)
        print(index)
        try :
            shutil.move(num,'R:/Install/xampp/htdocs/Python/scraip/jpg4')
        except shutil.Error:
            print('同じ名前のファイルがあります')

        # global filenames2#クラスを超えて利用可能な変数です
        # global ff2 #クラスを超えて利用可能な変数です
        # fTyp = [('', '*')]
        # # iDir = os.path.abspath(os.path.dirname(__file__))#現在のディレクトリで開く
        # iDir = os.path.abspath(os.path.dirname('R:/Install/xampp/htdocs/Python/scraip/jpg4/'))
        # filenames = tkFileDialog.askopenfilenames(filetypes=fTyp, initialdir=iDir)
        
        
# t 2回目の選択は初期化する
# t フォルダ毎取り込む機能
# t クリックしたら保存する
# y画像を押したら拡大する
# y拡大してもスクロールできる
# yスライドショーから戻れるように
# yスライドショーをストップ、巻き戻し
# メインプログラム


if __name__ == '__main__':
    # flameをwindowに入れ込む
    root = Tk()
    root.title("Tkinter win")
    root.geometry('+0+10')
    imgs=[]
    c = CA(root)
    # button1
    button1 = Button(c.c, text=u'ファイル選択',
    command=c.button1_clicked)
    button1.grid(row=0, column=1) 
    button1.place(x=370, y=12)
    # button2
    button2 = tk.Button(c.c, text = '選択終了', 
    command=c.quit)
    button2.grid(row=0, column=1) 
    button2.place(x=470, y=12)
    # button3
    button3 = Button(c.c, text=u'ファイル選択',
    command=c.print_varsize,bg = 'red')
    button3.grid(row=0, column=1) 
    button3.place(x=870, y=12)
    # ラジオボタンの状態
    rdo_var = tkinter.IntVar()
    radio0 = tk.Radiobutton(c.c, 
                            text = "1列3枚表示",      # ラジオボタンの表示名
                            # command = self.radio_click,  # クリックされたときに呼ばれるメソッド
                            variable = rdo_var, # 選択の状態を設定する
                            value = 0,                    # ラジオボタンに割り付ける値の設定
                            height = 2
                            )

    radio1 = tk.Radiobutton(c.c, 
                            text = "1列2枚表示",      # ラジオボタンの表示名
                            # command = c.radio_click,  # クリックされたときに呼ばれるメソッド
                            variable = rdo_var, # 選択の状態を設定する
                            value = 1 ,                   # ラジオボタンに割り付ける値の設定
                            bg = 'green',
                            height = 2,command=c.button1_clicked)
    # ラベル
    lbl = tkinter.Label(c.c, text='読み込み状況 : 0')
    lbl.place(x=630, y=32)
    # rdo_var.set('0')#初期値を設定
    radio0.place(x=160, y=12)
    radio1.place(x=270, y=12)
    c.mainloop()
    

# 0503
# flameを入れ子にして画面の初期位置を変更した
# 読み込みファイル数を表示したいが、終了後のみ表示される
# 2枚表示を可能にした
# あとは保存機能
# !表示した画像にbuttonインデックスを振って、filenames[index]を
    # 対象にすれば軽くできそう
# 閲覧後にそのファオルダを消したい
# ウィジェットの表示、非表示切り替え
# 0505
# メモリ開放できない、5000枚でエラーになる

