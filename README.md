## Objective
- To build a basic end to end MapReduce pipeline using Python and Kubernetes
- Each Pod is either a master, mapper or reducer
- Using Redis/ Distributed KV as an intermediate value store instead of in memory storage

## Requirements
### Master Python container
- Will be a simple Docker OCI Image
- Will take number of Mappers and Reducers as Sys args
- Will have InitContainer endpoints so Mappers and Reducers can begin to process data
- Will keep track of how many Mappers and Reducers have finished their task
- Comms through Apache Kafka

### Mapper Python container
- Will be a simple Docker OCI Image
- Will take the initial key value pair stored in store, apply map function to them, save in store
- Pods wait to initalize until master signals them to begin
- Pods terminate and inform Master that mapping is done

### Reducer Python container
- Will be simple Docker OCI Image
- Will take key values stored by mappers and process them based on logic in image
- Pods wait to initalize until master signals them to begin
- Pods terminate and inform reducing is done

### KV Store
- Kubernetes PV Resource
- Need to decide on a distributed store. 
- Deciding on Apache Cassandra
- https://cassandra.apache.org/_/index.html

### Messaging Layer 
- Messages need to come from master to mapper to being mapping
- Master picks up messgaing from mappers to keep track on how much mapping is done
- Master then adds message to kafka, reducers begin work only when they find correct message
- Master picks up message from reducers. Once all reducers end terminates the process
- Deciding on Apache Kafka (just for fun)
- https://kafka.apache.org/documentation/

### Config Layer
- Kubernetes config resource for Cassandra and Kafka access

---

### Steps
- Create 3 Docker images, one each for master mapper and reducer. Version control them nicely
- Begin working on Kafka streaming between them. Test with docker images
- Begin on setup of Cassandra setup and access between pods
- Once this done, add Ingress rules between applications
- Connect and have fun