﻿# plugins/OSM/__init__.py
#
# Copyright (C)  2009 Pako  (lubos.ruckl@quick.cz)
#
# This file is a plugin for EventGhost.
#
# EventGhost is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# EventGhost is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EventGhost; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#Last change: 2010-02-12 09:35 GMT+1


eg.RegisterPlugin(
    name = "OS Menu",
    author = "Pako",
    version = "0.1.14",
    kind = "other",
    guid = "{FCF3C7A7-FBC1-444D-B768-9477521946DC}",
    description = u"""<rst>
Allows you to create custom On Screen Menu.
        
Plugin OSM has built-in a function **"Stop processing this event"**,
if the menu is shown on the screen. This facilitates
the use of OSM in your configuration. You can use to control
the menu the same events (the same remote buttons)
as elsewhere in the configuration, without having
to explicitly use the **"Stop processing this event"**,
**"Disable an item"** or **"Exclusive enable a folder / macro"**.
Only it is necessary to place the folder with the OSM as high
as possible in the configuration tree.""",
    createMacrosOnAdd = True,
    url = "http://www.eventghost.org/forum/viewtopic.php?f=9&t=1051",
    icon = (
        "iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAMAAACelLz8AAADAFBMVEX/////9/f/goL/"
        "z8//x8f//v7/2dn/Kir/gID/c3P/5ub/vb3/TU3/QED/ysr/oqL/7Oz/3t7/rq7/hob/"
        "t7f/qKj/k5P/a2v/hYX/d3f/T0//WVn/NDT/7u7/MTH/vLz/MzP/+fn/0ND/ZGT/tbX/"
        "nJz/LS3/UlL/l5f/wsL/mZn/Skr/8PD/Vlb/qqr/pqb/fn7/wMD/ior/YmL/4uL/kZH/"
        "enr/0dH/b2//Rkb/4OD/aGj/6ur/6Oj/MDD/Pz//Pj7/Ly//Nzf/5OT/cXH/QkL/yMj/"
        "srL/W1v/1dX/rKz/iYn/29v/dnb/ubn/PDz/j4//np7/dHT/e3v/qan/09P/o6P/r6//"
        "ZWX/19f/ODj/Q0P/8fEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABoAABoAAFAY"
        "AAEaAAAAACgAABoAABoYAAEAAAAACCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        "AAAAAPAAASf/////9/fP/4LHx////v4q/9mAgP//c3O9/+ZNTf//QECi/8rs7P//3t6G"
        "/663t///qKhr/5OFhf//d3dZ/080NP//7u68/zEzM///+flk/9C1tf//nJxS/y2Xl///"
        "wsJK/5nw8P//Vlam/6p+fv//wMBi/4ri4v//kZHR/3pvb///RkZo/+Dq6v//6Og//zA+"
        "Pv//Ly/k/zdxcf//QkKy/8hbW///1dWJ/6zb2///dnY8/7mPj///np57/3Spqf//09Ov"
        "/6NlZf//19dD/zjx8f8AAAAABWgAABfHxtwAEQTHyQAAAGjHzBjHzBgAAFxuZVJpcmUu"
        "LmcAABwAAENCblQAAABBmj0AAAAAAAAAAAAAAAAAAAABAAFCadPG/kwAAADabVLsAAAA"
        "AXRSTlMAQObYZgAAAAlwSFlzAAALEgAACxIB0t1+/AAAAThJREFUeNp9kudWAjEQRkcQ"
        "BxSkWSgKVlAXBFQUVBTF3ju2938O55sJ7i/NOZvcL3fPTrIJ0b9tKIAWtDCsIeTUCKOF"
        "LUQ0jDo1pilqIaZh3Km4Jk6Ak8Ypp9IWJ8CTxlNOTVvM+KU461TOYs4vxXmnZizy7G8p"
        "jplJgAvyFK3UHPK8qgXgojxpKwXkpKol4HKJuaylCivIq6rWgEWPuVRBqeo6ck1VHRjM"
        "StfAbEZ/zoaqTeAWZpvb2PkOcktVW1e0K91eVLr9DnIZJnQgdEjUZe4eMXs2cQzVw0tV"
        "ohPbbJ3oFGNF1Jn7dM3UOdEFxktRV4BrohtTHaJbjHeimoC4wD2gLfAAeBR4GrzTAjwL"
        "vAACAnnAq8AboC/QALyTLtoO/wPQG1wjT26aHonu/ZP5C+O3P/VH+wFJCR8UaaZiYgAA"
        "AABJRU5ErkJggg=="
    ),
)

from threading import Timer
from eg.WinApi.Utils import GetMonitorDimensions
from eg.WinApi.Dynamic import CreateEvent, SetEvent
#===============================================================================

