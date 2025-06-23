# predictor/forms.py

from django import forms

class ExamPredictionForm(forms.Form):
    previous_gpa = forms.FloatField(
        label="Previous GPA (0.0 – 4.0)",
        min_value=0.0, max_value=4.0,
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 3.5',
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    motivation_level = forms.IntegerField(
        label="Motivation Level (1 – 10)",
        min_value=1, max_value=10,
        widget=forms.NumberInput(attrs={
            'placeholder': '1–10',
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    study_hours_per_day = forms.FloatField(
        label="Study Hours Per Day (0 – 12)",
        min_value=0, max_value=12,
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 4',
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    screen_time = forms.FloatField(
        label="Screen Time (0 – 12)",
        min_value=0, max_value=12,
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 5',
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    access_to_tutoring = forms.ChoiceField(
        label="Access to Tutoring",
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    study_environment = forms.ChoiceField(
        label="Study Environment",
        choices=[('Quiet Room', 'Quiet Room'), ('Library', 'Library'),
                 ('Co-Learning Group', 'Co-Learning Group'), ('Dorm', 'Dorm'), ('Cafe', 'Cafe')],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    sleep_hours = forms.FloatField(
        label="Sleep Hours (0 – 12)",
        min_value=0, max_value=12,
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 7.5',
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    exercise_frequency = forms.IntegerField(
        label="Exercise Frequency (0 – 7 days/week)",
        min_value=0, max_value=7,
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 3',
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    dropout_risk = forms.ChoiceField(
        label="Dropout Risk",
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    stress_level = forms.IntegerField(
        label="Stress Level (1 – 10)",
        min_value=1, max_value=10,
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 6',
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )

    exam_anxiety_score = forms.IntegerField(
        label="Exam Anxiety Score (1 – 10)",
        min_value=1, max_value=10,
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 4',
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none input-field'
        })
    )
