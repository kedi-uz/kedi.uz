from typing import List, Annotated
from ninja import Router
from django.shortcuts import get_object_or_404

from apps.common import models
from apps.common.api_endpoints import schemas


router = Router()


@router.get("/post/", response=List[schemas.PostSchema])
def get_post_all(request):
    queryset = models.Post.objects.prefetch_related("tag").all()
    return queryset


@router.get("/post/{post_id}", response=schemas.PostSchema)
def get_post(request, post_id: int):
    queryset = get_object_or_404(models.Post, id=post_id)
    return queryset


@router.get("/position/", response=Annotated[List[schemas.PositionSchema], 200])
def get_position_all(request):
    queryset = models.Position.objects.select_related("region", "event").all()
    return list(queryset)


@router.get("/position/{position_id}", response=schemas.PositionSchema)
def get_position(request, position_id: int):
    queryset = get_object_or_404(models.Position, id=position_id)
    return queryset
