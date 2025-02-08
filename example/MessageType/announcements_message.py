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

from dataclasses import dataclass
from cyclonedds.idl import IdlStruct

@dataclass
class AnnouncementsMessage(IdlStruct):
    counter: int = 0
    text: str = ""
    
    def trigger(self) -> None:
        self.counter += 1  
    
    def __str__(self) -> str:
        return f"{self.counter}: {self.text}"
