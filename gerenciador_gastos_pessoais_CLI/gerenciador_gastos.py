import json
import os

def carregar_dados():
    """Carrega os dados do arquivo JSON ou cria uma lista vazia se não existir."""
    if not os.path.exists('dados.json'):
        return []
    with open('dados.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(transacoes):
    """Salva a lista de transações no arquivo JSON."""
    with open('dados.json', 'w', encoding='utf-8') as f:
        json.dump(transacoes, f, indent=4, ensure_ascii=False)

def adicionar_transacao(tipo):
    """Adiciona uma nova receita ou despesa."""
    descricao = input(f"Descrição da {tipo}: ")
    try:
        valor = float(input(f"Valor da {tipo}: "))
        transacoes = carregar_dados()
        transacoes.append({
            "tipo": tipo,
            "descricao": descricao,
            "valor": valor
        })
        salvar_dados(transacoes)
        print(f"\n✅ {tipo.capitalize()} registrada com sucesso!")
    except ValueError:
        print("\n❌ Erro: Por favor, insira um valor numérico válido (use ponto para decimais).")

def exibir_extrato():
    """Exibe movimentações com análise percentual sobre a receita total."""
    transacoes = carregar_dados()
    if not transacoes:
        print("\n⚠️ Nenhuma transação registrada ainda.")
        return

    # Passo 1: Cálculo prévio dos totais
    total_receitas = sum(t['valor'] for t in transacoes if t['tipo'] == 'receita')
    total_despesas = sum(t['valor'] for t in transacoes if t['tipo'] == 'despesa')

    print("\n" + "="*60)
    print(f"{'TIPO':<10} | {'DESCRIÇÃO':<20} | {'VALOR':<12} | {'% S/ RECEITA'}")
    print("-" * 60)

    for t in transacoes:
        porcentagem_str = "-"
        if t['tipo'] == 'despesa' and total_receitas > 0:
            # Cálculo da porcentagem: (Parte / Todo) * 100
            perc = (t['valor'] / total_receitas) * 100
            porcentagem_str = f"{perc:>10.1f}%"
        
        print(f"{t['tipo'].upper():<10} | {t['descricao']:<20} | R$ {t['valor']:>9.2f} | {porcentagem_str}")

    saldo = total_receitas - total_despesas
    
    print("-" * 60)
    print(f"TOTAL RECEITAS:  R$ {total_receitas:>10.2f}")
    print(f"TOTAL DESPESAS:  R$ {total_despesas:>10.2f} ({((total_despesas/total_receitas)*100 if total_receitas > 0 else 0):.1f}% do total)")
    print(f"SALDO ATUAL:     R$ {saldo:>10.2f}")
    
    # "Pulo do Gato": Alerta de saúde financeira
    if saldo < 0:
        print("\n🔴 ATENÇÃO: Suas despesas superaram suas receitas!")
    elif total_receitas > 0 and total_despesas > total_receitas * 0.7:
        print("\n🟡 ALERTA: Você já comprometeu mais de 70% da sua renda.")
    
    print("="*60)
    
def menu():
    while True:
        print("\n--- GERENCIADOR DE GASTOS PESSOAIS ---")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Ver Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_transacao('receita')
        elif opcao == '2':
            adicionar_transacao('despesa')
        elif opcao == '3':
            exibir_extrato()
        elif opcao == '4':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()