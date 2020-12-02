import requests
from bs4 import BeautifulSoup
print("script by salah eddine elhandaoui")
print("-"*40)
website=input("enter link of social media website with https:// =>")
username=input("enter your user name in this web site =>")
URL="{}/{}/"

def pic_downloader(website,username):
	r=requests.get(URL.format(website,username))
	s=BeautifulSoup(r.text,"html.parser")
	
	p=s.find("meta",property="og:image").attrs['content']
	
	with open(username+".jpg","wb") as pic:
		binary=requests.get(p).content
		pic.write(binary)


if __name__=="__main__":
	print("landing ............")
	pic_downloader(website,username)
	print("your image profile is downloaded now ")
	