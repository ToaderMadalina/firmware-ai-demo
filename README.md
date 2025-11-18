# Firmware + AI Model Demo Pipeline

## Descriere
Acest proiect demonstrează un pipeline integrat pentru firmware ARM bare-metal și generare de model AI, cu simulare locală a unui pipeline de tip Azure DevOps.

Poate fi folosit pentru interviuri pentru roluri DevOps/Embedded/CI/CD.

---

## Structura proiectului

firmware-ai-demo/
│
├── src/ # Cod firmware ARM bare-metal
│ └── main.c
├── start.s # Startup minimal ARM
├── linker.ld # Linker script pentru ARM
├── Makefile # Build firmware ARM
├── model/
│ ├── build_model.py # Script pentru generare artefact AI
│ └── validate_model.py # Script de validare AI
├── pipelines/
│ └── azure-pipelines-demo.yml # YAML demo pipeline
├── run_pipeline.sh # Script local simulare pipeline
├── signed/ # Folder artefacte semnate (generat la run_pipeline.sh)
└── README.md # Acest fișier


---

## Pași de rulare (simulare locală)

1. Asigură-te că ai instalate:
   - `gcc-arm-none-eabi`, `make`, `python3`
2. Clonează repository-ul
3. Rulăm pipeline-ul local:

```bash
chmod +x run_pipeline.sh
./run_pipeline.sh


Veți vedea:
Build firmware (build/main.bin)
Build model AI (model_build/model.bin)
Validare model
Semnare și publicare artefacte (signed/)

Explicație rapidă

Firmware ARM: cod bare-metal simplu cu un counter infinit.

Model AI: script Python dummy care generează un fișier binar + metadata.

Pipeline YAML: reprezintă fluxul de build + validare + semnare (simulat).

run_pipeline.sh: execută toate etapele secvențial local.

Observații

Pipeline-ul local simulează complet un pipeline DevOps fără a necesita cont Azure.

Artefactele generate pot fi folosite pentru demonstrații la interviu.

Semnarea artefactelor este simulată, în producție ar folosi GPG/KeyVault.
