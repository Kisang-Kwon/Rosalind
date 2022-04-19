import sys
import os
import pytest

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(TEST_DIR)
sys.path.append(SRC_DIR)

from merge_tow_sorted_array import get_minimum_number, merge_arrays


@pytest.mark.parametrize(
    "array_indices, arrays, expected",
    [
        pytest.param(
            {0: 0, 1: 0},
            [[1, 5, 13, 24, 55], [-5, 2, 9, 18, 33, 47, 75]],
            -5
        ),
        pytest.param(
            {0: 0, 1: 0},
            [[-11, 5, 13, 24, 55], [-5, 2, 9, 18, 33, 47, 75]],
            -11
        ),
        pytest.param(
            {0: 0, 1: 0},
            [[-5, 5, 13, 24, 55], [-5, 2, 9, 18, 33, 47, 75]],
            -5
        )
    ]
)
def test_get_minimum_number(array_indices, arrays, expected):
    assert expected == get_minimum_number(array_indices, arrays)
    
@pytest.mark.parametrize(
    "array_indices, arrays, expected",
    [
        pytest.param(
            {0: 0, 1: 0},
            [[1, 5, 13, 24, 55], [-5, 2, 9, 18, 33, 47, 75]],
            [-5, 1, 2, 5, 9, 13, 18, 24, 33, 47, 55, 75]
        ),
        pytest.param(
            {0: 0, 1: 0},
            [[-11, 5, 13, 24, 55], [-5, 2, 9, 18, 33, 47, 75]],
            [-11, -5, 2, 5, 9, 13, 18, 24, 33, 47, 55, 75]
        ),
        pytest.param(
            {0: 0, 1: 0},
            [[-5, 5, 13, 24, 47, 55], [-5, 2, 9, 18, 33, 47, 75]],
            [-5, -5, 2, 5, 9, 13, 18, 24, 33, 47, 47, 55, 75]
        )
    ]
)
def test_merge_arrays(array_indices, arrays, expected):
    assert expected == merge_arrays(array_indices, arrays)