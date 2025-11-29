# Elevul 1 — Calculul și logica testului Ruffier (partea ta)

Acest fișier este doar pentru tine. Vei lucra exclusiv în fișierul `ruffier.py` și vei verifica rezultatele cu un fișier mic de test.

Obiectivele tale, în ordine:
1) Să înțelegi fiecare funcție din `ruffier.py` și să scrii explicații simple direct în cod (comentarii).
2) Să adaugi o mică îmbunătățire la calcul (rotunjire la o zecimală).
3) Să creezi un fișier de test și să rulezi calculul cu valori de exemplu.
4) Să verifici singur dacă rezultatul afișat are logică.

----------------------------------------------------------------

## 1. Deschidere proiect și fișierul tău

1. Deschide VS Code.
2. Meniu File → Open Folder → alege folderul proiectului (acolo unde este `main_app.py`).
3. În lista de fișiere din stânga, dă clic pe `ruffier.py`.

Nu schimba alte fișiere. Doar citește-le, dacă vrei să înțelegi proiectul.

----------------------------------------------------------------

## 2. Explică, pe rând, ce face fiecare funcție din `ruffier.py`

În acest fișier există patru funcții. Pentru fiecare, vei scrie deasupra lor un comentariu (un text care explică pe scurt, pentru oricine citește). Comentariile încep cu semnul `#` și nu afectează programul.

### 2.1. Funcția `ruffier_index(P1, P2, P3)`

Codul din proiect (nu schimba numele funcției sau parametrii):

```python
def ruffier_index(P1, P2, P3):
    return (4 * (P1+P2+P3) - 200) / 10
```

Scrie deasupra ei un comentariu, pe două-trei linii, cu ideile de mai jos, dar în cuvintele tale:
- Primește trei numere: P1, P2, P3 (pulsul numărat timp de 15 secunde).
- Transformă totalul în bătăi pe minut: înmulțește cu 4 (sunt patru intervale de 15 secunde într-un minut).
- Aplică formula: (4*(P1+P2+P3) - 200) / 10.
- Rezultatul este un număr real (poate avea virgulă) numit Indice Ruffier.

Exemplu de comentariu (poți copia exact):

```python
# Calculează Indicele Ruffier din cele trei măsurători P1, P2, P3.
# P1, P2 și P3 sunt pulsuri numărate fiecare timp de 15 secunde.
# Formula transformă în bătăi/minut și dă un scor: (4*(P1+P2+P3) - 200)/10.
```

### 2.2. Funcția `neud_level(age)`

Codul din proiect:

```python
def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age * 1.5
    return result
```

Comentariu recomandat (scrie-l deasupra funcției):

```python
# Întoarce pragul corespunzător rezultatului „nesatisfăcător” (valoare mare a indicelui) în funcție de vârstă.
# La 7 ani pragul e 21; din 2 în 2 ani scade cu 1.5 până la 15 ani (unde devine 15).
# Dacă vârsta este peste 15, folosim tot 15 (nu există date pentru adulți în acest tabel).
```

Explicație pe înțelesul tău:
- `min(age, 15)` înseamnă: dacă cineva are mai mult de 15 ani, considerăm 15 (tabelul e pentru copii).
- `// 2` înseamnă împărțire la 2 fără zecimale (doar partea întreagă).

### 2.3. Funcția `ruffier_result(r_index, level)`

Codul din proiect (citește-l atent, nu schimba liniile):

```python
def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4
    if r_index >= level:
        return 1
    level = level - 5
    if r_index >= level:
        return 2
    level = level - 5.5
    if r_index >= level:
        return 3
    return 4
```

Comentariu recomandat (scrie-l deasupra funcției):

```python
# Primește indicele Ruffier calculat (r_index) și pragul „nesatisfăcător” pentru vârsta dată (level).
# Întoarce o notă de la 0 la 4:
# 0 = nesatisfăcător, 1 = slab, 2 = satisfăcător, 3 = bun, 4 = perfect.
# Observație: diferențele dintre praguri sunt: 4, apoi 5, apoi 5.5 (conform tabelelor).
```

Ce se întâmplă, simplu:
- Dacă r_index e foarte mare (mai rău), primești 0.
- Apoi scădem din prag 4, 5 și 5.5. Dacă intri în zone mai bune, crește nota.
- Dacă r_index e mic, primești 4 (perfect).

### 2.4. Funcția `test(P1, P2, P3, age)`

Codul din proiect:

```python
def test(P1, P2, P3, age):
    if age < 7:
        return (txt_index + "0", txt_nodata)
    else:
        ruff_index = ruffier_index(P1, P2, P3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res
```

Comentariu recomandat (scrie-l deasupra funcției):

```python
# Folosită de ecranul de rezultat. Primește pulsurile și vârsta.
# Dacă vârsta este sub 7 ani, nu există date (returnează un mesaj).
# Altfel, calculează indicele Ruffier, stabilește nivelul și întoarce un text cu rezultatul final.
```

----------------------------------------------------------------

## 3. Îmbunătățire mică: rotunjire la o zecimală

În funcția `ruffier_index`, schimbă linia astfel încât rezultatul să fie rotunjit la o zecimală:

Linia veche:
```python
return (4 * (P1+P2+P3) - 200) / 10
```

Linia nouă:
```python
return round((4 * (P1+P2+P3) - 200) / 10, 1)
```

Salvează fișierul: Ctrl + S.

----------------------------------------------------------------

## 4. Creează un fișier mic de test și rulează-l

1. În VS Code, în lista de fișiere din stânga, apasă pe butonul „New File”.
2. Scrie numele fișierului: `test_ruffier.py`.
3. Pune în el acest cod:

```python
from ruffier import test

print("Testare calcul Ruffier")
print("----------------------")
print(test(20, 30, 25, 13))
```

4. Salvează: Ctrl + S.
5. Rulează: Ctrl + F5.

Dacă apare un text care începe cu „Your Ruffier index:” și încă un rând cu interpretarea (de tip „Heart performance: ...”), înseamnă că ai reușit.

----------------------------------------------------------------

## 5. Verificare logică simplă

- Dacă P1, P2, P3 sunt mari (de exemplu 40, 50, 45), indicele va fi mai mare, iar rezultatul va fi mai slab.
- Dacă P1, P2, P3 sunt mici (de exemplu 15, 20, 18), indicele va fi mai mic, iar rezultatul va fi mai bun.

Testează singur două-trei seturi de valori în `test_ruffier.py` și observă diferențele.

----------------------------------------------------------------

Ai terminat. Partea ta ține de matematică și interpretare. Ai scris explicații în cod, ai făcut o mică îmbunătățire și ai verificat rezultatul.
