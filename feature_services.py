from feast import FeatureService

from features import *

# we could just put features from all sources back together if we wanted
omniscient_service = FeatureService(
    name="omniscient_service",
    features=[survivors_view, demographics_view, genealogy_view, trip_view],
    owner="jary@redhat.com",
)

test_service = FeatureService(
    name="test_service",
    features=[test_view],
    owner="jary@redhat.com",
)