from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Существующая функция для отображения списка заметок
@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)  # Получаем все заметки
    
    return render(request, 'calendar_notes/note_list.html', {'notes': notes})

# Страница добавления новой заметки
@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Привязываем заметку к текущему пользователю
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'calendar_notes/add_note.html', {'form': form})


# Страница редактирования заметки
@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.user != request.user:  # Проверяем, принадлежит ли заметка текущему пользователю
        return redirect('register')  # Если нет, перенаправляем на список заметок
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'calendar_notes/edit_note.html', {'form': form, 'note': note})


# Страница удаления заметки
@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.user != request.user:  # Проверяем, принадлежит ли заметка текущему пользователю
        return redirect('note_list')
    note.delete()
    return redirect('note_list')

#Страница регистрации
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Авторизуем пользователя после регистрации
            return redirect('profile')  # Перенаправляем на страницу списка заметок
    else:
        form = UserRegisterForm()

    return render(request, 'calendar_notes/register.html', {'form': form})

@login_required
def profile_view(request):
    # Здесь можно передать дополнительные данные, например, информацию о пользователе
    return render(request, 'profile.html')  # Убедитесь, что этот шаблон существует

