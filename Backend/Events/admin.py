from django.contrib import admin
from django import forms
from .models import EventPoster
from supabase import create_client
import os, uuid

class EventPosterAdminForm(forms.ModelForm):
    # This field shows the file picker in admin
    image_file = forms.ImageField(required=False, label="Upload Event Poster")

    class Meta:
        model = EventPoster
        exclude = ("poster_image",)  # hide poster_image URL from admin form

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')

        if image_file:
            # Connect to Supabase
            supabase = create_client(
                os.getenv("SUPABASE_URL"),
                os.getenv("SUPABASE_KEY")
            )
            bucket = os.getenv("SUPABASE_BUCKET", "event_posters")

            # Create unique filename
            file_ext = image_file.name.split('.')[-1]
            file_name = f"{uuid.uuid4()}.{file_ext}"

            # Upload to Supabase
            supabase.storage.from_(bucket).upload(file_name, image_file.read())

            # Set the public URL
            public_url = f"{os.getenv('SUPABASE_URL')}/storage/v1/object/public/{bucket}/{file_name}"
            instance.poster_image = public_url

        if commit:
            instance.save()
        return instance

class EventPosterAdmin(admin.ModelAdmin):
    form = EventPosterAdminForm
    list_display = ("EventTitle", "EventDate", "Venue", "poster_image")

admin.site.register(EventPoster, EventPosterAdmin)
