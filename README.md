# Firmware & AI Pipeline Demo

**Author:** Mădălina Ștefania Toader  
**Email:** toaderms@gmail.com  

---

## **1. Descriere proiect**

Acest proiect este un demo de pipeline complet pentru un firmware ARM și modele AI.  
Scopul este să arăt cum se poate automatiza:

1. Build-ul codului ARM pentru arhitectura Cobalt/Neoverse.  
2. Generarea artefactelor model AI.  
3. Verificarea integrității artefactelor (checksum).  
4. Semnarea digitală a artefactelor și verificarea semnăturii.  

Proiectul combină **DevOps**, **cross-compilation ARM** și **Python scripting** într-un workflow real de tip CI/CD.

---

## **2. Arhitectură și tehnologii folosite**

- **Platformă:** Ubuntu 22.04  
- **Toolchain ARM:** `arm-none-eabi-gcc` (cross-compiler)  
- **Arhitectură firmware:** ARM Cortex-A76 / ARMv8-A, Neoverse  
- **Limbaje:** C pentru firmware, Python pentru scripting și pipeline  
- **Pipeline:** Simulat cu scripturi Python  
- **Criptografie:** RSA-PSS pentru semnare și verificare artefacte  

**Fișiere cheie și rolul lor:**

| Fișier | Rol |
|--------|-----|
| `start.s` | Cod bootstrap ARM |
| `src/main.c` | Cod firmware principal |
| `linker.ld` | Script de link pentru ELF/BIN |
| `ex1_bin_io.py` | Modificare binar model AI |
| `ex2_checksum.py` | Calculează MD5 & SHA256 pentru fișier |
| `sign_artifact.py` | Semnează artefactul cu cheia privată |
| `verify_signature.py` | Verifică semnătura artefactului |
| `run_full_pipeline.py` | Rulează pipeline-ul complet |
| `model/build_model.py` | Generează model AI binar |

---

## **3. Pipeline workflow**

Build Model (Python) ---> Modify Binary (Python) ---> Compute Checksums (Python)
| |
| v
v Sign Artifact (Python)
Cross-Compile Firmware (ARM GCC) |
| v
| Verify Signature (Python)
v
Generate ELF/BIN/MAP files

yaml
Copy code

- `run_full_pipeline.py` rulează toate scripturile în ordine, simulând un pipeline CI/CD.

---

## **4. Comenzi de rulare**

1. **Build model AI și firmware**

```bash
python3 model/build_model.py
make
Rulează pipeline complet

bash
Copy code
python3 run_full_pipeline.py
Verificare semnătură manuală

bash
Copy code
python3 sign_artifact.py keys/private_key_new.pem model_build/model.bin signed/model.bin.sig
python3 verify_signature.py keys/public_key_new.pem model_build/model.bin signed/model.b
