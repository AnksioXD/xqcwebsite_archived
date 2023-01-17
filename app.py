from flask import Flask, render_template
import random
import os

api = Flask(__name__, static_folder = 'static')
png_files = [f for f in os.listdir('static') if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]
used_images = []

@api.route('/')
def index():
    if len(used_images) == len(png_files):
        used_images.clear()
    random_image = random.choice(png_files)
    while random_image in used_images:
        random_image = random.choice(png_files)
    used_images.append(random_image)
    return render_template('index.html', image=random_image)

if __name__ == '__main__':
    api.run(port=7080)
