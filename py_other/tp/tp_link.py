from pywinauto.application import Application
import lackey
from keyboard import mouse
import time


def main():
    app = Application().start("D:\ProgramFiles\TP-LINK\Surveillance\TP-LINK Surveillance.exe")
    time.sleep(2)  # 等待应用程序启动
    # dlg = app.window(title="无标题 - 记事本")

    lackey.find(r'./photo/all1.png', sim=0.8)
    lackey.find(r'./photo/setting.png', sim=0.8)
    lackey.find(r'./photo/vedio_out.png', sim=0.8)
    lackey.find(r'./photo/today.png', sim=0.8)

    # app.window(title="无标题 - 记事本").close()  
    # app.quit()


if __name__ == "__main__":
    main()



