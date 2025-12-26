import pandas as pd

def muscle_growth_model(data, alpha=0.1, beta=0.05):
    data=data.sort_values('date')
    growth=0
    growth_list=[]
    for _, row in data.iterrows():
        volume=row['sets']*row['reps']*row['weight']
        growth+=alpha*volume-beta*growth
        growth_list.append(growth)
    data['predicted_muscle_growth']=growth_list
    return data

# Example usage
if __name__ == "__main__":
    sample_data = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=5),
        'sets': [3, 3, 4, 3, 5],
        'reps': [10, 12, 10, 15, 12],
        'weight': [50, 55, 55, 60, 65]
    })
    result = muscle_growth_model(sample_data)
    print(result[['date', 'predicted_muscle_growth']])