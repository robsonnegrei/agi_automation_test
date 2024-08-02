from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#   Scenario: Usuário pesquisa por um termo existente.
@given('Estou na home page do Blog')
def step_impl(context):
    assert "Blog do Agi | Tudo sobre empréstimo e educação financeira" in context.driver.title
@when('Eu clico no ícone de lupa no canto superior direito')
def step_impl(context):
    search_icon = context.driver.find_element(By.CLASS_NAME, 'slide-search astra-search-icon')
    search_icon.click()
@when('Digito {term} no campo de busca')
def step_impl(context, term):
    search_field = context.driver.find_element(By.ID, 'search-field')
    search_field.clear()
    search_field.send_keys(term)
@when('Pressiono Enter')
def step_impl(context):
    search_field = context.driver.find_element(By.ID, 'search-field')
    search_field.send_keys(Keys.ENTER)
@then('A página exibe o artigo {term} na lista de artigos relacionados a busca')
def step_impl(context, term):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    # term = post-252: antecipacao-saque-aniversario-fgts-agibank
    articles = context.driver.find_elements(By.ID, 'term')
    assert articles.text

# Scenario: Usuário pesquisa por um termo inexistente.
@then('A página exibe uma mensagem informando que não foram encontrados resultados para o termo pesquisado')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    no_results_message = context.driver.find_element(By.CLASS_NAME, 'no-results not-found')
    assert "Lamentamos, mas nada foi encontrado para sua pesquisa, tente novamente com outras palavras." in no_results_message.text





