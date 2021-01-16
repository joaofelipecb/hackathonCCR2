# Ei Vizinho
## Introdução
Ei Vizinho é uma plataforma de oferta de produtos e serviços baseados no comércio local,
tendo em vista incentivar novos empreendedores mais próximos dos consumidores,
com base em dados de consumo e geolocalização, gerando inclusão e profissionalização
para atender a demanda existente.

## Desenvolvimento Orientado ao Comportamento (BDD)
**Cenário 1.** <br>
*Dado que* haja um conjunto de dados de demanda com geolocalização<br>
*Quando* a inteligência artificial receber uma posição<br>
*Então* ela deve procurar quais são as demandas mais próximas do ponto e que tenham uma distância do estabelecimento maior do consumidor<br>

**Cenário 2.** <br>
*Dado que* haja um conjunto de dados de demanda com geolocalização mais próximas do ponto e que tenham uma distância do estabelecimento maior do consumidor<br>
*Quando* a inteligência artificial for solicitadas pelos negócios semelhantes<br>
*Então* ela deve retornar uma lista com os negócios semelhantes com maior frequência<br>

**Cenário 3.** <br>
*Dado que* o empreendedor queria saber qual é a demanda do seu bairro<br>
*Quando* ele abrir o aplicativo<br>
*Então* ele deve ver os dados de consumo da sua região em um mapa de calor com filtros dos negócio mais promissores, por inteligência artificial<br>

**Cenário 4.** <br>
*Dado que* o empreendedor esteja vizualizando o mapa de calor do seu bairro<br>
*Quando* ele arrastar o mapa<br>
*Então* ele deve ver o mapa sendo transladado<br>

**Cenário 5.** <br>
*Dado que* o empreendedor esteja vizualizando o mapa de calor do seu bairro<br>
*Quando* ele faça movimento de pinça/scroll<br>
*Então* ele deve ver o mapa sendo ampliado<br>

**Cenário 6.** <br>
*Dado que* o empreendedor esteja vizualizando o mapa de calor do seu bairro<br>
*Quando* ele escolher um filtro de negócio<br>
*Então* ele deve ver os dados de consumo apenas daquele negócio da sua região
em um mapa de calor e ter a opção de abrir os cursos sugeridos para aquele negócio<br>

**Cenário 7.** <br>
*Dado que* haja um conjunto de cursos<br>
*Quando* a inteligência artificial for solicitadas pelos cursos semelhantes a um negócio<br>
*Então* ela deve retornar uma lista com os cursos mais semelhantes com um negócio<br>

**Cenário 8.** <br>
*Dado que* o empreendedor esteja vizualizando o mapa de calor do seu bairro filtrado para um negócio<br>
*Quando* ele abrir os cursos sugeridos para aquele negócio<br>
*Então* ele deve ir para a tela dos mini cursos de negócios ordenados por semelhança com aquela demanda, por inteligência artificial<br>

**Cenário 9.** <br>
*Dado que* o empreendedor esteja vizualizando a tela dos mini cursos<br>
*Quando* ele clicar num curso de seu interesse<br>
*Então* ele deve ir para a tela do mini curso com área de conhecimento, habilidade e atitude<br>

**Cenário 10.** <br>
*Dado que* o empreendedor esteja vizualizando a tela de mini curso com área de conhecimento, habilidade e atitude<br>
*Quando* ele clicar em algum link do conhecimento<br>
*Então* ele deve ir para um conteúdo de dados: texto, imagem ou vídeo, em ordem de complexidade<br>

**Cenário 11.** <br>
*Dado que* o empreendedor esteja vizualizando a tela de mini curso com área de conhecimento, habilidade e atitude<br>
*Quando* ele clicar em algum link da habilidade<br>
*Então* ele deve ir para um conteúdo de testes: critérios que ele deve alcançar enquanto pratica, em ordem de complexidade<br>

**Cenário 12.** <br>
*Dado que* o empreendedor esteja vizualizando a tela de mini curso com área de conhecimento, habilidade e atitude<br>
*Quando* ele clicar em algum link da atitude<br>
*Então* ele deve ir para um conteúdo de comportamento: lógica pela qual o conhecimento é conectado com a habilidade<br>
