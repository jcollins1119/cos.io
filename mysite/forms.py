from django import forms


class ContactForm(forms.Form):

    fname = forms.CharField(label='First Name', max_length=100)
    lname = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    org = forms.CharField(label='Organization', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    checkbox = []
    for i in range(9):
        checkbox.append(i)
        checkbox[i] = forms.BooleanField(required=False)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    # proof_of_publication = forms.ChoiceField(
    #     label="Proof of publication",
    #     choices=(
    #         ("not_submitted", "Published Article Not Yet Submitted"),
    #         ("submitted", "Published Article Submitted"),
    #         ("under_review", "Published Article Under Review"),
    #         ("approved", "Published Article Approved"),
    #         ("rejected", "Published Article Rejected"),
    #     )
    # )
    # payment_sent = forms.BooleanField(
    #     label="Payment sent",
    #     required=False
    # )
    # assignee = forms.ChoiceField(
    #     label="Assignee",
    #     choices=list(),
    #     required=False,
    # )
    #
    # notes = forms.CharField(
    #     label="Notes",
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'prereg-form-notes'
    #         }
    #     ),
    #     required=False
    # )