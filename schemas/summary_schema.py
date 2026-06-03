from pydantic import BaseModel
from typing import List


class SummarySection(BaseModel):
    overview: str
    problem: str
    solution: str


class KeyPoint(BaseModel):
    point: str


class ActionItem(BaseModel):
    action: str


class SummaryResponse(BaseModel):
    title: str
    summary: SummarySection
    key_points: List[KeyPoint]
    action_items: List[ActionItem]