class Text:
    picker = "Colour Picker"
    showMenu = u'''<rst>The selected monitor shows the menu, created by user.

*Basic rules for the compilation of event string:*

1) Join **Front of event string** and **Back part(s) of event string**
2) If the string contains more than three parts, truncated to three parts.
3) Truncating is performed by slicing the front parts
4) The third part is applied either as a suffix or as a payload

Some examples of event string compilation in mode **"suffix"**:

+-----------------------+--------------+------------------------+
| Front of event string | Back part(s) | Resulting event string |
+=======================+==============+========================+
|         OSM           | test         | **OSM.test**           |
+-----------------------+--------------+------------------------+
|         OSM.Main      | test         | **OSM.Main.test**      |
+-----------------------+--------------+------------------------+
|         OSM           | Second.Third | **OSM.Second.Third**   |
+-----------------------+--------------+------------------------+
|         OSM.Main      | OnInit.dummy | **Main.OnInit.dummy**  |
+-----------------------+--------------+------------------------+

Some examples of event string compilation in mode **"payload"**:

+-----------------------+--------------+--------------------------+
| Front of event string | Back part(s) | Resulting event string   |
+=======================+==============+==========================+
|         OSM           | test         | **OSM.test**             |
+-----------------------+--------------+--------------------------+
|         OSM.Main      | test         | **OSM.Main u"test"**     |
+-----------------------+--------------+--------------------------+
|         OSM           | Second.Third | **OSM.Second u"Third"**  |
+-----------------------+--------------+--------------------------+
|         OSM.Main      | OnInit.dummy | **Main.OnInit u"dummy"** |
+-----------------------+--------------+--------------------------+

'''

       
    showMenuExpr = u'''<rst>The selected monitor shows the menu, created from python expression.
    
This action is almost identical with the action **"Show menu"**. Different is just
a way of creating menu. Here is a menu defined by using python expression. This
expression you enter in the edit box **"List of menu items:"**. He may contain also
variables (eg **eg.result** or **eg.event.payload**).

There are two options for the tuple (list) format choice:
    
1) It may be simple, such as **( "Item1", "Item2", "Item3")**. In this case, each
list item also used as a label in the menu and as part of the resulting event
(along with a contents of text box **"Front of event string:"**)

2) Tuple (list) can contain nested tuples (lists). Therefore looks eg like this:
**(( "Item1", "event1"), ( "Item2", "event2"), ( "Item3", "event3"))**.
In this case, the first items of nested lists apply as a label in the menu and
the seconds items are applied as **"Back part(s) of event string"** (see the edit box
**"Back part(s) of event string:"** in configuration dialog of action **"Show menu"**).

3) Both the previous form can be freely combined. Tuple (list) can look as follows: 
**(("Item1","event1"), ("Item2"), ("Item3","event3"))**

Please see the description of the action **"Show menu"**. There are examples,
which naturally also applies to this action.'''
#===============================================================================

newEVT_BUTTON_AFTER = wx.NewEventType()
EVT_BUTTON_AFTER = wx.PyEventBinder(newEVT_BUTTON_AFTER, 1)


class EventAfter(wx.PyCommandEvent):

    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        self.myVal = None
        
    def SetValue(self, val):
        self.myVal = val

    def GetValue(self):
        return self.myVal
#===============================================================================
        
class extColourSelectButton(eg.ColourSelectButton):

    def OnButton(self, event):
        colourData = wx.ColourData()
        colourData.SetChooseFull(True)
        colourData.SetColour(self.value)
        for i, colour in enumerate(eg.config.colourPickerCustomColours):
            colourData.SetCustomColour(i, colour)
        dialog = wx.ColourDialog(self.GetParent(), colourData)
        dialog.SetTitle(Text.picker)
        if dialog.ShowModal() == wx.ID_OK:
            colourData = dialog.GetColourData()
            self.SetValue(colourData.GetColour().Get())
            event.Skip()
        eg.config.colourPickerCustomColours = [
            colourData.GetCustomColour(i).Get() for i in range(16)
        ]
        dialog.Destroy()
        evt = EventAfter(newEVT_BUTTON_AFTER, self.GetId())
        evt.SetValue(self.GetValue())
        self.GetEventHandler().ProcessEvent(evt)
#===============================================================================

class extFontSelectButton(eg.FontSelectButton):

    def OnButton(self, event):
        fontData = wx.FontData()
        if self.value is not None:
            font = wx.FontFromNativeInfoString(self.value)
            fontData.SetInitialFont(font)
        else:
            fontData.SetInitialFont(
                wx.SystemSettings_GetFont(wx.SYS_ANSI_VAR_FONT)
            )
        dialog = wx.FontDialog(self.GetParent(), fontData)
        if dialog.ShowModal() == wx.ID_OK:
            fontData = dialog.GetFontData()
            font = fontData.GetChosenFont()
            self.value = font.GetNativeFontInfo().ToString()
            event.Skip()
        dialog.Destroy()
        evt = EventAfter(newEVT_BUTTON_AFTER, self.GetId())
        evt.SetValue(self.GetValue())
        self.GetEventHandler().ProcessEvent(evt)

#===============================================================================
#cls types for ACTIONS list :
#===============================================================================

class ShowMenu(eg.ActionClass):
    panel = None

    class text:
        label = 'Label:'
        evtString = 'Back part(s) of event string:'
        osmLabel = 'OSM show on:'
        menuPreview = 'On screen menu preview:'
        delete = 'Delete'
        insert = 'Insert new'
        menuFont = 'Menu font:'
        txtColour = 'Text colour'
        background = 'Background colour'
        prefixLabel = 'Front of event string:'
        modeLabel = "The third part applied as:"
        mode = ("event suffix", "event payload")
        toolTip_1 = '''If the string contains a dot, will be first part used as
                    a event prefix (instead default prefix)'''


    def Move(self,index,direction):
        tmpList=self.choices[:]
        max = len(self.choices)-1
        #Last to first position, other down
        if index == max and direction == 1:
            tmpList[1:] = self.choices[:-1]
            tmpList[0] = self.choices[max]
            index2 = 0
        #First to last position, other up
        elif index == 0 and direction == -1:
            tmpList[:-1] = self.choices[1:]
            tmpList[max] = self.choices[0]
            index2 = max
        else:
            index2 = index+direction
            tmpList[index] = self.choices[index2]
            tmpList[index2] = self.choices[index]
        self.choices=tmpList
        return index2
