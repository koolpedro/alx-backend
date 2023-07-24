#!/usr/bin/env python3
""" 0. Simple helper function
"""

def index_range(page, page_size):
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
