from datetime import timedelta

import pandas as pd
from feast import (
    FeatureView,
    Field,
)
import feast.types as types
from feast.on_demand_feature_view import on_demand_feature_view

from data_sources import *
from entities import *

survivors_view = FeatureView(
    name="survivors_view",
    description="list of passengers and survival status",
    entities=[passenger],
    ttl=timedelta(seconds=8640000000),
    schema=[
        Field(name="PassengerId", dtype=types.Int64),
        Field(name="Survived", dtype=types.Int64),
    ],
    online=True,
    source=survivors_stats,
    owner="jary@redhat.com",
)

demographics_view = FeatureView(
    name="demographics_view",
    description="list of passengers' demographics",
    entities=[passenger],
    ttl=timedelta(seconds=8640000000),
    schema=[
        Field(name="Pclass", dtype=types.Int64),
        Field(name="Name", dtype=types.String),
        Field(name="Sex", dtype=types.String),
        Field(name="Age", dtype=types.Float64),
    ],
    online=True,
    source=demographics_stats,
    owner="jary@redhat.com",
)

genealogy_view = FeatureView(
    name="genealogy_view",
    description="list of passengers' genealogical info",
    entities=[passenger],
    ttl=timedelta(seconds=8640000000),
    schema=[
        Field(name="SibSp", dtype=types.Int64),
        Field(name="Parch", dtype=types.Int64),
    ],
    online=True,
    source=genealogy_stats,
    owner="jary@redhat.com",
)

trip_view = FeatureView(
    name="trip_view",
    description="list of passengers' trip-related info",
    entities=[passenger],
    ttl=timedelta(seconds=8640000000),
    schema=[
        Field(name="Ticket", dtype=types.String),
        Field(name="Fare", dtype=types.Float64),
        Field(name="Cabin", dtype=types.String),
        Field(name="Embarked", dtype=types.String),
    ],
    online=True,
    source=trip_stats,
    owner="jary@redhat.com",
)

test_view = FeatureView(
    name="test_view",
    description="test dataset",
    entities=[passenger],
    ttl=timedelta(seconds=8640000000),
    schema=[
        Field(name="PassengerId", dtype=types.Int64),
        Field(name="Pclass", dtype=types.Int64),
        Field(name="Name", dtype=types.String),
        Field(name="Sex", dtype=types.String),
        Field(name="Age", dtype=types.Float64),
        Field(name="SibSp", dtype=types.Int64),
        Field(name="Parch", dtype=types.Int64),
        Field(name="Ticket", dtype=types.String),
        Field(name="Fare", dtype=types.Float64),
        Field(name="Cabin", dtype=types.String),
        Field(name="Embarked", dtype=types.String),
    ],
    online=True,
    source=test_stats,
    owner="jary@redhat.com",
)


@on_demand_feature_view(
    sources=[
        demographics_view,
    ],
    schema=[
        Field(name="PassengerId", dtype=types.Int64),
        Field(name="Title", dtype=types.Float64),
    ],
)
def transformed_title(input_df: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    title = input_df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    title = title.replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    title = title.replace('Mlle', 'Miss')
    title = title.replace('Ms', 'Miss')
    title = title.replace('Mme', 'Mrs')
    title = title.map({"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5})
    df['Title'] = title.fillna(0)
    df['PassengerId'] = input_df.Pclass
    return df
