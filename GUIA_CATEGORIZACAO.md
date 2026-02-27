# 📋 Guia de Categorização de Despesas

Este documento serve como referência para categorizar as despesas mensais do extrato bancário.

## 📊 Categorias e Regras

### 💰 Receitas/Transferências
**Critério:** Todos os valores positivos (entradas)
- Transferências de Gustavo Keusen Otero
- Transferências de Dev Patrick
- Transferências via Wise
- Cashback do bunq
- Qualquer outra entrada de dinheiro

---

### 🏠 Moradia
**Despesas fixas relacionadas à residência**
- **Aluguel:** HUNWONEN (Derdengelden Hunwonen)
- **Água:** VITENS NV
- **Internet/Telefone:** KPN B.V., KPN - Mobiel

---

### 🏥 Planos de Saúde
**Seguros e planos de saúde**
- **HollandZorg:** Zorgverzekering (seguro saúde mensal)
- **HollandZorg:** Eigen bijdrage (contribuição própria/copagamento)

---

### 🛒 Supermercado
**Compras de alimentação e produtos básicos**
- PLUS Beestenmarkt
- Albert Heijn (todas as lojas)
- Jumbo (todas as lojas)
- Dirk van den Broek
- BCK*AH (Albert Heijn to go - estações e lojas de conveniência)
- BCK*AH to go (todas as variações)
- BCK*AH Station (todas as variações)

---

### 🚆 Transporte
**Deslocamentos e viagens**
- NS Groep (trem)
- OVpay (transporte público)
- Estacionamento (AT3, AT5 Den Bosch, etc.)

---

### 🎓 Educação
**Despesas educacionais**
- Saxion (universidade)
- **Pagamento faculdade:** Transferência para P Silva Gomes dos CJ (NL08ABNA0142002305) - €625,00

---

### 💼 Empresa Gustavo Otero
**Despesas relacionadas ao negócio de terapia**
- **Facebook Ads:** FACEBK (anúncios)
- **Apple Services:** APPLE.COM/BILL (serviços Apple)
- **Zoom:** ZOOM.COM (videoconferências)

---

### 💳 Assinaturas & Serviços Digitais
**Serviços de streaming, software e assinaturas pessoais**
- Spotify
- ChatGPT / OpenAI
- YouTube Premium
- Google (Google One, etc.)
- Railway (hospedagem)
- Canva
- Singa Premium
- Microsoft 365
- WOW Presents Plus

**⚠️ Exceção:** APPLE.COM/BILL e ZOOM vão para "Empresa Gustavo Otero"

---

### 🍕 Restaurantes & Delivery
**Alimentação fora de casa**
- Domino's Pizza
- MIMIK eten & drinken
- Davo Proeflokaal
- Banketbakkerij Lent
- Broodbode Deventer
- K&B Venlo

---

### 🌿 Coffeeshop
**Categoria específica devido à frequência**
- Coffeeshop Dr Pleasure / Dr. Pleasur

---

### 💊 Farmácia & Saúde
**Produtos de farmácia e saúde (não inclui plano de saúde)**
- Kruidvat
- Holland & Barrett

---

### 🏋️ Academia
**Atividades físicas**
- SportCity (mensalidade)

---

### 🛍️ Compras & Varejo
**Lojas diversas e compras gerais**
- Coolblue (eletrônicos/assinaturas)
- Action (variedades)
- Toychamp (brinquedos)
- Donerix (kebab/restaurante)
- 1444 Deventer (loja)

---

### 🎉 Lazer & Entretenimento
**Diversão e eventos sociais**
- Midtown Blues Rock-C (bar/música)
- SumUp Studieverenigi (associação estudantil)
- Facebook (não relacionado à empresa)

---

### 🏦 Taxas Bancárias
**Custos bancários**
- bunq BV (nota fiscal/invoice)

---

### ❓ Outros
**Transações que não se encaixam nas categorias acima**
- Bookeo (agendamentos)
- Transações não identificadas
- Despesas pontuais sem categoria específica

---

## 🔄 Processo Mensal

1. **Exportar** o extrato bancário em formato CSV
2. **Nomear** o arquivo como `expenses_[mes].csv` (ex: `expenses_feb.csv`)
3. **Executar** o script Python de categorização
4. **Revisar** categorias e fazer ajustes necessários
5. **Gerar** o relatório HTML interativo
6. **Analisar** os gráficos e identificar oportunidades de economia

---

## 📝 Notas Importantes

- **Valores positivos** sempre vão para "Receitas/Transferências"
- **HollandZorg** tem dois tipos: seguro mensal (Moradia) e copagamento (Farmácia & Saúde) → **ATUALIZADO:** Ambos vão para "Planos de Saúde"
- **Despesas da empresa** do Gustavo devem ser separadas das pessoais
- **Pagamento da faculdade** é identificado pela conta NL08ABNA0142002305 e valor de €625,00

---

## 🎯 Dicas de Análise

- Compare mês a mês para identificar tendências
- Fique atento a aumentos em categorias específicas
- Revise a categoria "Outros" - se houver muitas transações, considere criar novas categorias
- Use os gráficos para visualizar onde está indo a maior parte do dinheiro

---

**Última atualização:** Fevereiro 2026
