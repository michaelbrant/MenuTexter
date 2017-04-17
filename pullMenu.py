import datetime
moment = datetime.datetime.now()

#Get the Current Day, Month, and year
if (moment.month < 10):
    month  = '0' + str(moment.month)
else:
    month = str(moment.month)
if (moment.day < 10):
    day  = '0' + str(moment.day)
else:
    day = str(moment.day)
year = str(moment.year)

#Uncomment out these three lines to test specific days
#month = '04'
#day = '18'
#year = '2017'

print("Menu Date set for:"+month+' '+day+' '+year+'')
def getLunchURL():
    url = 'widener.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=213&PeriodId=1468&MenuDate='+year+'-'+month+'-'+day+'&Mode=day&UIBuildDateFrom=2017-03-13'
    return url
    #myHTMLParser.sendMenu(url, 'Lunch')

def getDinnerURL():
    url = 'widener.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=213&PeriodId=1469&MenuDate='+year+'-'+month+'-'+day+'&Mode=day&UIBuildDateFrom=2017-03-13'
    return url
