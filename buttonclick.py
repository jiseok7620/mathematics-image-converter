import os

def image_add_btn(self):
    files = os.listdir("image_step1")
    for file in files:
        print(file)
        self.image_list.addItem(file)