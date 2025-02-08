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
from cyclonedds.pub import DataWriter
from MessageType.announcements_message import AnnouncementsMessage
import time

def signal_handler(sig, frame):
    print('\nShutting down gracefully...')
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    ros_domain_id: int = int(os.environ.get("ROS_DOMAIN_ID"))
    print(f"Domain ID: {ros_domain_id}")
    name = input("Please enter your name: ")
    message = AnnouncementsMessage(text=f"{name} has started their first DDS Python application!")
    participant = DomainParticipant(domain_id=ros_domain_id)
    topic = Topic(participant, "rt/announcement", AnnouncementsMessage)

    writer = DataWriter(participant, topic)
    while True:
        try: 
            time.sleep(1)
            print(message)
            writer.write(message)
            message.trigger()
        except KeyboardInterrupt:
            print('\nShutting down gracefully...')


