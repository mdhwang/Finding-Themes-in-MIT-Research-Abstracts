from bs4 import BeautifulSoup
import requests
import csv

eecs = 'https://www.eecs.mit.edu/people/faculty-advisors'
soup = BeautifulSoup(requests.get(eecs).content, 'html.parser') 

faculty = []
for each in soup.find_all('span', class_ = 'field-content card-title'):
    faculty.append(each.get_text())

lib = []
for author in faculty:
    adv_search = 'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term={}&terms-0-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first'.format(author)
    soup = BeautifulSoup(requests.get(adv_search).content, 'html.parser')
    for each in soup.find_all('span', class_ ='abstract-full'):
        lib.append(each.get_text()[9:-16])

with open('EECS_Abstracts.csv','w') as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow(lib)

