import joblib
import pandas as pd
from django.shortcuts import render
from .forms import ExamPredictionForm

# Load model once (reuse for all users)
model = joblib.load('exam_score_predictor.pkl')  # adjust the path

def predict_exam_score(request):
    result = None
    if request.method == 'POST':
        form = ExamPredictionForm(request.POST)
        if form.is_valid():
            data = {
                'previous_gpa': [form.cleaned_data['previous_gpa']],
                'motivation_level': [form.cleaned_data['motivation_level']],
                'study_hours_per_day': [form.cleaned_data['study_hours_per_day']],
                'screen_time': [form.cleaned_data['screen_time']],
                'access_to_tutoring': [form.cleaned_data['access_to_tutoring']],
                'study_environment': [form.cleaned_data['study_environment']],
                'sleep_hours': [form.cleaned_data['sleep_hours']],
                'exercise_frequency': [form.cleaned_data['exercise_frequency']],
                'dropout_risk': [form.cleaned_data['dropout_risk']],
                'stress_level': [form.cleaned_data['stress_level']],
                'exam_anxiety_score': [form.cleaned_data['exam_anxiety_score']]
            }
            df = pd.DataFrame(data)
            result = round(model.predict(df)[0], 2)
    else:
        form = ExamPredictionForm()
    
    return render(request, 'predictor/form.html', {'form': form, 'result': result})
