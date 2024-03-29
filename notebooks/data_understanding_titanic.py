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
Sex: Gênero (Int64) - 
Age 
SibSp 
Parch
Ticket 
Fare 
Cabin 
Embarked 
Survived
"""
# %%
print(df.columns, )
# %%
for c in df:
    print(f"{c}\n{df[c].unique()}\n")

# %%
