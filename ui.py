import tkinter as tk
class temporizador:
    """
    计时器ui类
    """
    def __init__(self,c):
        """
        初始化计时器ui
        :param c: 计时器类
        """
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW",self.close)
        self.countdown=c
        self.tlable=tk.Label(self.window,text="")
        self.window.title("计时器")
        self.window.geometry("300x100+300+300")

        self.state=0
    def run(self):
        """
        运行计时器
        """
        self.tlable.pack()
        self.countdown.start(self)
        self.window.mainloop()

    def close(self):
        """
        关闭计时器
        """
        self.state=1
        self.window.destroy()


