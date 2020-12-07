import unittest
from src.model.screen_actions.acoes_dispositivo_realizar_pesquisa import Acoes_Realizar_Pesquisa
from src.model.screen_actions.acoes_dispositivo_comecar_sem_login import Acoes_Comecar_Sem_Login
from src.model.screen_actions.acoes_dispositivo_verifica_dados_produto import Acoes_Verifica_Dados_Produto
from src.model.screen_actions.acoes_dispositivo_seleciona_produto import Acoes_Seleciona_Produto
from src.model.screen_actions.acoes_dispositivo_menu_pesquisa import Acoes_Menu_Navegacao
from src.model.screen_actions.acoes_dispositivo_ir_carrinho import Acoes_Ir_Carrinho
from src.model.screen_actions.acoes_dispositivo_produtos_carrinho import Acoes_Produtos_Carrinho
from src.model.support.config import Driver


class PesquisaPetzTest(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

        # Declaração de variáveis com os dados para preenchimento
        self.pesquisa = 'Ração'
        self.nome_produto = 'Ração Royal Canin 15kg Maxi Junior Cães Filhotes de Raças Grandes'
        self.nome_fornecedor = 'Royal Canin'
        self.valor_produto = '248,89'
        self.valor_assinante = 'R$ 224,00'

    def test_pesquisa_petz(self):

        try:
            # Preenche o numero do pesquisa e clicar em Ingressar para entrar na carteira
            clica_comecar_sem_login = Acoes_Comecar_Sem_Login(self.driver)
            clica_comecar_sem_login.clicar_comecar_sem_login()

            # Clicar no botão do menu de pesquisa
            clicar_no_botao_pesquisa_menu = Acoes_Menu_Navegacao(self.driver)
            clicar_no_botao_pesquisa_menu.clicar_botao_menu_pesquisa()

            # Preencher o pesquisa do produto
            preenche_pesquisa_produto = Acoes_Realizar_Pesquisa(self.driver)
            preenche_pesquisa_produto.escreve_pesquisa_produto(self.pesquisa)

            # # Clicar no produto selecionado para validação dos dados
            clicar_produto_menu = Acoes_Seleciona_Produto(self.driver)
            clicar_produto_menu.clicar_produto_menu()

            # Verifica se os dados que estão na tela estão corretos
            verifica_dados_produto = Acoes_Verifica_Dados_Produto(self.driver)
            self.assertEqual(verifica_dados_produto.verificar_texto_nome_produto(), self.nome_produto)
            self.assertEqual(verifica_dados_produto.verificar_texto_nome_fornecedor(), self.nome_fornecedor)
            self.assertEqual(verifica_dados_produto.verificar_texto_valor_produto(), self.valor_produto)
            self.assertEqual(verifica_dados_produto.verificar_texto_valor_assinante(), self.valor_assinante)

            # Adiciona o produto ao carrinho de compras
            verifica_dados_produto.clicar_adicionar_ao_carrinho()

            # Clicar na opção ir para o carrinho
            clicar_no_botao_ir_para_carrinho = Acoes_Ir_Carrinho(self.driver)
            clicar_no_botao_ir_para_carrinho.clicar_ir_carrinho()

            # Verfica se os dados estão corretos no carrinho
            verifica_produtos_carrinho = Acoes_Produtos_Carrinho(self.driver)
            self.assertEqual(verifica_produtos_carrinho.verificar_nome_produto_carrinho(), self.nome_produto)
            self.assertEqual(verifica_produtos_carrinho.verificar_nome_fornecedor_carrinho(), self.nome_fornecedor)
            self.assertEqual(verifica_produtos_carrinho.verificar_valor_produto_carrinho(), self.valor_produto)

        except ValueError:
            print(ValueError)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
