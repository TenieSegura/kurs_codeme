#l_per_100 = float(input("Podaj spalanie na sto"))
#dystans_km = int(input("Jak daleko chcesz pojechac?"))
#cena_litra_benzyny = 5.04

#total = cena_litra_benzyny * dystans_km/100 * l_per_100
#print(round(total, 2))

#txt = input('Podaj tekst o dlug. nieparzystej > 7:')
#center = len(txt)//2
#new_txt = txt[center - 1] + txt[center] + txt[center +1]
#print(new_txt)

#quote = 'Honesty is the first chapter in the book of wisdom.'
#print(len(quote))
#print(quote[-7:-1])

#middle = len(quote)//2
#print(quote[0:middle])
#print(quote[-1])
#print(quote[::2])
#print(quote[middle::3])
#print(quote[::-1])
#print(quote.replace('wisdom', 'friendship'))

#palindrom = input("Wpisz tekst:")
#print(palindrom[::-1] == palindrom[::1])

#palindrom = "Kobyla ma maly bok"
#palindrom = palindrom.replace(" ", "")
#palindrom = palindrom.lower()
#print(palindrom)

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print(zen)