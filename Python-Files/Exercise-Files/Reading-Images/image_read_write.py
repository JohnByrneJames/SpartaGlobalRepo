from PIL import Image

class ReadImage:
    def __init__(self):
        pass

    def read_my_image(self):
        my_image = Image.open("picture_as_kid.jpg")
        print(my_image.format, my_image.size, my_image.size)
        my_image.show()

# 2.
# Reading an image to writing to another file simultaneously
