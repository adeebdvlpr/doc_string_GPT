import vertexai
from vertexai.preview import reasoning_engines

#need to add following project ID and staging_bucket. Talk to matt for more information
vertexai.init(
    project="YOUR_PROJECT_ID",
    location="us-central1",
    staging_bucket="gs://YOUR_BUCKET_NAME",
)