import tkinter as tk
import time
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *


# root = Tk()
# root.title('')
# root.wm_attributes("-alpha", 0.1)        # 透明度(0.0~1.0)
# root.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
# root.wm_attributes("-topmost", True)     # 永远处于顶层
#
# ti=Label(root,text='啊这')
# ti.pack()
#
# # # 还可以调用如下方法去除窗口边框
# # root.overrideredirect(True)
# root.mainloop()

class DragWindow(tk.Tk):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=0.4, bg="gray", width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)      # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        self.bind('<B1-Motion>', self._on_move)
        self.bind('<ButtonPress-1>', self._on_tap)

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))

    def _on_move(self, event):
        offset_x = event.x_root - self.root_x
        offset_y = event.y_root - self.root_y

        if self.width and self.height:
            geo_str = "%sx%s+%s+%s" % (self.width, self.height,
                                       self.abs_x + offset_x, self.abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (self.abs_x + offset_x, self.abs_y + offset_y)
        self.geometry(geo_str)

    def _on_tap(self, event):
        self.root_x, self.root_y = event.x_root, event.y_root
        self.abs_x, self.abs_y = self.winfo_x(), self.winfo_y()


root = DragWindow(bg = None)
Label(root,text="老王时钟",font=Font(size=10)).pack()
timer= Label(root,text="时钟正在初始化...",font=Font(size=100))
# timer.("-alpha", 1)
def ut():
    timer["text"] = str(time.strftime('%Y/%m/%d', time.localtime(time.time())))+"\n"+str(time.strftime('%H:%M:%S', time.localtime(time.time())))
timer.after(1000,ut)
timer.pack()
root.mainloop()