#-------------------------------------------------------------------------------

    def __call__(
        self,
        choices,
        fore,
        back,
        fontInfo,
        prefix,
        monitor = 0,
        mode = 0
    ):
        if not self.plugin.menuDlg:
            self.plugin.choices = choices
            self.plugin.menuDlg = Menu()
            self.event = CreateEvent(None, 0, 0, None)
            wx.CallAfter(self.plugin.menuDlg.ShowMenu,
                fore,
                back,
                fontInfo,
                False,
                self.plugin,
                self.event,
                eg.ParseString(prefix),
                monitor,
                mode
            )
            eg.actionThread.WaitOnEvent(self.event)
#-------------------------------------------------------------------------------

    def GetLabel(
        self,
        choices,
        fore,
        back,
        fontInfo,
        prefix,
        monitor,
        mode
    ):
        res=self.text.showMenu+' '
        for n in range(0,min(3,len(choices))):
            res=res+choices[n][0]+', '
        res = res[:-2]
        if len(choices) > 3:
            res += ', ...'
        return res

    def Configure(
        self,
        choices=[],
        fore = (0, 0, 0),
        back = (255, 255, 255),
        fontInfo = None,
        prefix = 'OSM',
        monitor = 0,
        mode = 0
    ):
        self.choices = choices[:]
        self.fore = fore
        self.back = back
        self.oldSel=0
        global panel
        panel = eg.ConfigPanel(self)
        mainSizer = panel.sizer
        topSizer=wx.BoxSizer(wx.HORIZONTAL)
        topMiddleSizer=wx.BoxSizer(wx.VERTICAL)
        topRightSizer=wx.BoxSizer(wx.VERTICAL)
        previewLbl=wx.StaticText(panel, -1, self.text.menuPreview)
        mainSizer.Add(previewLbl)
        mainSizer.Add(topSizer,0,wx.TOP,5)
        bottomSizer=wx.GridBagSizer(3, 0)
        mainSizer.Add(bottomSizer,0,wx.TOP,6)
        listBoxCtrl=wx.ListBox(
            panel,-1,
            size=wx.Size(178,120),
            style=wx.LB_SINGLE|wx.LB_NEEDED_SB
        )
        listBoxCtrl.SetBackgroundColour(self.back)
        listBoxCtrl.SetForegroundColour(self.fore)
        if fontInfo is None:
            font = listBoxCtrl.GetFont()
            font.SetPointSize(36)
            fontInfo = font.GetNativeFontInfoDesc()
        else:
            font = wx.FontFromNativeInfoString(fontInfo)
        for n in range(10,20):
            font.SetPointSize(n)
            listBoxCtrl.SetFont(font)
            if listBoxCtrl.GetTextExtent('X')[1]>20:
                break
        topSizer.Add(listBoxCtrl)
        topSizer.Add((20,1))
        topSizer.Add(topMiddleSizer)
        topSizer.Add((30,1))
        topSizer.Add(topRightSizer)
        labelLbl=wx.StaticText(panel, -1, self.text.label)
        labelCtrl=wx.TextCtrl(panel,-1,'',size=wx.Size(180,-1))
        eventLbl=wx.StaticText(panel, -1, self.text.evtString)
        eventLbl.SetToolTipString(self.text.toolTip_1)
        eventCtrl = wx.TextCtrl(panel,-1,'',size=wx.Size(180,-1))
        eventCtrl.SetToolTipString(self.text.toolTip_1)
        prefixLbl=wx.StaticText(panel, -1, self.text.prefixLabel)
        prefixCtrl = wx.TextCtrl(panel,-1,prefix,size=wx.Size(96,-1))
        osmLbl = wx.StaticText(panel, -1, self.text.osmLabel)
        displayChoice = eg.DisplayChoice(panel, monitor)
        bottomSizer.Add((20,-1),(2, 2))
        bottomSizer.Add((20,-1),(2, 5))
        bottomSizer.Add(labelLbl,(0, 0),(1,1),flag = wx.TOP,border = 8)
        bottomSizer.Add(labelCtrl,(1, 0),(1,2),wx.EXPAND)
        bottomSizer.Add(prefixLbl,(0, 3),(1,1),flag = wx.TOP, border = 8)
        bottomSizer.Add(prefixCtrl,(1, 3),(1,2),flag = wx.EXPAND)
        bottomSizer.Add(eventLbl,(2, 0),(1,1),flag = wx.TOP,border = 8)
        bottomSizer.Add(eventCtrl,(3, 0),(1,2),flag = wx.EXPAND)
        bottomSizer.Add(osmLbl,(2, 6),(1,1),flag = wx.TOP, border = 8)
        bottomSizer.Add(displayChoice,(3, 6),(1,2),flag = wx.EXPAND)
        #Button UP
        bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_OTHER, (16, 16))
        btnUP = wx.BitmapButton(panel, -1, bmp)
        btnUP.Enable(False)
        topMiddleSizer.Add(btnUP)
        #Button DOWN
        bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_DOWN, wx.ART_OTHER, (16, 16))
        btnDOWN = wx.BitmapButton(panel, -1, bmp)
        btnDOWN.Enable(False)
        topMiddleSizer.Add(btnDOWN,0,wx.TOP,5)
        #Buttons 'Delete' and 'Insert new'
        w1 = panel.GetTextExtent(self.text.delete)[0]
        w2 = panel.GetTextExtent(self.text.insert)[0]
        if w1 > w2:
            btnDEL=wx.Button(panel,-1,self.text.delete)
            btnApp=wx.Button(panel,-1,self.text.insert,size=btnDEL.GetSize())
        else:
            btnApp=wx.Button(panel,-1,self.text.insert)
            btnDEL=wx.Button(panel,-1,self.text.delete,size=btnApp.GetSize())
        btnDEL.Enable(False)
        topMiddleSizer.Add(btnDEL,0,wx.TOP,12)
        topMiddleSizer.Add(btnApp,0,wx.TOP,9)
        #Font button
        fontLbl=wx.StaticText(panel, -1, self.text.menuFont)
        fontButton = extFontSelectButton(panel, value = fontInfo)
        topRightSizer.Add(fontLbl,0,wx.TOP,-15)
        topRightSizer.Add(fontButton,0,wx.TOP,2)
        #Button Text Colour
        foreLbl=wx.StaticText(panel, -1, self.text.txtColour+':')
        foreColourButton = extColourSelectButton(panel,fore)
        topRightSizer.Add(foreLbl,0,wx.TOP,10)
        topRightSizer.Add(foreColourButton,0,wx.TOP,2)
        #Button Background Colour
        backLbl=wx.StaticText(panel, -1, self.text.background+':')
        backColourButton = extColourSelectButton(panel,back)
        topRightSizer.Add(backLbl,0,wx.TOP,10)
        topRightSizer.Add(backColourButton,0,wx.TOP,2)
        modeLbl = wx.StaticText(panel, -1, self.text.modeLabel)
        modeCtrl = wx.Choice(
            panel,
            -1,
            choices = self.text.mode
        )
        bottomSizer.Add(modeLbl,(2, 3),(1, 1),flag = wx.TOP,border = 8)
        bottomSizer.Add(modeCtrl,(3, 3),(1, 2),flag = wx.EXPAND)
        modeCtrl.SetSelection(mode)

        def OnFontBtn(evt):
            value = evt.GetValue()
            font = wx.FontFromNativeInfoString(value)
            for n in range(10,20):
                font.SetPointSize(n)
                listBoxCtrl.SetFont(font)
                if listBoxCtrl.GetTextExtent('X')[1]>20:
                    break            
            evt.Skip()
        fontButton.Bind(EVT_BUTTON_AFTER, OnFontBtn)        

        def OnColourBtn(evt):
            id = evt.GetId()
            value = evt.GetValue()
            if id == foreColourButton.GetId():
                listBoxCtrl.SetForegroundColour(value)
            elif id == backColourButton.GetId():
                listBoxCtrl.SetBackgroundColour(value)
            listBoxCtrl.Refresh()
            evt.Skip()
        foreColourButton.Bind(EVT_BUTTON_AFTER, OnColourBtn)
        backColourButton.Bind(EVT_BUTTON_AFTER, OnColourBtn)

        def OnClick(evt):
            sel = listBoxCtrl.GetSelection()
            label = labelCtrl.GetValue()
            event = eventCtrl.GetValue()
            if label.strip()<>"":
                if [item[0] for item in self.choices].count(label)==1:
                    self.oldSel=sel
                    item = self.choices[sel]
                    labelCtrl.SetValue(item[0])
                    eventCtrl.SetValue(item[1])
            listBoxCtrl.SetSelection(self.oldSel)
            listBoxCtrl.SetFocus()
            evt.Skip()
        listBoxCtrl.Bind(wx.EVT_LISTBOX, OnClick)


        def OnButtonUp(evt):
            newSel=self.Move(listBoxCtrl.GetSelection(),-1)
            listBoxCtrl.Set([item[0] for item in self.choices])
            listBoxCtrl.SetSelection(newSel)
            self.oldSel = newSel
            evt.Skip()
        btnUP.Bind(wx.EVT_BUTTON, OnButtonUp)


        def OnButtonDown(evt):
            newSel=self.Move(listBoxCtrl.GetSelection(),1)
            listBoxCtrl.Set([item[0] for item in self.choices])
            listBoxCtrl.SetSelection(newSel)
            self.oldSel = newSel
            evt.Skip()
        btnDOWN.Bind(wx.EVT_BUTTON, OnButtonDown)


        def OnButtonDelete(evt):
            lngth=len(self.choices)
            if lngth==2:
                btnUP.Enable(False)
                btnDOWN.Enable(False)
            sel = listBoxCtrl.GetSelection()
            if lngth == 1:
                self.choices=[]
                listBoxCtrl.Set([])
                labelCtrl.SetValue('')
                eventCtrl.SetValue('')
                labelCtrl.Enable(False)
                labelLbl.Enable(False)
                eventCtrl.Enable(False)
                eventLbl.Enable(False)
                panel.EnableButtons(False)
                btnDEL.Enable(False)
                btnApp.Enable(True)
                evt.Skip()
                return
            elif sel == lngth - 1:
                sel = 0
            self.oldSel = sel
            tmp = self.choices.pop(listBoxCtrl.GetSelection())
            listBoxCtrl.Set([item[0] for item in self.choices])
            listBoxCtrl.SetSelection(sel)
            item = self.choices[sel]
            labelCtrl.SetValue(item[0])
            eventCtrl.SetValue(item[1])
            evt.Skip()
        btnDEL.Bind(wx.EVT_BUTTON, OnButtonDelete)
        if len(self.choices) > 0:
            listBoxCtrl.Set([item[0] for item in self.choices])
            listBoxCtrl.SetSelection(0)
            labelCtrl.SetValue(self.choices[0][0])
            eventCtrl.SetValue(self.choices[0][1])
            self.oldSel=0
            btnUP.Enable(True)
            btnDOWN.Enable(True)
            btnDEL.Enable(True)
        else:
            labelCtrl.Enable(False)
            labelLbl.Enable(False)
            eventCtrl.Enable(False)
            eventLbl.Enable(False)
            panel.EnableButtons(False)
        panel.sizer.Layout()


        def OnTextChange(evt):
            if self.choices<>[]:
                flag = False
                sel = self.oldSel
                label = labelCtrl.GetValue()
                event = eventCtrl.GetValue()
                self.choices[sel]=(label,event)
                listBoxCtrl.Set([item[0] for item in self.choices])
                listBoxCtrl.SetSelection(sel)
                if label.strip()<>"":
                    if event.strip()<>"":
                        if [item[0] for item in self.choices].count(label)==1:
                            flag = True
                panel.EnableButtons(flag)
                btnApp.Enable(flag)
            evt.Skip()
        labelCtrl.Bind(wx.EVT_TEXT, OnTextChange)
        eventCtrl.Bind(wx.EVT_TEXT, OnTextChange)


        def OnButtonAppend(evt):
            if len(self.choices)==1:
                btnUP.Enable(True)
                btnDOWN.Enable(True)
            labelCtrl.Enable(True)
            labelLbl.Enable(True)
            eventCtrl.Enable(True)
            eventLbl.Enable(True)
            sel = listBoxCtrl.GetSelection() + 1
            self.oldSel=sel
            self.choices.insert(sel,('',''))
            listBoxCtrl.Set([item[0] for item in self.choices])
            listBoxCtrl.SetSelection(sel)
            labelCtrl.SetValue('')
            labelCtrl.SetFocus()
            eventCtrl.SetValue('')
            btnApp.Enable(False)
            btnDEL.Enable(True)
            evt.Skip()
        btnApp.Bind(wx.EVT_BUTTON, OnButtonAppend)

        # re-assign the test button
        def OnButton(event):
            if not self.plugin.menuDlg:
                self.plugin.choices = self.choices
                self.plugin.menuDlg = Menu()
                self.event = CreateEvent(None, 0, 0, None)
                wx.CallAfter(self.plugin.menuDlg.ShowMenu,
                    foreColourButton.GetValue(),
                    backColourButton.GetValue(),
                    fontButton.GetValue(), 
                    True,
                    self.plugin,
                    self.event,
                    prefixCtrl.GetValue(),
                    displayChoice.GetSelection(),
                    modeCtrl.GetSelection()
                )
                eg.actionThread.WaitOnEvent(self.event)
        panel.dialog.buttonRow.testButton.Bind(wx.EVT_BUTTON, OnButton)

        while panel.Affirmed():
            panel.SetResult(
            self.choices,
            foreColourButton.GetValue(),
            backColourButton.GetValue(),
            fontButton.GetValue(),
            prefixCtrl.GetValue(),
            displayChoice.GetSelection(),
            modeCtrl.GetSelection()
        )
