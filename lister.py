import os

def extract_model_name(file_name):
    return file_name.split('_')[1]

images_folder = "images"  # Update the path to your images folder

models = {condition: [extract_model_name(file) for file in os.listdir(os.path.join(images_folder, condition)) if file.endswith("_Choices.png")] for condition in os.listdir(images_folder) if os.path.isdir(os.path.join(images_folder, condition))}

for condition, model_list in models.items():
    print(f'{condition}: {model_list}')
