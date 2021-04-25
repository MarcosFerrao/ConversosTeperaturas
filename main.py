"""
Programa em Python 3 para converter Celsius em Fahrenheit e Kelvin.
"""

from helpers import celsius_para_kelvin, celsius_para_fahrenheit

if __name__ == '__main__':
    while True:
        mensagem = "\nPor favor ensira a temperatura em Celsius."
        mensagem += "\nPara sair, presione 'q':  "

        try:
            celsius = input(mensagem)
            if celsius.lower() != 'q':
                print(f"\nTemperatura em Kelvin(K): {celsius_para_kelvin(float(celsius))}")
                print(f"\nTemperatura em Fahrenheit (F): {celsius_para_fahrenheit(float(celsius))}")
            else:
                print('\nO APP foi finalizado.\nAté  próxima!')
                break
        except ValueError:
            print("\nVocê digitou um caractér inválido. \n Por favor insira um numero ou a letra 'q'.")