#===============================================================================
class CreateMenuFromList(eg.ActionClass):
    panel = None

    class text:
        label = 'List of menu items:'
        osmLabel = 'OSM show on:'
        menuPreview = 'On screen menu preview:'
        menuFont = 'Menu font:'
        txtColour = 'Text colour'
        background = 'Background colour'
        prefixLabel = 'Front of event string:'
        modeLabel = "The third part applied as:"
        mode = ("event suffix", "event payload")
        toolTip_1 = 'If the string contains a dot, will be first part used as\
                    a event prefix (instead default prefix)'


    def __call__(
        self,
        choices,
        fore,
        back,
        fontInfo,
        prefix,
        monitor=0,
        mode = 0
    ):
   
        if not self.plugin.menuDlg:
            try:
                lst = eg.ParseString(choices)
                lst =  eval(lst)
            except:
                return
            choices = []
            for item in lst:
                if type(item) is unicode or type(item) is str:
                    choices.append((item, item))
                elif type(item) is tuple or type(item) is list:
                    if len(item) == 1:
                        choices.append((item[0], item[0]))
                    else:
                        choices.append(item)
            self.plugin.choices = choices                
            self.plugin.menuDlg = Menu()
            self.event = CreateEvent(None, 0, 0, None)
            wx.CallAfter(self.plugin.menuDlg.ShowMenu,
                fore,
                back,
                fontInfo,
                False,
                self.plugin,
                self.event,
                eg.ParseString(prefix),
                monitor,
                mode
            )
            eg.actionThread.WaitOnEvent(self.event)
