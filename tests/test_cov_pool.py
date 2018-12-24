import pytest
from example.cov_pool import get_items_with_pool

source_items = [0, 1, 2, 3]


@pytest.mark.parametrize(
    "count, start_index, cpu_count, expected_items",
    [
        (1, 0, 4, [source_items[0]]),
        (1, 3, 10, [source_items[3]]),
        (1, 3, 10, [source_items[3:]]),
    ],
)
def test_get_items_with_pool(mocker, count, start_index, cpu_count, expected_items):
    mocker.patch("os.cpu_count", return_value=cpu_count)
    assert get_items_with_pool(count, start_index) == expected_items
