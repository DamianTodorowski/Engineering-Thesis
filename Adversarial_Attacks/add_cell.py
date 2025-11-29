import json
import os

file_path = r"c:\Users\Damian\Documents\GitHub\Engieering Thesis\Adversarial_Attacks\Adversarial_Attack_Spam_Filter.ipynb"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_cell = {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Interpretacja wyników\n",
    "\n",
    "Wykres słupkowy przedstawia podsumowanie skuteczności ataku adwersarzowego na wybranej próbce danych. Poniżej znajduje się wyjaśnienie poszczególnych kategorii:\n",
    "\n",
    "- **Sukces (Success)**: Liczba przykładów, dla których atak zakończył się powodzeniem. Oznacza to, że algorytm zdołał zmodyfikować tekst wejściowy w taki sposób, że model zmienił swoją predykcję (np. z \"spam\" na \"nie-spam\"), zachowując jednocześnie semantyczne podobieństwo do oryginału.\n",
    "\n",
    "- **Porażka (Failed)**: Liczba przykładów, dla których atak nie powiódł się. Algorytm nie był w stanie znaleźć takiej modyfikacji tekstu, która zmyliłaby model, przy zachowaniu zadanych ograniczeń (np. maksymalna liczba zmienionych słów, minimalne podobieństwo semantyczne).\n",
    "\n",
    "- **Pominięte (Skipped)**: Liczba przykładów, które zostały pominięte w procesie ataku. Najczęściej dzieje się tak, gdy model błędnie sklasyfikował oryginalny tekst jeszcze przed atakiem. Ataki adwersarzowe zazwyczaj przeprowadza się tylko na poprawnie sklasyfikowanych przykładach, aby mierzyć skuteczność samego ataku, a nie błędy modelu."
   ]
}

data['cells'].append(new_cell)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1, ensure_ascii=False)

print("Cell added successfully.")
