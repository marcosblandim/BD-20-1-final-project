# BD-20-1-final-project

## TODO
- mandar todas as pks disponiveis para aquela entidade, listar elas em um select (parecido com o front do visita), e usar elas para mostrar a relacao depois.
- fazer as PKs levarem para uma tela de visualização da relacao
  - paciente cadastra 1 leito e N visitantes
  - visitante cadastra N pacientes
  - (implementar depois) leito cadastra N pacientes
  - toda entidade vai ter um link que leva para uma tela de visualizacao de suas pks (uma PK por vez)
- implementar os contadores na home
- melhorar o front
- resolver o problema das entradas negativas nos numero inteiros
- colocar alerta em todas as acoes
- fazer legenda do estado de saúde
- transformar o estado de saude em um select que no back vira um numero antes de ir pro bd
- tornar os inputs nao obrigatorios como nao requireds no front, e arrumar as querys para conseguirem inserir vazio

## Geral
- SGBD -> MySQL
- CRUS -> Python.

## Ideias

### COVID
- sistema de mapeamento de casos em qualquer região do mundo, com entidades como
  - **pessoa**: nome, cpf, endereço, idade, histórico clínico, é grupo de risco (booleano derivado do histórico clínico), data de aparição de sintomas, data de confirmação da doença, tipo de teste feito para tal confirmação, gravidade do caso, cidade (chave externa), com quantas pessoas mora (pensar em outros dados nessa linha, que deêm pra gerar estatísticas úteis)
  - **cidade**: nome, número de habitantes, país (chave externa), adotou isolamento/outros meios de combate ao COVID, número de casos confirmados, número de testes, o quanto adotou as recomendações da ONU (por exemplo) (pensar em algum meio de determinar isso de forma padronizada e bem determinada)
  - **país**: nome, número de habitantes, número de casos confirmados, número de testes, adotou isolamento/outros meios de combate ao COVID, o quanto adotou as recomendações da ONU (por exemplo) (pensar em algum meio de determinar isso de forma padronizada e bem determinada)
  - **pensar em mais entidades**
- _gravidade do caso_ seria algo que identificasse o estado de saúde da pessoa no ápice da doença, como um valor de 0 a 10 por exemplo (seria algo padronizado e bem determinado)
- note que _gravidade do caso_ seria um atributo "volátil", ou seja, a pessoa iria atualizando conforme seu estado de saúde fosse mudando

## Parágrafo de proposta
Tema: COVID \
Alunos: 
- Marcos Blandim Andrade 18/0145223; 
- Igor Laranja Borges Taquary 18/0122231. 

Um Banco de Dados para mapeamento de casos de pessoas infectadas com COVID-19 em qualquer região do mundo. O banco teria entidades como pessoas, cidade e países, e atributos pensados para gerar estatísticas úteis para a análise da evolução de casos de COVID naquela região, e também de seu impacto nas pessoas do local, já que teremeos atributos que indicam o estado de saúde das pessoas por exemplo. O SGBD escolhido foi o MySQL e a linguagem escolhida para o CRUS foi Python.

## Modelo Relacional

Link para o MER no app Creately: 
https://app.creately.com/diagram/ncASERcbqLC
