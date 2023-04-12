# This is to prepare Docker image

version_tag="0.1.1"
docker_username="chenyingzhao"

# build on linux system:
docker build -t ${docker_username}/fmirprep_fake:${version_tag} -f Dockerfile .
