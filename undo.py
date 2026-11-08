import os
import shutil
# 桌面路径
folder = "把这里改成你要整理的文件夹路径"
# 整理文件夹的位置
sorted_dir = folder + "/整理"
# True 只显示不移动，确认没问题再改成 False
preview = True
# 路径不存在时，提示后退出
if not os.path.isdir(sorted_dir):
    print("请先把 folder 改成真实的文件夹路径")
    raise SystemExit
for ext in os.listdir(sorted_dir):
    ext_dir = sorted_dir + "/" + ext
    # 只进入分类子文件夹
    if os.path.isdir(ext_dir):
        for name in os.listdir(ext_dir):
            src = ext_dir + "/" + name
            dst = folder + "/" + name
            if os.path.isfile(src):
                # 桌面已有同名文件就跳过，避免覆盖
                if os.path.exists(dst):
                    print("跳过（桌面已有同名文件）：", name)
                    continue
                if preview:
                    print("预演：", name, "->", folder)
                else:
                    shutil.move(src, dst)
                    print(name, "->", folder)