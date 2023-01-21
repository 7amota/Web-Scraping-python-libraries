import requests
from bs4 import BeautifulSoup
lib =  input("enter lib name: ")
request = requests.get(f'https://pypi.org/project/{lib}/')

def main(request):
    
    page =  request.content
    soup = BeautifulSoup(page , 'lxml')
    
    def banner(soup):
        print('=================================================')
        print('======================INFO=======================')
        print('=================================================')
        banner = soup.find('div' , {'class' : 'banner'})
        libname = banner.find('h1' , {'class' : 'package-header__name'}).text.strip()
        libinstall = banner.find('p' , {'class' : 'package-header__pip-instructions'}).find('span').text.strip()
        print('lib name: ' +libname)
        print( "lib install: " +libinstall)
    banner(soup)

    def descraption(soup):
        print('=================================================')
        print('==================DESCRIPTION====================')
        print('=================================================')
        descraption = soup.find('div' , {'id' : 'description'})
        projectdescraption = descraption.find('div', {'class' : 'project-description'}).contents[0].text.strip()
        print(projectdescraption)
    descraption(soup)
    
main(request)

