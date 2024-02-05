def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        carro_session = request.session.get("carro", {})
        for key, value in carro_session.items():
            total += float(value.get("precio", 0.0)) * value.get("cantidad", 0)

        # Redondear el total a dos decimales
        total = round(total, 2)

    return {"importe_total_carro": total}
