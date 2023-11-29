from rest_framework import generics

class GeneralListAPIView(generics.ListAPIView):
    """List all General"""

    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)