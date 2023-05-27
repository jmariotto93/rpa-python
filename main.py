from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


options = Options()
options.headless = False

# Configurações do email
email_de = 'josemarioto@gmail.com'
email_para = 'jmariotto16@gmail.com'
senha = '*************'

# Inicializar o driver do Selenium
driver = webdriver.Chrome(options=options)

# Abrir o site do Tribunal de Justiça-SP
link = "https://esaj.tjsp.jus.br/cpopg/open.do"
driver.get(url=link)
sleep(1)

# Inseri o número do ano unificado no input do site do e-SAJ TJ-SP
inputNumeroAnoUnificado = driver.find_element(by=By.ID,value="numeroDigitoAnoUnificado")
inputNumeroAnoUnificado.send_keys("1502626-50.2022")
sleep(1)

# Inseri o número do foro no input do site do e-SAJ
inputNumeroDoForo = driver.find_element(by=By.ID,value="foroNumeroUnificado")
inputNumeroDoForo.send_keys("0323")
sleep(1)

#
buttonLogin = driver.find_element(by=By.ID,value="botaoConsultarProcessos")
buttonLogin.click()

# Localizar a última movimentação do processo no site
element = driver.find_element(by=By.ID, value="tabelaUltimasMovimentacoes")

# Guardando a ultima movimentação na variavel texto
texto = element.text
print(texto)

# Configurar o email
msg = MIMEMultipart()
msg['From'] = email_de
msg['To'] = email_para
msg['Subject'] = 'Dados do Seu processo'

# Corpo do email
corpo = f'''
Caro, 'Nome do cliente'

As informações do processo são os senguintes:

{texto}

Atenciosamente,
José Mariotto
'''
msg.attach(MIMEText(corpo, 'plain'))

# Enviar o email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_de, senha)
    server.send_message(msg)
    server.quit()
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Ocorreu um erro ao enviar o e-mail: {str(e)}')



