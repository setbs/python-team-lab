from django.db.models import Q

from goods.models import Products


def q_search(query):
    
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)








#               /`·.¸
#              /¸...¸`:·
#         ¸.·´  ¸   `·.¸.·´)   0 0  02 0  -    з з2 з  01 0 0 0 0 0 1 01 0  
#         : © ):´;      ¸  {  - -  - - 11   0 0      1 0 1    1 010    0   
#         `·.¸ `·  ¸.·´\`·¸)   -    - - - 1  01 0   1 1001     - -  -   - -0
#              `\\\\´´\¸.·´
#