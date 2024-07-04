@login_required(login_url="/login/")
def ver_inmueble(request):
    inmuebles = Inmuebles.objects.filter(id_usuario = request.user)
    return render(request, 'ver_inmuebles.html', {"inmuebles" : inmuebles})


@login_required(login_url="/login/")
def editar_inmueble(request):
    if request.method == 'POST':
        inmueble = type(Inmuebles()).objects.filter(id_usuario = request.user)
        form = InmuebleUpdateForm(request.POST, instance=inmueble)
        if form.is_valid():

            form.save()
            messages.success(request, "Inmueble actualizado")
            return redirect("perfil", form.user)
    inmueble = type(Inmuebles()).objects.filter(id_usuario = request.user).first()
    if inmueble:
        form = InmuebleUpdateForm(instance=inmueble)
        return render(request, 'editar_inmuebles.html', {'form' : form})
    return redirect("inicio/")