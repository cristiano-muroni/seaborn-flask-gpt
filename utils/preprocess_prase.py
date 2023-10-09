import re
import unicodedata

def preprocess_input(userInput):  
  userInput = userInput.lower()

  # Removendo acentos
  userInput = ''.join(c for c in unicodedata.normalize('NFD', userInput)
                      if unicodedata.category(c) != 'Mn')

  # Removendo caracteres não alfanuméricos
  userInput = re.sub(r'[^a-z0-9\s]', '', userInput)
  return userInput