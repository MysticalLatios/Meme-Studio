#Some code adapted from wxpython.org

from PIL import Image
import wx

###### Conversions ######

def wxbit_to_wx(bit_map: wx.Bitmap):
    ''' Converts a wx bitmap to a wx image '''
    return bit_map.ConvertToImage()

def wx_to_wxbit(img: wx.Image):
    ''' Converts a wx image to a wx bitmap '''
    return img.ConvertToBitmap()

def wxbit_to_pil(bit_map):
    ''' turn a wxbitmap into a pil image '''
    return wx_to_pil(wxbit_to_wx(bit_map))

def pill_to_wxbit(img):
    ''' turn a pill image to a bitmap '''
    return wx_to_wxbit(pil_to_wx(img))

def wx_to_pil(img: wx.Image):
    '''turn a WX bitmap into a PIL image one'''
    #Make a new image setting the size
    pil_img = Image.new('RGB', (img.GetWidth(), img.GetHeight()))
    pil_img.frombytes(bytes(img.GetData())) #Copy the data into the new image

    return pil_img #Return that new image

def pil_to_wx(img: Image, alpha=True):
    '''turn a PIL image into a wx one'''

    alpha_present = False
    if (img.mode[-1] == 'A'):
        alpha_present = True

    if (alpha and alpha_present):
        
        wx_img = wx.EmptyImage(*img.size)
        pil_RGBA = img.copy()
        pil_RGB = pil_RGBA.convert('RGB') #RGBA to RGB
        myPilImageRgbData = pil_RGB.tobytes()
        wx_img.SetData( myPilImageRgbData )
        wx_img.SetAlphaData( pil_RGBA.tobytes()[3::4] )  # Insert alpha values into layer
        
    else: #Image without alpha
        wx_img = wx.EmptyImage(*img.size)
        pil_img = img.copy()
        pil_img_rgb = pil_img.convert("RGB")
        pil_img_data = pil_img_rgb.tobytes()
        wx_img.SetData(pil_img_data)

    return wx_img


###### Normal tools ######

def crop(img, x, y, x_size, y_size):
    ''' crops an image '''


def resize(img, x_size, y_size):
    ''' resize an image '''
    return img.resize((x_size,y_size))

def rotate(img, rotation):
    ''' rotate an image '''
    img_conv = wxbit_to_pil(img)
    img_conv_2 = pill_to_wxbit(img_conv.rotate(rotation))

    return img_conv_2

def flip_left_right(img: Image):
    '''flip an image left to right'''
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def flip_top_bottom(img: Image):
    '''flip an image top to bottom (For those images that are a switch(works both ways))'''
    return img.transpose(Image.FLIP_TOP_BOTTOM)