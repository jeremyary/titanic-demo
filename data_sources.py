from feast import FileSource

survivors_stats = FileSource(
    name="survivors_source",
    path="s3://titanic-ml-jary/survivors_source.parquet",
    s3_endpoint_override="http://s3.us-west-1.amazonaws.com",
    event_timestamp_column="event_timestamp",
    description="A table containing a list of passengerIds and whether they survived or not",
    owner="jary@redhat.com",
)

demographics_stats = FileSource(
    name="demographics_source",
    path="s3://titanic-ml-jary/demographics_source.parquet",
    s3_endpoint_override="http://s3.us-west-1.amazonaws.com",
    event_timestamp_column="event_timestamp",
    description="A table containing passengers' demographics",
    owner="jary@redhat.com",
)

genealogy_stats = FileSource(
    name="genealogy_source",
    path="s3://titanic-ml-jary/genealogy_source.parquet",
    s3_endpoint_override="http://s3.us-west-1.amazonaws.com",
    event_timestamp_column="event_timestamp",
    description="A table containing passengers' genealogical information",
    owner="jary@redhat.com",
)

trip_stats = FileSource(
    name="trip_source",
    path="s3://titanic-ml-jary/trip_source.parquet",
    s3_endpoint_override="http://s3.us-west-1.amazonaws.com",
    event_timestamp_column="event_timestamp",
    description="A table containing passengers' trip-related info",
    owner="jary@redhat.com",
)

test_stats = FileSource(
    name="test_source",
    path="s3://titanic-ml-jary/test_source.parquet",
    s3_endpoint_override="http://s3.us-west-1.amazonaws.com",
    event_timestamp_column="event_timestamp",
    description="A table containing testing data - the same passenger info sans 'Survived'",
    owner="jary@redhat.com",
)
