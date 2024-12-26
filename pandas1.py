import matplotlib.pyplot as plt
import pandas as pd

def importar_dados():
    # URL corrigida
    url_dados = 'aluguel.csv'
    leitura_dados = pd.read_csv(url_dados, sep=";")
    return leitura_dados

def manipulacao_dos_dados(leitura_dados):
    numero_de_imoveis = leitura_dados["Tipo"].value_counts()
    return numero_de_imoveis

def graficos(numero_de_imoveis):
    # Utilizando os índices e valores da contagem de tipos
    tipos = numero_de_imoveis.index
    quantidade = numero_de_imoveis.values

    # Criando o gráfico de barras
    plt.bar(tipos, quantidade)
    plt.xlabel("Tipos de Imóveis")
    plt.ylabel("Quantidade")
    plt.title("Tipos de Imóveis")
    
    # Rotacionando os labels do eixo x para melhor visualização
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show()

def main():
    leitura_dados = importar_dados()
    numero_de_imoveis = manipulacao_dos_dados(leitura_dados)
    graficos(numero_de_imoveis)

if __name__ == "__main__":
    main()
