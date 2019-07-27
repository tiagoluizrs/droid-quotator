from rest_framework import generics, status
from .models import Demand
from .serializers import DemandSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import user_show

class DemandList(generics.ListCreateAPIView):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    def list(self, request):
        """
        Estratégia criada para permitir a expansão do programa
        Poderia ser feito apenas verificando o usuário é um superuser ou não.
        Fiz dessa forma para seguir o conceito do usuário admin e anunciante.
        """
        query_all = user_show(request)
        
        if query_all:
            queryset = Demand.objects.all()
        else:
            queryset = Demand.objects.filter(id=request.user.id)

        serializer = DemandSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request.data.update({
            "user": request.user.id
        })
        return self.create(request, *args, **kwargs)
    
class DemandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Estratégia criada para permitir a expansão do programa
        Poderia ser feito apenas verificando o usuário é um superuser ou não.
        Fiz dessa forma para seguir o conceito do usuário admin e anunciante.
        """
        query_all = user_show(request)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = []
        
        if query_all:
            data = serializer.data
        elif serializer.data['user'] == request.user.id:
            data = serializer.data

        return Response(data)

    def patch(self, request, *args, **kwargs):
        query_all = user_show(request)
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if query_all or serializer.data['user'] == request.user.id:
            return self.partial_update(request, *args, **kwargs)
        else:
            content = {'erro': 'You do not have permission to update this demand.'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, *args, **kwargs):
        query_all = user_show(request)
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if query_all or serializer.data['user'] == request.user.id:
            return self.destroy(request, *args, **kwargs)
        else:
            content = {'erro': 'You do not have permission to delete this demand.'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

        
class DemandDetailFinish(generics.RetrieveUpdateDestroyAPIView):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    def patch(self, request, *args, **kwargs):
        query_all = user_show(request)
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if query_all or serializer.data['user'] == request.user.id:
            request.data.update({
                'status': False
            })
            return self.partial_update(request, *args, **kwargs)
        else:
            content = {'erro': 'You do not have permission to finish this demand.'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
