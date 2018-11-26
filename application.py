#For launching the gui of the program
import wx
import sys
import os
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
        fileItem = menuFile.Append(wx.ID_EXIT, 'Quit', 'Quit Option')
        fileItem2 = menuFile.Append(wx.ID_EXIT, 'Open file', 'Open File Option')
        fileItem3 = menuFile.Append(wx.ID_EXIT, 'Save file', 'Save File Option')
        fileItem4 = menuFile.Append(wx.ID_EXIT, 'Save file as...', 'Saving File As Option')
        fileItem5 = menuFile.Append(wx.ID_EXIT, 'Export...', 'Export Option')
        toolItem = menuTools.Append(wx.ID_EXIT, 'Open Tools', 'Open Tools Application')

        # these are our binds for menubar and toolbar methods
        # Note that all are set to quit the program until
        # actual functions are implemented
        self.SetMenuBar(themenubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        self.Bind(wx.EVT_MENU, self.OnQuit, toolItem)
        self.Bind(wx.EVT_TOOL, self.OnQuit, savetool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, undotool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, redotool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, cuttool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, copytool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, pastetool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, deselecttool)


        # this is the size of our window, title, etc
        self.SetSize((1000, 800))
        self.SetTitle('Meme Studio (Main Frame)')
        self.Centre()

    # function for quitting our application, under the file menu tab (?)
    def OnQuit(self, e):
        self.Close()

    # Here we will instantiate our Tools window
class ToolFrame(wx.Frame):
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Show()

    # this creates the 'canvas' in the actual application
class ToolPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        btn = wx.Button(self, label = 'Tools Window')
        btn.Bind(wx.EVT_BUTTON, self.on_new_frame)
        self.frame_number = 1

    def on_new_frame(self, event):
        title = 'Subframe {}'.format(self.frame_number)
        frame = ToolFrame(title=title)
        self.frame_number += 1

# this is the class for our image browsing window
# NOTE: this opens a separate window for the browse
# will find a way to have it be called upon when
# the MenuBar file --> Open File is selected
class ImageBrowse(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='Browse for Image')

        self.panel = wx.Panel(self.frame)

        self.PhotoMaxSize = 480

        self.createBrowse()
        self.frame.Show()
    
    def createBrowse(self):
        self.photoTxt = wx.TextCtrl(self.panel, size=(200, -1))
        browseBtn = wx.Button(self.panel, label='Browse')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY), 
                            0, wx.ALL|wx.EXPAND, 5)

        self.sizer.Add(self.photoTxt, 0, wx.ALL, 5)
        self.sizer.Add(browseBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)

        self.panel.Layout()

    def onBrowse(self, event):
        wildcard = "PNG files (*.png)|*.png"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN)

        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()

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
    memestudio.Show()
    app.MainLoop()

if __name__ == '__main__':
    # this is the image file browse function call
    app = ImageBrowse()
    main() 