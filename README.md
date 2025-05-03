# Kursinis
# 📘 Kursinio darbo ataskaita – Wordle Solver (OOP projektas)

## 1. Įžanga

### a. Kas yra ši aplikacija?

Ši programa yra interaktyvus Wordle žaidimo sprendėjas, paremtas objektinio programavimo principais. Ji padeda žaidėjui spėti žodį, remiantis įvestais spėjimais ir gauta grįžtamojo ryšio informacija (G = green, Y = yellow, B = gray).

### b. Kaip paleisti programą?

1. Turėti įdiegtą Python 3.10+.
2. Atsisiųsti visą projektą iš GitHub: `git clone https://github.com/Rokusena/Kursinis`
3. Paleisti terminale:

```bash
python src/main.py
```

### c. Kaip naudotis programa?

* Įvedi 5 raidžių žodį (pvz. `alert`)
* Įvedi feedback iš Wordle (pvz. `BGYGB`)
* Programa pateikia geriausias spėjimo strategijas ir kitą žodį
* Kartoji, kol atspėji žodį arba išeini įrašęs `exit`

---

## 2. Pagrindinė analizė

### a. Kaip įgyvendinti funkcionalūs reikalavimai?

* **OOP principai:**

  * **Encapsulation:** Klasės `WordleSolver`, `WordList`, `Feedback` turi privatų duomenų saugojimą
  * **Abstraction:** Bazinė klasė `SolverStrategy` apibrėžia bendrą sąsają
  * **Inheritance:** `FrequencySolverStrategy` paveldi iš `SolverStrategy`
  * **Polymorphism:** `top_guesses()` veikia skirtingai priklausomai nuo pasirinktos strategijos

* **Dizaino šablonas:** Naudojamas `Strategy Pattern` spėjimo logikai keisti

* **Testavimas:** Visi pagrindiniai funkcionalumai patikrinti su `unittest`

* **Failų valdymas:** Žodžiai įkeliami iš `data/words.txt`, sesijos saugomos į `guess_log.txt`

---

## 3. Rezultatai ir santrauka

### a. Rezultatai:

* Programa sėkmingai sumažina žodžių sąrašą pagal `GYB` atsakymus
* Strategijos veikimas optimizuotas raidžių dažnio analize
* Vartotojas gauna TOP 10 efektyviausių žodžių kiekviename žingsnyje
* Vartotojo įvestis apsaugota nuo simbolių, pasikartojimų ar neteisingo ilgio

### b. Išvados:

* Programa sėkmingai realizuoja OOP ir strateginį dizaino šabloną
* Lengva palaikyti ir praplėsti su naujomis strategijomis
* Visi techniniai reikalavimai įgyvendinti

### c. Kaip būtų galima išplėsti programą?

* Sukurti grafinę sąsają (pvz. su Tkinter arba PyQt)
* Pridėti automatinį žaidimo simuliatorių
* Įgyvendinti daugiau strategijų (statistinę analizę, machine learning)

---

## 4. Naudoti šaltiniai ir įrankiai (pasirinktinai)

* Python 3.13
* `unittest`, `collections`, `random`
* Wordle oficialus žodynas (panaudota dalis žodžių)
* Git + GitHub versijavimo kontrolei
* ChatGPT , Gemini 
