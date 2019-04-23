import wx
from wxgui import *
import wxgui
import sqlite3
import datetime
import matplotlib.pyplot as plt
import numpy as np


###Main window GUI##############################################
class ApplicationWindow(wxgui.mainWindow):
  def __init__(self,parent):
    wxgui.mainWindow.__init__(self,parent)

  #check to update the load button when a file is loaded
  def CheckForPath(self,event):
    if self.m_filePicker.GetPath() != "":
      #some awful math to make the box size dependant on the length of the path to the file
      pathlength = int(len(self.m_filePicker.GetPath()) * 7) + 30
      if pathlength > 1700:
        pathlength = 1700
      self.m_filePicker.Size = (pathlength, -1)
      self.m_buttonLoad.Enable(True)
      global filePath
      filePath = self.m_filePicker.GetPath()

  #actually load the sqlitedatabase into the software    
  def LoadChromeHistory(self,event):
    self.m_buttonLoad.Enable(False)
    global filePath
    #connecting to sqlite3 database
    connecttosqlite = sqlite3.connect(filePath)
    sqlsession = connecttosqlite.cursor()
    
    #counting how long the database is
    for count in sqlsession.execute('SELECT count(*) FROM urls;'):
      databaselength = int(str(count).strip("(),"))
    #self. grid object. AppendRows ( number of rows to add or minus, update the labels of these )
    self.m_gridList.AppendRows(numRows=databaselength, updateLabels=True)
    
    #inputting the full url first
    placeinlist = 0
    for row in sqlsession.execute('SELECT url FROM urls ORDER BY last_visit_time;'):
      #self.grid object. set the cell. (ROW, COLUMN, VARIABLE)
      self.m_gridList.SetCellValue(placeinlist,3,row[0])
      #increase the place in the list
      placeinlist += 1
    
    #parsing the full URL to JUST the website name and not full url
    placeinlist = 0
    for row in sqlsession.execute('SELECT url FROM urls ORDER BY last_visit_time;'):
      data = str(row[0]) #collect the important part grabbed from sql command
      data = data.replace("http://","") #take away http://
      data = data.replace("https://","")#take away https://
      data = data.replace("www.","")    #take away www.
      data = str([parsed.split('/')[0] for parsed in data.split()])#attach everything before the first /
      #add this to the grid without the list container E.G ['facebook.com']
      self.m_gridList.SetCellValue(placeinlist,0,data[2:(len(data)-2)])
      placeinlist += 1

    #turn the ticks from the last_visit_time and put them in the list
    placeinlist = 0
    for row in sqlsession.execute('SELECT last_visit_time FROM urls ORDER BY last_visit_time;'):
      if row[0] == 0:
        #if the addition has no timestamp, it is a bookmark, so rather than a weird timestamp, just put bookmark
        
        self.m_gridList.SetCellValue(placeinlist,1,"bookmark")#place nothing in date
        self.m_gridList.SetCellValue(placeinlist,2,"bookmark")#place nothing in time
        
      elif row[0] != 0:
        #formatting the tick into a date and time
        row = str(datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds = row[0]) )
        row = row.split()
        #row[0:19] removes the decimal seconds, so it shows YEAR/MONTH/DAY HOUR/MINUTE/SEC(without decimal)
        self.m_gridList.SetCellValue(placeinlist,1,row[0])
        self.m_gridList.SetCellValue(placeinlist,2,row[1][0:8])
      placeinlist +=1

    #Removing bookmarks so they don't tamper with our data
    placeinlist = 0
    print("Removing bookmarks: ")
    #while our place in list hasn't gone past our length of our datalist
    while placeinlist < self.m_gridList.GetNumberRows():
      #if the row is a bookmark
      if self.m_gridList.GetCellValue(placeinlist,1) == "bookmark":
        print(self.m_gridList.GetCellValue(placeinlist,0))
        #remove it
        self.m_gridList.DeleteRows(placeinlist, 1, updateLabels=False)
      else:
        #if not, move on to the next place in the list
        placeinlist += 1
    print("Bookmarks removed! \n")
    sqlsession.close()
    connecttosqlite.close()
    print("Closed SQL Connection")


  ###Open the Pie Chart Generator##################
  def OpenPieSiteCount(self, event):
    dialogPieSiteCountWindow = PieSiteCountDialog(self,ApplicationWindow)
    dialogPieSiteCountWindow.Show()


  ###Open The Time Line Bar Chart Generator ######
  def OpenTimeLineChart(self, event):
    dialogTimeLineAnalysis = TimeLineAnalysisDialog(self,ApplicationWindow)
    dialogTimeLineAnalysis.Show()






