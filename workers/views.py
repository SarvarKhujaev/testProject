from django.db.models import Count, Sum
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import JSONParser

from .serializer import *
from .inspectors.schema_inspector import *
from .inspectors.data_validate_inspector import *
from .inspectors.error_handler_inspector import ErrorInspector

ERROR_INSPECTOR: typing.Final[ErrorInspector] = ErrorInspector()


class EmployeeView(ViewSet):
    queryset: typing.Final = Employee.objects.all()

    def list(self, request) -> JsonResponse:
        return JsonResponse(
            data=EmployeeSerializer(
                self.queryset,
                many=True,
            ).data,
            status=status.HTTP_200_OK,
            safe=False,
        )

    def create(self, request) -> JsonResponse:
        employee: typing.Dict[str, typing.Any] = JSONParser().parse(request)

        """
        сравниваем форму отправленную от клиентам с правильной формой
        """
        check, e = compare_objects_identity(
            form=employee,
            right_form=employee_model_json,
        )

        """
        если объект правильно составлен, то дальше уже сохраняем в БД
        """
        if check:
            employee_serializer: EmployeeSerializer = EmployeeSerializer(data=employee)

            if employee_serializer.is_valid(raise_exception=True):
                employee_serializer.save()

            return JsonResponse(
                data=employee_serializer.data, status=status.HTTP_201_CREATED, safe=False
            )

        return ERROR_INSPECTOR.get_response(
            message=f"Wrong format of request: {e}",
            api_status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None) -> JsonResponse:
        employee: typing.Final[Employee] = get_object_or_404(
            self.queryset,
            pk=pk,
        )

        if ((updated_employee := EmployeeSerializer(employee, data=JSONParser().parse(request)))
                .is_valid(raise_exception=True)):
            updated_employee.save()  # сохраняем изменения
            return JsonResponse(
                data=updated_employee.data,
                safe=False,
                status=status.HTTP_200_OK,
            )

    def destroy(self, request, pk=None) -> JsonResponse:
        employee: typing.Final[Employee] = get_object_or_404(
            self.queryset,
            pk=pk,
        )

        employee.delete()

        return ERROR_INSPECTOR.get_response(
            message=f"Employee: {pk} was deleted",
        )

    def retrieve(self, request, pk=None) -> JsonResponse:
        if pk is None:
            return ERROR_INSPECTOR.get_response(
                message='wrong key',
                api_status=status.HTTP_400_BAD_REQUEST,
            )

        return JsonResponse(
            data=EmployeeSerializer(
                get_object_or_404(
                    self.queryset,
                    pk=pk
                )
            ).data,
            status=status.HTTP_200_OK,
        )


class ClientView(ViewSet):
    queryset: typing.Final = Client.objects.all()

    def list(self, request) -> JsonResponse:
        return JsonResponse(
            data=ClientSerializer(
                self.queryset,
                many=True,
            ).data,
            status=status.HTTP_200_OK,
            safe=False,
        )

    def create(self, request) -> JsonResponse:
        client: typing.Dict[str, typing.Any] = JSONParser().parse(request)

        """
        сравниваем форму отправленную от клиентам с правильной формой
        """
        check, e = compare_objects_identity(
            form=client,
            right_form=employee_model_json,
        )

        """
        если объект правильно составлен, то дальше уже сохраняем в БД
        """
        if check:
            client_serializer: ClientSerializer = ClientSerializer(data=client)

            if client_serializer.is_valid(raise_exception=True):
                client_serializer.save()

            return JsonResponse(
                data=client_serializer.data, status=status.HTTP_201_CREATED, safe=False
            )

        return ERROR_INSPECTOR.get_response(
            message=f"Wrong format of request: {e}",
            api_status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None) -> JsonResponse:
        client: typing.Final[Client] = get_object_or_404(
            self.queryset,
            pk=pk,
        )

        if ((updated_employee := ClientSerializer(client, data=JSONParser().parse(request)))
                .is_valid(raise_exception=True)):
            updated_employee.save()  # сохраняем изменения
            return JsonResponse(
                data=updated_employee.data,
                safe=False,
                status=status.HTTP_200_OK,
            )

    def destroy(self, request, pk=None) -> JsonResponse:
        client: typing.Final[Client] = get_object_or_404(
            self.queryset,
            pk=pk,
        )

        client.delete()

        return ERROR_INSPECTOR.get_response(
            message=f"Client: {pk} was deleted",
        )

    def retrieve(self, request, pk=None) -> JsonResponse:
        if pk is None:
            return ERROR_INSPECTOR.get_response(
                message='wrong key',
                api_status=status.HTTP_400_BAD_REQUEST,
            )

        return JsonResponse(
            data=ClientSerializer(
                get_object_or_404(
                    self.queryset,
                    pk=pk
                )
            ).data,
            status=status.HTTP_200_OK,
        )


