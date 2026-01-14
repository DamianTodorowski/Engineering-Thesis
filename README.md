# Analiza i Demonstracja Ataków Adwersarialnych w Systemach Uczenia Maszynowego

Projekt został zrealizowany w ramach pracy inżynierskiej i skupia się na badaniu bezpieczeństwa modeli uczenia maszynowego (ML) w obliczu ataków adwersarialnych (*adversarial attacks*). Projekt obejmuje szerokie spektrum zastosowań, badając podatność na ataki zarówno w przetwarzaniu języka naturalnego (NLP), jak i w widzeniu komputerowym (*Computer Vision*).

## Opis Projektu

Głównym celem projektu jest praktyczna weryfikacja odporności popularnych architektur sieci neuronowych i algorytmów ML na celowe zaburzenia danych wejściowych (przykłady zwodnicze). Prace badawcze obejmują generowanie ataków typu *white-box* i *black-box*, analizę ich skuteczności oraz metody obrony, takie jak trening adwersarialny.

Zakres realizowanych eksperymentów:

1.  **NLP (Natural Language Processing) - Wykrywanie Spamu i Analiza Sentymentu**:
    *   Ataki na filtry spamu (zbiory `Enron`, `SMS Spam`) oraz modele analizy sentymentu.
    *   Testowanie modeli o różnej złożoności: od Regresji Logistycznej po modele oparte na Transformerach (BERT, DistilBERT).
    *   Wykorzystanie zaawansowanych technik ataków tekstowych: **TextFooler**, **PWWS**, **TextBugger**, **DeepWordBug** oraz **HopSkipJump**.

2.  **Computer Vision - Klasyfikacja Obrazów**:
    *   Ataki na modele splotowe (CNN) na zbiorze **MNIST**.
    *   Ataki na zaawansowane modele klasyfikacji obrazów (**ImageNet**).
    *   Implementacja metody **FGSM (Fast Gradient Sign Method)**.

3.  **Obrona - Trening Adwersarialny**:
    *   Implementacja mechanizmów obronnych polegających na douczaniu modelu na wygenerowanych przykładach adwersarialnych w celu zwiększenia jego odporności na ataki.

## Technologie i Biblioteki

Projekt został zrealizowany w języku **Python** z wykorzystaniem interaktywnych notatników **Jupyter Notebook**. Wykorzystane technologie to między innymi:

*   **TensorFlow** / **PyTorch**: Frameworki do uczenia głębokiego.
*   **Adversarial Robustness Toolbox (ART)**: Biblioteka do zapewniania bezpieczeństwa modeli AI.
*   **TextAttack**: Framework do ataków adwersarialnych, augmentacji danych i treningu adwersarialnego w NLP.
*   **Hugging Face Transformers & Datasets**: Dostęp do wytrenowanych modeli i zbiorów danych.
*   **Scikit-learn**: Klasyczne algorytmy uczenia maszynowego i narzędzia do ewaluacji.
*   **Pandas, NumPy**: Przetwarzanie i analiza danych.
*   **Matplotlib**: Wizualizacja wyników.

## Struktura Katalogów

Główny kod projektu znajduje się w katalogu `Adversarial_Attacks`. Poniżej znajduje się opis kluczowych plików:

*   `Adversarial_Attack_Email_Spam_ART.ipynb`: Atak HopSkipJump (ART) przeciwko modelowi regresji logistycznej na zbiorze Enron.
*   `Adversarial_Attack_Spam_Filter.ipynb`: Ataki TextBugger, TextFooler i DeepWordBug przeciwko modelowi </br> BERT-Tiny na zbiorze SMS Spam.
*   `Adversarial_attack_1.ipynb`: Demonstracja ataku FGSM na prosty model CNN (zbiór MNIST).
*   `Adversarial_attack_TextAttackv1.ipynb`: Eksperymenty z metodami TextFooler i PWWS na modelu DistilBERT (analiza sentymentu).
*   `Adversarial_attack_V2.ipynb`: Atak FGSM na model ImageNet (klasyfikacja obrazów).
*   `Adversarial_trainingV1.ipynb`: Trening adwersarialny modelu CNN na zbiorze MNIST w celu zwiększenia odporności.
*   `CSV_based_attack.ipynb`: Eksperymenty na danych w formacie CSV.
*   `translate_notebook.py`: Skrypt pomocniczy do tłumaczenia zawartości notatników.
*   `requirements.txt`: Plik zawierający listę wszystkich zależności niezbędnych do uruchomienia projektu.
*   `*.csv` (np. `results.csv`, `textfooler_results.csv`): Pliki zawierające zapisane wyniki przeprowadzonych eksperymentów.

## Instalacja i Uruchomienie

Aby uruchomić projekt na lokalnej maszynie, postępuj zgodnie z poniższymi instrukcjami:

1.  **Sklonuj repozytorium** (jeśli jeszcze tego nie zrobiłeś).

2.  **Przejdź do katalogu projektu**:
    ```bash
    cd "Adversarial_Attacks"
    ```

3.  **Zalecane: Utwórz wirtualne środowisko Python**, aby uniknąć konfliktów bibliotek:
    ```bash
    python -m venv .venv
    # Aktywacja środowiska (Windows):
    .venv\Scripts\activate
    # Aktywacja środowiska (Linux/macOS):
    source .venv/bin/activate
    ```

4.  **Zainstaluj wymagane zależności**:
    ```bash
    pip install -r requirements.txt
    ```
    *Uwaga: Plik `requirements.txt` zawiera m.in. `tensorflow`, `torch`, `textattack`, `adversarial-robustness-toolbox`.*

5.  **Uruchom Jupyter Notebook/Lab**:
    ```bash
    jupyter lab
    ```
    lub
    ```bash
    jupyter notebook
    ```

6.  **Otwórz wybrany plik `.ipynb`** (np. `Adversarial_Attack_Email_Spam_ART.ipynb`) i uruchom komórki kodowe, aby przeprowadzić symulację ataku.

## Autor

Damian Todorowski - Projekt Inżynierski
