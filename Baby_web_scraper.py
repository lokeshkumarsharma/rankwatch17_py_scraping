"""web scraping
to store the baby names in csv file from the given Url"""

import bs4												#import to beautifulsoup package 
try:
    from urllib.request import urlopen as urlGetData	
except ImportError:										#to catch an exception 
    from urllib2 import urlopen as urlGetData
from bs4 import BeautifulSoup as bs						#used beautifulsoup as bs

"""read the content of given url 
find the values from div tag where class name is "wcontent" """

def baby_name():

	baby_info = bs(urlGetData("https://www.babynamesdirect.com/").read(), "html.parser").findAll("div",{"class":"wcontent"})

	fwrite = open("baby/baby_csv_file.csv", "w")					#create a csv file and open it in writing mode
	top = "BabyName, Gender \n"								
											
	fwrite.write(top)												#write the heading of both the column
	for line in baby_info[:-1]:										#read each line from the retrieved data
		tag = line.findAll('a')	
		for val in tag[:-1]:   					
			gender = val.get('class')								#store the gender
			name = val.text											#store the name of gender in name variable
			print(name + "," + str(gender)[2:-2])					
			fwrite.write(name + "," + str(gender)[2:-2]+ "\n")			#write name and gender in csv and "\n" for new line
	fwrite.close()														#close to file
	
	
if __name__ == '__main__':
  baby_name()					#call to function														