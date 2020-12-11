"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    a = float(input("Quantos quilos foram pescados?"))
    p = (a - 50) * 4
    if p < 0:
      p = 0
    print(f'O peixe tem {a}kg, a multa devida é {p:.2f}.')


if __name__ == '__main__':
    main()