#-------------------------------------------------------------------------------

    def GetLabel(
        self,
        choices,
        fore,
        back,
        fontInfo,
        prefix,
        monitor,
        mode
    ):
        res=self.text.showMenu+' '
        for n in range(0,min(3,len(choices))):
            res=res+choices[n][0]+', '
        res = res[:-2]
        if len(choices) > 3:
            res += ', ...'
        return res

    def Configure(
        self,
        choices="",
        fore = (0, 0, 0),
        back = (255, 255, 255),
        fontInfo = None,
        prefix = 'OSM',
        monitor = 0,
        mode = 0
    ):
        self.fore = fore
        self.back = back
        self.oldSel=0
        global panel
        panel = eg.ConfigPanel(self)
        mainSizer = panel.sizer
        topSizer=wx.BoxSizer(wx.HORIZONTAL)
        topRightSizer=wx.BoxSizer(wx.VERTICAL)
        previewLbl=wx.StaticText(panel, -1, self.text.menuPreview)
        mainSizer.Add(previewLbl)
        mainSizer.Add(topSizer,0,wx.TOP,5)
        bottomSizer=wx.GridBagSizer(2, 0)
        mainSizer.Add(bottomSizer,0,wx.TOP,6)
        listBoxCtrl=wx.ListBox(
            panel,-1,
            size=wx.Size(240,120),
            style=wx.LB_SINGLE|wx.LB_NEEDED_SB
        )
        listBoxCtrl.SetBackgroundColour(self.back)
        listBoxCtrl.SetForegroundColour(self.fore)
        if fontInfo is None:
            font = listBoxCtrl.GetFont()
            font.SetPointSize(36)
            fontInfo = font.GetNativeFontInfoDesc()
        else:
            font = wx.FontFromNativeInfoString(fontInfo)
        for n in range(10,20):
            font.SetPointSize(n)
            listBoxCtrl.SetFont(font)
            if listBoxCtrl.GetTextExtent('X')[1]>20:
                break
        topSizer.Add(listBoxCtrl)
        topSizer.Add((40,1))
        topSizer.Add(topRightSizer)
        listLbl=wx.StaticText(panel, -1, self.text.label)
        #listCtrl=wx.TextCtrl(panel,-1,choices,size=wx.Size(405,-1))
        listCtrl=wx.TextCtrl(panel,-1,choices)
        listCtrl.SetToolTipString(self.text.toolTip_1)
        prefixLbl=wx.StaticText(panel, -1, self.text.prefixLabel)
        prefixCtrl = wx.TextCtrl(panel,-1,prefix,size=wx.Size(96,-1))
        osmLbl = wx.StaticText(panel, -1, self.text.osmLabel)
        displayChoice = eg.DisplayChoice(panel, monitor)
        
        bottomSizer.Add((30,-1),(2, 2))
        bottomSizer.Add((30,-1),(2, 5))

        bottomSizer.Add(listLbl,(0, 0), (1, 1),flag = wx.TOP,border = 8)
        bottomSizer.Add(listCtrl,(1, 0), (1, 8),flag = wx.EXPAND)

        bottomSizer.Add(prefixLbl,(2, 0), (1, 1),flag = wx.TOP, border = 8)
        bottomSizer.Add(prefixCtrl,(3, 0), (1, 2),flag = wx.EXPAND)
        
        bottomSizer.Add(osmLbl,(2, 6), (1, 1),flag = wx.TOP, border = 8)
        bottomSizer.Add(displayChoice, (3, 6),(1, 2),flag = wx.EXPAND)
        #Font button
        fontLbl=wx.StaticText(panel, -1, self.text.menuFont)
        fontButton = extFontSelectButton(panel, value = fontInfo)
        topRightSizer.Add(fontLbl,0,wx.TOP,-15)
        topRightSizer.Add(fontButton,0,wx.TOP,2)
        #Button Text Colour
        foreLbl=wx.StaticText(panel, -1, self.text.txtColour+':')
        foreColourButton = extColourSelectButton(panel,fore)
        topRightSizer.Add(foreLbl,0,wx.TOP,10)
        topRightSizer.Add(foreColourButton,0,wx.TOP,2)
        #Button Background Colour
        backLbl=wx.StaticText(panel, -1, self.text.background+':')
        backColourButton = extColourSelectButton(panel,back)
        topRightSizer.Add(backLbl,0,wx.TOP,10)
        topRightSizer.Add(backColourButton,0,wx.TOP,2)
        #mode choice
        modeLbl = wx.StaticText(panel, -1, self.text.modeLabel)
        modeCtrl = wx.Choice(
            panel,
            -1,
            choices = self.text.mode
        )
        bottomSizer.Add(modeLbl,(2, 3),(1, 1),flag = wx.TOP,border = 8)
        bottomSizer.Add(modeCtrl,(3, 3),(1, 2),flag = wx.EXPAND)
        modeCtrl.SetSelection(mode)

        def OnFontBtn(evt):
            value = evt.GetValue()
            font = wx.FontFromNativeInfoString(value)
            for n in range(10,20):
                font.SetPointSize(n)
                listBoxCtrl.SetFont(font)
                if listBoxCtrl.GetTextExtent('X')[1]>20:
                    break
            evt.Skip()
        fontButton.Bind(EVT_BUTTON_AFTER, OnFontBtn)        

        def OnColourBtn(evt):
            id = evt.GetId()
            value = evt.GetValue()
            if id == foreColourButton.GetId():
                listBoxCtrl.SetForegroundColour(value)
            elif id == backColourButton.GetId():
                listBoxCtrl.SetBackgroundColour(value)
            listBoxCtrl.Refresh()
            evt.Skip()
        foreColourButton.Bind(EVT_BUTTON_AFTER, OnColourBtn)
        backColourButton.Bind(EVT_BUTTON_AFTER, OnColourBtn)


        def OnTextChange(evt=None):
            try:
                lst = eg.ParseString(listCtrl.GetValue())
                lst =  eval(lst)
                if lst and len(lst) > 0:
                    self.choices = []
                    for item in lst:
                        if type(item) is unicode or type(item) is str:
                            self.choices.append((item, item))
                        elif type(item) is tuple or type(item) is list:
                            if len(item) == 1:
                                self.choices.append((item[0], item[0]))
                            else:
                                self.choices.append(item)
                    listBoxCtrl.Set([item[0] for item in self.choices])
                    self.plugin.choices = self.choices
            except:
                listBoxCtrl.Set([])
                lst = None
            if evt:
                evt.Skip()
        listCtrl.Bind(wx.EVT_TEXT, OnTextChange)
        OnTextChange()


        # re-assign the test button
        def OnButton(event):
            if not self.plugin.menuDlg:
                self.plugin.choices = self.choices
                self.plugin.menuDlg = Menu()
                self.event = CreateEvent(None, 0, 0, None)
                wx.CallAfter(self.plugin.menuDlg.ShowMenu,
                    foreColourButton.GetValue(),
                    backColourButton.GetValue(),
                    fontButton.GetValue(), 
                    True,
                    self.plugin,
                    self.event,
                    prefixCtrl.GetValue(),
                    displayChoice.GetSelection(),
                    modeCtrl.GetSelection()
                )
                eg.actionThread.WaitOnEvent(self.event)
        panel.dialog.buttonRow.testButton.Bind(wx.EVT_BUTTON, OnButton)

        while panel.Affirmed():
            panel.SetResult(
            listCtrl.GetValue(),
            foreColourButton.GetValue(),
            backColourButton.GetValue(),
            fontButton.GetValue(),
            prefixCtrl.GetValue(),
            displayChoice.GetSelection(),
            modeCtrl.GetSelection()
        )
