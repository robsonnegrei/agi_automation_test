from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@given('Estou na home page do Blog')
def step_impl(context):
    page = context.driver.find_element(By.ID, 'page').text
    assert "O Agibank" in page

@when('Eu clico no icone de lupa no canto superior direito')
def step_impl(context):
    search_icon = context.driver.find_element(By.CSS_SELECTOR, 'a.slide-search.astra-search-icon')
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

@then('A pagina exibe o artigo post-4302 na lista de artigos relacionados a busca')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    # post-4302: antecipacao-saque-aniversario-fgts-agibank
    article = context.driver.find_elements(By.ID, 'post-4302')
    assert article

@then('A pagina exibe uma mensagem nao foram encontrados resultados')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    no_result_message = context.driver.find_element(By.XPATH, '//*[@id="main"]/section')
    assert no_result_message




