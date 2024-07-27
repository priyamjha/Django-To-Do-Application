from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Note
from .forms import NoteForm
from django.contrib import messages


def note_list(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-created_at')
    else:
        notes = Note.objects.all().order_by('-created_at')
    paginator = Paginator(notes, 6)  # 10 notes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'notes/note_list.html', {'page_obj': page_obj, 'query': query})

def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_update(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request,"Sorry, you are not delete a note except you logged in!")
    else:
        note = Note.objects.get(pk=pk)
        if request.method == 'POST':
            note.delete()
            return redirect('note_list')
        else:
            messages.warning(request,"Sorry, you are have permission to change this!")
            return redirect('note_list')
