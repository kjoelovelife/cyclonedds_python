#!/usr/bin/env pytohn3
##########################################################################
# Copyright 2025 Wei-Chih Lin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Wei-Chih Lin (weichih.lin@protonmail.com)
##########################################################################

import os
import signal
import sys
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import DataReader
from cyclonedds.util import duration
from MessageType.announcements_message import AnnouncementsMessage

def signal_handler(sig, frame):
    print('\nShutting down gracefully...')
    sys.exit(0)

def received_for_a_while():
    """If we don't receive a single announcement for five minutes we want the script to exit.
    """
    for msg in reader.take_iter(timeout=duration(minutes=0.1)):
        print(msg)

def received_in_time(last_message: AnnouncementsMessage) -> AnnouncementsMessage:
    if reader.read():
        current_message = reader.read()[0]
        if current_message != last_message:
            last_message = current_message
            print(last_message)
    return last_message

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    ros_domain_id: int = int(os.environ.get("ROS_DOMAIN_ID"))
    print(f"Domain ID: {ros_domain_id}")
    participant = DomainParticipant(domain_id=ros_domain_id)
    topic = Topic(participant, "announcement", AnnouncementsMessage)
    reader = DataReader(participant, topic)

    last_message = AnnouncementsMessage()
    while True:
        try:
            last_message = received_in_time(last_message)
        except KeyboardInterrupt:
            print('\nShutting down gracefully...')
