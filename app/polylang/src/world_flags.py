"""_summary_
"""

from tkinter import Tk, Label
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM


def main() -> None:
    """_summary_
    """

    URLs = {
        "england": "https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg",
        "spain": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg",
        "france": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg",
        "germany": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg",
        "china": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_the_People%27s_Republic_of_China.svg",
    }

    url = URLs["england"]

    root = Tk()
    
    # Download the image of the English flag from Wikipedia
    with urlopen(url) as u:
        raw_data = u.read()
    
    # Convert the raw image data to a PIL image object
    england_flag_image = Image.open(BytesIO(raw_data))
    
    # Convert the PIL image to a Tkinter-compatible object
    england_flag_tk = ImageTk.PhotoImage(england_flag_image)
    
    # Create a label to display the image
    flag_label = Label(root, image=england_flag_tk)
    flag_label.pack()
    
    root.mainloop()


if __name__ == "__main__":
    main()
