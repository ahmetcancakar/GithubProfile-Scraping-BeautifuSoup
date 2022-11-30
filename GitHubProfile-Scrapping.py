import requests
from bs4 import BeautifulSoup

url="https://github.com/"
githubUser = input("Enter the Github Username: ")
request = requests.get(url+githubUser)
soup = BeautifulSoup(request.content, 'html.parser')

#Get the avatar image of the user
profileImage = soup.find('img', {'alt' : 'Avatar'})['src']
print(profileImage)

#Get the bio of the user
profileBio=soup.find("div",{"class":"p-note user-profile-bio mb-3 js-user-profile-bio f4"})
print(githubUser + "'s : " + profileBio.text)

#Get the name of the user
profileName=soup.find("span",{"class":"p-name vcard-fullname d-block overflow-hidden"})
print("Name of the User: " + profileName.text)

#Get the followers of the user
profileFollowers=soup.find("span",{"class":"text-bold color-fg-default"})
print("Followers: " + profileFollowers.text)


