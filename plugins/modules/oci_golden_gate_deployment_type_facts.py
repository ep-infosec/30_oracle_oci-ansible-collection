#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_golden_gate_deployment_type_facts
short_description: Fetches details about one or multiple DeploymentType resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DeploymentType resources in Oracle Cloud Infrastructure
    - Returns an array of DeploymentTypeDescriptor
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
        type: str
        required: true
    display_name:
        description:
            - A filter to return only the resources that match the entire 'displayName' given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is
              descending.  Default order for 'displayName' is ascending. If no value is specified
              timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List deployment_types
  oci_golden_gate_deployment_type_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
deployment_types:
    description:
        - List of DeploymentType resources
    returned: on success
    type: complex
    contains:
        category:
            description:
                - The deployment category defines the broad separation of the deployment type into categories.  Currently
                  the separation is 'DATA_REPLICATION' and 'STREAM_ANALYTICS'.
            returned: on success
            type: str
            sample: DATA_REPLICATION
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: str
            sample: display_name_example
        deployment_type:
            description:
                - "The type of deployment, the value determines the exact 'type' of service executed in the Deployment.
                  NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.  Its use is discouraged
                        in favor of the equivalent 'DATABASE_ORACLE' value."
            returned: on success
            type: str
            sample: OGG
        connection_types:
            description:
                - An array of connectionTypes.
            returned: on success
            type: list
            sample: []
        source_technologies:
            description:
                - "List of the supported technologies generally.  The value is a freeform text string generally consisting
                  of a description of the technology and optionally the speific version(s) support.  For example,
                  [ \\"Oracle Database 19c\\", \\"Oracle Exadata\\", \\"OCI Streaming\\" ]"
            returned: on success
            type: list
            sample: []
        target_technologies:
            description:
                - "List of the supported technologies generally.  The value is a freeform text string generally consisting
                  of a description of the technology and optionally the speific version(s) support.  For example,
                  [ \\"Oracle Database 19c\\", \\"Oracle Exadata\\", \\"OCI Streaming\\" ]"
            returned: on success
            type: list
            sample: []
    sample: [{
        "category": "DATA_REPLICATION",
        "display_name": "display_name_example",
        "deployment_type": "OGG",
        "connection_types": [],
        "source_technologies": [],
        "target_technologies": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentTypeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_deployment_types,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DeploymentTypeFactsHelperCustom = get_custom_class("DeploymentTypeFactsHelperCustom")


class ResourceFactsHelper(
    DeploymentTypeFactsHelperCustom, DeploymentTypeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="deployment_type",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(deployment_types=result)


if __name__ == "__main__":
    main()
