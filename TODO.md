# Done
1. Create an interative tty pod using python:alpine3.18 to ensure that this image works
2. Need to make Helm chart to take care of deploying correct config of mapper and reducer pods
3. Make separate Dockerfiles for master and reducer pods. Fix commands and versioning, image name tag syntax

# Todo
1. Setup Kafka streaming
    1. Create Persistent Volume for kafka store.
        - Find a good PVC or create one that does not del data between reads
        - https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/
    2. Read doc here : https://hub.docker.com/r/bitnami/kafka
    3. Use image : bitnami/kafka:3.6.1
    > Can maybe use a side car pattern, store data in one container and access in another to be sure. I anyways need temp storage only

2. Kafka is mostly up now
    - Maybe add an InitContainer that checks that Zookeeper is up before starting kafka
    - Need to figure out the broker parts of kafka