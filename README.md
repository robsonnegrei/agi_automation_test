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
- Termo de busca: "empréstimo"

**Passo a Passo com Resultado Esperado:**
1. **Ação:** Clicar no ícone de lupa no canto superior direito.
   - **Resultado Esperado:** O campo de busca é exibido.
2. **Ação:** Digitar "empréstimo" no campo de busca.
   - **Resultado Esperado:** O termo "empréstimo" aparece no campo de busca.
3. **Ação:** Pressionar Enter.
   - **Resultado Esperado:** A página exibe uma lista de artigos relacionados ao termo "empréstimo".

---

## Caso de Teste 2: Pesquisa Inválida

**Título:** Pesquisa por um termo inexistente.  
**Cenário:** Usuário pesquisa por um termo inexistente.  
**Prioridade:** ALTA  

**Dados de Teste:**  
- Termo de busca: "NAO CONSTA"

**Passo a Passo com Resultado Esperado:**
1. **Ação:** Clicar no ícone de lupa no canto superior direito.
   - **Resultado Esperado:** O campo de busca é exibido.
2. **Ação:** Digitar "NAO CONSTA" no campo de busca.
   - **Resultado Esperado:** O termo "NAO CONSTA" aparece no campo de busca.
3. **Ação:** Pressionar Enter.
   - **Resultado Esperado:** A página exibe uma mensagem informando que não foram encontrados resultados para o termo pesquisado.
