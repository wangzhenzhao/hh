# import os
# pid = os.fork()
# if pid == 0:
#     print('创建新进程成功')
# elif pid < 0:
#     print('创建失败')
# else:
#     print('老的进程')
# print('程序到此完毕')


import tkinter as tk
from PIL import ImageTk,Image
root=tk.Tk()
root.title('新用户注册')
root.geometry('500x400')

im = './bj1.jpg'
img = Image.open(im)
photo = ImageTk.PhotoImage(img)

label_im=tk.Label(root,image=photo)
label_im.place(x=0,y=0)
img.close()
root.mainloop()