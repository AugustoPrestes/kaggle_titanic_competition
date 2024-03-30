#%% Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
# %% Carregando dados
df = pd.read_csv("../data/titanic_complete.csv")
# %%
df.head()
#%% Dicionario de dados
"""
PassengerId: Código de identificação (Int64);
Pclass: Classe do passageio (Int64) - 3 = Terceira,  2 = Segunda, 1 = Primeira;
Name: Nome dos passageiros (String);
Sex: Gênero (Int64) - male = Masculino, female = Feminino;
Age: Idade(Int64);
SibSp: Número de irmãos/esposa abordo (Int64);
Parch: Número de pais/filhos abordo (Int64);
Ticket: Código da passagem (String);
Fare: Preço da passagem (Float64);
Cabin: Código da cabine (String);
Embarked: Local de Embarque (String) - C = Cherbourg, Q = Queenstown, S = Southhampton;
Survived: Sobreviveu (Int64) - 0 = Não, 1 = Sim
"""
#%% Alterando o nome das colunas em lower case
df.columns = df.columns.str.lower()
df.head()
#%% Tratando os dados ausentes 
df.info()
#%% Porcentagem de dados ausentes por variavel
(df.isnull().mean() * 100).plot(kind='barh')
(df.isnull().mean() * 100)
# %%
"""
Conseguimos ver que apenas as variaveis 'Fare', 'Embarked', 'Age' e 'Cabin', possuem dados ausentes.
    A variavel 'Cabin' pode estar nos dizendo que a maior parte das pessoas embarcadas não possuia uma cabin
isso pode siguinificar que a maioria era funcionário do navio ou não foi possuivei relacionar a pessoa a uma cabine,
pois não sabemos se os dados foram coletados antes ou depois do acidente.
    A ausência de dados na coluna 'Age', não nos explica muita coisa por si só, visto que isso pode ter ocorrido
apenas por algum problema na coleta dos dados originais.
    A variavel 'Embarked', também pode nos dizer algo como pessoas que entraram no navio clandestinamente.
Ou também podem ter ocorrido perda de dados durante a coleta.
    A variavel 'Fare' possui uma perdade de dados muito pequena, e com isso faremos apenas uma alteração
dos dados faltantes para a média dos demais dados.
"""
# %% Ausentes 'Cabin'
df['cabin'] = df['cabin'].fillna('vazio')
# %% Ausentes 'Age'
df['age'] = df['age'].fillna(df.age.mean().round(0))
# %% Ausentes 'Embarked'
df['embarked'] = df['embarked'].fillna('vazio')
# %% ausentes 'Fare'
df['fare'] = df['fare'].fillna(0)
#%%
(df[['fare', 'age']].mean() * 100).plot(kind='barh')