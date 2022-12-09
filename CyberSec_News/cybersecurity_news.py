import feedparser
import webbrowser
from tabulate import tabulate
import pyfiglet
from datetime import datetime



def main():

    ascii_banner = pyfiglet.figlet_format("--Security News Website List--")
    print(ascii_banner)

    data = [["TheHackerNews"], 
        ["ThreatPost"],
        ["NakedSecurity"],
       

       ]
  
    #define header names
    col_names = ["Features"]
  
    #display table
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))

    #banner_time and date
    print("_" * 100)
    print("Scanning started at: " + str(datetime.now()))
    print("_" * 100)


    website_list = ("https://feeds.feedburner.com/TheHackersNews", "https://threatpost.com/feed", "https://nakedsecurity.sophos.com/feed")

    website_input = int(input("Enter website by number (0-2): "))

    NewsFeed = feedparser.parse(website_list[website_input])
    article_list = []
    article_link = []
    for i in range(5):
        article = NewsFeed.entries[i]
        titles = article.title
        link = article.link
        article_link.append(link)
        article_list.append(titles)

    article_num = 1
    for article in article_list:
        print('[{}] {}'.format(str(article_num), article))
        article_num += 1

    article_link_click = False
    while not article_link_click:
        user_click = int(input("Choose the link you want to open (1-5): "))
        webbrowser.open(article_link[user_click-1])
        article_link_click = True

main()
