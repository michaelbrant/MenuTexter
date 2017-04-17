from bs4 import BeautifulSoup
import requests

def parse(url):
    r  = requests.get("http://" +url)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")
    #Parse the HTML at menu-details-sation 
    menu = soup.find_all("div", class_="menu-details-station")
    locations = []
    for element in menu:
        locations.append(element.get_text().encode('utf-8'))
    #Clean up the menu text a bit
    k=[]
    for i in locations:
        j = i.replace(' ','')
        k.append(j)
    m=[]
    for i in k:
        l = i.replace('\n','')
        m.append(l)
    menuList = []
    #Only add to menuList these locations: Comfort line, Approved Locations, Grill, and vegetarian.
    for locationMenu in m:
        if "COMFORT" in locationMenu or "Approved" in locationMenu or "GRILL" in locationMenu or "VEGETARIAN" in locationMenu:
            menuList.append(remove_caltext(remove_digits(add_spaces(locationMenu))))
            menuList.append('\n')
    #Location Titles are all capitals so add_spaces() will add spaces in between each letter. This looks dumb so here's a quick fix:
    menuList = [w.replace('Approved Location Specific Recipes', 'INTERNATIONAL \n') for w in menuList]
    menuList = [w.replace('C O M F O R T L I N E', 'COMFORT LINE \n') for w in menuList]
    menuList = [w.replace('G R I L L', 'GRILL \n') for w in menuList]
    menuList = [w.replace('V E G E T A R I A N', 'VEGETARIAN \n') for w in menuList]
    return menuList

def add_spaces(text):
    return text[:1] + ''.join((' ' + char if char.isupper() else char)
    for char in text[1:])

def remove_digits(text):
    return ''.join([i for i in text if not i.isdigit()])

def remove_caltext(text):
    return text.replace("Cal", "\n")
