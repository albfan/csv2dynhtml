#!/usr/bin/env python

# modify HTML table to use bootstrap table
  
from bs4 import BeautifulSoup as bs
import os
import re
import sys
 
def customize(fd):
     
   soup = bs(fd, 'html.parser')
   
   #add metadata to table
   table = soup.find(lambda tag: tag.name=='table')
   table.attrs['data-toggle']="table"
   table.attrs['data-show-columns']="true"
   table.attrs['data-filter-control']="true"
   table.attrs['data-show-search-clear-button']="true"
   table.attrs['data-sortable']="true"
   table.attrs['data-page-list']="[10, 25, 50, 100, all]"
   table.attrs['data-pagination']="true"

   #add metadata to table headers
   tableheaders = table.findAll(lambda tag: tag.name=='th')
   for th in tableheaders:
       th.attrs['data-field']=th.getText().replace(" ", "_")
       th.attrs['data-sortable']='true'
       th.attrs['data-filter-control']='select'
   
     
   sys.stdout.write(soup.prettify()) 

if __name__ == "__main__":
    fd = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

    customize(fd)

