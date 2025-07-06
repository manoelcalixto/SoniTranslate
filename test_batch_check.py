#!/usr/bin/env python3
import os

# Verificar se a variável está definida
coqui_batch_env = os.getenv("COQUI_TTS_BATCH")
print(f"COQUI_TTS_BATCH = {coqui_batch_env}")

if coqui_batch_env is not None:
    batch_size_env = max(1, int(coqui_batch_env))
    print(f"Batch size será: {batch_size_env}")
else:
    print("COQUI_TTS_BATCH não está definida - usando padrão 2") 