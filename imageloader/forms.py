from django import forms
from imageloader.sqlite3_helper import *

class ImagesForm(forms.Form):
    # Get images from the database
    OPTIONS = get_images()
    # Take only first two elements of the tuple
    OPTIONS = [x[:2] for x in OPTIONS]
    SelectedImages = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)

class PipelinesForm(forms.Form):
    # Get pipelines from the database
    OPTIONS = get_pipelines()
    print(OPTIONS)
    SelectedPipelines = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)