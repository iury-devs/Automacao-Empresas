from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl
driver = webdriver.Chrome()
driver.get('https://contabilidade-devaprender.netlify.app/')
driver.maximize_window()
sleep(5)
# Digitar email
email = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/input")
sleep(2)
email.send_keys('teste@gmail.com')
# Digitar a senha
senha = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/input")
sleep(2)
senha.send_keys('12345')
# Clicar no botão de entrar
botao_entrar = driver.find_element(By.XPATH, "//button[@id='Entrar']")
sleep(2)
botao_entrar.click()
sleep(5)
planilha_empresas = openpyxl.load_workbook('./empresas.xlsx')
pagina_empresas = planilha_empresas['dados empresas']

for linha in pagina_empresas.iter_rows(min_row= 2, values_only=True):
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_funcionarios, data_fundacao = linha

    nome_empresa = driver.find_element(By.ID, 'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)
    email = driver.find_element(By.ID, 'emailEmpresa').send_keys(email)
    sleep(1)
    telefone = driver.find_element(By.ID, 'telefoneEmpresa').send_keys(telefone)
    sleep(1)
    endereco = driver.find_element(By.ID, 'enderecoEmpresa').send_keys(endereco)
    sleep(1)
    cnpj = driver.find_element(By.ID, 'cnpj').send_keys(cnpj)
    sleep(1)
    area_atuacao = driver.find_element(By.ID, 'areaAtuacao').send_keys(area_atuacao)
    sleep(1)
    quantidade_funcionarios = driver.find_element(By.ID, 'numeroFuncionarios').send_keys(quantidade_funcionarios)
    sleep(1)
    data_fundacao = driver.find_element(By.ID, 'dataFundacao').send_keys(data_fundacao)
    sleep(1)

    cadastrar = driver.find_element(By.ID, 'Cadastrar').click()
    sleep(3)
   