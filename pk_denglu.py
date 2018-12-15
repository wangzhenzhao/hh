import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import sys,time
import pymysql
from multiprocessing import Process#线程
from queue import Queue#线程间通信队列
from socket import *
#套接字
HOST = ''
POST = 8888
ADDR=(HOST,POST)

top = tk.Tk()
top.resizable(width=False,height=False)
top.attributes('-alpha',0)
varZh = tk.StringVar()#帐号文本框的窗口
varZh.set('')
varpwd= tk.StringVar()#密码文本框的窗口
varpwd.set('')

top.title('咸鱼斗地主')
top.geometry('800x600')
top.geometry('800x600')
top.geometry('800x600')
    #背景图
im = './bj.jpg'
img = Image.open(im)
photo = ImageTk.PhotoImage(img)

label_im=tk.Label(top,image=photo)
label_im.place(x=0,y=0)
img.close()

#登录注册图
# im1 = './dl.jpg'
# img1 = Image.open(im1)
# photo1 = ImageTk.PhotoImage(img1)

# im2 = './zc3.png'
# img2 = Image.open(im2)
# photo2 = ImageTk.PhotoImage(img2)


# tk.Label(top,text='帐号:',font=('宋体',20)).place(x=250,y=200)
# tk.Label(top,text='密码:',font=('宋体',20)).place(x=250,y=300)
#创帐号建文本框
entr_yZh= tk.Entry(top,font=('宋体',15),textvariable=varZh,highlightcolor='gray'
        ,relief='raised')
entr_yZh.place(x=520,y=212,width=220,height=35)
    #创建密码文本框
entr_ypwd= tk.Entry(top,show='*',font=('宋体',15),textvariable=varpwd,highlightcolor='gray')
entr_ypwd.place(x=520,y=295,width=220,height=35)


def close1():
    from pygam_e import jiem1
    

def dlshijian():
    # event.char
    zhanghao=entr_yZh.get()
    mima=entr_ypwd.get()
    #线程通信  将主线程接收消息发往队列1,发送线程从队列取消息  通过队列传递消息

    #接收线程接收消息 发往队列2,主线程接收消息,根据消息类型做相应的界面刷新

    if zhanghao == '666'and mima == '1234':
        p = Process(target=close1)
        print('调用')
        p.start()

        top.destroy()
        print('父进程还在')
    else:
        tk.messagebox.showinfo(title='提示',message='帐号或密码输入错误')
    return
    

def zcshijian():
    root = tk.Toplevel()
    varname = tk.StringVar()#帐号文本框的窗口
    varzh = tk.StringVar()
    varpwd1 = tk.StringVar()#密码文本框的窗口
    # varpwd1.set('')
    varpwd2 = tk.StringVar()#密码文本框的窗口
    # varpwd2.set('')

    root.title('新用户注册')
    root.geometry('500x400')
    

    tk.Label(root,text='用户名:',font=('宋体',15),justify=tk.RIGHT).place(x=100,y=40)
    #tk.Label(root,text='帐号:',font=('宋体',15),justify=tk.RIGHT).place(x=100,y=100)
    tk.Label(root,text='密码:',font=('宋体',15),justify=tk.RIGHT).place(x=100,y=110)
    tk.Label(root,text='确认密码:',font=('宋体',15)).place(x=100,y=170)
    
    name= tk.Entry(root,font=('宋体',15),textvariable=varname,highlightcolor='gray')
    name.place(x=200,y=40,width=150,height=30)
    tk.Label(root,text="请输入8~16位字符").place(x=210,y=70)

    #zh= tk.Entry(root,font=('宋体',15),textvariable=varzh,highlightcolor='gray')
    #zh.place(x=200,y=100,width=150,height=30)

    pwd1= tk.Entry(root,show='*',font=('宋体',15),textvariable=varpwd1,highlightcolor='gray')
    pwd1.place(x=200,y=110,width=150,height=30)
    tk.Label(root, text="不能含有特殊字符及空格").place(x=210, y=140)
    pwd2= tk.Entry(root,show='*',font=('宋体',15),textvariable=varpwd2,highlightcolor='gray')
    pwd2.place(x=200,y=170,width=150,height=30)
    tk.Label(root, text="不能含有特殊字符及空格").place(x=210, y=200)

    def zhuce():
        # db = pymysql.connect(host='localhost',user='root',password='123456'
        #                             ,database='denglu',charset='utf8')
        # cur=db.cursor()
        try:
            mima1=pwd1.get()
            mima2=pwd2.get()
            yonghuming = name.get() 
        
        
            if mima1 != mima2:
                tk.messagebox.showerror(message='两次密码不一样')
            elif len(mima1)<6 or len(mima1)>18:
                tk.messagebox.showerror(message='注意密码格式')
        
            #elif len(str(zhanghao)) != 8:

        #     print('注意帐号格式')
            else:
                # db = pymysql.connect(host='localhost',user='root',password='123456'
                #                     ,database='denglu',charset='utf8')
                # cur=db.cursor()
                # sql = "insert into yonghuxinxi (name,zhanghao,password) values (%s,%s,%s)"
                #         # (%s,%d,%s)"%(yonghuming,zhanghao,mima1)
                # cur.execute(sql,[yonghuming,zhanghao,mima1])
                # print(sql)
                # db.commit()
                # cur.close()
                # db.close()

                tk.messagebox.showinfo(message='注册成功')
                root.destroy()
        except ValueError:
            tk.messagebox.showerror(message='注意帐号格式')


    #设置立即注册按钮并绑定函数
    lijizhuce=tk.Button(root,text='立即注册',bd=4,activebackground='red',command=zhuce)
    lijizhuce.place(x=125,y=310,width=170,height=45)
    root.mainloop()

def key(event):
    dlshijian()

def sb(event):
    if 440<=event.x<=572 and 413<=event.y<=456:
        dlshijian()
    if 622<=event.x<=763 and 413<=event.y<=455:
        zcshijian()
    #print('当前位置:',event.x,event.y)

top.bind('<Button-1>',sb)





#开始设置按钮 首先是登录-->注册

# dlanniu=tk.Button(top,image=photo1,bd=1,bg='blue',\
#     activebackground='sky blue',command=dlshijian)

top.bind_all('<Key-Return>',key)
# dlanniu.place(x=420,y=450,width=160,height=45)
# zcanniu = tk.Button(top,bd=0,bg='orange',activebackground='red',command=zcshijian)
# zcanniu.place(x=620,y=450,width=100,height=45)
# label_zc=tk.Label(top,image=photo2)
# label_zc.place(x=620,y=450)
top.mainloop()

def recv_sock():
    sockfd = socket()
    sockfd.connect(ADDR)
