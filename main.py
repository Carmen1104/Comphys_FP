import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('data/airplane-accident-severity.csv')

X=data.drop(['Severity', 'Accident_ID'],axis=1)
y=data.Severity

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

window = tk.Tk()
window.title('Plane Crash Prediction')
window.geometry('400x200')

def predict_crash():
    # Get the input values from the text entry fields
    input_values = [entry.get() for entry in entry_fields]

    prediction = classifier.predict([input_values])[0]
    result = 'Crash' if prediction else 'No Crash'

    # Show the prediction result
    messagebox.showinfo('Prediction Result', f'Prediction: {result}')

    label = tk.Label(window, text='Enter flight details:')
    label.pack()

    entry_fields = []
      
    for feature in features:
        entry_label = tk.Label(window, text=feature)
        entry_label.pack()
        entry = tk.Entry(window)
        entry.pack()
        entry_fields.append(entry)

    predict_button = tk.Button(window, text='Predict', command=predict_crash)
    predict_button.pack()

    window.mainloop()