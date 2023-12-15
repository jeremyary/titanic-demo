from datetime import timedelta

import pandas as pd
from feast import (
    FeatureView,
    Field,
)
import feast.types as types

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
