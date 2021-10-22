# TEST TECH PARA VAGA DE ESTAGIO GETTER - FLEX
#
# Autor: Ewerllon Cristian Batista Nonato
# 
# DESAFIO: 
#   Crie uma Rotina que busque os dados da url abaixo
#   https://random-data-api.com/api/app/random_app 
#   busque 100 registros, salve os dados em um csv

from requests import get
import pandas as pd

endpoint = "https://random-data-api.com/api/app/random_app"


def busca_dados(qtd_registros):
    
  payload = {'size': qtd_registros}
  response = get(endpoint, params=payload)
  to_parse = response.json()
  df= pd.DataFrame(to_parse)
  return df

busca_dados(100)

def exporte_seu_df(filename,df):
    # filename: base.csv (str) 
    # df: dataframe (pandas)
    # use o metodo to_csv do pandas
    # para gerar sua base 
    df = df.to_csv(filename)
    print("... Salvo {} ...".format(filename))

def main():
  # não precisa alterar essa parte do Código
  print("... Buscando dados ...")
  df = busca_dados(qtd_registros=100)
  print("... Salvando dados ...")
  exporte_seu_df("base_app.csv",df)

if __name__ == "__main__":
     main()