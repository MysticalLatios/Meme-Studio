#For launching the gui of the program
import wx
import wx.lib.scrolledpanel
import sys
import os
import time

from studio import tools
from studio import io

#Global list of the windows the images will be on
WINDOWS = []

class MemeStudioGUI(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MemeStudioGUI, self).__init__(*args, **kwargs)
        panel = ToolPanel(self)
        self.Show()
        self.InitUI()

    def InitUI(self):
        toolbar = self.CreateToolBar()
        themenubar = wx.MenuBar()
        #toolbar.SetToolBitmapSize((16, 16))
        # adding comment here for change. Also, icons should be fixed below
        savetool = toolbar.AddTool(wx.ID_ANY, 'Save', wx.Bitmap('Meme_Studio_Icons/save.png'))
        undotool = toolbar.AddTool(wx.ID_ANY, 'Undo', wx.Bitmap('Meme_Studio_Icons/undo.png'))
        redotool = toolbar.AddTool(wx.ID_ANY, 'Redo', wx.Bitmap('Meme_Studio_Icons/redo.png'))
        cuttool = toolbar.AddTool(wx.ID_ANY, 'Cut', wx.Bitmap('Meme_Studio_Icons/cut.png'))
        copytool = toolbar.AddTool(wx.ID_ANY, 'Copy', wx.Bitmap('Meme_Studio_Icons/copy.png'))
        pastetool = toolbar.AddTool(wx.ID_ANY, 'Paste', wx.Bitmap('Meme_Studio_Icons/paste.png'))
        deselecttool = toolbar.AddTool(wx.ID_ANY, 'Deselect', wx.Bitmap('Meme_Studio_Icons/deselect.png'))
        toolbar.Realize()

        # these are our menu tabs in our menu bar
        menuFile = wx.Menu()
        menuEdit = wx.Menu()
        menuTools = wx.Menu()
        menuWindow = wx.Menu()
        menuSelect = wx.Menu()
        menuHelp = wx.Menu()

        themenubar.Append(menuFile, '&File')
        themenubar.Append(menuEdit, '&Edit')
        themenubar.Append(menuTools, '&Tools')
        themenubar.Append(menuWindow, '&Window')
        themenubar.Append(menuSelect, '&Select')
        themenubar.Append(menuHelp, '&Help')

        # submenu option for file tab
        fileQuit = menuFile.Append(wx.ID_ANY, 'Quit', 'Quit Option')
        fileOpen = menuFile.Append(wx.ID_ANY, 'Open file', 'Open File Option')
        fileSave = menuFile.Append(wx.ID_EXIT, 'Save file', 'Save File Option')
        fileSaveAs = menuFile.Append(wx.ID_EXIT, 'Save file as...', 'Saving File As Option')
        fileExport = menuFile.Append(wx.ID_EXIT, 'Export...', 'Export Option')
        
        #toolItem = menuTools.Append(wx.ID_ANY, 'Show Tools', 'Shows Tools Application')

        self.toolItem = menuTools.Append(wx.ID_ANY, 'Show tools',
                                        'Show Tool window', kind=wx.ITEM_CHECK)
        menuTools.Check(self.toolItem.GetId(), True)

        
        self.tools = ToolFrame(self, "Tools Window")
        self.tools.Show()

        # these are our binds for menubar and toolbar methods
        # Note that all are set to quit the program until
        # actual functions are implemented
        self.SetMenuBar(themenubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileQuit)
        self.Bind(wx.EVT_MENU, self.onFileSearch, fileOpen)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, fileSaveAs)
        self.Bind(wx.EVT_MENU, self.toggleTools, self.toolItem)

        self.Bind(wx.EVT_TOOL, self.OnSaveAs, savetool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, undotool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, redotool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, cuttool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, copytool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, pastetool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, deselecttool)



        # this is the size of our window, title, etc
        self.SetSize((400, 300))
        self.SetTitle('Meme Studio (Main Frame)')
        self.Centre()


        # just testing to see if I can open a new window
        # test = ImageWindow(300, 300)

    # function for quitting our application, under the file menu tab (?)
    def OnQuit(self, e):
        self.Close()
    
    def OnSaveAs(self, event):

        if WINDOWS != []:
            file_dialog = wx.FileDialog(self, "Save XYZ file", wildcard="PNG files (*.png)|*.png", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                print("User decided on not saving after all")
                return     # the user changed their mind

        # save the current contents in the file
            print(file_dialog.GetPath())
            pathname = file_dialog.GetPath()
            print("Saving to:" + pathname)
            file_dialog.Destroy()
            io.write_Image(pathname, WINDOWS[-1].get_bitmap())
            

    #responsible for the searching of files/images to open, currently only supports png
    def onFileSearch(self, e):

        wildcard = "PNG files (*.png)|*.png"
        dialog = wx.FileDialog(None, "Choose a file", wildcard=wildcard, style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
        
            filepath = dialog.GetPath()
            dialog.Destroy()
            if filepath != '' or filepath != "":

                #Create image given the filepath
                img2 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)

                #Get the bit map of the image
                imageBitmap = wx.Bitmap(img2)
                #wx.BitmapFromImage(img2)

                #Get Size of the image to shape the image window size
                width = img2.GetWidth()
                height = img2.GetHeight()

                #Create image window with the bitmap
                WINDOWS.append(ImageWindow(width, height, imageBitmap))

    def toggleTools(self, e):
        if self.toolItem.IsChecked():
            self.tools = ToolFrame(self, "title")
            self.tools.Show()
        else:
            self.tools.Hide()

    # Here we will instantiate our Tools window
class ToolFrame(wx.Frame):
    def __init__(self, parent, title):
        #wx.Frame.__init__(self, parent=parent, title=title)
        super(ToolFrame, self).__init__(parent, title = title, size = (300, 200))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        p = wx.Panel(self)
        gs = wx.GridSizer(4, 4, 5, 5)

#        if WINDOWS != []:
            #Line of code to rotate something 25 degress
#            WINDOWS[0].update_bitmap(tools.rotate(WINDOWS[0].get_bitmap(), 25))

        rotateBtn = wx.Button(p, wx.ID_ANY, 'Rotate')
        gs.Add(rotateBtn, 0, wx.EXPAND)

        omegaRotateBtn = wx.Button(p, wx.ID_ANY, 'Omega')
        gs.Add(omegaRotateBtn, 0, wx.EXPAND)

        verticalFlipBtn = wx.Button(p, wx.ID_ANY, 'Verti-Flip')
        gs.Add(verticalFlipBtn, 0, wx.EXPAND)

        horizantalFlipBtn = wx.Button(p, wx.ID_ANY, 'Hori-Flip')
        gs.Add(horizantalFlipBtn, 0, wx.EXPAND)

        resizeBtn = wx.Button(p, wx.ID_ANY, 'Resize')
        gs.Add(resizeBtn, 0, wx.EXPAND)
        
        jpgBtn = wx.Button(p, wx.ID_ANY, 'To-JPG')
        gs.Add(jpgBtn, 0, wx.EXPAND)

     #   for i in range(1, 11):
      #      btn = "Btn" + str(i)
      #      gs.Add(wx.Button(p, label = btn), 0, wx.EXPAND)

        rotateBtn.Bind(wx.EVT_BUTTON, self.onRotate)
        omegaRotateBtn.Bind(wx.EVT_BUTTON, self.onOmegaRotate)
        verticalFlipBtn.Bind(wx.EVT_BUTTON, self.onVerticalFlip)
        horizantalFlipBtn.Bind(wx.EVT_BUTTON, self.onHorizantalFlip)
        resizeBtn.Bind(wx.EVT_BUTTON, self.onResize) 
        jpgBtn.Bind(wx.EVT_BUTTON, self.onJPG)       

        p.SetSizer(gs)

    def onRotate(self, e):
        if (WINDOWS != []):
            rotate=self.GetRotate()
            value=float(self.txt.GetValue())
            WINDOWS[-1].update_bitmap(tools.rotate(WINDOWS[-1].get_bitmap(), value))

    def onOmegaRotate(self, e):
        if (WINDOWS != []):
            self.GetRotate()
            value=int(self.txt.GetValue())
            WINDOWS[-1].update_bitmap(tools.omega_rotate(WINDOWS[-1].get_bitmap(), value))

    def onVerticalFlip(self, e):
        if (WINDOWS != []):
            WINDOWS[-1].update_bitmap(tools.flip_top_bottom(WINDOWS[-1].get_bitmap()))

    def onJPG(self, e):
        if (WINDOWS != []):
            WINDOWS[-1].update_bitmap(tools.jpegify(WINDOWS[-1].get_bitmap()))
            
    def onHorizantalFlip(self, e):
        if (WINDOWS != []):
            WINDOWS[-1].update_bitmap(tools.flip_left_right(WINDOWS[-1].get_bitmap()))

    def onResize(self, e):
        if (WINDOWS != []):
            x=self.GetX()
            value=int(self.txt.GetValue())
            y=self.GetY()
            value2=int(self.txt2.GetValue())
            WINDOWS[-1].update_bitmap(tools.resize(WINDOWS[-1].get_bitmap(), value, value))
    
    def GetRotate(self):
        self.panel = wx.Panel(self)
        self.txt = wx.TextCtrl(self.panel, -1, size=(1,1))
        dlg = wx.TextEntryDialog(self.panel, 'Rotate by:',"", style=wx.OK)
        dlg.ShowModal()
        self.txt.SetValue(dlg.GetValue())
        dlg.Destroy()

    def GetX(self):
        self.panel = wx.Panel(self)
        self.txt = wx.TextCtrl(self.panel, -1, size=(1,1))
        dlg = wx.TextEntryDialog(self.panel, 'New width:',"", style=wx.OK)
        dlg.ShowModal()
        self.txt.SetValue(dlg.GetValue())
        dlg.Destroy()

    def GetY(self):
        self.panel = wx.Panel(self)
        self.txt2 = wx.TextCtrl(self.panel, -1, size=(1,1))
        dlg = wx.TextEntryDialog(self.panel, 'New Height:',"", style=wx.OK)
        dlg.ShowModal()
        self.txt2.SetValue(dlg.GetValue())
        dlg.Destroy()
        


    # this creates the 'canvas' in the actual application
class ToolPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.frame_number = 1

    def on_new_frame(self, event):
        title = 'Subframe {}'.format(self.frame_number)
        frame = ToolFrame(title=title)
        self.frame_number += 1

# We need a seprate window where we can display our image to the user
# Here's my attempt at making another window to do just that
class ImageWindow(wx.Frame):
 # Initiates with width, height, and the bitmap of image  


    def __init__(self, width, height, imgbitmap: wx.Bitmap):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Image Window")

        panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1)

        panel.SetupScrolling()
        imagebitmap = imgbitmap

        self.imageCtrl = wx.StaticBitmap(panel, wx.ID_ANY, 
                                         imagebitmap)

        
        
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        


        self.mainSizer.AddStretchSpacer()
        self.mainSizer.Add(self.imageCtrl, 0, wx.CENTER)
        self.mainSizer.AddStretchSpacer()
    

        panel.SetSizer(self.mainSizer)
        panel.SetBackgroundColour('#D3D3D3')

        self.SetSize(width, height)


        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_title)
        self.timer.Start(40)

        self.SetTitle("Image Layer")
        self.Show()

    def update_title(self, e):
        pos = self.imageCtrl.ScreenToClient(wx.GetMousePosition())
        self.SetTitle("Your mouse is at (%s,%s)" % (pos.x, pos.y))

    def update_bitmap(self, bitmap):
        self.imageCtrl.SetBitmap(bitmap)

    def get_bitmap(self):
        return self.imageCtrl.GetBitmap()

#    def OpenTools(self, e):
#        p = wx.Panel(self)
#        gs = wx.GridSizer(4, 4, 5, 5)
#
#        for i in range(1, 17):
#            btn = "Btn" + str(i)
#            gs.Add(wx.Button(p, label='stuff'), 0, wx.EXPAND)

#            p.SetSizer(gs) '''

# our main
def main():
    app = wx.App()
    memestudio = MemeStudioGUI(None)
    #memestudio.Show() Not really needed the init shows the frame
    app.MainLoop()

if __name__ == '__main__':
    # this is the image file browse function call
    main() 