import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Isso configura o matplotlib no modo "headless", que não requer um loop de eventos.
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.lines import Line2D  # classe Line2D para criar marcadores personalizados
from db_fake.db_fake import sales_in_last_months, full_year
from flask import current_app
import os
import uuid 

def millions(x, pos):
    'Função de formatação para exibir valores em milhões'
    return f'{x/1e6:.0f}M'

def show_graphs_lm() :
    sales = sales_in_last_months()
    df = pd.DataFrame(sales)
    
    sns.set(style="white")
    plt.figure(figsize=(8, 4))

    # Mapeando os valores do eixo y para milhões de litros
    df["total-litros (milhões)"] = df["total-litros"] / 1000000

    ax = sns.barplot(x="mes", y="total-litros (milhões)", data=df, color="#FF8C00")
    plt.xlabel("Mês")
    plt.ylabel("total-litros (milhões)")
    plt.title("Total de Litros por Mês")

    # Usando a função de formatação personalizada para o eixo y
    formatter = FuncFormatter(millions)
    ax.yaxis.set_major_formatter(formatter)
   # plt.gca().yaxis.set_major_formatter(formatter)


    # Definindo os valores de marcação do eixo y manualmente
    plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400], ["0M", "0.2M", "0.4M", "0.6M", "0.8M", "1.0M", "1.2M", "1.4M"])

    # Adicionando rótulos de texto no topo de cada barra
    for p in ax.patches:              
        ax.annotate(f'{p.get_height():.1f}M', (p.get_x() + p.get_width() / 2., p.get_height()),                    
                    ha='center', va='center', fontsize=9, color='black', xytext=(0, 5),
                    textcoords='offset points')
    
     # Criando uma única lista de elementos de legenda com bolinhas de cores correspondentes para ambas as barras
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Total de litros', markersize=10, markerfacecolor='#FF8C00'),
        Line2D([0], [0], marker='o', color='w', label='Qtd de Caminhões Tanques', markersize=10, markerfacecolor='#228B22')
    ]

    # Adicionando a legenda ao gráfico
    ax.legend(handles=legend_elements, loc='upper right')
    
    # Adicionando barras de "quantidade de tanques" no mesmo gráfico
    ax2 = ax.twinx()
    sns.barplot(x="mes", y="quantidade-de-tanques", data=df, ax=ax2, color="#228B22", alpha=1)
    ax2.set_ylabel("Quantidade de Tanques")
    ax2.set_ylim(0, df["quantidade-de-tanques"].max() * 1.2)  # Ajustando conforme necessário

    # Ajustando a largura das barras para as quantidades de tanques
    for p in ax2.patches:
        p.set_width(0.1)  # Ajuste manual da largura das barras
    
    # Adicionando uma linha vermelha na altura de 300 milhões
    ax.axhline(y=300, color='red', linestyle='--', label='Limite de 300M')

    # Obtendo o caminho absoluto para a pasta "static"
    static_folder = current_app.static_folder

    # Criando um nome de arquivo exclusivo
    file_name = str(uuid.uuid4()) + ".png"

    # Criando o caminho completo para a imagem na pasta "static"
    file_path = os.path.join(static_folder, file_name)

    # Salvando a imagem no caminho completo
    plt.savefig(file_path)
    print(file_path)
    return file_path

def show_graphs_full() :
    sales = full_year()
    df = pd.DataFrame(sales)    
    sns.set(style="white")
    plt.figure(figsize=(8, 4))
    
    df["total-litros (milhões)"] = df["total-litros"] / 1000000

    ax = sns.barplot(x="mes", y="total-litros (milhões)", data=df, color="#FF8C00")
    plt.xlabel("Mês")
    plt.ylabel("total-litros (milhões)")
    plt.title("Total de Litros por Mês")
    
    formatter = FuncFormatter(millions)
    ax.yaxis.set_major_formatter(formatter)
    
    plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400], ["0M", "0.2M", "0.4M", "0.6M", "0.8M", "1.0M", "1.2M", "1.4M"])
   
    for p in ax.patches:              
        ax.annotate(f'{p.get_height():.1f}M', (p.get_x() + p.get_width() / 2., p.get_height()),                    
                    ha='center', va='center', fontsize=5, color='black', xytext=(0, 10),
                    textcoords='offset points')    
     
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Total de litros', markersize=10, markerfacecolor='#FF8C00'),
        Line2D([0], [0], marker='o', color='w', label='Qtd de Caminhões Tanques', markersize=10, markerfacecolor='#228B22')
    ]
    
    ax.legend(handles=legend_elements, loc='upper right')    
    
    ax2 = ax.twinx()
    sns.barplot(x="mes", y="quantidade-de-tanques", data=df, ax=ax2, color="#228B22", alpha=1)
    ax2.set_ylabel("Quantidade de Tanques")
    ax2.set_ylim(0, df["quantidade-de-tanques"].max() * 1.2)
    
    for p in ax2.patches:
        p.set_width(0.1)      
    
    ax.axhline(y=300, color='red', linestyle='--', label='Limite de 300M')
    
    static_folder = current_app.static_folder   
    file_name = str(uuid.uuid4()) + ".png"    
    file_path = os.path.join(static_folder, file_name)    
    plt.savefig(file_path)
    print(file_path)
    return file_path


