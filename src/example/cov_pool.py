from multiprocessing import Pool
import os
import math
from itertools import repeat


def get_items(start_index: int, count: int):
    items = [i for i in range(start_index, count)]
    return items


def get_items_with_pool(count: int, start_index: int = 0):
    items = []
    processes_count = os.cpu_count()

    batch_size = math.ceil(count / processes_count)
    with Pool(processes_count) as p:
        results = p.starmap(
            get_items,
            zip(
                [i for i in range(start_index, start_index + count, batch_size)],
                repeat(batch_size),
            ),
        )
        for items_batch in results:
            items.extend(items_batch)
    p.join()
    return items


if __name__ == "__main__":
    get_items_with_pool(1, 10)

