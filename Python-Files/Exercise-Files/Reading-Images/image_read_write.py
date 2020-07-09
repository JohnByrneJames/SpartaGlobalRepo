from PIL import Image  # I installed the PIL 'pip install Pillow' through the terminal

class ReadImage:
    my_image = None

    def __init__(self, image):
        self.my_image = Image.open(image)

    def read_my_image(self):
        print(self.my_image.format, self.my_image.size, self.my_image.size)
        self.my_image.show()

    def convert_image(self):
        image_to_convert = self.my_image
        if image_to_convert.format.upper() == 'JPEG':
            image_to_convert.save("picture_as_kid.png")
        elif image_to_convert.format.upper() == 'PNG':
            image_to_convert.save("picture_as_kid.jpg")
        print(image_to_convert.format)
        print("We do not support this format sorry!")




# 2.
# Reading an image to writing to another file simultaneously
