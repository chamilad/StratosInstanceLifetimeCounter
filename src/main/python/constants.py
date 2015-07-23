# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


MB_IP = "mb.ip"
MB_PORT = "mb.port"

# topic names to subscribe
INSTANCE_NOTIFIER_TOPIC = "instance/#"
HEALTH_STAT_TOPIC = "health/#"
TOPOLOGY_TOPIC = "topology/#"
TENANT_TOPIC = "tenant/#"
INSTANCE_STATUS_TOPIC = "instance/status/"
APPLICATION_SIGNUP = "application/signup/#"


# MB events
ARTIFACT_UPDATED_EVENT = "ArtifactUpdatedEvent"
INSTANCE_STARTED_EVENT = "InstanceStartedEvent"
INSTANCE_ACTIVATED_EVENT = "InstanceActivatedEvent"
INSTANCE_MAINTENANCE_MODE_EVENT = "InstanceMaintenanceModeEvent"
INSTANCE_READY_TO_SHUTDOWN_EVENT = "InstanceReadyToShutdownEvent"
INSTANCE_CLEANUP_CLUSTER_EVENT = "InstanceCleanupClusterEvent"
INSTANCE_CLEANUP_MEMBER_EVENT = "InstanceCleanupMemberEvent"
COMPLETE_TOPOLOGY_EVENT = "CompleteTopologyEvent"
COMPLETE_TENANT_EVENT = "CompleteTenantEvent"
DOMAIN_MAPPING_ADDED_EVENT = "DomainMappingAddedEvent"
DOMAIN_MAPPING_REMOVED_EVENT = "DomainMappingRemovedEvent"
MEMBER_INITIALIZED_EVENT = "MemberInitializedEvent"
MEMBER_ACTIVATED_EVENT = "MemberActivatedEvent"
MEMBER_TERMINATED_EVENT = "MemberTerminatedEvent"
MEMBER_SUSPENDED_EVENT = "MemberSuspendedEvent"
MEMBER_STARTED_EVENT = "MemberStartedEvent"
TENANT_SUBSCRIBED_EVENT = "TenantSubscribedEvent"
APPLICATION_SIGNUP_REMOVAL_EVENT = "ApplicationSignUpRemovedEvent"


# Messaging Model
TENANT_RANGE_DELIMITER = "-"
