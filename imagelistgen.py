import os

# Change this to your local images folder path
images_folder = 'images'

# Supported image extensions
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}

# Get all image files in the folder
image_files = [f for f in os.listdir(images_folder) if os.path.splitext(f)[1].lower() in image_extensions]

# Generate the HTML list items
for img in image_files:
    print(f'<li><img src="/images/{img}" alt="{os.path.splitext(img)[0]}"></li>')
