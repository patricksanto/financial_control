#!/usr/bin/env python3
import json
import sys

def analyze_month(year, month):
    # Carregar dados
    month_key = f"{year}-{month:02d}"
    with open(f'data/{year}/categorized_{year}_{month:02d}.json', 'r') as f:
        data = json.load(f)
    
    with open('budget_config.json', 'r') as f:
        budget = json.load(f)['monthly_budget']
    
    # Calcular totais
    total_budget = sum(budget.values())
    total_spent = sum(abs(sum(t['amount'] for t in transactions)) 
                     for cat, transactions in data.items() 
                     if cat != 'Receitas/Transferências')
    diff = total_spent - total_budget
    
    # Identificar estouros
    overages = []
    for cat, expected in budget.items():
        if cat in data:
            actual = abs(sum(t['amount'] for t in data[cat]))
            if actual > expected:
                diff_cat = actual - expected
                pct = (actual / expected * 100) - 100
                overages.append({
                    'category': cat,
                    'budgeted': expected,
                    'actual': actual,
                    'difference': diff_cat,
                    'percent': pct
                })
    
    overages.sort(key=lambda x: x['difference'], reverse=True)
    
    # Carregar análises existentes
    try:
        with open('monthly_analysis.json', 'r') as f:
            all_analysis = json.load(f)
    except FileNotFoundError:
        all_analysis = {}
    
    # Criar entrada para este mês
    all_analysis[month_key] = {
        "total_budget": round(total_budget, 2),
        "total_spent": round(total_spent, 2),
        "difference": round(diff, 2),
        "percent_over": round(diff/total_budget*100, 1),
        "top_overages": overages[:3],
        "narrative": ""  # Será preenchido manualmente
    }
    
    # Salvar
    with open('monthly_analysis.json', 'w') as f:
        json.dump(all_analysis, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Análise salva em monthly_analysis.json")
    print(f"\n📊 DADOS PARA ANÁLISE - {month:02d}/{year}\n")
    print(f"💰 Orçamento: €{total_budget:.2f}")
    print(f"💸 Gasto: €{total_spent:.2f}")
    print(f"{'📈' if diff > 0 else '📉'} Diferença: €{diff:+.2f} ({(diff/total_budget*100):+.1f}%)\n")
    
    if overages:
        print("🔥 TOP 3 ESTOUROS:\n")
        for item in overages[:3]:
            print(f"  • {item['category']}: €{item['budgeted']:.2f} → €{item['actual']:.2f} (+€{item['difference']:.2f}, +{item['percent']:.1f}%)")
    
    print(f"\n📝 Agora edite monthly_analysis.json e adicione o campo 'narrative' para {month_key}")
    print("   Use | para separar parágrafos")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python3 analyze_month.py <ano> <mês>")
        print("Exemplo: python3 analyze_month.py 2026 02")
        sys.exit(1)
    
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    analyze_month(year, month)
