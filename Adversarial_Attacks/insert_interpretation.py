import json
import os

file_path = r"c:\Users\Damian\Documents\GitHub\Engieering Thesis\Adversarial_Attacks\Adversarial_Attack_Email_Spam_ART.ipynb"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_cell = {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Interpretacja wyników\n",
    "\n",
    "Wykres przedstawia porównanie wektorów cech TF-IDF dla oryginalnej wiadomości spam (linia ciągła) oraz wygenerowanego przykładu adwersarialnego (linia przerywana). Widoczne różnice w wartościach cech na osi Y dla poszczególnych indeksów (oś X) obrazują zaburzenia wprowadzone przez algorytm ataku. Mimo że zmiany te mogą wydawać się niewielkie (co potwierdza niska średnia odległość L2), są one wystarczające, aby zmylić model klasyfikacyjny i spowodować błędną klasyfikację wiadomości jako 'ham' (nie-spam)."
   ]
}

# Insert after the plot cell (which is index 13, so insert at 14)
# Check if index 14 exists, if so insert, else append
if len(data['cells']) > 14:
    data['cells'].insert(14, new_cell)
else:
    data['cells'].append(new_cell)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1, ensure_ascii=False)

print("Interpretation cell inserted successfully.")
