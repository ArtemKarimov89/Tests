import requests


def discriminant(a, b, c):
    discrim = b ** 2 - 4 * a * c
    return discrim


def square_perimeter(a):
    perimeter = a * 4
    return perimeter


def square_area(square_length):
    area = square_length * square_length
    return area


# class YandexTest:
#
#     def __init__(self):
#         header = {
#             'Authorization': 'OAuth y0_AgAAAAB0L5Z6AADLWwAAAAD9NYFPAABLZLbzwQVHXqbWWBSDSwxhgBY-0A'
#         }
#         params = {
#             'path': 'test'
#         }
#
#         response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=header, params=params)
#         self.response = response
#         print(response)
#
#     def test_create_folder(self):
#         assert self.response.status_code == 201
#
#
# f = YandexTest()
# f.test_create_folder()