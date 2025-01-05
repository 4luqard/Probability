import polars as pl
import numpy as np

music_data = pl.read_csv("problem_sets/pset4/music/data/music.csv")


# part (a) - completed for you
def music_proba(music_type="Folk", type_value=5):
    return (
        music_data.filter(pl.col(music_type) == type_value).shape[0]
        / music_data.shape[0]
    )


# part (b)
def music_pmf(music_type="Folk"):
    return [
        (music_data.filter(pl.col(music_type) == i).shape[0] / music_data.shape[0])
        for i in range(1, 6)
    ]


# part (c)
def music_mean(music_type="Musical"):
    return sum([music_pmf(music_type)[i - 1] * i for i in range(1, 6)])


# part (d)
def music_cond_proba(
    music_type1="Folk", type1_value=5, music_type2="Musical", type2_value=5
):
    return (
        music_data.filter(
            (pl.col(music_type1) == type1_value) & (pl.col(music_type2) == type2_value)
        ).shape[0]
        / music_data.filter(pl.col(music_type2) == type2_value).shape[0]
    )


# part (e)
def music_cond_pmf(music_type1="Folk", music_type2="Musical", type2_value=5):
    return [
        (
            music_data.filter(
                (pl.col(music_type1) == i) & (pl.col(music_type2) == type2_value)
            ).shape[0]
            / music_data.filter(pl.col(music_type2) == type2_value).shape[0]
        )
        for i in range(1, 6)
    ]
