
#%% Importacoes 
import pandas as pd
import matplotlib.pyplot as plt
# %% Carregando os dados
df1 = pd.read_csv('./data/test.csv')
df2 = pd.read_csv('./data/train.csv')
survived = pd.read_csv('./data/gender_submission.csv')

display(df1, df2, survived)
# %% Juntando a variavel Survived ao df1
df1 = df1.merge(survived, 
          left_on='PassengerId',
          right_on='PassengerId')
# %% Criando uma lista com o nome das variaveis do df1
names = ["PassengerId", "Pclass", "Name", "Sex", "Age", "SibSp",	"Parch", "Ticket", "Fare", "Cabin", "Embarked", "Survived"]
#%% Reordenando as variaveis no df2
df2 = df2[names]
#%% Unificando o df1 ao df2
df = pd.concat([df1, df2])
# %% Salvando o df que foi unificado em um novo arquivo
df.to_csv('./data/titanic_complete.csv',
          sep=',',
          index_label=False
          )
# %%
