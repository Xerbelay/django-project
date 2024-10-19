from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden


def product_detail(request): 
    id = int(request.GET.get('id'))
    products = ['cucumber', 'tomato', 'carrot', 'lettuce', 'potato', 'onion', 'garlic', 'pepper', 'broccoli']
    if id in range(0, len(products)):
        return HttpResponse(products[id], status=200)
    else:
        return HttpResponseNotFound("Product not found", status=404)
def check_availability(request):
    number = int(request.GET.get('number'))
    if (number<0):
        return HttpResponseBadRequest("Number must be positive", status=400)
    if(number == 0):
        return HttpResponse("The product is missing", status=204)
    else:
        return HttpResponse("Product is available", status=200)

