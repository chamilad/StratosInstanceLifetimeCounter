# StratosInstanceLifetimeCounter
Listens to MemberInitialized and MemberTerminated events to calculate member uptime for billing

# Configuration

`counter.conf` is the configuration file where the message broker IP address and the port should be specified. 

# Event deserialization

Events are deserialized anticipating Apache Stratos 4.1.0 events. If any errors occur during event desirialization, please open an issue. 
