import os
import sys
from PIL import Image, ImageTk

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_image(name, size=None):
    """Load an image from /images, optionally resize."""
    path = resource_path(os.path.join("images", name))
    img = Image.open(path)
    if size:
        img = img.resize(size)
    return ImageTk.PhotoImage(img)