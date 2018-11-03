names = {
 'Robert': 'Robert Baratheon',
 'Jon': 'Jon Snow',
 'Robb': 'Robb Stark',
 'Jaime': 'Jaime Lannister',
 'Cersei': 'Cersei Lannister',
 'Sansa': 'Sansa Stark',
 'Joffrey': 'Joffrey Baratheon',
 'Tywin': 'Tywin Lannister',
 'Tyrion': 'Tyrion Lannister',
 'Stannis': 'Stannis Baratheon',
 'Catelyn': 'Catelyn Stannis',
 'Bran': 'Bran Stark',
 'Arya': 'Arya Stark',
 'Ned': 'Ned Stark',
 'Renly': 'Renly Baratheon',
 'Hound': 'Sandor Clegane',
 'Varys': 'Varys',
 'Lysa': 'Lysa Arryn',
 'Tommen': 'Tommen Baratheon',
 'Pycelle': 'Maester Pycelle', ## looks like he is not in Wikidata -- skip him
 'Balon': 'Balon Greyjoy',
 'Loras': 'Loras Tyrell',
 'Theon': 'Theon Greyjoy',
 'Petyr': 'Petyr Baelish',
 'Edmure': 'Edmure Tully',
 'Barristan': 'Barristan Selmy',
 'Roose': 'Roose Bolton',
 'Margaery': 'Margaery Tyrell',
 'Hoster': 'Hoster Tully',
 'Myrcella': 'Myrcella Baratheon'}

wikidata_sparql = 
"""
SELECT ?x ?z
WHERE
{
	?x wdt:P1080 wd:Q2461698 .
    ?x rdfs:label ?z 
  	SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
  FILTER (lang(?z) = 'en')
  
}
"""

