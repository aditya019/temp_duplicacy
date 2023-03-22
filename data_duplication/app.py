from strsimpy.ngram import NGram
from strsimpy.cosine import Cosine

file1 = open('one.txt', 'r', encoding="UTF-8")
s1 = file1.read().rstrip()
file1.close

file2 = open('two.txt', 'r', encoding="UTF-8")
s2 = file2.read().rstrip()
file2.close

fourgram = NGram(4)
n_gram = fourgram.distance(s1, s2)

cosine = Cosine(2)
p1 = cosine.get_profile(s1)
p2 = cosine.get_profile(s2)
cosine = cosine.similarity_profiles(p1, p2)

if cosine >= 0.8 and n_gram <= 0.2:
    print("suspected duplicacy")
else:
    print("not duplicates")