#===============================================================================

class MoveCursor(eg.ActionClass):

    def __call__(self):
        if self.plugin.menuDlg:
            max=len(self.plugin.choices)
            if max > 0:
                sel=self.plugin.menuDlg.GetSizer().GetChildren()[0].\
                    GetWindow().GetSelection()
                if sel == eval(self.value[0]):
                    sel = eval(self.value[1])
                self.plugin.menuDlg.GetSizer().GetChildren()[0].GetWindow().\
                    SetSelection(sel+self.value[2])
            eg.event.skipEvent = True
#===============================================================================

class OK_Btn(eg.ActionClass):

    def __call__(self):
        if self.plugin.menuDlg:
            self.plugin.menuDlg.SendEvent()
            eg.event.skipEvent = True
#===============================================================================

class Num_Btn(eg.ActionClass):

    def __call__(self):
        if self.plugin.menuDlg:
            self.plugin.menuDlg.SendEventNum(self.value if self.value > 0 else 10)
            eg.event.skipEvent = True
#===============================================================================

class Cancel_Btn(eg.ActionClass):

    def __call__(self):
        if self.plugin.menuDlg:
            self.plugin.menuDlg.destroyMenu()
            eg.event.skipEvent = True
#===============================================================================

class Get_Btn (eg.ActionClass):
    class text:
        radiobox = 'Choice of menu attribute'
        boxLabel = 'Label'
        boxEvent = 'Event string'
        boxBoth  = 'Both'
        labelGet = 'Get'

    def __call__(self,val = 0):
        if self.plugin.menuDlg:
            eg.event.skipEvent = True
            sel = self.plugin.menuDlg.GetSizer().GetChildren()[0].GetWindow().\
                GetSelection()
            if val < 2:
                return self.plugin.choices[sel][val]
            else:
                return self.plugin.choices[sel]

    def GetLabel(self,val):
        LabelList = (self.text.boxLabel, self.text.boxEvent, self.text.boxBoth)
        return self.text.labelGet+' '+LabelList[val]

    def Configure(self, val=0):
        panel = eg.ConfigPanel(self)
        radioBoxItems = wx.RadioBox(
            panel,
            -1,
            self.text.radiobox,
            (0,0),
            (200,90),
            choices=[self.text.boxLabel, self.text.boxEvent,self.text.boxBoth],
            style=wx.RA_SPECIFY_ROWS
        )
        radioBoxItems.SetSelection(val)
        panel.AddCtrl(radioBoxItems)

        while panel.Affirmed():
            panel.SetResult(radioBoxItems.GetSelection())
