# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Mar 13 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class mainWindow
###########################################################################

class mainWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"History Genius - Make History Automate Itself!", pos = wx.DefaultPosition, size = wx.Size( 1920,1040 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 1920,1040 ), wx.Size( 1920,1040 ) )

		self.m_toolBar3 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_buttonLoad = wx.Button( self.m_toolBar3, wx.ID_ANY, u"Load", wx.Point( -1,-1 ), wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB )
		self.m_buttonLoad.Enable( False )

		self.m_toolBar3.AddControl( self.m_buttonLoad )
		self.m_filePicker = wx.FilePickerCtrl( self.m_toolBar3, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 260,-1 ), wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST )
		self.m_filePicker.SetMaxSize( wx.Size( 1700,-1 ) )

		self.m_toolBar3.AddControl( self.m_filePicker )
		self.m_toolBar3.Realize()

		self.m_menubar = wx.MenuBar( 0 )
		self.m_menubar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )

		self.m_menuGenerate = wx.Menu()
		self.m_menuItemPieSiteCount = wx.MenuItem( self.m_menuGenerate, wx.ID_ANY, u"Pie Chart of Site Visits...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuGenerate.Append( self.m_menuItemPieSiteCount )

		self.m_menuItemBarChartTimeLine = wx.MenuItem( self.m_menuGenerate, wx.ID_ANY, u"Bar Chart of Time Line Activity...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuGenerate.Append( self.m_menuItemBarChartTimeLine )

		self.m_menubar.Append( self.m_menuGenerate, u"Generate" )

		self.SetMenuBar( self.m_menubar )

		bSizerList = wx.BoxSizer( wx.VERTICAL )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_gridList = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1920,965 ), 0 )

		# Grid
		self.m_gridList.CreateGrid( 0, 4 )
		self.m_gridList.EnableEditing( False )
		self.m_gridList.EnableGridLines( True )
		self.m_gridList.EnableDragGridSize( False )
		self.m_gridList.SetMargins( 0, 0 )

		# Columns
		self.m_gridList.SetColSize( 0, 171 )
		self.m_gridList.SetColSize( 1, 85 )
		self.m_gridList.SetColSize( 2, 65 )
		self.m_gridList.SetColSize( 3, 1500 )
		self.m_gridList.EnableDragColMove( False )
		self.m_gridList.EnableDragColSize( True )
		self.m_gridList.SetColLabelSize( 30 )
		self.m_gridList.SetColLabelValue( 0, u"Site" )
		self.m_gridList.SetColLabelValue( 1, u"Date" )
		self.m_gridList.SetColLabelValue( 2, u"Time" )
		self.m_gridList.SetColLabelValue( 3, u"Full URL" )
		self.m_gridList.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_gridList.EnableDragRowSize( True )
		self.m_gridList.SetRowLabelSize( 80 )
		self.m_gridList.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_gridList.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_gridList.SetMinSize( wx.Size( 1920,965 ) )
		self.m_gridList.SetMaxSize( wx.Size( 1920,965 ) )

		gbSizer1.Add( self.m_gridList, wx.GBPosition( 0, 0 ), wx.GBSpan( 2, 2 ), wx.ALL|wx.FIXED_MINSIZE, 0 )


		bSizerList.Add( gbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerList )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonLoad.Bind( wx.EVT_BUTTON, self.LoadChromeHistory )
		self.m_filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.CheckForPath )
		self.Bind( wx.EVT_MENU, self.OpenPieSiteCount, id = self.m_menuItemPieSiteCount.GetId() )
		self.Bind( wx.EVT_MENU, self.OpenTimeLineChart, id = self.m_menuItemBarChartTimeLine.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def LoadChromeHistory( self, event ):
		event.Skip()

	def CheckForPath( self, event ):
		event.Skip()

	def OpenPieSiteCount( self, event ):
		event.Skip()

	def OpenTimeLineChart( self, event ):
		event.Skip()


###########################################################################
## Class dialogPieSiteCount
###########################################################################

class dialogPieSiteCount ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generate a Pie Chart of Site Occurences", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 600,600 ), wx.Size( 600,600 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer2.SetMinSize( wx.Size( 600,600 ) )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer3.SetMinSize( wx.Size( 600,500 ) )
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Number of visits to be in other (smaller number makes pie chart harder to read)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrlOtherSites = wx.TextCtrl( self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrlOtherSites, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Filter List, add domains followed by a new line to filter them. (RESETS ON CLOSE)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrlFilterList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 580,400 ), wx.TE_MULTILINE )
		self.m_textCtrlFilterList.SetMinSize( wx.Size( 580,400 ) )
		self.m_textCtrlFilterList.SetMaxSize( wx.Size( 580,400 ) )

		bSizer3.Add( self.m_textCtrlFilterList, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.ALL, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buttonPieSiteCountGenerate = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_buttonPieSiteCountGenerate, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_checkBoxFilter = wx.CheckBox( self, wx.ID_ANY, u"Tick to remove filtered objects, un tick to remove anything NOT on list.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxFilter.SetValue(True)
		gbSizer2.Add( self.m_checkBoxFilter, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( gbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonPieSiteCountGenerate.Bind( wx.EVT_BUTTON, self.GeneratePieChart )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def GeneratePieChart( self, event ):
		event.Skip()


###########################################################################
## Class dialogTimeLineAnalysis
###########################################################################

class dialogTimeLineAnalysis ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generate a Time Line Analysis Acitivity Bar Chart", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 600,600 ), wx.Size( 600,600 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer2.SetMinSize( wx.Size( 600,600 ) )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer3.SetMinSize( wx.Size( 600,500 ) )
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Generate a timeline showing how many websites were visited during different times in total.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer5.SetMinSize( wx.Size( 600,100 ) )
		self.m_buttonTimeLineGenerate = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_buttonTimeLineGenerate, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer5, 1, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonTimeLineGenerate.Bind( wx.EVT_BUTTON, self.GenerateTimeLineChart )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def GenerateTimeLineChart( self, event ):
		event.Skip()


