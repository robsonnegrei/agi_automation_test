Feature: Funcionalidade de Busca no Blog (homePage)

  @high
  Scenario: Usuario pesquisa por um termo existente.
    Given Estou na home page do Blog
    When Eu clico no icone de lupa no canto superior direito
    When Digito saque-aniversario no campo de busca
    When Pressiono Enter
    Then A pagina exibe o artigo post-4302 na lista de artigos relacionados a busca

  @high
  Scenario: Usuario pesquisa por um termo inexistente.
    Given Estou na home page do Blog
    When Eu clico no icone de lupa no canto superior direito
    When Digito NAO-CONSTA no campo de busca
    When Pressiono Enter
    Then A pagina exibe uma mensagem nao foram encontrados resultados
