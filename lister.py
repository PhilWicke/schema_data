import os

def extract_model_name(file_name):
    return file_name.split('_')[1]

images_folder = "images"  # Update the path to your images folder

models = {condition: [extract_model_name(file) for file in os.listdir(os.path.join(images_folder, condition)) if file.endswith("_Choices.png")] for condition in os.listdir(images_folder) if os.path.isdir(os.path.join(images_folder, condition))}

for condition, model_list in models.items():
    print(f'{condition}: {model_list}')


# define a variable "cut"
cut = 210
# cut the same amount off the top and bottom of each image
# it should be a total of 400 pixels

from PIL import Image

for condition, model_list in models.items():
    for model in model_list:
        image = Image.open(os.path.join(images_folder, condition, f'{condition}_{model}_Choices.png'))
        width, height = image.size
        image = image.crop((0, cut, width, height - cut))
        image.save(os.path.join(images_folder, condition, f'{condition}_{model}_Choices.png'))
        print(f'{condition}_{model}_Choices.png has been cropped and saved')

# add header_text.png in the TEXT subfolder to the top of each image in the TEXT subfolder
# add header_pseudo.png in the PSEUDO-VISUAL subfolder to the top of each image in the PSEUDO-VISUAL subfolder
# add header_visual.png in the VISUAL subfolder to the top of each image in the VISUAL subfolder

for condition, model_list in models.items():
    for model in model_list:
        image = Image.open(os.path.join(images_folder, condition, f'{condition}_{model}_Choices.png'))
        header = Image.open(os.path.join(images_folder, condition, f'header_{condition.lower()}.png'))
        header_width, header_height = header.size
        # create a new image that starts with the header image and append the image of the model below it
        new_image = Image.new('RGB', (image.width, header_height + image.height))
        new_image.paste(header, (0, 0))
        new_image.paste(image, (0, header_height))
        new_image.save(os.path.join(images_folder, condition, f'{condition}_{model}_Choices.png'))
        print(f'{condition}_{model}_Choices.png has been saved with header')
