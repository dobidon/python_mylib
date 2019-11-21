# -*- coding: utf-8 -*-

import os
#import imageio

from PIL import Image, ImageFilter

# Creates gif from images in a folder with the same 
#
# Prototype img_out_path = Gif_From_Dir('/home/pi/images', 'image', '.png', 5)
#
def Gif_From_Dir_Trans(img_dir, img_out, ext='png', duration=1):
    if (not(len(os.listdir(img_dir)) > 1)):
        return None
    images = []
    for file_name in os.listdir(img_dir):
        if file_name.endswith(ext):
            file_path = os.path.join(img_dir, file_name)
#            images.append(imageio.imread(file_path))
            images.append(PNG_Alpha_to_Gif(file_path))
    images[0].save(img_out + '.gif', transparency=255, format='GIF',    \
                   append_images=images[1:], save_all=True,             \
                   duration=duration*1000, disposal=2, loop=0)
#    imageio.mimsave(img_out + '.gif', images, duration=duration)
    return (os.getcwd() + '/' + img_out + '.gif')

def PNG_Alpha_to_Gif(img_dir):#, img_out):
    im = Image.open(img_dir)
    
    # Get the alpha band
    alpha = im.split()[3]

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').filter(ImageFilter.SMOOTH).convert('P', palette=Image.ADAPTIVE, colors=255)
    
    # Set all pixel values below 128 to 255,
    # and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
    
    # Paste the color of index 255 and use alpha as a mask
    im.paste(255, mask)
#    im = im.convert('RGB').filter(ImageFilter.SMOOTH).convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
#    im.paste(255, mask)

    # The transparency index is 255
#    im.save(img_out + '.gif', transparency=255)
#    return (os.getcwd() + '/' + img_out + '.gif')
    return im

def Trans_to_White_BG_Save(img_src, img_out):
    image = Image.open(img_src + ".png")
    width, height = image.size
    image.convert("RGBA") # Convert this to RGBA if possible
    
    canvas = Image.new('RGBA', image.size, (255,255,255,255)) # Empty canvas colour (r,g,b,a)
    canvas.paste(image, mask=image) # Paste the image onto the canvas, using it's alpha channel as mask
    canvas.thumbnail([width, height], Image.ANTIALIAS)
    canvas.save(img_out+'.png', format="PNG")
    
    
def Trans_to_White_BG(img_path):
    image = Image.open(img_path)
    width, height = image.size
    image.convert("RGBA") # Convert this to RGBA if possible
    
    canvas = Image.new('RGBA', image.size, (255,255,255,255)) # Empty canvas colour (r,g,b,a)
    canvas.paste(image, mask=image) # Paste the image onto the canvas, using it's alpha channel as mask
    canvas.thumbnail([width, height], Image.ANTIALIAS)
    return canvas
    
# Creates gif from images in a folder with the same 
#
# Prototype img_out_path = Gif_From_Dir('/home/pi/images', 'image', '.png', 5)
#
def Gif_From_Dir(img_dir, img_out, ext='png', duration=1):
    res = None
    if (not(len(os.listdir(img_dir)) > 0)):
        return None
    images = []
    for file_name in os.listdir(img_dir):
        if file_name.endswith(ext):
            file_path = os.path.join(img_dir, file_name)
            images.append(Trans_to_White_BG(file_path))
    if len(images) > 0:
        if len(images) > 1:
            images[0].save(img_out + '.gif', transparency=255, format='GIF',   \
                           append_images=images[1:], save_all=True,            \
                           duration=duration*1000, disposal=2, loop=0)
        else:
            images[0].save(img_out + '.gif', transparency=255, format = 'GIF')
            
        res = os.path.join(os.getcwd(), img_out + '.gif')
    
    return res