def show_graphs_lm_scatter() :
    sales = sales_in_last_months()
    df = pd.DataFrame(sales)    
    sns.set(style="white")
    plt.figure(figsize=(8, 4))
    
    df["Total de litros (milhões)"] = df["total-litros"] / 1000000

    ax = sns.scatterplot(x="quantidade-de-tanques", y="Total de litros (milhões)", data=df, color="#FF8C00")
    plt.xlabel("Qtd de Carga entregues")
    plt.ylabel("Total de litros (milhões)")
    plt.title("Relações entre cargas e volumes")
    
    formatter = FuncFormatter(millions)
    ax.yaxis.set_major_formatter(formatter)

    plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400], ["0M", "0.2M", "0.4M", "0.6M", "0.8M", "1.0M", "1.2M", "1.4M"])  
      
       
     
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Total de litros', markersize=10, markerfacecolor='#FF8C00'),
        Line2D([0], [0], marker='o', color='w', label='Qtd de Caminhões Tanques', markersize=10, markerfacecolor='#228B22')
    ]
    
    ax.legend(handles=legend_elements, loc='upper left') 

    ax2 = ax.twinx()
    sns.scatterplot(x="quantidade-de-tanques", y="total-litros", data=df, ax=ax2, color="#228B22", alpha=1)
    ax2.set_ylabel("")
    ax2.yaxis.set_major_locator(plt.NullLocator()) # Remove as marcas do eixo paralelo ao y    
    
    for p in ax2.patches:
        p.set_width(0.1)     
      
    static_folder = current_app.static_folder 
    file_name = str(uuid.uuid4()) + ".png"    
    file_path = os.path.join(static_folder, file_name)    
    plt.savefig(file_path)
    print(file_path)
    return file_path


def show_graphs_lm_line() :
    sales = sales_in_last_months()
    df = pd.DataFrame(sales)
    
    sns.set(style="white")
    plt.figure(figsize=(8, 4))
    
    df["total-litros (milhões)"] = df["total-litros"] / 1000000

    ax = sns.lineplot(x="mes", y="total-litros (milhões)", data=df, color="#FF8C00")
    plt.xlabel("Mês")
    plt.ylabel("total-litros (milhões)")
    plt.title("Total de Litros/ Mês")
    
    formatter = FuncFormatter(millions)
    ax.yaxis.set_major_formatter(formatter) 

    plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400], ["0M", "0.2M", "0.4M", "0.6M", "0.8M", "1.0M", "1.2M", "1.4M"])          
     
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Total de litros', markersize=10, markerfacecolor='#FF8C00'),
        Line2D([0], [0], marker='o', color='w', label='Qtd de Caminhões Tanques', markersize=10, markerfacecolor='#228B22')
    ]
    
    ax.legend(handles=legend_elements, loc='upper right')    
    
    ax2 = ax.twinx()
    sns.lineplot(x="mes", y="quantidade-de-tanques", data=df, ax=ax2, color="#228B22", alpha=1)
    ax2.set_ylabel("Quantidade de Tanques")    
    
    for p in ax2.patches:
        p.set_width(0.1)       
      
    static_folder = current_app.static_folder
    
    file_name = str(uuid.uuid4()) + ".png"
    
    file_path = os.path.join(static_folder, file_name)
    
    plt.savefig(file_path)
    print(file_path)
    return file_path