class ProductView(ViewSet):
    queryset: typing.Final = Product.objects.all()

    def list(self, request) -> JsonResponse:
        return JsonResponse(
            data=ProductSerializer(
                self.queryset,
                many=True,
            ).data,
            status=status.HTTP_200_OK,
            safe=False,
        )

    def create(self, request) -> JsonResponse:
        product: typing.Dict[str, typing.Any] = JSONParser().parse(request)

        """
        сравниваем форму отправленную от клиентам с правильной формой
        """
        check, e = compare_objects_identity(
            form=product,
            right_form=product_model_json,
        )

        """
        если объект правильно составлен, то дальше уже сохраняем в БД
        """
        if check:
            product_serializer: ProductSerializer = ProductSerializer(data=product)

            if product_serializer.is_valid(raise_exception=True):
                product_serializer.save()

            return JsonResponse(
                data=product_serializer.data, status=status.HTTP_201_CREATED, safe=False
            )

        return ERROR_INSPECTOR.get_response(
            message=f"Wrong format of request: {e}",
            api_status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None) -> JsonResponse:
        product: typing.Final[Product] = get_object_or_404(
            self.queryset,
            pk=pk,
        )

        if ((updated_product := ProductSerializer(product, data=JSONParser().parse(request)))
                .is_valid(raise_exception=True)):
            updated_product.save()  # сохраняем изменения
            return JsonResponse(
                data=updated_product.data,
                safe=False,
                status=status.HTTP_200_OK,
            )

    def destroy(self, request, pk=None) -> JsonResponse:
        product: typing.Final[Product] = get_object_or_404(
            self.queryset,
            pk=pk,
        )

        product.delete()

        return ERROR_INSPECTOR.get_response(
            message=f"Product: {pk} was deleted",
        )

    def retrieve(self, request, pk=None) -> JsonResponse:
        if pk is None:
            return ERROR_INSPECTOR.get_response(
                message='wrong key',
                api_status=status.HTTP_400_BAD_REQUEST,
            )

        return JsonResponse(
            data=ProductSerializer(
                get_object_or_404(
                    self.queryset,
                    pk=pk
                )
            ).data,
            status=status.HTTP_200_OK,
        )


