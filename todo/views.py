from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, User, Item
from .serializers import TaskSerializer, UserSerializer, ItemSerializer

# ✅ Task List + Create
class TaskListCreateView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# ✅ Task Detail
class TaskDetailView(APIView):

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


# ✅ User Profile
class UserProfileView(APIView):

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# ✅ Item List + Create
class ItemListCreateView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = request.data.get('user')
        unit = request.data.get('unit')

        user = User.objects.get(id=user_id)

        SI_UNITS = ['kg', 'g']
        IMP_UNITS = ['lb', 'oz']
        COMMON = ['packet', 'piece']

        allowed_units = COMMON.copy()

        if user.preferred_units == 'SI':
            allowed_units += SI_UNITS
        else:
            allowed_units += IMP_UNITS

        if unit not in allowed_units:
            return Response({"error": "Invalid unit for this user"}, status=400)

        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)