# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 00:24:58 2021

@author: Mausam
"""

import requests
import csv


with open('data.csv','w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product Title','Supplier Name', 'Hyperlink', 'Stock Status'])


def url_dev(sku_value):
    link = f"https://cdn-ws.turnto.com/v5/sitedata/fn7upu9h3FoXXgPsite/{sku_value}/d/question/en_US/0/6/BEST/false?"
    return link


def write_csv(title, url, itemUrl, stock_status='Out of Stock'):
    with open('data.csv','a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([title, url, itemUrl, stock_status])
    

def main():
    sku_value = []

    lines = open('links.txt','r').read().splitlines()

    for i in range(3):
        txt = lines[i]
        if txt.endswith('bulk-pack-xm193bkf.html'):
            sku_value.append("51655104908")    
        elif txt.endswith('bblkhc.html'):
            sku_value.append("51927")
        elif txt.endswith('20rds-81501.html'):
            sku_value.append("96123")
        else:
            pass
        
    for i in range(3):
        link = url_dev(sku_value[i])
        #print(link)
        result = requests.get(link)
        data = result.json()
        if sku_value[i] == "51927":
            for question in data['questions']:
                title = question['catItem']['title']
                url = question['catItem']['url'][0:32]
                itemUrl = question['catItem']['itemUrl']
        else:
            for question in data['questions']:
                for ans in question['answers']:
                    title = ans['catItem']['title']
                    url = ans['catItem']['url'][0:32]
                    itemUrl = ans['catItem']['itemUrl']
                    break
                break
        #print(title)
        #print(url)
        #print(itemUrl)
        #print("\n")
        write_csv(title, url, itemUrl)
        

if __name__ == "__main__":
    main()
