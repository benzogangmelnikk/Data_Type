#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

moscow_sites = sites['Moscow']
london_sites = sites['London']
paris_sites = sites['Paris']

distances = dict()

moscow_london = ((moscow_sites[0] - london_sites[0]) ** 2 + (moscow_sites[1] - london_sites[1]) ** 2) ** .5
moscow_paris = ((moscow_sites[0] - paris_sites[0]) ** 2 + (moscow_sites[1] - paris_sites[1]) ** 2) ** .5
distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

london_paris = ((london_sites[0] - paris_sites[0]) ** 2 + (london_sites[1] - paris_sites[1]) ** 2) ** .5
distances['London'] = {}
distances['London']['Paris'] = london_paris
distances['London']['Moscow'] = moscow_london

distances['Paris'] = {}
distances['Paris']['London'] = london_paris
distances['Paris']['Moscow'] = moscow_paris

pprint(distances)



