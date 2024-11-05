import re
import os
import subprocess
from datetime import datetime

lilypond_path = "/Users/master/Documents/lilypond-2.24.3/bin/lilypond"

# Cartella di output per le partiture
output_folder = "_site/assets/img/scores"
os.makedirs(output_folder, exist_ok=True)

# Trova i file HTML solo nella cartella _site e nelle sue sottocartelle
for root, dirs, files in os.walk("_site"):
    for filename in files:
        if filename.endswith(".html"):
            file_path = os.path.join(root, filename)
            with open(file_path, "r") as file:
                content = file.read()

            # Trova tutti i div con classe lilyFragment
            lilypond_blocks = re.findall(r'<div class="lilyFragment">(.*?)</div>', content, re.DOTALL)
            
            for code in lilypond_blocks:
                # Genera un nome file unico usando data e ora
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                output_path = f"{output_folder}/{filename}-{timestamp}"

                # Salva il codice lilypond temporaneamente
                temp_file_path = "temp.ly"
                with open(temp_file_path, "w") as temp_file:
                    temp_file.write(code)
                
                # Compila il codice LilyPond in SVG
                subprocess.run([lilypond_path, "-dbackend=svg", "-o", output_path, temp_file_path])
                
                # Rimuovi il file temporaneo dopo la compilazione
                os.remove(temp_file_path)
                
                # Sostituisci il div nel contenuto con l’immagine SVG
                svg_path = f"{output_path}.svg"
                img_tag = f'<img src="{svg_path}" alt="Partitura generata">'
                content = content.replace(f'<div class="lilyFragment">{code}</div>', img_tag)

            # Salva le modifiche nel file HTML
            with open(file_path, "w") as file:
                file.write(content)
