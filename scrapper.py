#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def authenticate():
	s = requests.Session()
	s.get('https://teleservices.paris.fr/srtm/jsp/web/index.jsp')
	s.post(
		'https://teleservices.paris.fr/srtm/authentificationConnexion.action',
		data = {'login': '130388019', 'password': '2394'}
	)

	return s

def get_slots(startAtDate, startAtHour='18', district=None):
	s = authenticate()

	payload = {
		'provenanceCriteres': True,
		'actionInterne': 'recherche',
		'dateDispo': startAtDate,
		'heureDispo': startAtHour,
		'courtEclaire': 'on',
	}

	if not district:
		payload['arrondissement'] = district
	else:
		payload['tousArrondissements'] = 'on'

	r = s.post(
		'https://teleservices.paris.fr/srtm/reservationCreneauListe.action',
		data = payload
	)

	soup = BeautifulSoup(r.text, 'html.parser')

	tab_header_el = soup.find('th', class_="sortable")
	print(tab_header_el)
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
