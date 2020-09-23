# BD-20-1-final-project

## GERAL
- SGBD -> Postgresql
- CRUS -> Python (?), JS, Go, ruby

-----
## Ideias

### COVID
- sistema de mapeamento de casos em qualquer região do mundo, com tabelas como
  - pessoa: nome, cpf, endereço, idade, histórico clínico, é grupo de risco (booleano derivado das condições de saúde), data de aparição de sintomas, data de confirmação da doença, tipo de teste feito para tal confirmação, gravidade do caso, cidade (chave externa), com quantas pessoas mora (pensar em outros dados nessa linha, que deêm pra gerar estatísticas úteis)
  - cidade: país (chave externa)
  - país
  - pensar em mais tabelas
- _gravidade do caso_ seria algo que identificasse o estado de saúde da pessoa no ápice da doença, como um valor de 0 a 10 por exemplo (seria algo padronizado e bem determinado)
- note que _gravidade do caso_ seria um atributo "volátil", ou seja, a pessoa iria atualizando conforme seu estado de saúde fosse mudando
