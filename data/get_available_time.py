#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

def get_slots(url):
	# TODO: replace with open('./data/sample_page.html') with url reading
	with open('./data/sample_page.html') as data_file:
		sample = data_file.read()
		soup = BeautifulSoup(sample, 'html.parser')

		tab_header_el = soup.find('th', class_="sortable")
		table = tab_header_el.find_parent('table')
		tbody = table.find('tbody')
		data = tbody.find_all('tr')

		slots = list()
		for line in data:
			slot_data = line.find_all('td')
			slot = dict()
			slot['place'] = slot_data[0].string
			slot['district'] = int(slot_data[1].string)
			slots.append(slot)

		return slots

if __name__ == '__main__':
    print(get_slots(''))