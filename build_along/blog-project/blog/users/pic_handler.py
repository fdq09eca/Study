import os
from PIL import Image
from flask import url_for, current_app

def add_profile_pic(pic_upload, username): #Jose
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(username) + '.' + ext_type
    filepath = os.path.join(current_app.root_path,'static/profile_img', storage_filename)
    output_size = (200,200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    if os.path.exists(filepath): # Chris
        os.remove(filepath)
    pic.save(filepath)
    return storage_filename

def save_picture(form_pic): # Corey Schafer
    rand_hx = secrets.token_hex(8)
    f_name, f_ext = os.path.splittext(form_pic.filename)
    pic_filename = rand_hx + f_ext
    picture_path = os.path.join(app.root_path,'static/profile_img', pic_filename)
    form_pic.save(picture_path)
    return pic_filename