#===============================================================================

ACTIONS = (
    (ShowMenu, 'ShowMenu', 'Show menu', Text.showMenu, None),
    (CreateMenuFromList, 'CreateMenuFromList', 'Show menu, created from expression', Text.showMenuExpr, None),
    (MoveCursor, 'MoveDown', 'Cursor Down', 'Cursor Down.', ('max-1', '-1', 1)),
    (MoveCursor, 'MoveUp', 'Cursor Up', 'Cursor Up.', ('0', 'max', -1)),
    (OK_Btn, 'OK_Btn', 'OK', 'OK button pressed.', None),
    (Cancel_Btn, 'Cancel_Btn', 'Cancel', 'Cancel button pressed.', None),
    ( eg.ActionGroup, 'HotKeys', 'Numeric Hot Keys', 'Numeric Hot Keys ',(
        (Num_Btn, 'Num_Btn_1', 'Button 1', 'Button 1 pressed.', 1),
        (Num_Btn, 'Num_Btn_2', 'Button 2', 'Button 2 pressed.', 2),
        (Num_Btn, 'Num_Btn_3', 'Button 3', 'Button 3 pressed.', 3),
        (Num_Btn, 'Num_Btn_4', 'Button 4', 'Button 4 pressed.', 4),
        (Num_Btn, 'Num_Btn_5', 'Button 5', 'Button 5 pressed.', 5),
        (Num_Btn, 'Num_Btn_6', 'Button 6', 'Button 6 pressed.', 6),
        (Num_Btn, 'Num_Btn_7', 'Button 7', 'Button 7 pressed.', 7),
        (Num_Btn, 'Num_Btn_8', 'Button 8', 'Button 8 pressed.', 8),
        (Num_Btn, 'Num_Btn_9', 'Button 9', 'Button 9 pressed.', 9),
        (Num_Btn, 'Num_Btn_0', 'Button 0', 'Button 0 pressed.', 0),
        )),
    (Get_Btn, 'Get_Btn', 'Get value', 'Get value of selected item.', None),
)
#===============================================================================

