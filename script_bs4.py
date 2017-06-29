from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import sys

#use pandas for read .csv files and make dataframe
def read_data(path):
	df = pd.read_csv(path)
	df.columns=['links']
	return df

#use urllib to download wikipedia page
def download_web_page(url):
	page = urllib.request.urlopen(url)
	return page

#use BeautifulSoup(bs4) to find needed element in downloaded wikipedia page
def find_link(url):
	page = download_web_page(url)
	soup = BeautifulSoup(page,'html.parser')
	url = soup.find('table',class_='infobox').find('th',text='Website').nextSibling.nextSibling.find('a').get('href')
	return url
	
#use pandas to make output dataframe and convert to .csv file
def make_output(wiki_links,webpage_links):
	index = [x for x in range(1,len(wiki_links)+1)]
	
	output_df = pd.DataFrame(index=index)
	output_df['wikipedia_page']=wiki_links
	output_df['webpage']=webpage_links
	output_df.to_csv('wikipedia_answer_bs4.csv')
	output_df.to_csv('./data/wikipedia_answer_bs4.csv')


def main():
	#check input variables length
	if len(sys.argv)>1:
		df = read_data(sys.argv[1])
		webpage_links=map(lambda x:find_link(x),df.links)
		make_output(list(df.links),list(webpage_links))

		print('See "wikipedia_answer_bs4.csv" file')
	else:
		print("Give me a file, which contains wikipedia urls in '.csv' format please")

main()
