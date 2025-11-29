# Student 1 — **Calculul Ruffier & Logică medicală**
**Branch recomandat:** `feature-ruffier-calculations`  
**Fișiere principale:** `ruffier.py` (logică), `instructions.py` (texte)  
**Fișiere noi:** `tests/test_ruffier.py` (teste unitare)

---

## 🎯 Obiectiv
Tu ești responsabil de **corectitudinea matematică** și **claritatea documentării** pentru testul Ruffier. Scopul: un modul ușor de înțeles, bine comentat și acoperit de teste, pe care colegii tăi îl pot folosi fără să-l modifice.

---

## 📚 Descriere pe scurt a metodei Ruffier
- Se măsoară ritmul cardiac (bătăi) în 3 momente, fiecare pe **15 secunde**:  
  **P1** = înainte de efort, **P2** = imediat după efort, **P3** = după **30 secunde** de pauză.  
- Transformăm în bătăi/minut: `S = 4 * (P1 + P2 + P3)`  
- **Indice Ruffier (IR)**: `IR = (S - 200) / 10`  
- Interpretare în funcție de vârstă (7–15 ani) prin praguri: „nesatisfăcător”, „slab”, „satisfăcător”, „bun”, „perfect”. Diferențele dintre praguri sunt: **4**, **5**, **5.5** (în această ordine).

---

## 🧩 Ce trebuie să livrezi în `ruffier.py`
1. **Docstring-uri și comentarii clare** pentru fiecare funcție:
   - `ruffier_index(P1, P2, P3)`  
     - Explică formula, unitățile de măsură, exemple numerice.
   - `neud_level(age)`  
     - Explică logica pragului „nesatisfăcător” pentru o vârstă dată.  
       - La **7 ani** pragul este **21**; la fiecare **2 ani** scade cu **1.5**, până la **15–16 ani** unde devine **15**.  
       - Limitează vârsta maxim la 15 pentru tabel.
   - `ruffier_result(r_index, level)`  
     - Explică maparea în **categorii 0..4** (0 = nesatisfăcător, 4 = perfect) conform scăderilor succesive: `-4`, apoi `-5`, apoi `-5.5`.
   - `test(P1, P2, P3, age)`  
     - Explică structura rezultatului text: include indicele + interpretarea.  
     - Pentru `age < 7` întoarce mesajul că nu există date pentru acea vârstă.

2. **(Opțional) Adaugă adnotări de tip** (PEP 484) pentru lizibilitate.

3. **Note despre validarea intrărilor** (în docstring):  
   - Modulul **nu** blochează valori atipice (negative/zero). Validarea e în GUI.  
   - Explică efectul valorilor greșite (IR mai mare → interpretare mai slabă).

4. **Exemple numerice** (în docstring la începutul fișierului):  
   - Exemplu: `P1=20, P2=30, P3=25` → `S=4*(20+30+25)=300`, `IR=(300-200)/10=10.0`.  
     Pentru `age=13`: `neud_level(13)=18.0` → rezultatul ar trebui să fie **„satisfăcător”**.

---

## 🧪 Teste unitare — creează `tests/test_ruffier.py`
Instalează `pytest` în mediul virtual și adaugă teste minime precum:

```python
import math
from ruffier import ruffier_index, neud_level, ruffier_result

def test_ruffier_index_numeric_example():
    # P1=20, P2=30, P3=25 → IR = 10.0
    assert math.isclose(ruffier_index(20, 30, 25), 10.0, rel_tol=1e-9)

def test_neud_level_table_points():
    assert neud_level(7) == 21.0
    assert neud_level(8) == 21.0      # banda 7–8 ani
    assert neud_level(9) == 19.5
    assert neud_level(15) == 15.0
    assert neud_level(100) == 15.0    # plafonare

def test_category_boundaries():
    level = neud_level(7)             # 21.0
    assert ruffier_result(level + 0.01, level) == 0   # nesatisfăcător
```

**Cum rulezi testele:**
```bash
python -m venv venv
source venv/bin/activate
pip install pytest
pytest -q
```

---

## 📝 Contribuții în `instructions.py`
- Revizuiește textele în engleză sau traduce-le clar în română, păstrând sensul.  
- Evită jargonul medical; folosește un ton educativ.

---

## ✅ Criterii de acceptare
- [ ] `ruffier.py` are docstring-uri detaliate și coerente.
- [ ] Pragurile și diferențele 4 / 5 / 5.5 sunt explicate corect.
- [ ] `tests/test_ruffier.py` există și trece.
- [ ] Nu ai modificat GUI-ul.

---

## 🧭 Workflow Git (minim)
```bash
git checkout -b feature-ruffier-calculations
# editezi ruffier.py și adaugi tests/test_ruffier.py
git add ruffier.py tests/test_ruffier.py
git commit -m "docs: docstring-uri complete; test: adaugă teste Ruffier"
git push origin feature-ruffier-calculations
# creezi Pull Request către 'main' și ceri review
```

---

## 🌟 Bonus (opțional)
- Funcție `format_index(value: float) -> str` care rotunjește la 1 zecimală.
- Funcție `to_json(p1, p2, p3, age)` care întoarce un obiect serializabil cu scorul și interpretarea.
