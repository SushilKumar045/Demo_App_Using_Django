from django.shortcuts import render
import os
import pickle

# Create your views here.
def home(request):
    return render(request, "index.html")

def predict(request):
    if request.method == 'POST':
        income = int(request.POST.get('income'))
        score = int(request.POST.get('score'))

        # Load the model
        model = pickle.load(open('Demo_App_Django.pkl','rb'))
       
        # Make prediction
        predict = model.predict([[income, score]])

        # Determine the result based on prediction
        if predict == [0]:
            result = "Customer is Careless"
        elif predict == [1]:
            result = "Customer is Standard"
        elif predict == [2]:
            result = "Customer is Target"
        elif predict == [3]:
            result = "Customer is Careful"
        else:
            result = "Customer is Sensible"

        # Render the result
        return render(request, 'index.html', {'prediction_text': 'Model has predicted: {}'.format(result)})

    return render(request, "index.html")
