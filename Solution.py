#!/usr/bin/env python

__author__ = 'Ismat Sumar'

'''My Solution to the Sortable Coding Challenge. Associate products with their respective listing(s).

'''

import os
import glob


def program():

    files = glob.glob('*.txt')
    print(files)
    x = 0
    Products=[]
    Listings=[]
    Listings_Titles=[]
    while x < len(files):
        text = []
        with open(files[x]) as txt_file:
            for line in txt_file:
                text.append(line)
        print(len(text))
        if any('","price":"' in s for s in text):
            for line in text:
                Listings.append(line)
                head, sep, tail = line.partition('","manufacturer":"')
                Listings_Titles.append(head.replace('{"title":"', "").replace("_", " ") + "\n")
        elif any('{"product_name":"' in s for s in text):
            for line in text:
                head, sep, tail = line.partition('","manufacturer":"')
                Products.append(head.replace('{"product_name":"', '').replace("_", " ") + "\n")
        else:
            print("Txt file does not contain products or listings")
        x += 1

    writing = str(os.getcwd() + "/Results")
    if not os.path.exists(writing): os.makedirs(writing)
    os.chdir(writing)

    zeta = []
    x = 0
    while x < len(Products):
        Test=[]
        z = 0
        y = 0
        Test.append('{"product_name":"' + Products[x].replace(" ", '_').replace("\n", '') + '","listings":')
        while z < len(Listings_Titles):
            if Products[x][0:-1] == Listings_Titles[z][0:len(Products[x])-1]:
                Test.append(Listings[z].replace("\n", '').replace("title", 'title' + str(y+1)).replace("manufacturer", 'manufacturer' + str(y+1)).replace("currency", 'currency' + str(y+1)).replace("price", 'price' + str(y+1))+ "}")
                z += 1
                y += 1
            else:
                z += 1

        zeta.append(Test[0:y+1])
        zeta.append("\n\n")
        x += 1

    z = 0
    with open("Results.txt", mode='w') as file:
        while z < len(zeta):
            file.write(str(zeta.pop(0)).replace("['", '').replace("', '", '').replace(":']", ': "none"}').replace("']", '').replace('}}{', ','))

if __name__ == '__main__':
    program()