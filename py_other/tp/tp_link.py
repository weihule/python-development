import pywinauto
from pywinauto.application import Application
import mouse
import time


def main():
    # 连接到已经打开的 "TP-LINK安防系统" 窗口
    # app = Application(backend="uia").connect(title="TP-LINK安防系统")
    app = Application().start(r"D:\ProgramFiles\TP-LINK\Surveillance\TP-LINK Surveillance.exe")
    time.sleep(2)  # 等待应用程序启动

    dlg = app["TP-LINK安防系统"]
    dlg.wait('exists enabled', timeout=10)  # 等待窗口出现
    dlg.wait('ready', timeout=10)  # 等待窗口就绪
    dlg.print_control_identifiers()

    menu = dlg["Qt5QWindowIcon"]
    print(menu.print_control_identifiers())
    


if __name__ == "__main__":
    main()



