# 💰 Controle Financeiro

Sistema de categorização e análise de despesas mensais com visualização interativa.

## 📁 Estrutura do Projeto

```
financial_control/
├── data/
│   └── 2026/
│       ├── expenses_2026_02.csv          # Extrato original
│       └── categorized_2026_02.json      # Dados categorizados
├── index.html                             # Dashboard principal (multi-mês)
├── expenses_report.html                   # Relatório Fevereiro (legado)
├── GUIA_CATEGORIZACAO.md                 # Guia de categorias
└── README.md                             # Este arquivo
```

## 🚀 Como Usar

### Visualizar Relatórios

Abra o arquivo `index.html` no navegador:

```bash
open index.html
```

O dashboard permite:
- Selecionar diferentes meses
- Ver resumo de receitas, despesas e saldo
- Visualizar gráficos interativos
- Expandir categorias para ver transações detalhadas

### Adicionar Novo Mês

1. **Exportar extrato** do banco em formato CSV
2. **Salvar** como `data/YYYY/expenses_YYYY_MM.csv`
3. **Executar script** de categorização (criar script Python)
4. **Atualizar** `index.html` adicionando o novo mês no objeto `months`

## 📊 Categorias

O sistema utiliza 14 categorias principais:

- 💰 Receitas/Transferências
- 🏠 Moradia
- 🏥 Planos de Saúde
- 🛒 Supermercado
- 🚆 Transporte
- 🎓 Educação
- 💼 Empresa Gustavo Otero
- 💳 Assinaturas & Serviços Digitais
- 🍕 Restaurantes & Delivery
- 🌿 Coffeeshop
- 💊 Farmácia & Saúde
- 🏋️ Academia
- 🛍️ Compras & Varejo
- 🎉 Lazer & Entretenimento
- 🏦 Taxas Bancárias
- ❓ Outros

Consulte `GUIA_CATEGORIZACAO.md` para detalhes completos.

## 🔧 Tecnologias

- HTML5 + CSS3
- JavaScript (Vanilla)
- Chart.js (gráficos)
- Python (processamento de dados)

## 📝 Próximos Passos

- [ ] Criar script Python automatizado para categorização
- [ ] Adicionar comparação entre meses
- [ ] Implementar gráfico de evolução temporal
- [ ] Exportar relatórios em PDF

---

**Última atualização:** Fevereiro 2026
