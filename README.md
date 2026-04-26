# 🔓 Password Cracker (Edukativni projekt)

Jednostavan alat za demonstraciju kako se mogu razbiti hashirane lozinke. Ovaj projekt je napravljen da pokaže kako napadi funkcioniraju i zašto su jake lozinke i sigurni algoritmi važni.

---

## ⚠️ Upozorenje

Ovaj alat je samo za:
* učenje
* testiranje vlastitih sustava
* sigurnosna istraživanja u kontroliranom okruženju

Nemojte ga koristiti za neovlašten pristup tuđim podacima.

---

## 🚀 Što radi

Ovaj alat ima neke korisne funkcije:
* podrška za hash algoritme: MD5, SHA1, SHA256
* može napraviti brute-force napad
* može koristiti listu poznatih lozinki
* broji pokušaje i vrijeme izvođenja

---

## 🧠 Kako funkcionira

Alat uzima hash i pokušava pronaći originalni password:
* **brute-force** generira sve moguće kombinacije znakova
* **dictionary attack** koristi listu poznatih lozinki

---

## 📦 Kako instalirati

1. Preuzmi repozitorij:
```bash
git clone https://github.com/your-username/password-cracker.git
cd password-cracker
```

2. Pokreni program:
```bash
python password_cracker.py
```

---

## ▶️ Kako koristiti

Nakon pokretanja:

1. Odaberi tip napada:
   * `1` za brute force
   * `2` za dictionary attack

2. Unesi:
   * hash
   * algoritam (`md5`, `sha1`, `sha256`)

3. Ako koristiš dictionary:
   * unesi putanju do wordlist filea

---

## 📁 Primjer wordlist-a

```text
password
123456
admin
qwerty
letmein
```

---

## 🧪 Primjer

Hash:
```text
5e884898da28047151d0e56f8dc6292773603d0d6aabbddf...
```

Rezultat:
```text
[+] Password pronađen: password
```

---

## 🔒 Sigurnosne lekcije

Ovaj projekt pokazuje:
* zašto su kratke lozinke loše
* zašto su MD5 i SHA1 zastarjeli
* zašto treba koristiti:
  * jake lozinke
  * salt
  * moderne algoritme (npr. bcrypt)

> Inspiracija: [Hashcat](https://hashcat.net)

---

## 💡 Moguća poboljšanja

* multithreading za brži brute-force
* podrška za bcrypt
* CLI argumenti
* benchmark performansi
* automatsko učitavanje velikih wordlista

---

## 🛠️ Tehnologije

* Python 3
* Standardne biblioteke:
  * `hashlib`
  * `itertools`
  * `time`
  * `string`

---

## 📜 Licenca

MIT License

---

## 👨‍💻 Autor

Projekt napravljen kao dio učenja cyber securityja i demonstracije razumijevanja password sigurnosti.
