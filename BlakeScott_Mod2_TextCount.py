import string
from string import punctuation

s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, 
instead of remaining fixed in their places, move freely about, on or in the surface, 
but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - 
and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe":
 but now my mind has been opened to higher views of things."""
print("original str: " + s)

s_lower = s.lower()
print("str in all lowercase:")
print(s_lower)

words = list()
words = s_lower.split()
print("str in a list:")
print(words)

print("str word count:")
count = len(words)

print(count)

uni_count = len(set(words))
print("str distinct word count:")
print(uni_count)


j = []
for i in words:
    word_count = words.count(i)
    j.append((i, word_count))

freq_occur = dict(j)
print("str word freq dict:")
print(freq_occur)

#punctuation_list = list(string.punctuation)
#print(punctuation_list)

w_clean = list()
new=[i.strip(punctuation) for i in s_lower.split()]
w_clean = " ".join(new).split()

print("str list w no punct:")
print(w_clean)
print("str w no punct word count:")
print(len(w_clean))

