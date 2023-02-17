from django.db.models import ImageField
from django.forms import forms


class ImageRestrictedFileField(ImageField):
    """
    Same as FileField, but you can specify:
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB - 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.max_upload_size = kwargs.pop("max_upload_size", 0)
        super(ImageRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ImageRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        try:
            if file.size > self.max_upload_size:
                raise forms.ValidationError('Please keep filesize lower.')
        except AttributeError:
            pass

        return data
