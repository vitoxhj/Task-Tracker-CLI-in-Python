import json
import os

def create_json(arquive,dados):
    if not os.path.exists(arquive):
        with open(arquive, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    else:
        return