def show_graphs_full_scatter() :
    sales = full_year()
    df = pd.DataFrame(sales)    
    sns.set(style="white")
    plt.figure(figsize=(8, 4))
    
    df["Total de litros (milhões)"] = df["total-litros"] / 1000000

    ax = sns.scatterplot(x="quantidade-de-tanques", y="Total de litros (milhões)", data=df, color="#FF8C00")
    plt.xlabel("Qtd de Carga entregues")
    plt.ylabel("Total de litros (milhões)")
    plt.title("Relações entre cargas e volumes")
    
    formatter = FuncFormatter(millions)
    ax.yaxis.set_major_formatter(formatter)

    plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400], ["0", "0.2M", "0.4M", "0.6M", "0.8M", "1.0M", "1.2M", "1.4M"])  
      
       
     
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Total de litros', markersize=10, markerfacecolor='#FF8C00'),
        Line2D([0], [0], marker='o', color='w', label='Qtd de Caminhões Tanques', markersize=10, markerfacecolor='#228B22')
    ]
    
    ax.legend(handles=legend_elements, loc='upper left') 

    ax2 = ax.twinx()
    sns.scatterplot(x="quantidade-de-tanques", y="total-litros", data=df, ax=ax2, color="#228B22", alpha=1)
    ax2.set_ylabel("")
    ax2.yaxis.set_major_locator(plt.NullLocator()) # Remove as marcas do eixo paralelo ao y    
    
    for p in ax2.patches:
        p.set_width(0.1)     
      
    static_folder = current_app.static_folder 
    file_name = str(uuid.uuid4()) + ".png"    
    file_path = os.path.join(static_folder, file_name)    
    plt.savefig(file_path)
    print(file_path)
    return file_path

def show_graphs_full_line() :
    sales = full_year()
    df = pd.DataFrame(sales)    
    sns.set(style="white")
    plt.figure(figsize=(8, 4))
    
    df["total-litros (milhões)"] = df["total-litros"] / 1000000

    ax = sns.lineplot(x="mes", y="total-litros (milhões)", data=df, color="#FF8C00")
    plt.xlabel("Mês")
    plt.ylabel("total-litros (milhões)")
    plt.title("Total de Litros/ Mês")
    
    formatter = FuncFormatter(millions)
    ax.yaxis.set_major_formatter(formatter)
    
    plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400], ["0M", "0.2M", "0.4M", "0.6M", "0.8M", "1.0M", "1.2M", "1.4M"])          
     
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Total de litros', markersize=10, markerfacecolor='#FF8C00'),
        Line2D([0], [0], marker='o', color='w', label='Qtd de Caminhões Tanques', markersize=10, markerfacecolor='#228B22')
    ]
    
    ax.legend(handles=legend_elements, loc='upper left')    
    
    ax2 = ax.twinx()
    sns.lineplot(x="mes", y="quantidade-de-tanques", data=df, ax=ax2, color="#228B22", alpha=1)
    ax2.set_ylabel("Quantidade de Tanques")    
    
    for p in ax2.patches:
        p.set_width(0.1)      
    
    static_folder = current_app.static_folder   
    file_name = str(uuid.uuid4()) + ".png"    
    file_path = os.path.join(static_folder, file_name)    
    plt.savefig(file_path)
    print(file_path)
    return file_path

def show_graphs_lm_dataframe() :
    sales = sales_in_last_months()
    df = pd.DataFrame(sales)
    html_table = df.to_html()

    with open('tabela.html', 'w') as f:
        f.write(html_table)

    # Ajuste o tamanho das células e a largura das colunas
    fig, ax = plt.subplots(figsize=(6, 2))

    new_names = ['Meses', 'Qtd / tanque', 'Qtd. de tanques', 'Total de litros']
    df.columns = new_names
    
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(3)
    table.scale(1.5, 1.5)  # Ajuste a escala da tabela

    # Acessar cada célula e definir a largura da borda
    for i, cell in enumerate(table.get_celld().values()):
        cell.set_linewidth(0.6)

    # Obtenha as dimensões da tabela
    num_linhas, num_colunas = df.shape
    altura = table.get_celld()[0, 0].get_height() * num_linhas
    largura = table.get_celld()[0, 0].get_width() * num_colunas

    # Defina o tamanho da figura com base nas dimensões da tabela
    fig.set_size_inches(largura, altura) 


    ax.axis('off')  # Desligar os eixos

    static_folder = current_app.static_folder
    file_name = str(uuid.uuid4()) + ".png"
    file_path = os.path.join(static_folder, file_name)

    plt.savefig(file_path, bbox_inches='tight', pad_inches=0.1, dpi=300)
    print(file_path)
    return file_path
