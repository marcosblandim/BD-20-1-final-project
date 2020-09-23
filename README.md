# BD-20-1-final-project

## Geral
- SGBD -> Postgresql
- CRUS -> Python (?), JS, Go, ruby (o que é CRUS?)

## Ideias

### COVID
- sistema de mapeamento de casos em qualquer região do mundo, com entidades como
  - **pessoa**: nome, cpf, endereço, idade, histórico clínico, é grupo de risco (booleano derivado do histórico clínico), data de aparição de sintomas, data de confirmação da doença, tipo de teste feito para tal confirmação, gravidade do caso, cidade (chave externa), com quantas pessoas mora (pensar em outros dados nessa linha, que deêm pra gerar estatísticas úteis)
  - **cidade**: nome, número de habitantes, país (chave externa), adotou isolamento/outros meios de combate ao COVID, número de casos confirmados, número de testes, o quanto adotou as recomendações da ONU (por exemplo) (pensar em algum meio de determinar isso de forma padronizada e bem determinada)
  - **país**: nome, número de habitantes, número de casos confirmados, número de testes, adotou isolamento/outros meios de combate ao COVID, o quanto adotou as recomendações da ONU (por exemplo) (pensar em algum meio de determinar isso de forma padronizada e bem determinada)
  - **pensar em mais entidades**
- _gravidade do caso_ seria algo que identificasse o estado de saúde da pessoa no ápice da doença, como um valor de 0 a 10 por exemplo (seria algo padronizado e bem determinado)
- note que _gravidade do caso_ seria um atributo "volátil", ou seja, a pessoa iria atualizando conforme seu estado de saúde fosse mudando

#### Parágrafo de proposta
Escrever o parágrafo aqui.

-----
