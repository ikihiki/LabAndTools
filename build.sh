DOCKERILES=`find ./ -name Dockerfile`
for DOCKERILE in $DOCKERILES
do
    DOCKERDIR=`dirname $DOCKERILE`
    #git diff --quiet --exit-code master^ $DOCKERDIR
    #if [ $? = 1 ]; then
        DOCKERTAG=${DOCKERDIR#./}
        DOCKERTAG=${DOCKERTAG////_}
        docker build -t gcr.io/ikihikilabandtools/$DOCKERTAG $DOCKERDIR
        docker push  gcr.io/ikihikilabandtools/$DOCKERTAG
    #fi
done