###Dialog for generating a pie chart of common visited sites###
class PieSiteCountDialog(wxgui.dialogPieSiteCount):
  def __init__(self,parent,ApplicationWindow):
    wxgui.dialogPieSiteCount.__init__(self,parent)

  def GeneratePieChart(self, event):
    print("LOADING PIE CHART...")
    urllist = {}
    filterlist = []
    global filePath
    connecttosqlite = sqlite3.connect(filePath)
    sqlsession = connecttosqlite.cursor()
    for row in sqlsession.execute('SELECT url FROM urls ORDER BY last_visit_time;'):
      data = str(row[0]) #collect the important part grabbed from sql command
      data = data.replace("http://","") #take away http://
      data = data.replace("https://","")#take away https://
      data = data.replace("www.","")    #take away www.
      data = str([parsed.split('/')[0] for parsed in data.split()])#attach everything before the first /
      #add this to the grid without the list container E.G ['facebook.com']
      if data not in urllist:
        urllist[data] = 1 #if this item isn't already in our dictionary, add it and say it has been counted once
      else:
        urllist[data]+= 1 #if it has been added, plus 1 to its count
    print("URL LIST MADE")
    #Seperating our dictionary(urllist) into two lists!
    labels = []#making a list of urls
    count = []#making a list of how many times they come up
    for item in urllist.keys():
      labels.append(item.strip("[]'"))#removing unnecessary brackets
    for item in urllist.values():
      count.append(item)
    labels.append("other")#adding the 'other' to the list for 'one visit' sites
    count.append(0)#adding other's count as zero
    placeinlist = 0#start at the start of the list
    while placeinlist < len(labels): #whilst we're not at the end of the list
      if count[placeinlist] < int(self.m_textCtrlOtherSites.GetValue()): #if they user has visited this website less than "" times
        count[len(count)-1] += count[placeinlist] #add it to the other count
        count.pop(placeinlist) #remove it from the count list
        labels.pop(placeinlist)#remove it from the labels list
      else:
        placeinlist += 1 #if they have visited more than "" times, move on to next item

    filterlist = self.m_textCtrlFilterList.GetValue()
    print(filterlist)
    if self.m_checkBoxFilter.GetValue() == True: #if the box is ticked, remove filtered objects
      placeinlist = 0
      while placeinlist < len(labels): #working through the list of domains
        if labels[placeinlist] in filterlist: #if the domain is in the filter list
          print("Removing: " + labels[placeinlist]) #remove it from the final plots
          count.pop(placeinlist)
          labels.remove(labels[placeinlist])
        else:
          placeinlist += 1
    else: #if the box isn't ticked, remove anything NOT in the list
      placeinlist = 0
      while placeinlist < len(labels):
        if labels[placeinlist] not in filterlist: #if the domain ISN'T in the filter list
          print("Removing: " + labels[placeinlist])#remove it from the final plot
          count.pop(placeinlist)
          labels.remove(labels[placeinlist])
        else:
          placeinlist += 1
      
    print("Printing Pie chart labels and counts!")
    for i in range(0,len(labels)):
      print(labels[i] + ":" + str(count[i]))
    print("Done! \n")
    plt.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.show()





#####TIME LINE DIALOG BOX CODE #####
class TimeLineAnalysisDialog(wxgui.dialogTimeLineAnalysis):
  def __init__(self,parent,ApplicationWindow):
    wxgui.dialogTimeLineAnalysis.__init__(self,parent)

  def GenerateTimeLineChart(self, event):
    print("LOADING TimeLine CHART...")
    global filePath
    connecttosqlite = sqlite3.connect(filePath)
    sqlsession = connecttosqlite.cursor()

    datalist = []#grabbing all timestampts in order
    for row in sqlsession.execute('SELECT last_visit_time FROM urls ORDER BY last_visit_time;'): #select all the visiting times
        row = str(datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds = row[0]) ) #configure them into proper data and times
        row = row.split()
        if row[1] != "00:00:00":#if the selected timestamp is all zeros, it's a bookmark, so skip it
           datalist.append(row[1][0:8]) #get the times in a HOUR:MINUTE:SECOND parsing
    #starting at midnight, and working our way up to 23(11pm)
    xlabels = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']#our labels from 12am - 11pm
    ydata = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #our starting counters
    for data in datalist:
        #this checks where the timestamp lies on the label, and adds it to the correct place
        #in the list
        ydata[(xlabels.index(data[0:2]))] += 1 #if '04' is found under hours, add it to the 4th part of the time line list.
    print("Plot data: " + str(ydata))

    plt.bar(np.arange(len(xlabels)), ydata, align='center')#sorting the labels evenly and applying data to them
    plt.xticks(np.arange(len(xlabels)), xlabels)
    plt.ylabel('Websites Visited')#setting Y label
    plt.title('Activity Within Different Hours')#setting title
    plt.xlabel('Time in 24-Hour Format')
    plt.show()
    print("Generated Bar Chart for Timeline analysis!")

    



app = wx.App(False)
frame = ApplicationWindow(None)
frame.Show(True)
app.MainLoop()
