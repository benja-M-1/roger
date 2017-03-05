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
		'dateDispo': '10/03/2017',
		'heureDispo': 18,
		'courtEclaire': 'on',
		'tousArrondissements': 'on',
		'libellePlageHoraire':'',
		'nomCourt':'',
		'actionInterne':'recherche',
		'champ':'',
		'tennisArrond':'',
		'arrondissement':'',
		'arrondissement2':'',
		'arrondissement3':'',
		'plageHoraireDispo':'',
		'revetement':'',
		'court':''
	}

	print(payload)

	r = s.post(
		'https://teleservices.paris.fr/srtm/reservationCreneauListe.action',
		data = payload,
		headers = {
			'referer': 'https://teleservices.paris.fr/srtm/reservationCreneauListe.action'
		}
	)

	print(r.text)
	soup = BeautifulSoup(r.text, 'html.parser')

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
