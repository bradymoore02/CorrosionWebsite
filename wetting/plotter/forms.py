from django import forms


class MyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop('options')
        super(MyForm, self).__init__(*args, **kwargs)
        for option in options:
            self.fields[option] = forms.BooleanField(required=False,
                                                     label=option)
