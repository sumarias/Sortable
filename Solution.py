#!/usr/bin/env python

__author__ = 'Ismat Sumar'

'''My Solution to the Sortable Coding Challenge. Associate products with their respective listing(s).
   Step 1: Search all local .txt files and look for keywords specific to either a products or listings file.
   Step 2: After determining which txt file is related to products or listings save them as separate arrays.
   Step 3: Create another array that just has the title of the Listings, this is used to match with the Products array.
   Step 4: Create local Results directory where the Results.txt file will be placed separately from other .txt files.
           This is so that if this script is run twice Results.txt will not have interfere with the script.
   Step 5: Create Results array where the final data will be appended to, and a Product_Listings array that matches
           a product to all of its listings.
   Step 6: Initialize loop that firstly appends the product to the Product_Listings array and then checks for matches
           between the arrays Products and Listings_Titles. A successful match indicates that the product matches with
           the title of the listing, that index is then appended to the Product_Listings array in an exhaustive manner.
           Each successful match increases the number on each of the titles of the listings array. This is just to keep
           track of the number of listings for each product. Some string manipulation is done here to get it in proper
           JSON format.
   Step 7: Append Product_Listings array to the Results array. This is done so that each index in the Results array
           corresponds to a product with multiple listings. A new line is appended after this so the Results.txt file is
           easier to read.
   Step 8: Write Results array to the file Results.txt. String manipulation is used again here to ensure each line is
           valid JSON.
'''

import os
import glob


def program():

    files = glob.glob('*.txt')
    x = 0
    Products=[]
    Listings=[]
    Listings_Titles=[]
    while x < len(files):
        text = []
        with open(files[x]) as txt_file:
            for line in txt_file:
                text.append(line)
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

    Results = []
    x = 0
    while x < len(Products):
        Product_Listing=[]
        z = 0
        y = 0
        Product_Listing.append('{"product_name":"' + Products[x].replace(" ", '_').replace("\n", '') + '","listings":')
        while z < len(Listings_Titles):
            if Products[x][0:-1] == Listings_Titles[z][0:len(Products[x])-1]:
                Product_Listing.append(Listings[z].replace("\n", '').replace("title", 'title' + str(y+1)).replace("manufacturer", 'manufacturer' + str(y+1)).replace("currency", 'currency' + str(y+1)).replace("price", 'price' + str(y+1))+ "}")
                z += 1
                y += 1
            else:
                z += 1

        Results.append(Product_Listing[0:y+1])
        Results.append("\n\n")
        x += 1

    z = 0
    with open("Results.txt", mode='w') as file:
        while z < len(Results):
            file.write(str(Results.pop(0)).replace("['", '').replace("', '", '').replace(":']", ': "none"}').replace("']", '').replace('}}{', ','))

if __name__ == '__main__':
    program()
