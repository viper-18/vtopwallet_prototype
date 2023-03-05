from django import forms

expirydm_choices = [
    ('january', '1 - january'),
    ('february', '2 - february'),
    ('march', '3 - march'),
    ('april', '4 - april'),
    ('may', '5 - may'),
    ('june', '6 - june'),
    ('july', '7 - july'),
    ('august', '8 - august'),
    ('september', '9 - september'),
    (' october', '10 - october'),
    (' november', '11 -november'),
    (' december', '12 -december')
]

expiryy_choices = [
    ('2023','2023'),
    ('2024','2024'),
    ('2025','2025'),
    ('2026','2026'),
    ('2027','2027'),
    ('2028','2028'),
    ('2029','2029'),
]

class ppgPay(forms.Form):
    card_holder = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
        'class':'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
        'placeholder':'vishesh bansal',
        'type':'text'
    }))
    
    card_no = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
        'class':'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
        'placeholder':'0000 0000 0000 0000',
        'type':'text'
    }))
    expiry_dm = forms.CharField(widget=forms.Select(choices=expirydm_choices, attrs={
        'class':'form-select w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors cursor-pointer'
    }))
    expiry_y = forms.CharField(widget=forms.Select(choices=expiryy_choices, attrs={
        'class':'form-select w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors cursor-pointer'
    }))
    security = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'w-32 px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors required',
        # 'pattern':'([0-9]|[0-9]|[0-9])',
        'max':'999',
        
    }))
    amount = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'w-32 px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors required',
        'type':'number'
    }))
