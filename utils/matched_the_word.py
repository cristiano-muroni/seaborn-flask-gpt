import re
from utils.preprocess_prase import preprocess_input

def matched_the_word_graph(userInput):
  # Definindo o padrão regex para procurar "exibir gráfico" ou "últimos meses"
  default_display_graph = r'exibir grafico|graficos|grafico'
  default_display_last_months = r'ultimos meses|ultimo mes'
  default_display_full_year = r'full year|ano todo|todos os meses|todo ano|ano cheio'
  default_display_scatter_plot = r'dispersão|disperçao|dispersao|dispercao'
  default_display_list_chart = r'lista|tipo lista|list|linha|linhas'
  default_display_table = r'lista em tabelas|tipo tabela|tabela|tabelas'

  userInput = preprocess_input(userInput)

  # Tentando encontrar uma correspondência no texto
  match_with_text_graph = re.search(default_display_graph, userInput, re.IGNORECASE)
  match_with_text_last_months = re.search(default_display_last_months, userInput, re.IGNORECASE)
  match_with_text_full_year = re.search(default_display_full_year, userInput, re.IGNORECASE)
  match_with_text_scatter_plot = re.search(default_display_scatter_plot, userInput, re.IGNORECASE)
  match_with_text_list_chart = re.search(default_display_list_chart, userInput, re.IGNORECASE)
  match_with_text_table = re.search(default_display_table, userInput, re.IGNORECASE)

  # Verificando se deu match
  return {
      'graph': bool(match_with_text_graph),
      'last_months': bool(match_with_text_last_months),
      'full_year': bool(match_with_text_full_year),
      'scatter_plot': bool(match_with_text_scatter_plot),
      'list_chart': bool(match_with_text_list_chart),
      'table': bool(match_with_text_table)
  }