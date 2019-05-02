DOCKERILES=`find ./ -name Dockerfile`
for DOCKERILE in $DOCKERILES
do
    DOCKERDIR=`dirname $DOCKERILE`
    git diff --stat HEAD^ $DOCKERDIR
    if [ $? = 1 ]; then
        echo 'aa'
    fi
done