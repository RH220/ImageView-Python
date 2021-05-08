import tkinter

# メインウィンドウ作成
app = tkinter.Tk()
app.title("NO1")
app.geometry("600x600")
# app2 = tkinter.Tk()
# app2.title("NO2")
# app2.geometry("600x400")

# 青色のキャンバス作成
canvas1 = tkinter.Canvas(
    app,
    
    width=600,
    height=100,
    bg="blue"
)

# # 緑色のキャンバス作成
canvas2 = tkinter.Canvas(
    app,
    # canvas1,
    width=600,
    height=200,
    bg="green"
)
canvas3 = tkinter.Canvas(
    app,
    # canvas1,
    width=600,
    height=200,
    bg="red"
)

# # １つ目のボタン作成
# button1 = tkinter.Button(
#     canvas2,
#     width=10,
#     height=10,
#     text="ボタン１"
# )

# # ２つ目のボタン作成
# button2 = tkinter.Button(
#     canvas2,
#     width=1,
#     height=2,
#     text="ボタン\n２"
# )

# # 各ウィジェットの配置
# # canvas1.pack(side=tkinter.TOP)
# canvas1.pack(fill = tkinter.BOTH,side=tkinter.BOTTOM)
# canvas2.pack(side=tkinter.RIGHT)
# canvas3.pack(side=tkinter.RIGHT)
canvas1.pack()
canvas2.pack()
canvas3.pack()
# button1.pack()
# button2.pack()


# メインループ
app.mainloop()