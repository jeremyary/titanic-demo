from feast import (
    Entity,
    ValueType,
)

passenger = Entity(
    name="passenger",
    join_keys=["PassengerId"],
    value_type=ValueType.INT64,
    description="PassengerId",
)
