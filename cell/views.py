from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cell

@login_required(login_url="/login/")
def index(request):
    cells = Cell.objects.all()
    return render(request, 'cell/index.html', {'cells': cells})



@login_required(login_url="/login/")
def detail_cell(request, id):
    cell = get_object_or_404(Cell, id=id)
    return render(request, 'cell/pages/detail_cell.html', {'cell':cell})




@login_required(login_url="/login/")
def new_cell(request):
    if request.method == "POST":
        cell_label = request.POST['cell_label']
        cell_addr = request.POST['cell_addr']
        cell_link_map = request.POST['cell_link_map']

        new_cell = Cell.objects.create(
            cell_label = cell_label,
            cell_addr= cell_addr,
            cell_link_map = cell_link_map,
        )
        new_cell.save()
        
        return redirect("/cell")

    return render(request, 'cell/pages/new_cell.html')

@login_required(login_url="/login/")
def edit_cell(request, id):
    member = get_object_or_404(Cell, id=id)
    if request.method == "POST":
        cell_label = request.POST['cell_label']
        cell_addr = request.POST['cell_addr']
        cell_link_map = request.POST['last_name']

        member_to_edit = Cell.objects.filter(pk=member.id)
        member_to_edit.update(
            cell_label = cell_label,
            cell_addr= cell_addr,
            cell_link_map = cell_link_map,
        )
        return redirect("/cell")
    return render(request, 'cell/pages/edit_cell.html', {'cell': cell})


@login_required(login_url="/login/")
def delete_cell(request, id):
    cell = get_object_or_404(Cell, id=id) 
    if request.method == "POST":
        cell.delete()
        return redirect("/cell")
    return render(request, 'cell/pages/delete_cell.html', {'cell':cell})