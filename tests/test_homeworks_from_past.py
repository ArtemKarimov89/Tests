import pytest
import requests

from main import square_perimeter, square_area, discriminant


@pytest.mark.parametrize(
    'actual, expected',
    (
            [5, 20],
            [11, 44],
            [7, 28]
    )
)
class TestSquarePerimeter:

    def test_square_perimeter(self, actual, expected):
        assert square_perimeter(actual) == expected


@pytest.mark.parametrize(
    'actual, expected',
    (
            [5, 25],
            [11, 121],
            [7, 49]
    )
)
class TestSquareArea:

    def test_square_area(self, actual, expected):
        assert square_area(actual) == expected


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
            [5, 1, 10, -199],
            [1, 6, 3, 24],
            [7, 15, 5, 85]
    )
)
class TestDiscriminant:

    def test_discriminant(self, a, b, c, expected):
        assert discriminant(a, b, c) == expected


@pytest.mark.parametrize(
    'param, folder_name',
    (
            ['path', 'test'],
    )
)
class TestYandexDisk:

    def setup_method(self):
        self.header = {
            'Authorization': 'OAuth y0_AgAAAAB0L5Z6AADLWwAAAAD9NYFPAABLZLbzwQVHXqbWWBSDSwxhgBY-0A'
        }

    def test_create_folder(self, param, folder_name):
        params = {param: folder_name}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.header,
                                params=params)
        assert response.status_code == 201

    def test_create_folder_again(self, param, folder_name):
        params = {param: folder_name}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.header,
                                params=params)
        assert response.status_code == 201

    @pytest.mark.xfail
    def test_delete_folder(self, param, folder_name):
        params = {param: folder_name + '1'}
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                   headers=self.header,
                                   params=params)
        assert response.status_code == 404
