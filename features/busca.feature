Feature: Funcionalidade de Busca no Blog (homePage)

  @high
  Scenario: Usuário pesquisa por um termo existente.
    Given Estou na home page do Blog
    When Eu clico no ícone de lupa no canto superior direito
    When Digito saque-aniversario no campo de busca
    When Pressiono Enter
    Then A página exibe o artigo post-2527 na lista de artigos relacionados a busca

  @high
  Scenario: Usuário pesquisa por um termo inexistente.
    Given Estou na home page do Blog
    When Eu clico no ícone de lupa no canto superior direito
    When Digito NAO-CONSTA no campo de busca
    When Pressiono Enter
    Then A página exibe uma mensagem informando que não foram encontrados resultados para o termo pesquisado
