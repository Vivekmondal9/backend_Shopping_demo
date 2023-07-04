from django.http import JsonResponse,Http404
from django.views import View
from .serializer import ProductSerializer
from .models import Products
from django.core.paginator import Paginator
from django.db.models import Q


    

class ProductByFilter(View):
    def get(self,request):

        
        products=Products.objects.all()

        product_title=request.GET.get("title","")
        product_brand=request.GET.get("brand")
        product_category=request.GET.get("category")
        min_price=request.GET.get("min")
        max_price=request.GET.get("max")
        page_number=request.GET.get("page")  
       

        products=Products.objects.all()
        if product_title:
            products=products.filter(Q(title__icontains=product_title) | Q(description__icontains=product_title))
        if product_brand:
            products=products.filter(brand__icontains=product_brand)  
        if product_category:
            products=products.filter(category__icontains=product_category)  
        if min_price:
            products=products.filter(price__gte=min_price)
        if max_price:
            products=products.filter(price__lte=max_price) 

        # This part is for without pagination
        # serialized_products=[{

        #     "product_id":product.id,
        #     "product_title":product.title,
        #     "product_price":product.price,
        #     "product_image":product.image,
        #     "product_brand":product.brand,
        #     "product_category":product.category
        # } for product in products] 

        # return JsonResponse(serialized_products,safe=False)        


        # This part is with pagination .
        paginator=Paginator(products,5) 
        page_number=request.GET.get("page")
        page_obj=paginator.get_page(page_number)
        product_pages=page_obj.object_list
        serialized=ProductSerializer(product_pages,many=True).data
        serialized_products=[{
            "product_id":product["id"],
            "product_title":product["title"],
             "product_price":product["price"],
            "product_image":product["image"],
            "product_brand":product["brand"],
            "product_category":product["category"]
         } for product in serialized] 

        return JsonResponse({
             'products':serialized_products,
            'total_pages':paginator.num_pages,
            "has_next":page_obj.has_next()
        },safe=False)
    
        
          
   

              





    
# class ProductPagination(View):
#     def get(self,request):
#         products=Products.objects.all()

#         paginator=Paginator(products,5) 
#         page_number=request.GET.get("page")
#         page_obj=paginator.get_page(page_number)

#         product_pages=page_obj.object_list

#         serialized=ProductSerializer(product_pages,many=True).data

#         return JsonResponse({
#             'products':serialized,
#             'total_pages':paginator.num_pages,
#             "has_next":page_obj.has_next()
#         },safe=False)   






