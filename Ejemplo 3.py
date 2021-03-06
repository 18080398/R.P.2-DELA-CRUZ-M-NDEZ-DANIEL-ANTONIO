import wx
class MyApp(wx.App):
    def __init__(self):
        super().__init__()

    def OnInit(self):
        frame = MyFrame(parent=None, title="This is a frame")
        frame.Show()
        return True


class MyFrame(wx.Frame):
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can (usually) be changed by the user.
    # Usually represents the first/main window a user will see
    def __init__(self, parent, title):
        super().__init__(parent=parent, title=title, pos = (100, 100))

        self.OnInit()

    def OnInit(self):
        panel = MyPanel(self)


class MyPanel(wx.Panel):
    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self,parent):
        super().__init__(parent=parent)
        self._dont_show = False # for message dialog box
        
        # add a hello message to the panel
        welcomeText = wx.StaticText(self, label="hola joven programador!", pos=(20,20))

        # add a text box
        self._text = wx.TextCtrl(parent= self, value = 'Inserter el texto aqui', pos = (20,60), size=(300, 50))

        # add a button to bring up the dialog box
        self._button = wx.Button(parent=self, label='Enviar', pos = (20, 120))
        self._button.Bind(wx.EVT_BUTTON, self.onSubmit) # bind action to button


    def ShowDialog(self):
        # pop up a message dialog window on submit!
        if self._dont_show:
            return None

        dlg = wx.RichMessageDialog(parent=None, 
                message= "¿Estas listo para aprende la programacion en python?",
                caption="wxPythonStuff",
                style=wx.YES_NO|wx.CANCEL|wx.CENTRE)
        dlg.ShowCheckBox("no lo vuelvas a mostrar")
        dlg.ShowModal() # shows the dialog

        if dlg.IsCheckBoxChecked():
            print("¿esta marcado la casilla?", dlg.IsCheckBoxChecked())
            self._dont_show=True
    

    def onSubmit(self, event):
        # stuff for the submit button to do
        print(self._text.GetValue())
        self.ShowDialog()
        
if __name__ == "__main__":

    app = MyApp()
    frame = MyFrame(parent=None, title="Aprendiendo las ventanas")
    app.MainLoop()
    