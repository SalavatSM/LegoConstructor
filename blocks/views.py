from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import Block, Set
from .serializers import BlockSerializer, SetSerializer


class BlockListCreate(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class BlockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class SetListCreate(generics.ListCreateAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


class SetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


def block_list(request):
    blocks = Block.objects.all()
    return render(request, 'blocks/block_list.html', {'blocks': blocks})


def block_detail(request, pk):
    block = get_object_or_404(Block, pk=pk)
    return render(request, 'blocks/block_detail.html', {'block': block})


def block_create(request):
    if request.method == 'POST':
        form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block-list')
    else:
        form = BlockForm()
    return render(request, 'blocks/block_form.html', {'form': form})


def block_update(request, pk):
    block = get_object_or_404(Block, pk=pk)
    if request.method == 'POST':
        form = BlockForm(request.POST, instance=block)
        if form.is_valid():
            form.save()
            return redirect('block-detail', pk=block.pk)
    else:
        form = BlockForm(instance=block)
    return render(request, 'blocks/block_form.html', {'form': form, 'block': block})


def block_delete(request, pk):
    block = get_object_or_404(Block, pk=pk)
    if request.method == 'POST':
        block.delete()
        return redirect('block-list')
    return render(request, 'blocks/block_confirm_delete.html', {'block': block})
