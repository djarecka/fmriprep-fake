# This is to prepare Docker image

version_tag="0.1.2"
dockerhub_username="chenyingzhao"

# ----------------------------------------------------------
# Build on linux system
#   this is only to try out the building
# ----------------------------------------------------------
docker build -t ${dockerhub_username}/fmirprep_fake:${version_tag} -f Dockerfile .

# ----------------------------------------------------------
# Push to Docker Hub:
# ----------------------------------------------------------

# Option #1: Build for linux system only
#   Takes less time to build
# docker push ${dockerhub_username}/fmriprep_fake:${version_tag}
# ^^ this is for linux system

# if `docker push` fails with error "An image does not exist locally with the tag":
#   you need to tag it first:
#   ref: https://stackoverflow.com/questions/48038969/an-image-does-not-exist-locally-with-the-tag-while-pushing-image-to-local-regis
# $ docker images    # find the image ID of the desired one
# $ docker tag <image ID> ${dockerhub_username}/fmriprep_fake:${version_tag}
# then try `docker push` command again.

# Option #2: Multi-arch build, for both Mac M1 + Linux systems
#   though takes longer time than regular build, it's still very fast (several seconds).
# on Mac M1, we need to use multi-architecture,
# so that docker image built on Mac M1 can be run on other architectures e.g., cubic with amd64

# ref: https://docs.docker.com/desktop/multi-arch/
docker buildx use mybuilder   # use the builder which gives access to the new multi-architecture features. | created by: $ docker buildx create --name mybuilder
docker buildx build --platform linux/amd64,linux/arm64 --push \
    -t ${dockerhub_username}/fmriprep_fake:${version_tag} -f Dockerfile .
