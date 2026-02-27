#!/usr/bin/env python3
import json
import re

# Ler dados corrigidos
with open('data/2026/categorized_2026_02.json', 'r') as f:
    feb_data = json.load(f)

# Ler HTML
with open('index.html', 'r') as f:
    html = f.read()

# Converter dados para string JSON compacta
feb_json = json.dumps(feb_data, separators=(',', ':'), ensure_ascii=False)

# Substituir dados de fevereiro no HTML
pattern = r"('2026-02':\s*\{\s*label:\s*'Fevereiro 2026',\s*data:\s*)(\{.*?\})\s*\}"
replacement = f"'2026-02': {{ label: 'Fevereiro 2026', data: {feb_json} }}"

html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# Salvar HTML atualizado
with open('index.html', 'w') as f:
    f.write(html)

print("✅ HTML atualizado com dados corrigidos de fevereiro")
print(f"   - Supermercado: €{abs(sum(t['amount'] for t in feb_data['Supermercado'])):.2f}")
print(f"   - Outros: €{abs(sum(t['amount'] for t in feb_data['Outros'])):.2f}")
