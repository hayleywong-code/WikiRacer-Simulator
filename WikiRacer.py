# import required modules
from bs4 import BeautifulSoup
import requests

wikiLinkStart = "https://en.wikipedia.org"


def getNeighbors(link: str) -> list:
    # get URL
    try:
        page = requests.get(wikiLinkStart + link)
    except:
        return []

    # scrape webpage
    soup = BeautifulSoup(page.content, "html.parser")

    # get page content and find all <a> elements
    pageContent = soup.find(id="bodyContent")
    try:
        pElements = pageContent.find_all("p")
    except:
        return []
    aElements = []

    # add <a> elements to the aElements list only if they have a title attribute
    for p in pElements:
        for a in p.find_all("a"):
            if a.get("title") != None:
                aElements.append(a.get("href"))

    return aElements


def tracePath(parent: dict, firstLink: str, secondLink: str):

    path = [secondLink]

    while True:
        path.append(parent[secondLink])
        secondLink = path[-1]

        if firstLink == secondLink:
            path.reverse()
            return path


def bfs(firstLink: str, secondLink: str) -> bool:

    print(f"Beginning search from {firstLink[6:]} to {secondLink[6:]}...")

    queue = []
    queries = 0
    marked = set()
    parent = {}
    queue.append(firstLink)

    while queue:
        link = queue.pop(0)
        current_parent = link
        neighbors = getNeighbors(link)

        for n in neighbors:
            if n not in marked:
                parent[n] = current_parent
                marked.add(n)
                queue.append(n)
                queries += 1
            if n == secondLink:
                print(f"Connection found after {queries} queries")
                print(
                    "============================================================================="
                )
                print("Printing path below:")
                path = tracePath(parent, firstLink, secondLink)
                for l in path:
                    print(l[6:])
                return True
    return False


# get user input
print("************************************************")
print("*    PLEASE ENTER FULL VALID WIKIPEDIA URLs    *")
print("*  Ex: 'https://en.wikipedia.org/wiki/QWERTY'  *")
print("*            Code By: Hayley Wong              *")
print("************************************************")
print()


startingURL = input("Please enter your starting Wikipedia URL: ")
startingURL = startingURL[24:]

endingURL = input("Please enter your ending Wikipedia URL: ")
endingURL = endingURL[24:]

print("*****************************************************************************")
bfs(startingURL, endingURL)
