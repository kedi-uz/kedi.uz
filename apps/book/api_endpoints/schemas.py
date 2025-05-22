from typing import Optional
from django.contrib.auth.models import User
from ninja import ModelSchema

from apps.book import models


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]


class CommunitySchema(ModelSchema):
    class Meta:
        model = models.Community
        fields = [
            "id",
            "title",
            "image",
            "description",
            "telegram_link",
        ]


class GenderTypeSchema(ModelSchema):
    class Meta:
        model = models.GenderType
        fields = [
            "id",
            "title",
        ]


class AnimalTypeSchema(ModelSchema):
    class Meta:
        model = models.AnimalType
        fields = [
            "id",
            "title",
        ]


class DistrictSchema(ModelSchema):
    class Meta:
        model = models.District
        fields = [
            "id",
            "title",
        ]


class LostAnimalSchema(ModelSchema):
    animal_type: AnimalTypeSchema
    gender_type: GenderTypeSchema
    posted_by: UserSchema
    district: Optional[DistrictSchema] = None

    class Meta:
        model = models.LostAnimal
        fields = [
            "id",
            "title",
            "photo",
            "description",
            "location",
            "latitude",
            "longitude",
            "date_lost",
            "phone_number",
        ]
