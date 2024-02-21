from psycopg2 import sql
from django.db import connection
from django.http.response import JsonResponse

from rest_framework import status
from inspectors.error_handler_inspector import ErrorInspector
from constants.postgre_table_names import TableNamesAndCommands as tableNames


class PostgreCommands(ErrorInspector):
    def _delete_row(self, **kwargs) -> JsonResponse:
        if kwargs.get('id') is None:
            return self.get_response(
                message='Empty value',
                api_status=status.HTTP_400_BAD_REQUEST,
            )

        with connection.cursor() as cursor:
            stmt: sql.Composed = sql.SQL(
                tableNames.Delete.value,
            ).format(
                table_name=sql.Identifier(kwargs.get('table_name')),
                id=sql.Literal(kwargs.get('id')),
            )

            cursor.execute(stmt)
            return self.get_response(
                message='Deleted',
                api_status=status.HTTP_204_NO_CONTENT)

    def _get_average(self, **kwargs) -> JsonResponse:
        with connection.cursor() as cursor:
            average_temperature_sql: sql.Composed = sql.SQL(
                kwargs.get('command_for_temperature')
            ).format(
                table_name=sql.Identifier(kwargs.get('table_name_for_temperature')),
                id=sql.Literal(kwargs.get('id')),
            )

            cursor.execute(average_temperature_sql)
            average_temperature: float = cursor.fetchone()[0]

            average_pressure_sql: sql.Composed = sql.SQL(
                kwargs.get('command_for_pressure')
            ).format(
                table_name=sql.Identifier(kwargs.get('table_name_for_pressure')),
                id=sql.Literal(kwargs.get('id')),
            )

            cursor.execute(average_pressure_sql)
            average_pressure: float = cursor.fetchone()[0]

            return JsonResponse(
                data={
                    'average_pressure: ': average_pressure,
                    'average_temperature': average_temperature,
                }, status=status.HTTP_200_OK,
            )
