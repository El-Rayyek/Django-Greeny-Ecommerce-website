from .models import Brand , Category


def get_brand(request):
    brands = Brand.objects.all()

    return {'c_brands':brands}