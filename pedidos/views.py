from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO


def Procesar_pedido(request):
    # ... (código anterior)

    # Generar el PDF
    pdf_buffer = BytesIO()
    p = canvas.Canvas(pdf_buffer)

    # Aquí puedes agregar contenido al PDF utilizando las funciones de reportlab
    p.drawString(100, 100, "Gracias por tu pedido")
    p.drawString(100, 80, f"Usuario: {request.user.username}")
    # Agrega más contenido según tus necesidades

    p.showPage()
    p.save()

    # Configurar la respuesta HTTP para enviar el PDF
    pdf_buffer.seek(0)
    response = HttpResponse(pdf_buffer, content_type="application/pdf")
    response["Content-Disposition"] = 'filename="pedido.pdf"'

    # ... (puedes agregar más acciones si es necesario, como guardar el PDF en el servidor)

    return response
