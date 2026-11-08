import os
# 要整理的文件夹
folder = "把这里改成你要整理的文件夹路径"
# True 只显示不改名，确认没问题再改成 False
preview = True
# 路径不存在时，提示后退出
if not os.path.isdir(folder):
    print("请先把 folder 改成真实的文件夹路径")
    raise SystemExit
# 编号从 1 开始
count = 1
for name in os.listdir(folder):
    # 只处理 .txt 文件
    if name.endswith(".txt"):
        # 新名字：001.txt、002.txt……
        new_name = str(count).zfill(3) + ".txt"
        # 新名字已存在就跳过，避免覆盖
        if os.path.exists(folder + "/" + new_name):
            print("跳过（已有同名文件）：", new_name)
        elif preview:
            print("预演：", name, "->", new_name)
        else:
            os.rename(folder + "/" + name, folder + "/" + new_name)
            print(name, "->", new_name)
        count = count + 1