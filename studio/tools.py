#Some code adapted from wxpython.org

from PIL import Image
import wx

def wxbit_to_wx(bit_map):
    ''' Converts a wx bitmap to a wx image '''
    return wx.ImageFromBitmap(bit_map)

def wx_to_wxbit(img: wx.Image):
    ''' Converts a wx image to a wx bitmap '''
    return img.ConvertToBitmap()

def wxbit_to_pil(bit_map):
    ''' turn a wxbitmap into a pil image '''
    return wx_to_pil(wxbit_to_wx(bit_map))

def wx_to_pil(img: wx.Image):
    '''turn a WX bitmap into a PIL image one'''
    #Make a new image setting the size
    pil_img = Image.new('RGB', (img.GetWidth(), img.GetHeight()))
    pil_img.fromstring(img.GetData()) #Copy the data into the new image
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
        myPilImageRgbData = pil_RGB.tostring()
        wx_img.SetData( myPilImageRgbData )
        wx_img.SetAlphaData( pil_RGBA.tostring()[3::4] )  # Insert alpha values into layer
        
    else: #Image without alpha
        wx_img = wx.EmptyImage(*img.size)
        pil_img = img.copy()
        pil_img_rgb = pil_img.convert("RGB")
        pil_img_data = pil_img_rgb.tostring()
        wx_img.SetData(pil_img_data)

    return wx_img