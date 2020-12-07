from src.model.screen_definitions.elementos_dispositivo_ir_carrinho import Elementos_Ir_Carrinho


class Acoes_Ir_Carrinho(Elementos_Ir_Carrinho):

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_ir_carrinho(self):
        self.relativelayout_go_to_shop.click()