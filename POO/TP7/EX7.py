"""
texte = 
python est simple
python est puissant
java est puissant;
1. Compter les mots (Counter).
2. Construire un index : mot -&gt; lignes où il apparaît avec defaultdict(set).
3. Trouver les mots présents dans toutes les lignes.
"""

from collections import Counter, defaultdict

texte = """python est simple
python est puissant
java est puissant"""

# 1. Compter les mots (Counter).
word_count = Counter(texte.split())
print(word_count)

# 2. Construire un index : mot -> lignes où il apparaît avec defaultdict(set).
index = defaultdict(set)
for i, line in enumerate(texte.splitlines()):
    for word in line.split():
        index[word].add(i)
print(index)

# 3. Trouver les mots présents dans toutes les lignes.
common_words = set(texte.splitlines()[0].split())
for line in texte.splitlines()[1:]:
    common_words &= set(line.split())
print(common_words)
