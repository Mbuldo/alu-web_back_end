#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page of data based on index with deletion resilience.

        Args:
            index (int): Starting index of the page
            page_size (int): Number of items per page

        Returns:
            Dict: Dictionary containing pagination metadata and data
        """
        indexed_data = self.indexed_dataset()
        data_length = len(indexed_data)

        # Handle initial index
        if index is None:
            index = 0

        # Verify index is in valid range
        assert isinstance(index, int) and 0 <= index < data_length

        # Collect page data while handling deleted indices
        data = []
        curr_index = index
        next_index = None

        while len(data) < page_size and curr_index < data_length:
            if curr_index in indexed_data:
                data.append(indexed_data[curr_index])
            curr_index += 1
            if len(data) == page_size:
                next_index = curr_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
