#!/bin/bash

set -e  # exit on first error
echo "===== Starting Local Pipeline Simulation ====="

# Step 1: Build Firmware ARM
echo "Step 1: Building firmware..."
make clean
make
echo "Firmware build complete."

# Step 2: Build / Generate AI Model
echo "Step 2: Generating AI model..."
python3 model/build_model.py
echo "AI model build complete."

# Step 3: Sign / Publish Artifacts
echo "Step 3: Signing and publishing artifacts..."
mkdir -p signed
cp build/main.bin signed/main.bin.sig
cp model_build/model.bin signed/model.bin.sig
cp model_build/model_metadata.txt signed/
echo "Artifacts signed and published (simulated)."

# Step 4: Verify Artifacts
echo "Step 4: Listing final artifacts:"
ls -l signed/
echo "Firmware size: $(stat -c%s signed/main.bin.sig) bytes"
echo "Model size: $(stat -c%s signed/model.bin.sig) bytes"
cat signed/model_metadata.txt

echo "===== Local Pipeline Simulation Complete ====="
