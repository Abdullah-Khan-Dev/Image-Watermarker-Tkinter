import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


def upload_image():
    global img, img_display, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((400, 400))
        img_display = ImageTk.PhotoImage(img)
        canvas.create_image(200, 200, image=img_display)


def add_watermark():
    if not img_path:
        messagebox.showerror("Error", "No image uploaded!")
        return

    watermark_text = text_entry.get()
    if not watermark_text:
        messagebox.showerror("Error", "No watermark text entered!")
        return

    original = Image.open(img_path)
    width, height = original.size

    draw = ImageDraw.Draw(original)
    font = ImageFont.load_default()

    textwidth, textheight = draw.textsize(watermark_text, font)

    x = width - textwidth - 10
    y = height - textheight - 10

    draw.text((x, y), watermark_text, font=font)

    watermarked_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), (
    "JPEG files", "*.jpg *.jpeg")])
    if watermarked_image_path:
        original.save(watermarked_image_path)
        messagebox.showinfo("Success", "Watermark added and image saved!")


root = tk.Tk()
root.title("Watermark Application")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(padx=10, pady=10)

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)
text_entry.insert(0, "Enter watermark text here")

add_watermark_button = tk.Button(root, text="Add Watermark", command=add_watermark)
add_watermark_button.pack(pady=10)

root.mainloop()
