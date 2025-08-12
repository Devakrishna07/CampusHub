from rest_framework import serializers
from .models import EventPoster
from supabase import create_client
import uuid
import os

class EventSerializer(serializers.ModelSerializer):
    image_file = serializers.ImageField(write_only=True, required=True)

    class Meta:
        model = EventPoster
        fields = '__all__'
        read_only_fields = ['poster_image']

    def create(self, validated_data):
        image_file = validated_data.pop('image_file')

        # Initialize Supabase client
        supabase = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )

        # Generate unique file name
        file_ext = image_file.name.split('.')[-1]
        file_name = f"{uuid.uuid4()}.{file_ext}"

        # Upload to Supabase bucket
        bucket_name = os.getenv("SUPABASE_BUCKET", "events poster")
        supabase.storage.from_(bucket_name).upload(file_name, image_file.read())

        # Get public URL
        public_url = supabase.storage.from_(bucket_name).get_public_url(file_name)

        # Save public URL to poster_image
        validated_data['poster_image'] = public_url
        return EventPoster.objects.create(**validated_data)
