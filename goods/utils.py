from django.db.models import Q
from django.shortcuts import render
from django.contrib.postgres.search import SearchVector
from goods.models import Products


# def q_search(query):
    
#     if query.isdigit() and len(query) <= 5:
#         return Products.objects.filter(id=int(query))

#     return Products.objects.filter(description__search=query)






def catalog(request):
    query = request.GET.get('q', '')
    if query.isdigit() and len(query) <= 5:
       return Products.objects.filter(id=int(query))

    elif query:
        products = q_search(query)
        return render(request, 'catalog.html', {'products': products})
    else:
        return render(request, 'catalog.html', {})     
        

def q_search(query):
    return Products.objects.filter(description__icontains=query)












    # return Products.objects.annotated(search=SearchVector("name", "description")).filter(search=query)

    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return Products.objects.filter(q_objects)


#               /`·.¸
#              /¸...¸`:·
#         ¸.·´  ¸   `·.¸.·´)   0 0  02 0  -    з з2 з  01 0 0 0 0 0 1 01 0  
#         : © ):´;      ¸  {  - -  - - 11   0 0      1 0 1    1 010    0   
#         `·.¸ `·  ¸.·´\`·¸)   -    - - - 1  01 0   1 1001     - -  -   - -0                    #8:20 - 8:50 [search]
#              `\\\\´´\¸.·´
#