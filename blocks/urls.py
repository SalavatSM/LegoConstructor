from django.urls import path
from .views import (BlockListCreate, BlockDetail, SetListCreate, SetDetail, block_list, block_detail, block_create,
                    block_update, block_delete)


urlpatterns = [
    path('block/', BlockListCreate.as_view(), name='block-list-create'),
    path('blocks/<int:pk>/', BlockDetail.as_view(), name='block-detail'),
    path('sets/', SetListCreate.as_view(), name='set-list-create'),
    path('sets/<int:pk>/', SetDetail.as_view(), name='set-detail'),

    # Template URLs
    path('blocks/', block_list, name='block-list'),
    path('blocks/<int:pk>/', block_detail, name='block-detail'),
    path('blocks/create/', block_create, name='block-create'),
    path('blocks/<int:pk>/edit/', block_update, name='block-update'),
    path('blocks/<int:pk>/delete/', block_delete, name='block-delete'),
]

