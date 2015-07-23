# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from log import LogFactory
from subscriber import EventSubscriber
import constants
from config import CounterConfiguration
import time
from topologyevents import MemberInitializedEvent, MemberTerminatedEvent


log = LogFactory().get_log(__name__)


def main():

    log.debug("Starting message broker listeners")

    mb_ip = CounterConfiguration.read_property(constants.MB_IP)
    mb_port = CounterConfiguration.read_property(constants.MB_PORT)

    # __inst_topic_subscriber = EventSubscriber(constants.INSTANCE_NOTIFIER_TOPIC, mb_ip, mb_port)
    # __tenant_topic_subscriber = EventSubscriber(constants.TENANT_TOPIC, mb_ip, mb_port)
    # __app_topic_subscriber = EventSubscriber(constants.APPLICATION_SIGNUP, mb_ip, mb_port)
    __topology_event_subscriber = EventSubscriber(constants.TOPOLOGY_TOPIC, mb_ip, mb_port)

    # __topology_event_subscriber.register_handler("MemberActivatedEvent", on_member_activated)
    __topology_event_subscriber.register_handler("MemberTerminatedEvent", on_member_terminated)
    # __topology_event_subscriber.register_handler("MemberSuspendedEvent", on_member_suspended)
    # __topology_event_subscriber.register_handler("CompleteTopologyEvent", on_complete_topology)
    # __topology_event_subscriber.register_handler("MemberStartedEvent", on_member_started)
    # __topology_event_subscriber.register_handler("MemberCreatedEvent", on_member_created)
    __topology_event_subscriber.register_handler("MemberInitializedEvent", on_member_initialized)

    __topology_event_subscriber.start()
    log.info("Cartridge agent topology receiver thread started")

    # wait till subscribed to continue
    while not __topology_event_subscriber.is_subscribed():
        time.sleep(1)


def on_member_initialized(msg):
    log.debug("Member initialized event received: %r" % msg.payload)

    event = MemberInitializedEvent.create_from_json(msg)
    member_id = event.member_id
    received_timestamp = int(time.time())

    # write to db table member_id and receiver_timestamp


def on_member_terminated(msg):
    log.debug("Member terminated event received: %r" % msg.payload)

    event = MemberTerminatedEvent.create_from_json(msg)
    member_id = event.member_id
    received_timestamp = int(time.time())

    # write to db table member_id and receiver_timestamp


if __name__ == "__main__":
    main()
