import pywinauto
from pywinauto.application import Application
import mouse
import time


def main():
    # 连接到已经打开的 "TP-LINK安防系统" 窗口
    # app = Application(backend="uia").connect(title="TP-LINK安防系统")
    app = Application(backend="uia").start(r"D:\ProgramFiles\TP-LINK\Surveillance\TP-LINK Surveillance.exe")
    time.sleep(2)  # 等待应用程序启动

    dlg = app["TP-LINK安防系统"]
    # dlg.print_control_identifiers()

    groupbox = dlg["GroupBox"]
    # groupbox.print_control_identifiers()

    menu = groupbox.child_window(auto_id="SurveillanceSystem.centralWidget.topWidget", control_type="Group")
    # menu.print_control_identifiers()

    set_btn = menu.child_window(title="设置", auto_id="SurveillanceSystem.centralWidget.topWidget.btnSetting", control_type="RadioButton")
    # set_btn.print_control_identifiers()
    set_btn.click()

    custom = dlg["Custom"]
    # custom.print_control_identifiers()

    device_groupbox = custom.child_window(auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.leftWidget", control_type="Group")
    # device_groupbox.print_control_identifiers()

    video_out = device_groupbox.child_window(title="录像导出", auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.leftWidget.btnExport", control_type="RadioButton")
    # video_out.print_control_identifiers()
    video_out.click()
    time.sleep(2)

    # 设备列表
    device_list = custom.child_window(auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.stackedWidget.SettingExportWidgetTab.exportStackedWidget.fileListPage.controlWidget.devComboBox", control_type="ComboBox")
    items = device_list.children()

    # 遍历并操作每一项
    for item in items:
        print("设备：", item)

    time.sleep(4)
    # 日期
    one_month = custom.child_window(title="最近一个月", auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.stackedWidget.SettingExportWidgetTab.exportStackedWidget.fileListPage.controlWidget.dateWidget.btnRecentMonth", control_type="CheckBox")
    one_month.click()
    time.sleep(1)

    # 录像类型
    all_btn = custom.child_window(title="全部", auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.stackedWidget.SettingExportWidgetTab.exportStackedWidget.fileListPage.controlWidget.typeWidget.btnTypeAll", control_type="RadioButton")
    all_btn.click()

    # 查询按钮
    query_btn = custom.child_window(title="查询", auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.stackedWidget.SettingExportWidgetTab.exportStackedWidget.fileListPage.controlWidget.btnQuery", control_type="Button")
    query_btn.click()
    time.sleep(2)

    # 获取状态栏或标签的控件对象（假设它是唯一的，你需要根据实际情况调整标识符）
    static_control = custom.child_window(title="选中了0个文件", auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.stackedWidget.SettingExportWidgetTab.exportStackedWidget.fileListPage.exportOptionWidget.countLabel", control_type="Text")

    # 获取并输出初始文本
    initial_text = static_control.window_text()
    print("初始文本:", initial_text)

    print("="*10)
    result_list = custom.child_window(auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.stackedWidget.SettingExportWidgetTab.exportStackedWidget.fileListPage.widget", control_type="Group")
    # result_list.print_control_identifiers()

    tree = custom.child_window(auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.stackedWidget.SettingExportWidgetTab.exportStackedWidget.fileListPage.widget.fileListTreeView", control_type="Tree")
    # tree.print_control_identifiers()
    items = tree.children()
    print(f"len(items) = {len(items)}")

    # 选中所有项, 这里idx == 1就break，是因为前面第一个已经全选了所有，如果后续还选，就会出现把前面选中的取消选中
    for idx, item in enumerate(items):
        item.click_input()
        if idx == 1:
            break
    print("="*10)

    time.sleep(2)

    # 导出全部按钮
    out_all = custom.child_window(title="导出全部", auto_id="SurveillanceSystem.centralWidget.stackedWidget.SettingWidgetTab.stackedWidget.SettingExportWidgetTab.exportStackedWidget.fileListPage.exportOptionWidget.btnExportAll", control_type="Button")
    out_all.click()
    out_all.print_control_identifiers()


    time.sleep(2)
    # 弹出的导出窗口
    app2 = Application(backend="uia").connect(title="TPTitleDialog")
    dlg2 = app2["TPTitleDialog"]
    dlg2.print_control_identifiers()


if __name__ == "__main__":
    main()



