
  
# -*- coding: utf-8 -*-
# from selenium import webdriver
import time                                                                                                                                                                    
# import os
import urllib.request
import requests
# from bs4 import BeautifulSoup 
# import concurrent.futures 
# from webdriver_manager.chrome import ChromeDriverManager


try:
  url="https://www.google.com/search?q=jennkins+PermissionError%3A+%5BErrno+13%5D+Permission+denied%3A+%27%2Fusr%2Flocal%2Fbin%2Fpip%27&oq=jennkins+PermissionError%3A+%5BErrno+13%5D+Permission+denied%3A+%27%2Fusr%2Flocal%2Fbin%2Fpip%27&aqs=chrome..69i57.3980j0j9&sourceid=chrome&ie=UTF-8"
  rep = requests.get(url)
  print (rep)
except:
  print ('error occured jk')