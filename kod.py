# Importowanie bibliotek
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as px
from IPython.display import display

# Wczytywanie danych z pliku CSV
def load_data(file_name):
    data = pd.read_csv(file_name, skiprows=[1, 2, 3, 4, 5, 6, 211])
    data["Date"] = pd.to_datetime(data["Date"]).dt.year
    data = data.groupby("Date").mean().reset_index()
    return data

# Użycie funkcji load_data
data = load_data("Most_Popular_Programming_Languages_from_2004_to_2022.csv")

# Wyświetlenie pierwszych kilku wierszy danych
print(data.head())

# Wyświetlenie całego zestawu danych w postaci tabeli
display(data)

# Eksport danych do pliku Excel
data.to_excel("dane.xlsx", index=False)


# Wizualizacja danych za pomocą Matplotlib
def plot_with_matplotlib(data):

    # Scatter Plot
    plt.figure(figsize=(12, 6))
    plt.scatter(data['Date'], data['Python'],color='green', marker='o',zorder=2)
    plt.title("Popularność języka Python")
    plt.xlabel('Lata')
    plt.ylabel('Użycie [%]')
    plt.grid(True, linestyle='--', color='white')  # Dodanie białych linii siatki
    plt.gca().set_facecolor('lightgray')  # Ustawienie szarego tła
    plt.xticks(sorted(data['Date'].unique()))  # Unikalne lata na osi x
    plt.show()


    # Line Chart
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['R'], color="purple",zorder=2)
    plt.title("Popularność języka R")
    plt.xlabel('Lata')
    plt.ylabel('Użycie [%]')
    plt.grid(True, linestyle='--', color='white')
    plt.gca().set_facecolor('lightgray')
    plt.xticks(sorted(data['Date'].unique()))
    plt.show()

    # Bar Chart
    plt.figure(figsize=(12, 6))
    plt.bar(data['Date'], data['C/C++'], color ='skyblue', width=0.4,zorder=2)
    plt.title("Popularność języka C/C++")
    plt.xlabel('Lata')
    plt.ylabel('Użycie [%]')
    plt.grid(True, linestyle='-', color='white')
    plt.gca().set_facecolor('lightgray')
    plt.xticks(sorted(data['Date'].unique()))
    plt.show()

    # Porównanie Pythona i Javy
    plt.figure(figsize=(12, 6))
    plt.bar(data['Date'], data['Python'], color ='cadetblue', width=0.3, label="Python",zorder=2)
    plt.bar(data['Date'] + 0.3, data['Java'], color ='rosybrown', width=0.3, label="Java",zorder=2)
    plt.title("Porównanie popularności języka Python i Javy")
    plt.xlabel('Lata')
    plt.ylabel('Użycie [%]')
    plt.legend()
    plt.grid(True, linestyle='-', color='white')
    plt.gca().set_facecolor('lightgray')
    plt.xticks(sorted(data['Date'].unique()))
    plt.show()
    
    
    # Line chart
    # Plotting multiple graphs

def plot_with_matplotlib(data):
    """
    Wyświetla wykres liniowy przedstawiający popularność różnych języków programowania 
    (Python, Java, C/C++, PHP) w kolejnych latach.
    """
    plt.figure(figsize=(12,6))
    plt.style.use('ggplot')

    plt.plot(data['Date'], data['Python'], marker="o", label="Python")
    plt.plot(data['Date'], data['Java'], marker="o", label="Java")
    plt.plot(data['Date'], data['C/C++'], marker="o", label="C/C++")
    plt.plot(data['Date'], data['PHP'], marker="o", label="PHP")
    plt.xticks(data['Date'])

    plt.title("Popularność języków Python, Java, C/C++, PHP")
    plt.xlabel('Lata')
    plt.ylabel('Użycie [%]')

    # Dodanie legendy z boku wykresu
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    # Dodanie szarego tła
    plt.gca().set_facecolor('lightgray')
    
    # Dodanie białych linii siatki
    plt.grid(True, linestyle='--', color='white')
    
    plt.show()

    
def plot_with_matplotlib(data):
    # Wykres słupkowy wszystkich języków w 2021 roku
    plt.figure(figsize=(12, 6))
    plt.bar(data.columns[1:], data[data['Date'] == 2021].values[0][1:], color ='cadetblue')
    
    plt.title("Popularność języków w 2021 roku")
    plt.xlabel('Języki')
    plt.ylabel('Użycie [%]')
    
    # Dodanie szarego tła
    plt.gca().set_facecolor('lightgray')
    
    # Dodanie białych linii siatki
    plt.grid(True, linestyle='--', color='white')
    
    plt.xticks(rotation=45, ha='right')  # Obrócenie etykiet na osi x
    plt.tight_layout()  # Dopasowanie układu, aby uniknąć przycięcia etykiet
    
    plt.show()
    
    

# Wizualizacja danych za pomocą Seaborn
def plot_with_seaborn(data):
    
    sns.set(style="darkgrid")
    fig, axs = plt.subplots(2, 2, figsize=(15, 15))
    sns.histplot(data=data, x="Python", kde=True, color="skyblue", ax=axs[0, 0])
    sns.histplot(data=data, x="Java", kde=True, color="olive", ax=axs[0, 1])
    sns.histplot(data=data, x="PHP", kde=True, color="gold", ax=axs[1, 0])
    sns.histplot(data=data, x="C/C++", kde=True, color="teal", ax=axs[1, 1])
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.histplot(data=data, x="Python", color="blue", label="Python", kde=True)
    sns.histplot(data=data, x="Java", color="red", label="Java", kde=True)
    plt.title("Histogram popularności języków Python i Java")
    plt.xlabel('Użycie [%]')
    plt.ylabel('Ilość')
    plt.legend()
    plt.grid(True, linestyle='-', color='white')
    plt.gca().set_facecolor('lightgray')
    plt.show()

# Wizualizacja danych za pomocą Plotly
def plot_with_plotly(data):

    x = data['Date']
    y = data['Python']
    plot = px.Figure(data=[px.Scatter(x=x, y=y, mode='lines')])
    plot.update_layout(
        title="Popularność języka Python",
        xaxis_title=r'Lata',
        yaxis_title=r'Użycie [%]',
        xaxis=dict(rangeselector=dict(buttons=list([dict(count=1, step="year", stepmode="backward",)])),
                   rangeslider=dict(visible=True)))
    plot.show()


# Przetwarzanie danych dla roku 2021
data2 = data.set_index("Date")
data3 = data2.T
data4 = data3[2021]
data5 = data4.sort_values(ascending=False)

# Top 5 najpopularniejszych języków
data6 = data5[:5].copy()

# Tworzenie DataFrame z wszystkimi językami
data7 = pd.DataFrame({'language': data5.index, 'percentage': data5.values})

# Tworzenie DataFrame z top 5 językami
data6 = pd.DataFrame({'language': data6.index, 'percentage': data6.values})

# Dodanie kategorii 'others'
new_row = pd.DataFrame(data={
    'language': ['others'],
    'percentage': [data7['percentage'][5:].sum()]})

data8 = pd.concat([data6, new_row], ignore_index=True)

# Wyświetlenie końcowego DataFrame
display(data8)

# Wykres kołowy
data8.plot(kind='pie', y='percentage', labels=data8['language'], autopct='%1.1f%%', figsize=(10, 10), legend=False, 
           title="Top 5 Najpopularniejszych języków 2021 roku", ylabel=' ')
plt.show()


