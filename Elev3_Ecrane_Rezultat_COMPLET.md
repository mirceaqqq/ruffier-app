# Elevul 3 — Ecranele aplicației și rezultatul final (partea ta)

Acest fișier este doar pentru tine. Vei lucra exclusiv în `main_app.py` pentru a te asigura că ecranele trec corect și că rezultatul final apare bine.

Obiectivele tale, în ordine:
1) Să înțelegi ce face fiecare ecran și să adaugi câte un scurt comentariu la începutul clasei.
2) Să corectezi salvarea numelui și a vârstei, pentru ca ele să fie văzute de toate ecranele.
3) Să verifici, rulând aplicația, că tot fluxul merge de la început până la rezultat.

----------------------------------------------------------------

## 1. Deschidere proiect și fișierul tău

1. Deschide VS Code.
2. File → Open Folder → alege folderul proiectului.
3. Deschide fișierul `main_app.py`.

----------------------------------------------------------------

## 2. Adaugă scurte explicații la începutul fiecărei clase

La fiecare din clasele de ecran, scrie câte un rând deasupra clasei care spune pe scurt ce face:

- `InstrScr` — colectează nume și vârstă, verifică vârsta minimă 7.
- `PulseScr` — pornește un cronometru 15 secunde și citește pulsul P1.
- `CheckSits` — pornește animația pentru 30 de genuflexiuni și scade „Squats left”.
- `PulseScr2` — are 3 etape: 15 secunde măsurare P2, 30 secunde pauză, 15 secunde măsurare P3.
- `Result` — apelează funcția `test` din `ruffier.py` și afișează textul final.

Exemplu (îl pui deasupra clasei):
```python
# Ecranul de introducere: nume și vârstă, plus buton Start.
class InstrScr(Screen):
    ...
```

----------------------------------------------------------------

## 3. Corectarea salvării numelui și vârstei

Caută în clasa `InstrScr` metoda `next(self)`.
La începutul metodei, adaugă linia:

```python
global name, age
```

După această modificare, variabilele globale `name` și `age` vor fi actualizate pentru toate ecranele.

Nu modifica alte lucruri din metodă.

----------------------------------------------------------------

## 4. Verifică fluxul complet al aplicației

1. Rulează aplicația: Ctrl + F5.
2. Introdu nume și vârstă (dacă vârsta este sub 7, programul o va ridica la 7 automat).
3. Urmează toți pașii: puls 1, exerciții, puls 2 și 3.
4. Verifică ecranul final: apare numele introdus și rezultatul din `ruffier.py`.

Dacă vezi două rânduri în ecranul final (indice + interpretare), înseamnă că totul funcționează.

----------------------------------------------------------------

## 5. Îmbunătățire mică (opțional)

În clasa `Result`, în metoda `before`, după linia care setează `self.instr.text`, mai adaugă încă un rând pentru un mesaj politicos:

```python
self.instr.text += "\n\nMulțumim că ai folosit aplicația HeartCheck"
```

Salvează și rulează din nou. Verifică dacă apare mesajul.

----------------------------------------------------------------

Ai terminat. Partea ta ține de legarea corectă a ecranelor și afișarea rezultatului final.
