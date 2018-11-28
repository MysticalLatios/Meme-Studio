from PIL import Image
import wx

def WX_TO_PIL(img :wx.Image):
    '''turn a WX bitmap into a PIL image one'''
    PilImg = Image.new( 'RGB', (img.GetWidth(), img.GetHeight()) ) #Make a new image setting the size
    PilImg.fromstring( img.GetData() ) #Copy the data into the new image
    return PilImg #Return that new image

def PIL_TO_WX(img :Image):
    '''turn a PIL image into a wx one'''