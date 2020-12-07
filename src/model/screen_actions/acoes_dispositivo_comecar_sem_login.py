from src.model.screen_definitions.elementos_dispositivo_comecar_sem_login import Elementos_Comecar_Sem_Login


class Acoes_Comecar_Sem_Login(Elementos_Comecar_Sem_Login):

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_comecar_sem_login(self):
        self.tv_start_without_login.click()
