import sqlite3
from collections import Counter

metin1 = input("Birinci metni girin: ")
metin2 = input("İkinci metni girin: ")


c = sqlite3.connect('metinler.db')


c.execute('''CREATE TABLE IF NOT EXISTS Metinler
             (id INTEGER PRIMARY KEY AUTOINCREMENT, metin TEXT)''')


c.execute("INSERT INTO Metinler (metin) VALUES (?)", (metin1,))
c.execute("INSERT INTO Metinler (metin) VALUES (?)", (metin2,))

conn.commit()

def jaccard_similarity(metin1, metin2):
    kelimeler1 = set(metin1.split())
    kelimeler2 = set(metin2.split())

    kesisim = kelimeler1.intersection(kelimeler2)
    birlesim = kelimeler1.union(kelimeler2)

    return len(kesisim) / len(birlesim)


benzerlik_orani = jaccard_similarity(metin1, metin2)

print(f"Benzerlik Oranı: {benzerlik_orani:.2f}")


with open("benzerlik_durumu.txt", "w") as dosya:
    dosya.write(f"Birinci Metin: {metin1}\n")
    dosya.write(f"İkinci Metin: {metin2}\n")
    dosya.write(f"Benzerlik Oranı: {benzerlik_orani:.2f}\n")


conn.close()

