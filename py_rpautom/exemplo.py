from web_utils import iniciar_navegador


# baixar_webdriver(nome_navegador='Chrome')

iniciar_navegador(
    nome_navegador='Chrome',
    url='https://bing.com',
    options=(('start-maximized',)),
    baixar_webdriver_previamente=True,
)

# breakpoint()
