# Set up

We'll need a few things to install for this section:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)
- install requirements via pip install into the python Virtual env for this project by using requirements.txt file from source directory

### Linux/MacOS
``` bash
source venv/bin/activate
pip install -r requirements.txt 
```

### Windows
``` bash
pip install virtualenv
virtualenv venv
venv\Scripts\Activate.bat
```


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

### Linux/MacOS

```bash
source venv/bin/activate
cd section6/video_code/
python -m behave tests/acceptance
```
### Windows

```bash
venv/bin/activate
cd section6/video_code/
python -m behave tests/acceptance
```


## Casos de Teste - Funcionalidade de Busca

## Caso de Teste 1: Pesquisa Válida

**Título:** Pesquisa por um termo existente.  
**Cenário:** Usuário pesquisa por um termo existente.  
**Prioridade:** Alta  

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
**Prioridade:** Média  

**Dados de Teste:**  
- Termo de busca: "NAO CONSTA"

**Passo a Passo com Resultado Esperado:**
1. **Ação:** Clicar no ícone de lupa no canto superior direito.
   - **Resultado Esperado:** O campo de busca é exibido.
2. **Ação:** Digitar "NAO CONSTA" no campo de busca.
   - **Resultado Esperado:** O termo "NAO CONSTA" aparece no campo de busca.
3. **Ação:** Pressionar Enter.
   - **Resultado Esperado:** A página exibe uma mensagem informando que não foram encontrados resultados para o termo pesquisado.
