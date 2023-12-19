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

# didn't quite get on-demand (see features) working...yet
# sanitized_service = FeatureService(
#     name="sanitized_service",
#     features=[transformed_title],
#     owner="jary@redhat.com"
# )