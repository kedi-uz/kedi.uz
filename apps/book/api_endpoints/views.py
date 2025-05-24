from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from apps.book import models
from apps.book.api_endpoints import schemas


router = Router()


@router.get("/lost-animal-list/", response=List[schemas.LostAnimalSchema])
def get_lost_animal_list(request):
    queryset = models.LostAnimal.objects.select_related(
        "animal_type", "gender_type", "posted_by"
    ).all()
    return queryset


@router.get("/lost-animal/{lost_animal_id}", response=schemas.LostAnimalSchema)
def get_lost_animal(request, lost_animal_id: int):
    queryset = get_object_or_404(models.LostAnimal, id=lost_animal_id)
    return queryset


@router.get("/district/", response=List[schemas.DistrictSchema])
def get_district_all(request):
    queryset = models.District.objects.all()
    return list(queryset)


@router.get("/district/{id}", response=schemas.DistrictSchema)
def get_district(request, id: int):
    queryset = get_object_or_404(models.District, id=id)
    return queryset
