import os
import json
import hashlib

def  gerar_hash(caminho):
    sha256 = hashlib.sha256()
    try:
        with open (caminho, 'rb') as f:
            while True:
                bloco = f.read(8192)
                if not bloco:
                    break
                sha256.update(bloco)
            return sha256.hexdigest()
    except Exception as e:
        print(f"Erro ao abrir {caminho}: {e}")
        return None

#carregar hashe se tiver
def carregar_hashes():
    if os.path.exists("hashes.json"):
        with open("hashes.json", "r") as f:
            return json.load(f)
    return{}

#salvar hashe atualizado
def salvar_hashes(dados):
    with open("hashes.json", "w") as f:
        json.dump(dados, f, indent=4)

#main
def main():
    arquivos = [
        "seu arquivo"
    ]
    hashes_salvos = carregar_hashes()
    novos_hashes = {}

    for caminho in arquivos:
        hash_atual = gerar_hash(caminho)
        if hash_atual is None:
            continue

    if caminho in hashes_salvos:
        if hash_atual != hashes_salvos[caminho]:
            print(f"[ALTERADO] {caminho}")
        else:
            print(f"[SEM MUDANÇAS] {caminho}")
    else:
        print(f"[NOVO ARQUIVO] {caminho}")

    novos_hashes[caminho] = hash_atual
    salvar_hashes(novos_hashes)

if __name__ == "__main__":
    main()