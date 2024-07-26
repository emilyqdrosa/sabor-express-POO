from modelos.avaliacao import Avaliacao
from modelos.restaurante import Restaurante
# de  pasta .  arquivo   import   classe


restaurante_praca = Restaurante('praça',   'gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

#programa principal
if __name__ == '__main__':
    main()
