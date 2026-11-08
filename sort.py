import os
import shutil
# 要整理的文件夹
folder = "把这里改成你要整理的文件夹路径"
# True 只显示不移动，确认没问题再改成 False
preview = True
# 路径不存在时，提示后退出
if not os.path.isdir(folder):
    print("请先把 folder 改成真实的文件夹路径")
    raise SystemExit
for name in os.listdir(folder):
    # 拼出完整路径
    path = folder + "/" + name
    # 只处理文件，跳过文件夹
    if os.path.isfile(path):
        # 取出后缀：转小写，去掉前面的点
        ext = os.path.splitext(name)[1].lower().replace(".", "")
        # 没有后缀的文件，统一放进"无后缀"
        if ext == "":
            ext = "无后缀"
        # 用后缀当文件夹名
        target = folder + "/" + ext
        if preview:
            print("预演：", name, "->", target)
        else:
            # 目标文件夹不存在就创建
            os.makedirs(target, exist_ok=True)
            # 把文件移动过去
            shutil.move(path, target + "/" + name)
            print(name, "->", target)