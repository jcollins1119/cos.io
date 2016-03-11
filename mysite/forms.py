from django import forms


class ContactForm(forms.Form):

    fname = forms.CharField(label='First Name', max_length=100)
    lname = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    org = forms.CharField(label='Organization', max_length=100, required=False)
    title = forms.CharField(label='Title', max_length=100, required=False)
    checkbox = []
    for i in range(9):
        checkbox.append(i)
        checkbox[i] = forms.BooleanField(required=False)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=False)
