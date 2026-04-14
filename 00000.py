def est_ip_valide(ip):
    octets=ip.split('.')
    if len(octets)!= 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        valeur = int(octet)
        if valeur<0 or valeur>255:
            return False
    return True
# Exemples de tests
print(est_ip_valide("244.178.44.111"))  # True
print(est_ip_valide("192.168.256.1"))  # False  
print(est_ip_valide("10.0.0"))         # False  

""" 

def classe_ip(ip):
    octets=ip.split('.')
    if len(octets)!= 4 or not all(octet.isdigit() for octet in octets):
        return "Adresse IP invalide"
    premier_octet = int(octets[0])
    if 0 <= premier_octet <= 127:
        return "Classe A - Très grands réseaux"
    elif 128 <= premier_octet <= 191:
        return "Classe B - Réseaux moyens"
    elif 192 <= premier_octet <= 223:
        return "Classe C - Petits réseaux"
    elif 224 <= premier_octet <= 239:
        return "Classe D - Multicast"
    elif 240 <= premier_octet <= 255:
        return "Classe E - Expérimental"
    else:
        return "Adresse IP invalide"
""" 
"""
def get_id_reseau(ip): 
• Convertit l’adresse IP et le masque en binaire (32 bits chacun). 
• Fait un ET logique bit à bit (1 si les deux bits = 1, sinon 0). 
• Convertit le résultat en adresse IPv4 classique.
"""
"""
def get_id_reseau(ip):
    octets=ip.split('.')
    if len(octets)!= 4 or not all(octet.isdigit() for octet in octets):
        return "Adresse IP invalide"
    masque=[255,255,255,0]
    id_reseau=[]
    for i in range(4):
        id_reseau.append(str(int(octets[i]) & masque[i]))
    return '.'.join(id_reseau)
"""


"""
def get_broedcast(ip):

"""