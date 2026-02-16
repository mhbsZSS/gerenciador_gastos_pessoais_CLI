# 💰 Gerenciador de Gastos Pessoais (CLI)

Um sistema de controle financeiro via linha de comando desenvolvido em **Python**. O projeto permite o registro de receitas e despesas, oferecendo um extrato detalhado com análises percentuais e alertas de saúde financeira.

## 🚀 Funcionalidades

- **Registro de Transações:** Adição de receitas e despesas com descrição e valor.
- **Persistência de Dados:** Armazenamento automático em formato `JSON`, garantindo que os dados não sejam perdidos ao fechar o programa.
- **Análise Matemática:** - Cálculo automático de saldo.
  - Cálculo da representatividade de cada despesa em relação à receita total (%).
- **Tratamento de Erros:** Validação de entradas numéricas para evitar falhas de execução.
- **Alertas Inteligentes:** Avisos visuais caso o saldo esteja negativo ou os gastos ultrapassem 70% da renda.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca `json`**: Para manipulação de arquivos de dados.
- **Biblioteca `os`**: Para gestão de caminhos de arquivos.

## 📂 Estrutura do Projeto

```text
.
├── gerenciador_gastos.py  # Código fonte principal
├── dados.json             # Arquivo de persistência (gerado automaticamente)
└── README.md              # Documentação do projeto