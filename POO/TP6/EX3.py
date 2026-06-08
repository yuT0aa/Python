"""
Une application possède :
config_default = {
&quot;theme&quot;: &quot;clair&quot;,
&quot;langue&quot;: &quot;fr&quot;
}

config_user = {
&quot;theme&quot;: &quot;sombre&quot;
}
Travail demandé :
1. Créer une ChainMap.
2. Afficher toutes les clés/valeurs.
3. Afficher :
o le thème ;
o la langue.
4. Expliquer pourquoi &quot;theme&quot; vaut &quot;sombre&quot;.
5. Ajouter :
o &quot;volume&quot;: 80
dans la configuration utilisateur.
6. Afficher la nouvelle ChainMap.
"""

from collections import ChainMap

# 1. Créer une ChainMap
config_default = {
    "theme": "clair",
    "langue": "fr"
}
config_user = {
    "theme": "sombre"
}
config = ChainMap(config_user, config_default)

# 2. Afficher toutes les clés/valeurs
print("Configuration complète:", dict(config))

#3. Afficher le thème et la langue
print("Thème:", config["theme"])
print("Langue:", config["langue"])

# 4. Expliquer pourquoi "theme" vaut "sombre"
# "theme" vaut "sombre" car dans une ChainMap, les clés sont recherchées dans l'ordre des maps fournies. Ici, "theme" est trouvé dans config_user avant d'être recherché dans config_default, donc la valeur "sombre" est utilisée.

# 5. Ajouter "volume": 80 dans la configuration utilisateur
config_user["volume"] = 80

# 6. Afficher la nouvelle ChainMap
print("Nouvelle configuration:", dict(config))