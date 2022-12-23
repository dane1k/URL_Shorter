# this is URL shortener from Danil :3
import requests


def shorting_link(full_link, link_name):
    API_KEY = '1ad8be3e2c4999e48a2ea11aa141d3802d3c0' #API
    BASE_URL = 'https://cutt.ly/api/api.php' #shortingLink website *need for shorting :3*

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name} # equel value to value
    request = requests.get(BASE_URL, params=payload) #that request for getting information
    data = request.json() #report all

    print('') #free space for final answer will looks like something good :3

    try:
        title = data['url']['title'] #create a title subject
        short_link = data['url']['shortLink'] # and this is final shorten link

        print('Title: ', title) #print title
        print('Link: ', short_link) #print link
    except:
        status = data['url']['status'] #create a status error (statuts: https://cutt.ly/api-documentation/regular-api )
        print('Error Status: ', status)


link = input('Enter a link: >>> ')
name = input('Give your a link name: >>> ')

shorting_link(link, name)


