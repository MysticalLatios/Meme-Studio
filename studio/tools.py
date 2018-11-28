from PIL import Image
import wx

def wx_to_pil(img: wx.Image):
    '''turn a WX bitmap into a PIL image one'''
    #Make a new image setting the size
    pil_img = Image.new('RGB', (img.GetWidth(), img.GetHeight()))
    pil_img.fromstring(img.GetData()) #Copy the data into the new image
    return pil_img #Return that new image

def pil_to_wx(img: Image):
    '''turn a PIL image into a wx one'''