"""
data class
"""

from dataclasses import dataclass
from typing import List


@dataclass
class ExampleResult(object):
    pred_label: int
    pos_indexes: List[int]
    neg_indexes: List[int]
    pos_scores: List[float]
    neg_scores: List[float]