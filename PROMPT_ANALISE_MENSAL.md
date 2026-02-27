# 📝 Prompt para Análise Mensal de Orçamento

Use este prompt para gerar análises mensais dos gastos vs orçamento.

## Prompt

```
Analise os dados de gastos do mês comparando com o orçamento planejado.

DADOS:
- Orçamento total: €4.115,79
- Gasto real: [INSERIR TOTAL]
- Diferença: [INSERIR DIFERENÇA]

CATEGORIAS QUE ESTOURARAM:
[INSERIR LISTA DE CATEGORIAS COM VALORES]

INSTRUÇÕES:
1. Escreva uma análise concisa (2-3 parágrafos curtos)
2. Use linguagem divertida e descontraída, não técnica
3. Identifique os 2-3 principais vilões que estouraram o orçamento
4. Explique o impacto de cada um de forma clara
5. Use emojis para dar personalidade
6. Seja direto e honesto sobre o que saiu da curva
7. Termine com uma frase motivacional ou reflexão leve

EXEMPLO DE TOM:
"Opa, parece que alguém andou exagerando no [categoria]! 🚨 
O orçamento era de €X mas foram €Y - uma diferença de €Z que pesou bastante no bolso..."
```

## Como Usar

1. Execute o script de análise para obter os números:
```bash
python3 analyze_month.py 2026 02
```

2. Copie os dados e cole no prompt acima
3. Use um LLM (ChatGPT, Claude, etc) para gerar a análise
4. Copie o resultado e adicione no `index.html` na seção de overview

## Formato de Saída

A análise deve ter:
- 📊 Título com mês/ano
- 2-3 parágrafos curtos
- Destaque para os principais estouros
- Tom leve mas informativo
- Emojis para dar vida ao texto
