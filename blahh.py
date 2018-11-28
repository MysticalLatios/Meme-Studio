import wx
class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.btn = wx.Button(self.panel, -1, "Name-a-matic")
        self.Bind(wx.EVT_BUTTON, self.GetName, self.btn)
        self.txt = wx.TextCtrl(self.panel, -1, size=(140,-1))
        self.txt.SetValue('name goes here')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn)
        sizer.Add(self.txt)

        self.panel.SetSizer(sizer)
        self.Show()

    def GetName(self, e):

        dlg = wx.TextEntryDialog(self.panel, 'Whats yo name?:',"name-o-rama","", 
                style=wx.OK)
        dlg.ShowModal()
        self.txt.SetValue(dlg.GetValue())
        dlg.Destroy()

    def OnCloseWindow(self, e):
        self.Destroy()

app = wx.App()
frame = Frame(None, 'My Nameomatic')
app.MainLoop()