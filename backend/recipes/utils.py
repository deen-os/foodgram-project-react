from django.http import HttpResponse


class ShoppingCartDownload:
    def __init__(self, ing_list, content, ing_name, ing_meas_unit, sum_amount):
        self.ing_list = ing_list
        self.content = content
        self.ing_name = ing_name
        self.ing_meas_unit = ing_meas_unit
        self.sum_amount = sum_amount

    def download(self):
        if self.ing_list:
            for index, item in enumerate(self.ing_list, start=1):
                self.content += (
                    f'{index}. {item[self.ing_name]} '
                    f'({item[self.ing_meas_unit]}) - '
                    f'{item[self.sum_amount]} '
                    '\n'
                )
        else:
            self.content += 'Список покупок пуст'
        return HttpResponse(
            self.content,
            content_type='text/plain', charset='utf8',
            headers={'Content-Disposition': 'attachment; filename=to_buy.txt'},
        )
