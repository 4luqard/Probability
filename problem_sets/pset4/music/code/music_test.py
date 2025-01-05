import pytest

import polars as pl
from polars import col

from numpy import isclose

from music import *


@pytest.fixture
def music_helpers():
    data = pl.read_csv("problem_sets/pset4/music/data/music.csv")

    def _music_helpers(action, **kwargs):
        if action == "df":
            return data
        elif action == "mean":
            music_type = kwargs.get("music_type")
            return data.mean()[music_type][0]
        elif action == "proba":
            music_type = kwargs.get("music_type")
            type_value = kwargs.get("type_value")
            return data.filter(col(music_type) == type_value).shape[0] / data.shape[0]
        elif action == "cond_proba":
            music_type1 = kwargs.get("music_type1")
            type1_value = kwargs.get("type1_value")
            music_type2 = kwargs.get("music_type2")
            type2_value = kwargs.get("type2_value")
            return (
                data.filter(
                    (col(music_type1) == type1_value)
                    & (col(music_type2) == type2_value)
                ).shape[0]
                / data.filter(col(music_type2) == type2_value).shape[0]
            )

    return _music_helpers


def test_part_a(music_helpers):
    actual_folk_proba = music_proba()
    expected_folk_proba = music_helpers("proba", music_type="Folk", type_value=5)
    assert isclose(actual_folk_proba, expected_folk_proba, atol=1e-6)


def test_part_b(music_helpers):
    actual_pmf = music_pmf()
    expected_pmf = [
        music_helpers("proba", music_type="Folk", type_value=i) for i in range(1, 6)
    ]
    assert actual_pmf == expected_pmf


def test_part_c(music_helpers):
    actual_mean = music_mean()
    expected_mean = music_helpers("mean", music_type="Musical")
    assert isclose(actual_mean, expected_mean, atol=1e-6)


def test_part_d(music_helpers):
    actual_cond_proba = music_cond_proba()
    expected_cond_proba = music_helpers(
        "cond_proba",
        music_type1="Folk",
        type1_value=5,
        music_type2="Musical",
        type2_value=5,
    )
    assert isclose(actual_cond_proba, expected_cond_proba, atol=1e-6)


def test_part_e(music_helpers):
    actual_cond_proba = music_cond_pmf(
        music_type1="Musical", music_type2="Folk", type2_value=5
    )
    expected_cond_proba = [
        music_helpers(
            "cond_proba",
            music_type1="Musical",
            type1_value=i,
            music_type2="Folk",
            type2_value=5,
        )
        for i in range(1, 6)
    ]
    assert actual_cond_proba == expected_cond_proba


if __name__ == "__main__":
    pytest.main(["-v", __file__])
