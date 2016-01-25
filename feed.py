import feedparser

# sample tested links
# http://rss.cnn.com/rss/edition.rss
# http://www.dr.dk/nyheder/service/feeds/allenyheder

# TODO: save user choices to file
# TODO: read values on opening program
# TODO: have user choose what items from feed is shown

# initial user choices

print("Welcome to the simple RSS reader.")

feedLink = input("Please enter your rss link: ")
    
while True:   
    try:
        itemsToDisplay = int(input("How many items would you like to have displayed at a time: "))
        break
    except ValueError:
        print("Enter valid int")
    
saveValues = input("Would you like to save your prefs (y/n): ")

if saveValues == 'y':
    # Save the values
    print("Saved")
else:
    print("Discarding values on exit")

# Get data based on user choices

d = feedparser.parse(feedLink)

for i in range(0,int(itemsToDisplay)):
    # while items still avalible show title + link
    try:
        print("Title: " + d.entries[i].title)
        print("Link: " + d.entries[i].link +  "\n")
    except IndexError:
        print("No more items to display")
        break