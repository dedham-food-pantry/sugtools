
def scrape_signup(soup):
    # the first table in the page is the main table so that's what we'll
    # scan
    rows = soup.find("tbody")("tr", recursive=False)

    for row in rows:
        cols = row("td", recursive=False)

        events = cols[3]("td") # 4 columns total, the last column is
                               # the event. There can be multiple
                               # events.

        for event in events:
            name = event.find("span", class_="signupdata--slot-title ng-binding").text.strip()
            capacity = event.find("div", class_="signup--badge-wrap").text.strip()
            if "All" not in capacity:
                print(cols[0].text.replace('\n',' ') + name + ": " + capacity)
