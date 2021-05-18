
from PIL import Image, ImageTk
import threading
import time
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import glob
import PIL.Image
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from PIL import Image as I, ImageTk as Itk
from PIL import ImageFile
import RH.slice_list as SList
from functools import partial
from pathlib import Path
import gc
import math
ImageFile.LOAD_TRUNCATED_IMAGES = True
dir_original = os.getcwd()
class CA(tk.Frame):
# クラス初期設定
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # クラスウィジェット作成
        f=tk.Frame(master,
        relief="groove",borderwidth=3)
        
        # キャンバス作成
        self.c=tk.Canvas(f,width=1550,
        height=850,bg = "steel blue",
        scrollregion=(0,0,100,100))
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


    def print_varsize(self):
        import types
        print("{}{: >15}{}{: >10}{}".format('|','Variable Name','|','  Size','|'))
        print(" -------------------------- ")
        for k, v in globals().items():
            if hasattr(v, 'size') and not k.startswith('_') and not isinstance(v,types.ModuleType):
                print("{}{: >15}{}{: >10}{}".format('|',k,'|',str(v.size),'|'))
            elif hasattr(v, '__len__') and not k.startswith('_') and not isinstance(v,types.ModuleType):
                print("{}{: >15}{}{: >10}{}".format('|',k,'|',str(len(v)),'|'))

    # フォルダーを開く
    def dirdialog_clicked(self):
        iDir = os.path.abspath(os.path.dirname('R:/Install/xampp/htdocs/Python/scraip/jpg4/'))
        dir_Path = filedialog.askdirectory(initialdir = iDir)
        print(dir_Path)
        # 位置を初期化
        try:
            os.chdir(dir_original)
        # 対象フォルダに移動
            os.chdir(dir_Path)
        # フォルダ内の全ファイルを取得
            filenames = glob.glob("./*")
            # os.chdir(dir_original)
            return filenames,dir_Path
            
        except OSError:
            # sys.exit()
            return

    # ファイルを開く
    def filedialog_clicked(self):
        fTyp = [("", "*")]
        # iFile = os.path.abspath(os.path.dirname(__file__))
        iFile = os.path.abspath(os.path.dirname('R:/Install/xampp/htdocs/Python/scraip/jpg4/'))
        filenames = filedialog.askopenfilenames(filetype = fTyp, initialdir = iFile)
        return filenames

    
    def button1_clicked(self,switch): 
        global filenames 
        global all_files 
        # filenames =[]
        # # imgs=[] #枠だけ表示される

        # print (filenames)#デバッグ用
        # imgs = []
        if(switch == 1):
            filenames = self.filedialog_clicked()
        else:
            result = self.dirdialog_clicked()
            filenames = result[0]

        
        page =1

        all_files=len(filenames)

        # # # test用
        a = filenames
        s = SList.Slice_list(a,50)
        s.cut_list()
        y=40 #最初の表示する位置

        # 表示領域（x,y)
        # サムネイルの表示する大きさ
        if(rdo_var.get()== 0 ):
            print('3枚表示')
        
            viewCount = 3
            imWidth=480
            imHeight=524
            xWidth = 10
            x = xWidth
        else:
            print('2枚表示')
            viewCount = 2
            imWidth=712
            imHeight=786
            xWidth = 10
            x = xWidth
        # スクロールバー調整
        scroll_X = imWidth *viewCount
        scroll_Y = (imHeight+5) * math.ceil(all_files/viewCount)
        # print('scroll_X:'+str(scroll_X))
        # print('scroll_Y:'+str(scroll_Y))

        
        # enumerate関数を使うと、要素のインデックスと要素を同時に取り出す事が出来ます。
        for index, i in enumerate(SList.slice_list_file):
            
            rht='読み込みファイル数 :{0}/{1}'.format(all_files, all_files)
            # lbl['text']=rht
            root.title(title+rht)
            resultCount = (index+1)*50
            # print('{0}/{1}'.format(index*50, all_files))
            if(resultCount>all_files):
                resultCount = all_files
            # y ポップアップを自動的に消すにはctypesが必要
            # y https://teratail.com/questions/275438
            # messagebox.showinfo('確認', '読み込みファイル数 :{0}/{1}'.format(resultCount, all_files))
            print('読み込みファイル数 :{0}/{1}'.format(resultCount, all_files))#取り込み状況を表示
            
            for index, j in enumerate(i):
                # c = CA(root)#下に新しいcanvasができる
                # print('Jdesu'+str(j))
                # print(SList.slice_list_file)
            # for n in filenames:
                # print(index)
                # print(j)
                    # imgs = [] #画像が表示されない白枠だけ
                try:    
                    img = PIL.Image.open(j)

                    img =img.resize((imWidth,imHeight),PIL.Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    imgs.append(img)
                    buttons = [None]*all_files
                    buttons[index] = tk.Button(c.c,image=img,
                        command=partial(c.img_button_clicked,j,buttons[index],index))
                        # y command=partial(メソッド名,引数),text = index, font = '100')
                    c.c.create_window(x, y,
                    anchor=tk.NW, window = buttons[index])
                    # c.c.create_image(x, y,
                    # anchor=tk.NW, image=img)

                    if(page<viewCount):
                        page+=1
                        x += imWidth+5
                    else:
                        page=1
                        x=xWidth
                        y+=imHeight+5
                except PIL.UnidentifiedImageError:
                    print("PIL.UnidentifiedImageError:"+j)
                    continue

            else:
                # forが終わったら
                # print('done')
                # del c.c
                # imgs = []#何も表示されない
                gc.collect()
                c.c.configure(scrollregion=(0,0,scroll_X,scroll_Y))

        # button3 = Button(c.c, text=u'フォルダ削除',
        #             command=partial(c.button3_clicked,result[1]))
        # button3.grid(row=0, column=2) 
        # button3.place(x=770, y=10)        
                
        # os.chdir(dir_original)
        print('ファイル数 : '+str(all_files))
# y 保存用ボタン
    # 保存フォルダ
    global new_dir_path 
    new_dir_path = dir_original+"\\SAVE"  
    if(os.path.exists('R:/Install/xampp/htdocs/Python/scraip/jpg4')):
        new_dir_path = 'R:/Install/xampp/htdocs/Python/scraip/jpg4'
    
    def img_button_clicked(self,location,buttons,index): 
        print(location)
        print(buttons)
        print(index)
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
        try :
            shutil.move(location,new_dir_path)
            # shutil.move(location,'R:/Install/xampp/htdocs/Python/scraip/jpg4')
        except shutil.Error:
            messagebox.showinfo('エラー', '保存先に同じ名前のファイルがあります。\n'+location)
    # フォルダ削除,常に失敗する
    # def button3_clicked(self,dir_path):
    #     delete_Verification = messagebox.askyesno('確認', str(dir_path)+'\nを削除します。')
    #     if delete_Verification == True:
    #     # messagebox.showinfo('確認', str(dir_path)+'\nを削除します。')
    #         try:
    #             shutil.rmtree(dir_path)
    #             button3.destroy()
    #         except PermissionError as e:
    #             messagebox.showinfo('エラー : 失敗しました', e)
        
        


# メインプログラム
if __name__ == '__main__':
    # flameをwindowに入れ込む
    root = Tk()
    title='ImageView : '
    rht = ''
    root.title(title+rht)
    root.geometry('+0+10')
    imgs=[]
    c = CA(root)
    # button1
    button1 = Button(c.c, text=u'ファイル選択',
                    command=partial(c.button1_clicked,1))
    button1.grid(row=0, column=1) 
    button1.place(x=420, y=10)
    # button2
    button2 = Button(c.c, text=u'フォルダ選択',
                    command=partial(c.button1_clicked,2))
    button2.grid(row=0, column=2) 
    button2.place(x=570, y=10)
    # # button3
    # button3 = Button(c.c, text=u'フォルダ削除',
    #                 command=partial(c.button1_clicked,2))
    # button3.grid(row=0, column=2) 
    # button3.place(x=570, y=10)
    # command=partial(c.button3_clicked,j,buttons[index],index))


    # button3(メモリ確認用)
    # button3 = Button(c.c, text=u'ファイル選択',
    # command=c.print_varsize,bg = 'red')
    # button3.grid(row=0, column=1) 
    # button3.place(x=870, y=6)
    # ラジオボタンの状態
    rdo_var = tk.IntVar()
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
                            height = 2)
    # ラベル
    # lbl = tk.Label(root, text='読み込み状況 : 0',height = 2)
    # lbl.place(x=530, y=10)

    # rdo_var.set('0')#初期値を設定
    radio0.place(x=160, y=6)
    radio1.place(x=270, y=6)
    c.mainloop()
    
    # 完了
    # クリックしたら保存する



