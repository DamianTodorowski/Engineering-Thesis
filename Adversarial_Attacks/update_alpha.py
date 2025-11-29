import sys
import os

file_path = r"c:\Users\Damian\Documents\GitHub\Engieering Thesis\Adversarial_Attacks\Adversarial_Attack_Email_Spam_ART.ipynb"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace alpha=0.7 with alpha=0.5
    new_content = content.replace("alpha=0.7", "alpha=0.5")

    if content == new_content:
        print("No changes made. 'alpha=0.7' not found.")
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated alpha values in notebook.")

except Exception as e:
    print(f"Error: {e}")
