import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os  # 用来检查文件是否存在


# 点击YES：显示小猪图片（修复空白问题）
def show_pig_image():
    # 第一步：确认图片路径（重点！）
    # 替换成你的图片文件名，比如 "小猪.png" / "pig.png" / "pig.jpg"
    img_path = "pig.jpg"  # ********** 这里改你的图片名 **********

    # 检查图片是否存在（避免路径错）
    if not os.path.exists(img_path):
        messagebox.showerror("错误", f"没找到图片！请确认文件名为：{img_path}，且和代码在同一文件夹")
        return

    # 创建图片窗口
    image_window = tk.Toplevel()
    image_window.title("小猪来啦！")

    try:
        # 打开图片（兼容jpg/png等格式）
        img = Image.open(img_path)

        # 缩放图片（适配窗口，避免太大/太小导致空白）
        img.thumbnail((500, 400))  # 最大宽500，高400，保持比例

        # 关键：保留图片引用（新手最易漏，漏了就空白）
        photo = ImageTk.PhotoImage(img)

        # 显示图片
        img_label = tk.Label(image_window, image=photo)
        img_label.photo = photo  # 必须保留引用！！！
        img_label.pack(padx=10, pady=10)

    except Exception as e:
        messagebox.showerror("图片加载失败", f"原因：{str(e)}\n请检查图片格式（推荐jpg/png）")


# 点击NO：提示重新选择
def choose_again():
    messagebox.showinfo("提示", "请重新选择")


# 主界面
root = tk.Tk()
root.title("提问")
root.geometry("350x180")
root.resizable(False, False)

# 问题标签
tk.Label(root, text="郑雨晴是小猪吗？", font=("微软雅黑", 18)).pack(pady=30)

# 按钮
btn_frame = tk.Frame(root)
btn_frame.pack()
tk.Button(btn_frame, text="yes", font=20, width=8, command=show_pig_image).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="no", font=20, width=8, command=choose_again).grid(row=0, column=1)

root.mainloop()