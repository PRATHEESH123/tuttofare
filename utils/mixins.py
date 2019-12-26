""" 
This mixin can be used to make a signal serializer 
to return differnet fields based on the type of view 
the serializer is called on

right now it only supports list and retrive views

list: retruns all the field declared in fields
retrive: returns all the field declared in fields and detail_field

usage:

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
        )
        detail_fields = (
            'images',
            'rating',
            'descrption',
        )

"""


class DynamicSerializerMixin:

    def get_field_names(self, declared_fields, info):
        # TODO arrest shouldn't be raised if a declared field
        # is not used in field, but is used in detail_fields

        a = super().get_field_names(declared_fields, info)

        view = self.context.get('view')
        detail_fields = getattr(self.Meta, 'detail_fields', tuple())

        if view.action == 'retrieve':
            return a + detail_fields
        return a
