# BD-20-1-final-project

## GERAL
- SGBD -> Postgresql
- CRUS -> Python (?), JS, Go, ruby

-----
## Ideias

### COVID
- sistema de mapeamento de casos em qualquer região do mundo, com tabelas como
  - pessoa: nome, cpf, endereço, idade, condição de sáude, grupo de risco (derivado das condições de saúde), data de aparição de sintomas, data de confirmação da doença, tipo de teste feito para tal confirmação, cidade (chave externa)
  - cidade: país (chave externa)
  - país
