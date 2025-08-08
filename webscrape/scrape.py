import requests
import bs4

link = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"

parameters = {
    'stream' : True,
    'headers' : {"User-Agent": "Mozilla/5.0"}
}
html_raw_data = requests.get(link, parameters)
html_raw_data = bs4.BeautifulSoup(html_raw_data.text,"lxml")

html_tag = html_raw_data.select('table.wikitable.sortable.plainrowheaders tbody tr')[1:]

for data_row in html_tag:
    try:
        state_name = data_row.select("th[scope='row'] a")[0].getText()
        #print(state_name)
    except IndexError:
        pass # Do not print anything

    try:
        zone_name = data_row.select('td')[2].getText()
        #print(zone_name)
    except IndexError:
        pass # Do not print anything

    print(f"STATE:{state_name.strip()}----ZONE:{zone_name.strip()}---")