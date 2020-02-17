from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Member

@login_required(login_url="/login/")
def index(request):
    members = Member.objects.all()
    return render(request, 'member/index.html', {'members': members})


@login_required(login_url="/login/")
def detail_member(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, 'member/pages/detail_member.html', {'member':member})



@login_required(login_url="/login/")
def new_member(request):
    if request.method == "POST":
        code_member = request.POST['code_member']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number1 = request.POST['phone_number1']
        email = request.POST['email']

        new_member = Member.objects.create(
            code_member = code_member,
            first_name= first_name,
            last_name = last_name,
            phone_number1 = phone_number1,
            email = email,
        )
        new_member.save()
        return redirect("/member")

    return render(request, 'member/pages/new_member.html')

@login_required(login_url="/login/")
def edit_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == "POST":
        code_member = request.POST['code_member']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number1 = request.POST['phone_number1']
        email = request.POST['email']

        member_to_edit = Member.objects.filter(pk=member.id)
        member_to_edit.update(
            code_member = code_member,
            first_name= first_name,
            last_name = last_name,
            phone_number1 = phone_number1,
            email = email,
        )
        return redirect("/member")
    return render(request, 'member/pages/edit_member.html', {'member': member})


@login_required(login_url="/login/")
def delete_member(request, id):
    member = get_object_or_404(Member, id=id) 
    if request.method == "POST":
        member.delete()
        return redirect("/member")
    return render(request, 'member/pages/delete_member.html', {'member':member})