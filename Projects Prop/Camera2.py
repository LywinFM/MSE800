import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os

# Function to open the camera
def open_camera():
    try:
        cap = cv2.VideoCapture(0)  # 0 = default camera
        if not cap.isOpened():
            messagebox.showerror("Error", "Could not access the camera.")
            return

        # Create a new window for the camera feed
        cam_window = tk.Toplevel(root)
        cam_window.title("Camera Feed")

        # Label to display the video frames
        video_label = tk.Label(cam_window)
        video_label.pack()

        def update_frame():
            ret, frame = cap.read()
            if ret:
                # Convert BGR (OpenCV) to RGB (Pillow)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                video_label.imgtk = imgtk
                video_label.configure(image=imgtk)
            video_label.after(10, update_frame)

        def on_close():
            cap.release()
            cam_window.destroy()

        cam_window.protocol("WM_DELETE_WINDOW", on_close)
        update_frame()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main Tkinter window
root = tk.Tk()
root.title("Camera Launcher")

# Load an icon image for the button
try:
    # Create a simple icon if not available
    icon_path = "camera_icon.png"
    if not os.path.exists(icon_path):
        img = Image.new("RGB", (64, 64), color="blue")
        img.save(icon_path)

    icon_img = Image.open(icon_path)
    icon_img = icon_img.resize((64, 64), Image.LANCZOS)
    icon_photo = ImageTk.PhotoImage(icon_img)
except Exception as e:
    messagebox.showerror("Error", f"Could not load icon: {e}")
    sys.exit(1)

# Create a button with the icon
btn = tk.Button(root, image=icon_photo, command=open_camera)
btn.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()