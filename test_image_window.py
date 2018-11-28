import os
import wx

# we need the file path dialog to be accessible
# and grabbed from onBrowse
# or we at least want ImageView's onImageView
# to have access to the dialog setValue()
# from PhotoCtrl's onBrowse, and we want onBrowse to 
# call on ImageView.onImageView()

class ImageView(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self,redirect, filename)
        self.frame = wx.Frame(None, title='Meme View')

        self.panel = wx.Panel(self.frame)

        self.photoMaxSize = 960

        self.createImage()
        self.frame.Show()

    def createImage(self):
        image = wx.Image(720, 720)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                        wx.Bitmap(image))
        self.photoPath = wx.TextCtrl(self.panel, size=(200, -1))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)

        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.sizer.Add(self.photoPath, 0, wx.ALL, 5)

        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)
 

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)
        
        # comment this section out to get window
        # self.onImageView()
        self.panel.Layout()


    def onImageView(self):
        print('We have reach onImageView')
        filepath = self.photoPath.GetValue()
        print('this is the image: ' + filepath)
        image = wx.Image(filepath, wx.BITMAP_TYPE_ANY)

        # scale the image, preserving the aspect ratio
        W = image.GetWidth()
        H = image.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        image = image.Scale(NewW,NewH)
 
        self.imageCtrl.SetBitmap(wx.Bitmap(image))
        self.panel.Refresh()

# this class deals in controlling the image files
class PhotoCtrl(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='MEME STUDIO Browse')
 
        self.panel = wx.Panel(self.frame)
 
        self.PhotoMaxSize = 240
 
        self.createWidgets()
        self.frame.Show()

    # part of the main window that asks for you to browse for an image
    def createWidgets(self):
        instructions = 'Browse for an image'
        img = wx.Image(240,240)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                         wx.Bitmap(img))
        instructLbl = wx.StaticText(self.panel, label=instructions)
        self.photoPath = wx.TextCtrl(self.panel, size=(200,-1))

        browseBtn = wx.Button(self.panel, label='Browse')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
 
        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(instructLbl, 0, wx.ALL, 5)
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.sizer.Add(self.photoPath, 0, wx.ALL, 5)
        self.sizer.Add(browseBtn, 0, wx.ALL, 5)        
        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)
 

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)
 
        self.panel.Layout()
 
    # responsible for browsing for an image file
    def onBrowse(self, event):
        """ 
        Browse for file
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoPath.SetValue(dialog.GetPath())

        dialog.Destroy() 
        # used to be a call to onView
        # now it's a call to a new_frame
        # using ImageView class
        #self.new_frame()
        #thing = self.ImageView.onImageView()
        self.onView()

    def onView(self):
        filepath = self.photoPath.GetValue()
        image = wx.Image(filepath, wx.BITMAP_TYPE_ANY)

    
        # scale the image, preserving the aspect ratio
        W = image.GetWidth()
        H = image.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        image = image.Scale(NewW,NewH)
 
        self.imageCtrl.SetBitmap(wx.Bitmap(image))
        self.panel.Refresh()
    
    def new_frame(self):
        title = 'Image'
        # here we are making a call to open
        # a new frame, using the ImageView class
        print('should call on ImageView and open window')
        frame = ImageView()
        

if __name__ == '__main__':
    app = PhotoCtrl()
    #appy = ImageView()
    app.MainLoop()