import json
import os

file_path = r"c:\Users\Damian\Documents\GitHub\Engieering Thesis\Adversarial_Attacks\Adversarial_Attack_Email_Spam_ART.ipynb"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def replace_text(text):
    replacements = {
        "# Adversarial Attack on Email Spam Filter using ART": "# Atak adwersarzowy na filtr spamu e-mail przy użyciu ART",
        "This notebook demonstrates how to use the **Adversarial Robustness Toolbox (ART)** to perform an adversarial attack on a simple email spam filter.": "Ten notatnik demonstruje, jak używać **Adversarial Robustness Toolbox (ART)** do przeprowadzenia ataku adwersarzowego na prosty filtr spamu e-mail.",
        "We will:": "Będziemy:",
        "1. Load the `SetFit/enron_spam` dataset.": "1. Ładować zbiór danych `SetFit/enron_spam`.",
        "2. Train a Logistic Regression model on TF-IDF features.": "2. Trenować model regresji logistycznej na cechach TF-IDF.",
        "3. Use ART's `HopSkipJump` attack to generate adversarial examples in the feature space.": "3. Używać ataku `HopSkipJump` z ART do generowania przykładów adwersarzowych w przestrzeni cech.",
        "4. Evaluate the robustness of the model.": "4. Oceniać odporność modelu.",
        "# Install necessary libraries if not already installed": "# Zainstaluj niezbędne biblioteki, jeśli nie są jeszcze zainstalowane",
        "# Set random seed for reproducibility": "# Ustaw ziarno losowości dla powtarzalności",
        "## 1. Load and Preprocess Data": "## 1. Załaduj i przetwórz dane",
        "We use the `SetFit/enron_spam` dataset, which contains emails labeled as spam or ham.": "Używamy zbioru danych `SetFit/enron_spam`, który zawiera e-maile oznaczone jako spam lub ham (nie-spam).",
        "# Load dataset": "# Załaduj zbiór danych",
        "# Display first few rows": "# Wyświetl kilka pierwszych wierszy",
        "# Check class distribution": "# Sprawdź rozkład klas",
        "# Prepare data": "# Przygotuj dane",
        "y = df['label'].values  # 0 for ham, 1 for spam": "y = df['label'].values  # 0 dla ham, 1 dla spam",
        "# Split into train and test sets": "# Podziel na zbiory treningowe i testowe",
        "# Vectorize text using TF-IDF": "# Wektoryzuj tekst używając TF-IDF",
        "vectorizer = TfidfVectorizer(max_features=1000) # Limit features for speed and visualization": "vectorizer = TfidfVectorizer(max_features=1000) # Ogranicz cechy dla szybkości i wizualizacji",
        "## 2. Train Target Model": "## 2. Trenuj model docelowy",
        "We train a simple Logistic Regression model.": "Trenujemy prosty model regresji logistycznej.",
        "# Evaluate on test set": "# Oceń na zbiorze testowym",
        "## 3. Create ART Classifier": "## 3. Utwórz klasyfikator ART",
        "We wrap the Scikit-learn model with ART's `SklearnClassifier` to enable adversarial attacks.": "Opakowujemy model Scikit-learn za pomocą `SklearnClassifier` z ART, aby umożliwić ataki adwersarzowe.",
        "# Create ART classifier": "# Utwórz klasyfikator ART",
        "# Verify accuracy using ART classifier": "# Zweryfikuj dokładność używając klasyfikatora ART",
        "## 4. Perform Adversarial Attack (HopSkipJump)": "## 4. Przeprowadź atak adwersarzowy (HopSkipJump)",
        "We use the **HopSkipJump** attack, a powerful black-box attack that requires only output class probabilities. We will generate adversarial examples for a subset of the test data (spam emails) to try and evade the filter.": "Używamy ataku **HopSkipJump**, potężnego ataku typu black-box, który wymaga jedynie prawdopodobieństw klas wyjściowych. Wygenerujemy przykłady adwersarzowe dla podzbioru danych testowych (e-maile spam), aby spróbować ominąć filtr.",
        "# Select a subset of Spam emails to attack (Target: Spam -> Ham)": "# Wybierz podzbiór e-maili spam do ataku (Cel: Spam -> Ham)",
        "target_class = 1 # Spam": "target_class = 1 # Spam",
        "attack_indices = np.where(y_test == target_class)[0][:20] # Attack first 20 spam emails": "attack_indices = np.where(y_test == target_class)[0][:20] # Atakuj pierwsze 20 e-maili spam",
        "# Initialize HopSkipJump attack": "# Zainicjuj atak HopSkipJump",
        "# Generate adversarial examples": "# Wygeneruj przykłady adwersarzowe",
        "# Evaluate the attack": "# Oceń atak",
        "## 5. Analysis": "## 5. Analiza",
        "Let's compare the original and adversarial feature vectors to see how much perturbation was needed.": "Porównajmy oryginalne i adwersarzowe wektory cech, aby zobaczyć, jak duże zaburzenie było potrzebne.",
        ";# Calculate L2 distance (perturbation magnitude)": ";# Oblicz odległość L2 (wielkość zaburzenia)",
        "# Visualize perturbation for the first example": "# Wizualizuj zaburzenie dla pierwszego przykładu",
        "plt.plot(X_attack[0], label='Original (Spam)', alpha=0.7)": "plt.plot(X_attack[0], label='Oryginał (Spam)', alpha=0.7)",
        "plt.plot(X_adv[0], label='Adversarial (Classified as Ham)', alpha=0.7, linestyle='--')": "plt.plot(X_adv[0], label='Adwersarz (Sklasyfikowany jako Ham)', alpha=0.7, linestyle='--')",
        "plt.title(\"Feature Vector Comparison (TF-IDF)\")": "plt.title(\"Porównanie wektorów cech (TF-IDF)\")",
        "plt.xlabel(\"Feature Index\")": "plt.xlabel(\"Indeks cechy\")",
        "plt.ylabel(\"TF-IDF Value\")": "plt.ylabel(\"Wartość TF-IDF\")",
        "### Note on Feature Space Attacks": "### Uwaga dotycząca ataków w przestrzeni cech",
        "This attack operates in the **feature space** (TF-IDF vectors). In a real-world scenario, mapping these perturbed vectors back to discrete text (the \"inverse problem\") is non-trivial. However, this demonstrates the model's mathematical vulnerability to small perturbations in its input space.": "Ten atak działa w **przestrzeni cech** (wektory TF-IDF). W rzeczywistym scenariuszu odwzorowanie tych zaburzonych wektorów z powrotem na dyskretny tekst (\"problem odwrotny\") jest nietrywialne. Jednakże demonstruje to matematyczną podatność modelu na małe zaburzenia w jego przestrzeni wejściowej."
    }
    
    for en, pl in replacements.items():
        if en in text:
            text = text.replace(en, pl)
    return text

for cell in data['cells']:
    if 'source' in cell:
        new_source = []
        for line in cell['source']:
            new_source.append(replace_text(line))
        cell['source'] = new_source

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1, ensure_ascii=False)

print("Translation completed successfully.")
