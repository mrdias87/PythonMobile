from src.model.screen_definitions.elementos_dispositivo_seleciona_produto import Elementos_Seleciona_Produto


class Acoes_Seleciona_Produto(Elementos_Seleciona_Produto):

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_produto_menu(self):
        self.element_menu_produto.click()
