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

import ConfigParser
import os

from log import LogFactory
# from exception import ParameterNotFoundException
# import constants


class CounterConfiguration:

    log = LogFactory().get_log(__name__)
    __properties = None

    @staticmethod
    def __read_conf_file():
        """
        Reads and stores the agent's configuration file
        :return: void
        """

        conf_file_path = os.path.abspath(os.path.dirname(__file__)) + "/counter.conf"
        CounterConfiguration.log.debug("Config file path : %r" % conf_file_path)
        CounterConfiguration.__properties = ConfigParser.SafeConfigParser()
        CounterConfiguration.__properties.read(conf_file_path)

    @staticmethod
    def read_property(property_key):
        """
        Returns the value of the provided property
        :param str property_key: the name of the property to be read
        :return: Value of the property,
        :rtype: str
        :exception: ParameterNotFoundException if the provided property cannot be found
        """

        if CounterConfiguration.__properties.has_option("counter", property_key):
            temp_str = CounterConfiguration.__properties.get("counter", property_key)
            CounterConfiguration.log.debug("Reading property: %s = %s", property_key, temp_str)
            if temp_str is not None and temp_str.strip() != "" and temp_str.strip().lower() != "null":
                return str(temp_str).strip()

        # raise ParameterNotFoundException("Cannot find the value of required parameter: %r" % property_key)
        return None