class OSM(eg.PluginClass):
    menuDlg = None
    choices = []

    def __init__(self):
        self.AddActionsFromList(ACTIONS)
#===============================================================================
            
class Menu(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(
            self,
            None,
            -1,
            'OS_Menu',
            style = wx.STAY_ON_TOP|wx.SIMPLE_BORDER
        )


    def ShowMenu(
        self,
        fore,
        back,
        fontInfo,
        flag,
        plugin,
        event,
        prefix,
        monitor,
        mode
    ):
        self.fore    = fore
        self.back    = back
        self.plugin  = plugin
        self.choices = self.plugin.choices
        self.flag    = flag
        self.prefix  = prefix
        self.mode    = mode
    
        monDim = GetMonitorDimensions()
        try:
            x,y,ws,hs = monDim[monitor]
        except IndexError:
            x,y,ws,hs = monDim[0]
        
        eventChoiceCtrl=wx.ListBox(
            self,
            choices = [item[0] for item in self.choices],
            style=wx.LB_SINGLE|wx.LB_NEEDED_SB
        )
        if fontInfo is None:
            font = eventChoiceCtrl.GetFont()
            font.SetPointSize(36)
            fontInfo = font.GetNativeFontInfoDesc()
        else:
            font = wx.FontFromNativeInfoString(fontInfo)
        eventChoiceCtrl.SetFont(font)
        # menu height calculation:
        h=eventChoiceCtrl.GetCharHeight()
        height0 = len(self.choices)*h+5
        height1 = h*((hs-20)/h)+5
        height = min(height0,height1)+6
        # menu width calculation:
        width_lst=[]
        for item in [item[0] for item in self.choices]:
            width_lst.append(eventChoiceCtrl.GetTextExtent(item+' ')[0])
        width = max(width_lst)+8
        if height-6<height0:
            width += 20 #for vertical scrollbar
        width = min((width,ws-50))+6
        #self.SetSize((width+6,height+6))
        x_pos = x+(ws-width)/2
        y_pos = y + (hs-height)/2
        self.SetDimensions(x_pos,y_pos,width,height)
        eventChoiceCtrl.SetDimensions(2,2,width-6,height-6,wx.SIZE_AUTO)
        mainSizer =wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(mainSizer)
        eventChoiceCtrl.SetSelection(0)
        self.SetBackgroundColour((0,0,0))
        eventChoiceCtrl.SetBackgroundColour(self.back)
        eventChoiceCtrl.SetForegroundColour(self.fore)
        mainSizer.Add(eventChoiceCtrl, 0, wx.EXPAND)
        
        self.Bind(wx.EVT_CLOSE, self.onClose)
        eventChoiceCtrl.Bind(wx.EVT_LISTBOX_DCLICK, self.SendEvent)
        
        if self.flag:
            self.timer=MyTimer(t = 5.0, plugin = self.plugin)
        
        self.Show(True)
        wx.Yield()
        SetEvent(event)
        
    def SendEventSel(self, sel):
        evtString = self.prefix.split(".")
        evtString.extend(self.choices[sel][1].split("."))
        evtString = evtString[-3:]
        if len(evtString) == 3:
            if self.mode:
                eg.TriggerEvent(evtString[1], prefix = evtString[0], payload = evtString[2])
            else:            
                eg.TriggerEvent(".".join(evtString[-2:]), prefix = evtString[0])                         
        elif len(evtString) == 2:
            eg.TriggerEvent(evtString[1], prefix = evtString[0])
        self.destroyMenu()

    def SendEvent(self, event = None):
        sel=self.GetSizer().GetChildren()[0].GetWindow().\
            GetSelection()
        self.SendEventSel(sel)

    def SendEventNum(self, num):
        if num <= len(self.choices):
            sel = num-1
            self.SendEventSel(sel)

    def onClose(self, event):
        self.Destroy()
        self.plugin.menuDlg = None
        
    def destroyMenu(self):
        if self.flag:
            self.timer.Cancel()
        self.plugin.choices = []
        self.Show(False)
        self.Close()
#===============================================================================

class MyTimer():
    def __init__(self, t, plugin):
        self.timer = Timer(t, self.Run)
        self.plugin = plugin
        self.timer.start()
                
    def Run(self):
        try:
            self.plugin.menuDlg.destroyMenu()
            self.plugin.menuDlg = None
        except:
            pass
            
    def Cancel(self):
        self.timer.cancel()
#===============================================================================
