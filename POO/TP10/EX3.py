"""
trafic = '''
192.168.1.1 -> 10.0.0.5
192.168.1.1 -> 10.0.0.8
192.168.1.2 -> 10.0.0.5
192.168.1.3 -> 10.0.0.5
192.168.1.1 -> 10.0.0.5
'''
1. Extraire les IP source et destination.
2. Compter le nombre de communications par IP source.
3. Trouver l&#39;IP la plus active.
4. Trouver la destination la plus sollicitée.
"""

trafic = """
192.168.1.1 -> 10.0.0.5
192.168.1.1 -> 10.0.0.8
192.168.1.2 -> 10.0.0.5
192.168.1.3 -> 10.0.0.5
192.168.1.1 -> 10.0.0.5
"""

#1
ip_sources = []
ip_destinations = []
for ligne in trafic.strip().split('\n'):
    source, destination = ligne.split(' -> ')
    ip_sources.append(source)
    ip_destinations.append(destination)

#2
from collections import Counter
communications_par_source = Counter(ip_sources)

#3
ip_la_plus_active = communications_par_source.most_common(1)[0][0]
print("IP la plus active :", ip_la_plus_active)

#4
communications_par_destination = Counter(ip_destinations)
destination_la_plus_sollicitee = communications_par_destination.most_common(1)[0][0]
print("Destination la plus sollicitée :", destination_la_plus_sollicitee)