class OrderView(ViewSet):
    queryset: typing.Final = Order.objects.all()

    def list(self, request) -> JsonResponse:
        return JsonResponse(
            data=OrderSerializer(
                self.queryset,
                many=True,
            ).data,
            status=status.HTTP_200_OK,
            safe=False,
        )

    def create(self, request) -> JsonResponse:
        order: typing.Dict[str, typing.Any] = JSONParser().parse(request)

        """
        проверяем что указан клиент
        """
        if not CHECK_NONE(order.get('client')):
            return ERROR_INSPECTOR.get_response(
                message="Client was not attached",
                api_status=status.HTTP_400_BAD_REQUEST,
            )

        """
        проверяем что указаны продукты
        """
        if not CHECK_NONE(order.get('product')):
            return ERROR_INSPECTOR.get_response(
                message="Products was not attached",
                api_status=status.HTTP_400_BAD_REQUEST,
            )

        """
        проверяем что указан сотрудник
        """
        if not CHECK_NONE(order.get('employee')):
            return ERROR_INSPECTOR.get_response(
                message="Client was not attached",
                api_status=status.HTTP_400_BAD_REQUEST,
            )

        """
        сравниваем форму отправленную от клиентам с правильной формой
        """
        check, e = compare_objects_identity(
            form=order,
            right_form=order_model_json,
        )

        """
        если объект правильно составлен, то дальше уже сохраняем в БД
        """
        if check:
            """
            хранит общую стоимость всех товаров
            """
            price: float = 0

            """
            вычисляем общую стоимость всех товаров
            """
            for product in order['product']:
                price += product.price

            """
            сохраняем общую стоимость
            """
            order['price'] = price

            order_serializer: OrderSerializer = OrderSerializer(data=order)

            if order_serializer.is_valid(raise_exception=True):
                order_serializer.save()

            return JsonResponse(
                data=order_serializer.data, status=status.HTTP_201_CREATED, safe=False
            )

        return ERROR_INSPECTOR.get_response(
            message=f"Wrong format of request: {e}",
            api_status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None) -> JsonResponse:
        order: typing.Final[Order] = get_object_or_404(
            self.queryset,
            pk=pk,
        )

        if ((updated_order := OrderSerializer(order, data=JSONParser().parse(request)))
                .is_valid(raise_exception=True)):
            updated_order.save()  # сохраняем изменения
            return JsonResponse(
                data=updated_order.data,
                safe=False,
                status=status.HTTP_200_OK,
            )

    def destroy(self, request, pk=None) -> JsonResponse:
        order: typing.Final[Order] = get_object_or_404(
            self.queryset,
            pk=pk,
        )

        order.delete()

        return ERROR_INSPECTOR.get_response(
            message=f"Order: {pk} was deleted",
        )

    def retrieve(self, request, pk=None) -> JsonResponse:
        if pk is None:
            return ERROR_INSPECTOR.get_response(
                message='wrong key',
                api_status=status.HTTP_400_BAD_REQUEST,
            )

        return JsonResponse(
            data=OrderSerializer(
                get_object_or_404(
                    self.queryset,
                    pk=pk
                )
            ).data,
            status=status.HTTP_200_OK,
        )


class EmployeeStatisticsView(ViewSet):
    queryset: typing.Final = Employee.objects.all()

    def retrieve(self, request, *args, **kwargs) -> JsonResponse:
        employee: typing.Final[Client] = get_object_or_404(
            self.queryset,
            pk=kwargs.get('pk')
        )

        buyed_products_list: typing.List = Order.objects.all().values(
            'employee_id'
        ).filter(
            pk=kwargs.get('pk'),
            date__year=request.query_params.get('year'),
            date__month=request.query_params.get('month'),
        ).order_by(
            'employee_id'
        ).annotate(
            total_sum=Sum('price')
        ).annotate(
            total_count=Count('employee_id')
        )

        return JsonResponse(
            data={
                'id': employee.id,
                'full_name': employee.full_name,

                'buyed_products_sum': buyed_products_list[0].total_sum,
                'buyed_products_count': buyed_products_list[0].total_count,
            },
            status=status.HTTP_200_OK,
        )


class ClientStatisticsView(ViewSet):
    queryset: typing.Final = Client.objects.all()

    def retrieve(self, request, *args, **kwargs) -> JsonResponse:
        client: typing.Final[Client] = get_object_or_404(
            self.queryset,
            pk=kwargs.get('pk')
        )

        buyed_products_list: typing.List = Order.objects.all().values(
            'client_id'
        ).filter(
            pk=kwargs.get('pk'),
            date__year=request.query_params.get('year'),
            date__month=request.query_params.get('month'),
        ).order_by(
            'client_id'
        ).annotate(
            total_sum=Sum('price')
        ).annotate(
            total_count=Count('client_id')
        )

        return JsonResponse(
            data={
                'id': client.id,
                'full_name': client.full_name,

                'buyed_products_sum': buyed_products_list[0].total_sum,
                'buyed_products_count': buyed_products_list[0].total_count,
            },
            status=status.HTTP_200_OK,
        )
