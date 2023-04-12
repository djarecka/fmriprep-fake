# This is to prepare Docker image

version_tag="0.1.1"
dockerhub_username="chenyingzhao"

# build on linux system:
docker build -t ${dockerhub_username}/fmirprep_fake:${version_tag} -f Dockerfile .

# push to Docker Hub:
docker push ${dockerhub_username}/fmriprep_fake:${version_tag}

# if `docker push` fails with error "An image does not exist locally with the tag":
#   you need to tag it first:
#   ref: https://stackoverflow.com/questions/48038969/an-image-does-not-exist-locally-with-the-tag-while-pushing-image-to-local-regis
# $ docker images    # find the image ID of the desired one
# $ docker tag <image ID> ${dockerhub_username}/fmriprep_fake:${version_tag}
# then try `docker push` command again.
