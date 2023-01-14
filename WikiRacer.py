# import required modules
from bs4 import BeautifulSoup
import requests
import Hyperlink


def getNeighbors(link: Hyperlink.Hyperlink) -> list:
    # get URL
    page = requests.get(link.getFullWikiLink())

    # scrape webpage
    soup = BeautifulSoup(page.content, "html.parser")

    # get page content and find all <a> elements
    pageContent = soup.find(id="bodyContent")
    pElements = pageContent.find_all("p")
    aElements = []

    for p in pElements:
        for a in p.find_all("a"):
            if a.get("title") != None:
                title = a.get("title")
                href = a.get("href")

                hyperlink = Hyperlink.Hyperlink(title, href, a)

                aElements.append(hyperlink)

    return aElements


def bfs(firstLink: Hyperlink.Hyperlink, secondLink: Hyperlink.Hyperlink) -> bool:

    print(f"Beginning search for {secondLink} from {firstLink}.")

    parent = {}
    queue.append(firstLink)

    while queue:
        link = queue.pop(0)
        print(link)
        current_parent = link
        neighbors = getNeighbors(link)

        for n in neighbors:
            if n in marked:
                parent[n] = current_parent
                marked.add(n)
                queue.append(n)
            if n.__eq__(secondLink):
                print("connection found")
                print(parent)


# get user input
print("************************************************")
print("*    PLEASE ENTER FULL VALID WIKIPEDIA URLs    *")
print("*  Ex: 'https://en.wikipedia.org/wiki/QWERTY'  *")
print("*            Code By: Hayley Wong              *")
print("************************************************")
print()


startingURL = input("Please enter your starting Wikipedia URL: ")
startingURL = startingURL[24:]
startingHyperlink = Hyperlink.Hyperlink(startingURL[6:], startingURL, None)

endingURL = input("Please enter your ending Wikipedia URL: ")
endingURL = endingURL[24:]
endingHyperlink = Hyperlink.Hyperlink(endingURL[6:], endingURL, None)

queue = []
marked = set()


print("****************************************************")
bfs(startingHyperlink, endingHyperlink)
