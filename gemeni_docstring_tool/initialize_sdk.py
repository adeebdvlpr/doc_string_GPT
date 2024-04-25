import vertexai
from vertexai.preview import reasoning_engines

#need to add following project ID and staging_bucket. Talk to matt for more information
vertexai.init(
    project=" docstringtool",
    location="us-central1",
    staging_bucket="gs://vertex_app_bucket ",
)