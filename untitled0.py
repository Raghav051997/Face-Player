# -*- coding: utf-8 -*-
"""
Created on Sat May 19 15:01:57 2018

@author: Raghav Gandotra
"""

import urllib
import bs4
import urllib.request
from PyQt5.QtWidgets import QApplication
import PyQt5
#from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage
from bs4 import BeautifulSoup

class Client(QwebPage):
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(Qurl(url))
        self.app.exec_()
    
    def on_page_load(self):
        self.app.quit()