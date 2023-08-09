"""
File: webcrawler.py
Name: Liz
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all("table", {"class": "t-stripe"})
        male_number = 0
        female_number = 0
        for tag in tags:
            targets = tag.tbody
            for target in targets:
                rank = str(target.text).replace(",", "")
                data = rank.split()
                if 0 < len(data) < 6:
                    male_number += int(data[2])
                    female_number += int(data[-1])
        print("Male Number: ", male_number)
        print("Female Number: ", female_number)


if __name__ == '__main__':
    main()
