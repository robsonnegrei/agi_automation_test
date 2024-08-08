# DO QUE SE TRATA ESTE PROJETO?



# Automatização de Testes - Blog do Agi

Este projeto automatiza testes de busca no Blog do Agi usando Selenium e Behave. Abaixo estão as instruções de configuração e execução para Linux, macOS e Windows.

## Instruções para Uso

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/blog_automation.git
   cd blog_automation
   ```

## Estrutura do Projeto

```
blog_automation/
│
├── features/
│   ├── search.feature
│
├── features/steps/
│   └── search_steps.py
│
├── environment.py
│
├── run_tests.py
│
└── requirements.txt
```

## Dependências do Ambiente para iniciar a instalação:

### Verifique as Dependencias:
Certifique-se de ter Python 3.8 ou superior instalado. Instale as dependências usando `pip`:

## INSTALAÇÂO DOS REQUISITOS:
Vamos precisar instalar algums dependencias para rodar esta aplicação:

```bash
pip install -r requirements.txt
```

Contém:
- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)
- install requirements via pip install dentro da sua Virtual env: para este projeto estamos usando um arquivo requirements.txt no diretório principal

## EXECUTANDO O PROJETO:

### Linux / macOS

1. **Instale o ChromeDriver:**

   Utilize `webdriver-manager` para instalar o ChromeDriver:

   ```bash
   pip install webdriver-manager
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute os testes:**

   ```bash
   python run_tests.py
   ```

### Windows

1. **Instale o ChromeDriver:**

   - Baixe o ChromeDriver correspondente à sua versão do Chrome [aqui](https://sites.google.com/chromium.org/driver/).
   - Extraia o `chromedriver.exe` para um diretório acessível, como `C:\Drivers\`.

2. **Adicione o caminho do ChromeDriver ao sistema:**

   Adicione a variável de ambiente `PATH` apontando para o diretório onde você extraiu `chromedriver.exe`.

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute os testes:**

   ```bash
   python run_tests.py
   ```



## Arquivos de Configuração

### `environment.py`
### `run_tests.py`
### `search.feature`
### `search_steps.py`

## Relatórios

Os testes geram um relatório HTML em `report.html`. Abra este arquivo em um navegador para visualizar os resultados dos testes.



## Casos de Teste - Funcionalidade de Busca 

@Arquivo **busca.feature** na pasta (tests/features)

## Caso de Teste 1: Pesquisa Válida

**Título:** Pesquisa por um termo existente.  
**Cenário:** Usuário pesquisa por um termo existente.  
**Prioridade:** ALTA  

**Dados de Teste:**  
- Termo de busca: "saque-aniversario"

@high
  Scenario: Usuario pesquisa por um termo existente.                                # features\busca.feature:4
    Given Estou na home page do Blog                                                # features\steps\busca_steps.py:7
    When Eu clico no icone de lupa no canto superior direito                        # features\steps\busca_steps.py:12
    When Digito saque-aniversario no campo de busca                                 # features\steps\busca_steps.py:17
    When Pressiono Enter                                                            # features\steps\busca_steps.py:23
    Then A pagina exibe o artigo post-4302 na lista de artigos relacionados a busca # features\steps\busca_steps.py:28


---

## Caso de Teste 2: Pesquisa Inválida

**Título:** Pesquisa por um termo inexistente.  
**Cenário:** Usuário pesquisa por um termo inexistente.  
**Prioridade:** ALTA  

**Dados de Teste:**  
- Termo de busca: "NAO CONSTA"

**Passo a Passo com Resultado Esperado:**
 @high
  Scenario: Usuario pesquisa por um termo inexistente.                # features\busca.feature:12
    Given Estou na home page do Blog                                  # features\steps\busca_steps.py:7
    When Eu clico no icone de lupa no canto superior direito          # features\steps\busca_steps.py:12
    When Digito NAO-CONSTA no campo de busca                          # features\steps\busca_steps.py:17
    When Pressiono Enter                                              # features\steps\busca_steps.py:23
    Then A pagina exibe uma mensagem nao foram encontrados resultados # features\steps\busca_steps.py:37

