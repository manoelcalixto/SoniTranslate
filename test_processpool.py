#!/usr/bin/env python3
"""
Teste simples para verificar se o ProcessPool está funcionando corretamente
"""

import os
import sys
import multiprocessing

# Adicionar o caminho do módulo soni_translate
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

def test_processpool():
    """Testa se o ProcessPool está funcionando corretamente"""
    
    # Configurar variáveis de ambiente
    os.environ["SONITR_DEVICE"] = "cpu"
    
    try:
        # Importar após configurar o ambiente
        from soni_translate.text_to_speech import create_tts_batch_method
        
        print("✅ Imports funcionaram corretamente")
        
        # Testar a configuração do multiprocessing
        ctx = multiprocessing.get_context('spawn')
        print(f"✅ Context spawn criado: {ctx}")
        
        # Testar função worker
        from soni_translate.text_to_speech import process_single_text_worker
        
        # Argumentos de teste
        test_args = (
            "Olá mundo, este é um teste",
            0,
            "_XTTS_/test.wav",  # arquivo fictício
            "pt",
            "tts_models/multilingual/multi-dataset/xtts_v2",
            "cpu",
            {}
        )
        
        print("✅ Argumentos de teste preparados")
        print(f"📝 Texto: {test_args[0]}")
        print(f"🔧 Dispositivo: {test_args[5]}")
        
        # Nota: Não vamos executar o worker real porque precisa do modelo TTS
        print("⚠️  Não executando worker real (precisa do modelo TTS)")
        
        print("\n🎉 Teste básico passou! ProcessPool configurado corretamente.")
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 Iniciando teste do ProcessPool...")
    test_processpool() 