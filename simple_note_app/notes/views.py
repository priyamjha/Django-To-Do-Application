from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Note
from .forms import NoteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def note_list(request):
    query = request.GET.get('q')
    notes = Note.objects.filter(created_by=request.user)
    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-created_at')
    else:
        notes = notes.order_by('-created_at')
    if not notes.exists():
        messages.warning(request,"No notes found or created yet!")
    
    paginator = Paginator(notes, 6)  # 6 notes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'notes/note_list.html', context)

@login_required
def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    if note.created_by != request.user:
        messages.warning(request,"Sorry, you are have permission to see this!")
        return redirect('note_list')
    return render(request, 'notes/note_detail.html', {'note': note})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
            messages.info(request,"Note Created Successfully!")
            return redirect('note_list')  # Adjust this redirect as needed
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_update(request, pk):
    note = Note.objects.get(pk=pk)
    if note.created_by != request.user:
        messages.warning(request,"Sorry, you are have permission to update this!")
        return redirect('note_list')
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.info(request,"Note Updated Successfully!")
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


@login_required
def note_delete(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request,"Sorry, you are not delete a note except you logged in!")
    note = Note.objects.get(pk=pk)
    if note.created_by != request.user:
        messages.warning(request,"Sorry, you are have permission to delete this!")
        return redirect('note_list')
    if request.method == 'POST':
            note.delete()
            messages.info(request, "Note deleted successfully.")
            return redirect('note_list')
    else:
        messages.warning(request,"Sorry, you are have permission to change this!")
        return redirect('note_list')
