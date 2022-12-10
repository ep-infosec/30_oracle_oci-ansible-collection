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
module: oci_data_connectivity_folder
short_description: Manage a Folder resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Folder resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a folder under a specified registry.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_type:
        description:
            - The type of the folder.
            - Required for update using I(state=present) with folder_key present.
        type: str
    key:
        description:
            - Generated key that can be used in API calls to identify the folder. In scenarios where reference to the folder is required, a value can be passed
              in create.
            - Required for update using I(state=present) with folder_key present.
        type: str
    model_version:
        description:
            - The model version of an object.
            - This parameter is updatable.
        type: str
    parent_ref:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            parent:
                description:
                    - Key of the parent object.
                type: str
    name:
        description:
            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable
              and is restricted to 1000 characters.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    description:
        description:
            - User-defined description of the folder.
            - This parameter is updatable.
        type: str
    object_status:
        description:
            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
            - This parameter is updatable.
        type: int
    object_version:
        description:
            - The version of the object that is used to track changes in the object instance.
            - Required for update using I(state=present) with folder_key present.
        type: int
    identifier:
        description:
            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be
              modified.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    data_assets:
        description:
            - The list of data assets that belong to the folder.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            key:
                description:
                    - Currently not used while creating a data asset. Reserved for future.
                type: str
                required: true
            model_version:
                description:
                    - The model version of an object.
                type: str
            model_type:
                description:
                    - The type of the object.
                type: str
            name:
                description:
                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                type: str
                required: true
            description:
                description:
                    - User-defined description of the data asset.
                type: str
            object_status:
                description:
                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                type: int
            object_version:
                description:
                    - The version of the object that is used to track changes in the object instance.
                type: int
            identifier:
                description:
                    - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can
                      be modified.
                type: str
                required: true
            external_key:
                description:
                    - The external key of the object.
                type: str
            asset_properties:
                description:
                    - Additional properties for the data asset.
                type: dict
            properties:
                description:
                    - All the properties for the data asset in a key-value map format.
                type: dict
            type:
                description:
                    - Specific DataAsset Type
                type: str
            native_type_system:
                description:
                    - ""
                type: dict
                suboptions:
                    key:
                        description:
                            - The key of the object.
                        type: str
                    model_type:
                        description:
                            - The type of the object.
                        type: str
                    model_version:
                        description:
                            - The model version of an object.
                        type: str
                    parent_ref:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                        type: str
                    description:
                        description:
                            - A user-defined description for the object.
                        type: str
                    object_version:
                        description:
                            - The version of the object that is used to track changes in the object instance.
                        type: int
                    type_mapping_to:
                        description:
                            - The type system to map to.
                        type: dict
                    type_mapping_from:
                        description:
                            - The type system to map from.
                        type: dict
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                        type: int
                    identifier:
                        description:
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The
                              value can be modified.
                        type: str
                    types:
                        description:
                            - An array of types.
                        type: list
                        elements: dict
                        suboptions:
                            model_type:
                                description:
                                    - The property which differentiates the subtypes.
                                type: str
                                choices:
                                    - "STRUCTURED_TYPE"
                                    - "DATA_TYPE"
                                    - "CONFIGURED_TYPE"
                                    - "COMPOSITE_TYPE"
                                    - "DERIVED_TYPE"
                                required: true
                            key:
                                description:
                                    - The key of the object.
                                type: str
                            model_version:
                                description:
                                    - The model version of an object.
                                type: str
                            parent_ref:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    parent:
                                        description:
                                            - Key of the parent object.
                                        type: str
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            description:
                                description:
                                    - A user-defined description for the object.
                                type: str
                            dt_type:
                                description:
                                    - The data type.
                                type: str
                                choices:
                                    - "PRIMITIVE"
                                    - "STRUCTURED"
                            type_system_name:
                                description:
                                    - The data type system name.
                                type: str
                            config_definition:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    key:
                                        description:
                                            - The key of the object.
                                        type: str
                                    model_type:
                                        description:
                                            - The type of the object.
                                        type: str
                                    model_version:
                                        description:
                                            - The model version of an object.
                                        type: str
                                    parent_ref:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                type: str
                                    name:
                                        description:
                                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    is_contained:
                                        description:
                                            - Specifies whether the configuration is contained.
                                        type: bool
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                        type: int
                                    config_parameter_definitions:
                                        description:
                                            - The parameter configuration details.
                                        type: dict
                                        suboptions:
                                            parameter_type:
                                                description:
                                                    - ""
                                                type: dict
                                                suboptions:
                                                    wrapped_type:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            model_type:
                                                                description:
                                                                    - The property which differentiates the subtypes.
                                                                type: str
                                                                choices:
                                                                    - "STRUCTURED_TYPE"
                                                                    - "DATA_TYPE"
                                                                    - "CONFIGURED_TYPE"
                                                                    - "COMPOSITE_TYPE"
                                                                    - "DERIVED_TYPE"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            description:
                                                                description:
                                                                    - A user-defined description for the object.
                                                                type: str
                                                    config_values:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            config_param_values:
                                                                description:
                                                                    - The configuration parameter values.
                                                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                type: dict
                                                                suboptions:
                                                                    string_value:
                                                                        description:
                                                                            - A string value of the parameter.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: str
                                                                    int_value:
                                                                        description:
                                                                            - An integer value of the parameter.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: int
                                                                    object_value:
                                                                        description:
                                                                            - An object value of the parameter.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: dict
                                                                    ref_value:
                                                                        description:
                                                                            - The root object reference value.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: dict
                                                                    parameter_value:
                                                                        description:
                                                                            - Reference to the parameter by its key.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                type: dict
                                                                suboptions:
                                                                    parent:
                                                                        description:
                                                                            - Key of the parent object.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: str
                                                    dt_type:
                                                        description:
                                                            - The data type.
                                                            - Applicable when model_type is 'DATA_TYPE'
                                                        type: str
                                                        choices:
                                                            - "PRIMITIVE"
                                                            - "STRUCTURED"
                                                    type_system_name:
                                                        description:
                                                            - The data type system name.
                                                            - Applicable when model_type is 'DATA_TYPE'
                                                        type: str
                                                    schema:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'STRUCTURED_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            model_type:
                                                                description:
                                                                    - The property which differentiates the subtypes.
                                                                type: str
                                                                choices:
                                                                    - "STRUCTURED_TYPE"
                                                                    - "DATA_TYPE"
                                                                    - "CONFIGURED_TYPE"
                                                                    - "COMPOSITE_TYPE"
                                                                    - "DERIVED_TYPE"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            description:
                                                                description:
                                                                    - A user-defined description for the object.
                                                                type: str
                                                    model_type:
                                                        description:
                                                            - The property which differentiates the subtypes.
                                                        type: str
                                                        choices:
                                                            - "CONFIGURED_TYPE"
                                                            - "DERIVED_TYPE"
                                                            - "DATA_TYPE"
                                                            - "STRUCTURED_TYPE"
                                                            - "COMPOSITE_TYPE"
                                                        required: true
                                                    key:
                                                        description:
                                                            - The key of the object.
                                                        type: str
                                                    model_version:
                                                        description:
                                                            - The model version of an object.
                                                        type: str
                                                    parent_ref:
                                                        description:
                                                            - ""
                                                        type: dict
                                                        suboptions:
                                                            parent:
                                                                description:
                                                                    - Key of the parent object.
                                                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                type: str
                                                    name:
                                                        description:
                                                            - Free form text without any restriction on the permitted characters. Name can have letters,
                                                              numbers, and special characters. The value is editable and is restricted to 1000 characters.
                                                        type: str
                                                    object_status:
                                                        description:
                                                            - The status of an object that can be set to value 1 for shallow references across objects, other
                                                              values reserved.
                                                        type: int
                                                    description:
                                                        description:
                                                            - A user-defined description for the object.
                                                        type: str
                                                    parent_type:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'COMPOSITE_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            model_type:
                                                                description:
                                                                    - The property which differentiates the subtypes.
                                                                type: str
                                                                choices:
                                                                    - "STRUCTURED_TYPE"
                                                                    - "DATA_TYPE"
                                                                    - "CONFIGURED_TYPE"
                                                                    - "COMPOSITE_TYPE"
                                                                    - "DERIVED_TYPE"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            description:
                                                                description:
                                                                    - A user-defined description for the object.
                                                                type: str
                                                            parent_type:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            elements:
                                                                description:
                                                                    - An array of elements.
                                                                type: list
                                                                elements: dict
                                                            config_definition:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                    elements:
                                                        description:
                                                            - An array of elements.
                                                            - Applicable when model_type is 'COMPOSITE_TYPE'
                                                        type: list
                                                        elements: dict
                                                        suboptions:
                                                            labels:
                                                                description:
                                                                    - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You
                                                                      can define your own labels and use them to categorize content.
                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                type: list
                                                                elements: str
                                                            native_shape_field:
                                                                description:
                                                                    - ""
                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                type: dict
                                                                suboptions:
                                                                    model_type:
                                                                        description:
                                                                            - The type of the types object.
                                                                            - Required when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                        choices:
                                                                            - "SHAPE"
                                                                            - "SHAPE_FIELD"
                                                                            - "NATIVE_SHAPE_FIELD"
                                                                        required: true
                                                                    key:
                                                                        description:
                                                                            - The key of the object.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    model_version:
                                                                        description:
                                                                            - The model version of an object.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    parent_ref:
                                                                        description:
                                                                            - ""
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: dict
                                                                        suboptions:
                                                                            parent:
                                                                                description:
                                                                                    - Key of the parent object.
                                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                                type: str
                                                                    config_values:
                                                                        description:
                                                                            - ""
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: dict
                                                                        suboptions:
                                                                            config_param_values:
                                                                                description:
                                                                                    - The configuration parameter values.
                                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                                type: dict
                                                                                suboptions:
                                                                                    string_value:
                                                                                        description:
                                                                                            - A string value of the parameter.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: str
                                                                                    int_value:
                                                                                        description:
                                                                                            - An integer value of the parameter.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: int
                                                                                    object_value:
                                                                                        description:
                                                                                            - An object value of the parameter.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: dict
                                                                                    ref_value:
                                                                                        description:
                                                                                            - The root object reference value.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: dict
                                                                                    parameter_value:
                                                                                        description:
                                                                                            - Reference to the parameter by its key.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: str
                                                                            parent_ref:
                                                                                description:
                                                                                    - ""
                                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                                type: dict
                                                                                suboptions:
                                                                                    parent:
                                                                                        description:
                                                                                            - Key of the parent object.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: str
                                                                    object_status:
                                                                        description:
                                                                            - The status of an object that can be set to value 1 for shallow references across
                                                                              objects, other values reserved.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: int
                                                                    name:
                                                                        description:
                                                                            - Free form text without any restriction on the permitted characters. Name can have
                                                                              letters, numbers, and special characters. The value is editable and is restricted
                                                                              to 1000 characters.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    description:
                                                                        description:
                                                                            - A detailed description of the object.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    type:
                                                                        description:
                                                                            - The type reference.
                                                                            - Required when model_type is 'SHAPE_FIELD'
                                                                        type: dict
                                                                        required: true
                                                                    position:
                                                                        description:
                                                                            - The position of the attribute.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: int
                                                                    default_value_string:
                                                                        description:
                                                                            - The default value.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    is_mandatory:
                                                                        description:
                                                                            - Specifies whether the field is mandatory.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: bool
                                                            port_type:
                                                                description:
                                                                    - The port details of the data asset type.
                                                                    - Applicable when model_type is one of ['INPUT_PORT', 'OUTPUT_PORT']
                                                                type: str
                                                                choices:
                                                                    - "DATA"
                                                                    - "CONTROL"
                                                                    - "MODEL"
                                                            fields:
                                                                description:
                                                                    - An array of fields.
                                                                    - Applicable when model_type is one of ['INPUT_PORT', 'OUTPUT_PORT']
                                                                type: list
                                                                elements: dict
                                                                suboptions:
                                                                    model_type:
                                                                        description:
                                                                            - The type of the types object.
                                                                        type: str
                                                                        choices:
                                                                            - "SHAPE"
                                                                            - "SHAPE_FIELD"
                                                                            - "NATIVE_SHAPE_FIELD"
                                                                        required: true
                                                                    key:
                                                                        description:
                                                                            - The key of the object.
                                                                        type: str
                                                                    model_version:
                                                                        description:
                                                                            - The model version of an object.
                                                                        type: str
                                                                    parent_ref:
                                                                        description:
                                                                            - ""
                                                                        type: dict
                                                                    config_values:
                                                                        description:
                                                                            - ""
                                                                        type: dict
                                                                    object_status:
                                                                        description:
                                                                            - The status of an object that can be set to value 1 for shallow references across
                                                                              objects, other values reserved.
                                                                        type: int
                                                                    name:
                                                                        description:
                                                                            - Free form text without any restriction on the permitted characters. Name can have
                                                                              letters, numbers, and special characters. The value is editable and is restricted
                                                                              to 1000 characters.
                                                                        type: str
                                                                    description:
                                                                        description:
                                                                            - A detailed description of the object.
                                                                        type: str
                                                            default_value:
                                                                description:
                                                                    - The default value of the parameter.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: dict
                                                            root_object_default_value:
                                                                description:
                                                                    - The default value of the parameter, which can be an object in DIS, such as a data entity.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: dict
                                                            is_input:
                                                                description:
                                                                    - Specifies whether the parameter is an input value.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: bool
                                                            is_output:
                                                                description:
                                                                    - Specifies whether the parameter is an output value.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: bool
                                                            output_aggregation_type:
                                                                description:
                                                                    - The output aggregation type.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: str
                                                                choices:
                                                                    - "MIN"
                                                                    - "MAX"
                                                                    - "COUNT"
                                                                    - "SUM"
                                                            type_name:
                                                                description:
                                                                    - The type of value the parameter was created for.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: str
                                                            model_type:
                                                                description:
                                                                    - The type of the types object.
                                                                type: str
                                                                choices:
                                                                    - "OUTPUT_PORT"
                                                                    - "SHAPE"
                                                                    - "SHAPE_FIELD"
                                                                    - "INPUT_PORT"
                                                                    - "PARAMETER"
                                                                    - "NATIVE_SHAPE_FIELD"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                                suboptions:
                                                                    parent:
                                                                        description:
                                                                            - Key of the parent object.
                                                                            - Applicable when model_type is 'OUTPUT_PORT'
                                                                        type: str
                                                            config_values:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                                suboptions:
                                                                    config_param_values:
                                                                        description:
                                                                            - The configuration parameter values.
                                                                            - Applicable when model_type is 'OUTPUT_PORT'
                                                                        type: dict
                                                                        suboptions:
                                                                            string_value:
                                                                                description:
                                                                                    - A string value of the parameter.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: str
                                                                            int_value:
                                                                                description:
                                                                                    - An integer value of the parameter.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: int
                                                                            object_value:
                                                                                description:
                                                                                    - An object value of the parameter.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: dict
                                                                            ref_value:
                                                                                description:
                                                                                    - The root object reference value.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: dict
                                                                            parameter_value:
                                                                                description:
                                                                                    - Reference to the parameter by its key.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: str
                                                                    parent_ref:
                                                                        description:
                                                                            - ""
                                                                            - Applicable when model_type is 'OUTPUT_PORT'
                                                                        type: dict
                                                                        suboptions:
                                                                            parent:
                                                                                description:
                                                                                    - Key of the parent object.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: str
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            description:
                                                                description:
                                                                    - A detailed description of the object.
                                                                type: str
                                                            type:
                                                                description:
                                                                    - ""
                                                                    - Applicable when model_type is one of ['SHAPE', 'SHAPE_FIELD', 'PARAMETER']
                                                                    - Required when model_type is 'NATIVE_SHAPE_FIELD'
                                                                type: dict
                                                                suboptions:
                                                                    model_type:
                                                                        description:
                                                                            - The property which differentiates the subtypes.
                                                                        type: str
                                                                        choices:
                                                                            - "STRUCTURED_TYPE"
                                                                            - "DATA_TYPE"
                                                                            - "CONFIGURED_TYPE"
                                                                            - "COMPOSITE_TYPE"
                                                                            - "DERIVED_TYPE"
                                                                    key:
                                                                        description:
                                                                            - The key of the object.
                                                                        type: str
                                                                    model_version:
                                                                        description:
                                                                            - The model version of an object.
                                                                        type: str
                                                                    parent_ref:
                                                                        description:
                                                                            - ""
                                                                        type: dict
                                                                    name:
                                                                        description:
                                                                            - Free form text without any restriction on the permitted characters. Name can have
                                                                              letters, numbers, and special characters. The value is editable and is restricted
                                                                              to 1000 characters.
                                                                        type: str
                                                                    object_status:
                                                                        description:
                                                                            - The status of an object that can be set to value 1 for shallow references across
                                                                              objects, other values reserved.
                                                                        type: int
                                                                    description:
                                                                        description:
                                                                            - A user-defined description for the object.
                                                                        type: str
                                                            position:
                                                                description:
                                                                    - The position of the attribute.
                                                                    - Applicable when model_type is 'NATIVE_SHAPE_FIELD'
                                                                type: int
                                                            default_value_string:
                                                                description:
                                                                    - The default value.
                                                                    - Applicable when model_type is 'NATIVE_SHAPE_FIELD'
                                                                type: str
                                                            is_mandatory:
                                                                description:
                                                                    - Specifies whether the field is mandatory.
                                                                    - Applicable when model_type is 'NATIVE_SHAPE_FIELD'
                                                                type: bool
                                                    config_definition:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is one of ['DATA_TYPE', 'CONFIGURED_TYPE', 'COMPOSITE_TYPE']
                                                        type: dict
                                                        suboptions:
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_type:
                                                                description:
                                                                    - The type of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            is_contained:
                                                                description:
                                                                    - Specifies whether the configuration is contained.
                                                                type: bool
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            config_parameter_definitions:
                                                                description:
                                                                    - The parameter configuration details.
                                                                type: dict
                                            parameter_name:
                                                description:
                                                    - This object represents the configurable properties for an object type.
                                                type: str
                                            description:
                                                description:
                                                    - A user-defined description for the object.
                                                type: str
                                            default_value:
                                                description:
                                                    - The default value for the parameter.
                                                type: dict
                                            class_field_name:
                                                description:
                                                    - The parameter class field name.
                                                type: str
                                            is_static:
                                                description:
                                                    - Specifies whether the parameter is static.
                                                type: bool
                                            is_class_field_value:
                                                description:
                                                    - Specifies whether the parameter is a class field.
                                                type: bool
            registry_metadata:
                description:
                    - ""
                type: dict
                suboptions:
                    aggregator_key:
                        description:
                            - The owning object's key for this object.
                        type: str
                    labels:
                        description:
                            - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them
                              to categorize content.
                        type: list
                        elements: str
                    registry_version:
                        description:
                            - The registry version.
                        type: int
                    key:
                        description:
                            - The identifying key for the object.
                        type: str
                    is_favorite:
                        description:
                            - Specifies whether the object is a favorite.
                        type: bool
                    created_by_user_id:
                        description:
                            - The ID of the user who created the object.
                        type: str
                    created_by_user_name:
                        description:
                            - The name of the user who created the object.
                        type: str
                    updated_by_user_id:
                        description:
                            - The ID of the user who updated the object.
                        type: str
                    updated_by_user_name:
                        description:
                            - The name of the user who updated the object.
                        type: str
                    time_created:
                        description:
                            - The date and time that the object was created.
                        type: str
                    time_updated:
                        description:
                            - The date and time that the object was updated.
                        type: str
            metadata:
                description:
                    - ""
                type: dict
                suboptions:
                    created_by:
                        description:
                            - The user that created the object.
                        type: str
                    created_by_name:
                        description:
                            - The user that created the object.
                        type: str
                    updated_by:
                        description:
                            - The user that updated the object.
                        type: str
                    updated_by_name:
                        description:
                            - The user that updated the object.
                        type: str
                    time_created:
                        description:
                            - The date and time that the object was created.
                        type: str
                    time_updated:
                        description:
                            - The date and time that the object was updated.
                        type: str
                    aggregator_key:
                        description:
                            - The owning object key for this object.
                        type: str
                    aggregator:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            type:
                                description:
                                    - The type of the aggregator.
                                type: str
                            key:
                                description:
                                    - The key of the aggregator object.
                                type: str
                            name:
                                description:
                                    - The name of the aggregator.
                                type: str
                            identifier:
                                description:
                                    - The identifier of the aggregator.
                                type: str
                            description:
                                description:
                                    - The description of the aggregator.
                                type: str
                    identifier_path:
                        description:
                            - The full path to identify the object.
                        type: str
                    info_fields:
                        description:
                            - Information property fields.
                        type: dict
                    registry_version:
                        description:
                            - The registry version of the object.
                        type: int
                    labels:
                        description:
                            - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                              categorize content.
                        type: list
                        elements: str
                    is_favorite:
                        description:
                            - Specifies whether this object is a favorite.
                        type: bool
            default_connection:
                description:
                    - ""
                type: dict
                suboptions:
                    key:
                        description:
                            - Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is
                              required, a value can be passed in create.
                        type: str
                        required: true
                    model_version:
                        description:
                            - The model version of an object.
                        type: str
                    model_type:
                        description:
                            - The type of the object.
                        type: str
                    name:
                        description:
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                        type: str
                        required: true
                    description:
                        description:
                            - User-defined description for the connection.
                        type: str
                    object_version:
                        description:
                            - The version of the object that is used to track changes in the object instance.
                        type: int
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                        type: int
                    identifier:
                        description:
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The
                              value can be modified.
                        type: str
                        required: true
                    primary_schema:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            key:
                                description:
                                    - The object key.
                                type: str
                                required: true
                            model_type:
                                description:
                                    - The object type.
                                type: str
                                required: true
                            model_version:
                                description:
                                    - The model version of the object.
                                type: str
                            parent_ref:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    parent:
                                        description:
                                            - Key of the parent object.
                                        type: str
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                                required: true
                            resource_name:
                                description:
                                    - A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000
                                      characters.
                                type: str
                            description:
                                description:
                                    - User-defined description for the schema.
                                type: str
                            object_version:
                                description:
                                    - The version of the object that is used to track changes in the object instance.
                                type: int
                            external_key:
                                description:
                                    - The external key of the object.
                                type: str
                            is_has_containers:
                                description:
                                    - Specifies whether the schema has containers.
                                type: bool
                            default_connection:
                                description:
                                    - The default connection key.
                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            identifier:
                                description:
                                    - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or
                                      underscore. The value can be modified.
                                type: str
                                required: true
                            metadata:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    created_by:
                                        description:
                                            - The user that created the object.
                                        type: str
                                    created_by_name:
                                        description:
                                            - The user that created the object.
                                        type: str
                                    updated_by:
                                        description:
                                            - The user that updated the object.
                                        type: str
                                    updated_by_name:
                                        description:
                                            - The user that updated the object.
                                        type: str
                                    time_created:
                                        description:
                                            - The date and time that the object was created.
                                        type: str
                                    time_updated:
                                        description:
                                            - The date and time that the object was updated.
                                        type: str
                                    aggregator_key:
                                        description:
                                            - The owning object key for this object.
                                        type: str
                                    aggregator:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            type:
                                                description:
                                                    - The type of the aggregator.
                                                type: str
                                            key:
                                                description:
                                                    - The key of the aggregator object.
                                                type: str
                                            name:
                                                description:
                                                    - The name of the aggregator.
                                                type: str
                                            identifier:
                                                description:
                                                    - The identifier of the aggregator.
                                                type: str
                                            description:
                                                description:
                                                    - The description of the aggregator.
                                                type: str
                                    identifier_path:
                                        description:
                                            - The full path to identify the object.
                                        type: str
                                    info_fields:
                                        description:
                                            - Information property fields.
                                        type: dict
                                    registry_version:
                                        description:
                                            - The registry version of the object.
                                        type: int
                                    labels:
                                        description:
                                            - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels
                                              and use them to categorize content.
                                        type: list
                                        elements: str
                                    is_favorite:
                                        description:
                                            - Specifies whether this object is a favorite.
                                        type: bool
                    connection_properties:
                        description:
                            - The properties of the connection.
                        type: list
                        elements: dict
                        suboptions:
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                            value:
                                description:
                                    - The value for the connection name property.
                                type: str
                    properties:
                        description:
                            - All the properties of the connection in a key-value map format.
                        type: dict
                    type:
                        description:
                            - Specific Connection Type
                        type: str
                    is_default:
                        description:
                            - The default property of the connection.
                        type: bool
                    metadata:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            created_by:
                                description:
                                    - The user that created the object.
                                type: str
                            created_by_name:
                                description:
                                    - The user that created the object.
                                type: str
                            updated_by:
                                description:
                                    - The user that updated the object.
                                type: str
                            updated_by_name:
                                description:
                                    - The user that updated the object.
                                type: str
                            time_created:
                                description:
                                    - The date and time that the object was created.
                                type: str
                            time_updated:
                                description:
                                    - The date and time that the object was updated.
                                type: str
                            aggregator_key:
                                description:
                                    - The owning object key for this object.
                                type: str
                            aggregator:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    type:
                                        description:
                                            - The type of the aggregator.
                                        type: str
                                    key:
                                        description:
                                            - The key of the aggregator object.
                                        type: str
                                    name:
                                        description:
                                            - The name of the aggregator.
                                        type: str
                                    identifier:
                                        description:
                                            - The identifier of the aggregator.
                                        type: str
                                    description:
                                        description:
                                            - The description of the aggregator.
                                        type: str
                            identifier_path:
                                description:
                                    - The full path to identify the object.
                                type: str
                            info_fields:
                                description:
                                    - Information property fields.
                                type: dict
                            registry_version:
                                description:
                                    - The registry version of the object.
                                type: int
                            labels:
                                description:
                                    - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use
                                      them to categorize content.
                                type: list
                                elements: str
                            is_favorite:
                                description:
                                    - Specifies whether this object is a favorite.
                                type: bool
                    registry_metadata:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            aggregator_key:
                                description:
                                    - The owning object's key for this object.
                                type: str
                            labels:
                                description:
                                    - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and
                                      use them to categorize content.
                                type: list
                                elements: str
                            registry_version:
                                description:
                                    - The registry version.
                                type: int
                            key:
                                description:
                                    - The identifying key for the object.
                                type: str
                            is_favorite:
                                description:
                                    - Specifies whether the object is a favorite.
                                type: bool
                            created_by_user_id:
                                description:
                                    - The ID of the user who created the object.
                                type: str
                            created_by_user_name:
                                description:
                                    - The name of the user who created the object.
                                type: str
                            updated_by_user_id:
                                description:
                                    - The ID of the user who updated the object.
                                type: str
                            updated_by_user_name:
                                description:
                                    - The name of the user who updated the object.
                                type: str
                            time_created:
                                description:
                                    - The date and time that the object was created.
                                type: str
                            time_updated:
                                description:
                                    - The date and time that the object was updated.
                                type: str
            end_points:
                description:
                    - The list of endpoints with which this data asset is associated.
                type: list
                elements: dict
                suboptions:
                    dcms_endpoint_id:
                        description:
                            - The endpoint ID provided by control plane.
                            - Required when model_type is 'PRIVATE_END_POINT'
                        type: str
                    pe_id:
                        description:
                            - The OCID of the private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    compartment_id:
                        description:
                            - The compartmentId of the private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    dns_proxy_ip:
                        description:
                            - The IP address of the DNS proxy.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    private_endpoint_ip:
                        description:
                            - The OCID of the private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    dns_zones:
                        description:
                            - Array of DNS zones to be used during the private endpoint resolution.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: list
                        elements: str
                    state:
                        description:
                            - Specifies the private endpoint state.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                        choices:
                            - "ACTIVE"
                            - "INACTIVE"
                    model_type:
                        description:
                            - The type of the endpoint.
                        type: str
                        choices:
                            - "PRIVATE_END_POINT"
                            - "PUBLIC_END_POINT"
                        required: true
                    key:
                        description:
                            - Generated key that can be used in API calls to identify the endpoint. In scenarios where reference to the endpoint is required, a
                              value can be passed in create.
                        type: str
                    model_version:
                        description:
                            - The model version of an object.
                        type: str
                    parent_ref:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                    - Applicable when model_type is 'PRIVATE_END_POINT'
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                        type: str
                    description:
                        description:
                            - User-defined description of the endpoint.
                        type: str
                    object_version:
                        description:
                            - The version of the object that is used to track changes in the object instance.
                        type: int
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                        type: int
                    identifier:
                        description:
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The
                              value can be modified.
                        type: str
                    data_assets:
                        description:
                            - The list of data assets that belong to the endpoint.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                    - Currently not used while creating a data asset. Reserved for future.
                                type: str
                                required: true
                            model_version:
                                description:
                                    - The model version of an object.
                                type: str
                            model_type:
                                description:
                                    - The type of the object.
                                type: str
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                                required: true
                            description:
                                description:
                                    - User-defined description of the data asset.
                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            object_version:
                                description:
                                    - The version of the object that is used to track changes in the object instance.
                                type: int
                            identifier:
                                description:
                                    - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or
                                      underscore. The value can be modified.
                                type: str
                                required: true
                            external_key:
                                description:
                                    - The external key of the object.
                                type: str
                            asset_properties:
                                description:
                                    - Additional properties for the data asset.
                                type: dict
                            properties:
                                description:
                                    - All the properties for the data asset in a key-value map format.
                                type: dict
                            type:
                                description:
                                    - Specific DataAsset Type
                                type: str
                            native_type_system:
                                description:
                                    - ""
                                type: dict
                            registry_metadata:
                                description:
                                    - ""
                                type: dict
                            metadata:
                                description:
                                    - ""
                                type: dict
                            default_connection:
                                description:
                                    - ""
                                type: dict
                            end_points:
                                description:
                                    - The list of endpoints with which this data asset is associated.
                                type: list
                                elements: dict
    registry_id:
        description:
            - The registry OCID.
        type: str
        required: true
    folder_key:
        description:
            - The folder ID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    state:
        description:
            - The state of the Folder.
            - Use I(state=present) to create or update a Folder.
            - Use I(state=absent) to delete a Folder.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create folder
  oci_data_connectivity_folder:
    # required
    name: name_example
    identifier: identifier_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    model_type: model_type_example
    key: key_example
    model_version: model_version_example
    parent_ref:
      # optional
      parent: parent_example
    description: description_example
    object_status: 56
    object_version: 56
    data_assets:
    - # required
      key: key_example
      name: name_example
      identifier: identifier_example

      # optional
      model_version: model_version_example
      model_type: model_type_example
      description: description_example
      object_status: 56
      object_version: 56
      external_key: external_key_example
      asset_properties: null
      properties: null
      type: type_example
      native_type_system:
        # optional
        key: key_example
        model_type: model_type_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        description: description_example
        object_version: 56
        type_mapping_to: null
        type_mapping_from: null
        object_status: 56
        identifier: identifier_example
        types:
        - # required
          model_type: STRUCTURED_TYPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          object_status: 56
          description: description_example
          dt_type: PRIMITIVE
          type_system_name: type_system_name_example
          config_definition:
            # optional
            key: key_example
            model_type: model_type_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            is_contained: true
            object_status: 56
            config_parameter_definitions:
              # optional
              parameter_type:
                # required
                model_type: CONFIGURED_TYPE

                # optional
                wrapped_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                name: name_example
                object_status: 56
                description: description_example
                config_definition:
                  # optional
                  key: key_example
                  model_type: model_type_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  is_contained: true
                  object_status: 56
                  config_parameter_definitions: null
              parameter_name: parameter_name_example
              description: description_example
              default_value: null
              class_field_name: class_field_name_example
              is_static: true
              is_class_field_value: true
      registry_metadata:
        # optional
        aggregator_key: aggregator_key_example
        labels: [ "labels_example" ]
        registry_version: 56
        key: key_example
        is_favorite: true
        created_by_user_id: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
        created_by_user_name: created_by_user_name_example
        updated_by_user_id: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_user_name: updated_by_user_name_example
        time_created: time_created_example
        time_updated: time_updated_example
      metadata:
        # optional
        created_by: created_by_example
        created_by_name: created_by_name_example
        updated_by: updated_by_example
        updated_by_name: updated_by_name_example
        time_created: time_created_example
        time_updated: time_updated_example
        aggregator_key: aggregator_key_example
        aggregator:
          # optional
          type: type_example
          key: key_example
          name: name_example
          identifier: identifier_example
          description: description_example
        identifier_path: identifier_path_example
        info_fields: null
        registry_version: 56
        labels: [ "labels_example" ]
        is_favorite: true
      default_connection:
        # required
        key: key_example
        name: name_example
        identifier: identifier_example

        # optional
        model_version: model_version_example
        model_type: model_type_example
        description: description_example
        object_version: 56
        object_status: 56
        primary_schema:
          # required
          key: key_example
          model_type: model_type_example
          name: name_example
          identifier: identifier_example

          # optional
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          resource_name: resource_name_example
          description: description_example
          object_version: 56
          external_key: external_key_example
          is_has_containers: true
          default_connection: default_connection_example
          object_status: 56
          metadata:
            # optional
            created_by: created_by_example
            created_by_name: created_by_name_example
            updated_by: updated_by_example
            updated_by_name: updated_by_name_example
            time_created: time_created_example
            time_updated: time_updated_example
            aggregator_key: aggregator_key_example
            aggregator:
              # optional
              type: type_example
              key: key_example
              name: name_example
              identifier: identifier_example
              description: description_example
            identifier_path: identifier_path_example
            info_fields: null
            registry_version: 56
            labels: [ "labels_example" ]
            is_favorite: true
        connection_properties:
        - # optional
          name: name_example
          value: value_example
        properties: null
        type: type_example
        is_default: true
        metadata:
          # optional
          created_by: created_by_example
          created_by_name: created_by_name_example
          updated_by: updated_by_example
          updated_by_name: updated_by_name_example
          time_created: time_created_example
          time_updated: time_updated_example
          aggregator_key: aggregator_key_example
          aggregator:
            # optional
            type: type_example
            key: key_example
            name: name_example
            identifier: identifier_example
            description: description_example
          identifier_path: identifier_path_example
          info_fields: null
          registry_version: 56
          labels: [ "labels_example" ]
          is_favorite: true
        registry_metadata:
          # optional
          aggregator_key: aggregator_key_example
          labels: [ "labels_example" ]
          registry_version: 56
          key: key_example
          is_favorite: true
          created_by_user_id: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
          created_by_user_name: created_by_user_name_example
          updated_by_user_id: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
          updated_by_user_name: updated_by_user_name_example
          time_created: time_created_example
          time_updated: time_updated_example
      end_points:
      - # required
        dcms_endpoint_id: "ocid1.dcmsendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        model_type: PRIVATE_END_POINT

        # optional
        pe_id: "ocid1.pe.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dns_proxy_ip: dns_proxy_ip_example
        private_endpoint_ip: private_endpoint_ip_example
        dns_zones: [ "dns_zones_example" ]
        state: ACTIVE
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        description: description_example
        object_version: 56
        object_status: 56
        identifier: identifier_example
        data_assets:
        - # required
          key: key_example
          name: name_example
          identifier: identifier_example

          # optional
          model_version: model_version_example
          model_type: model_type_example
          description: description_example
          object_status: 56
          object_version: 56
          external_key: external_key_example
          asset_properties: null
          properties: null
          type: type_example
          native_type_system: null
          registry_metadata: null
          metadata: null
          default_connection: null
          end_points: [ "end_points_example" ]

- name: Update folder
  oci_data_connectivity_folder:
    # required
    model_type: model_type_example
    key: key_example
    object_version: 56
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    folder_key: folder_key_example

    # optional
    model_version: model_version_example
    parent_ref:
      # optional
      parent: parent_example
    name: name_example
    description: description_example
    object_status: 56
    identifier: identifier_example
    data_assets:
    - # required
      key: key_example
      name: name_example
      identifier: identifier_example

      # optional
      model_version: model_version_example
      model_type: model_type_example
      description: description_example
      object_status: 56
      object_version: 56
      external_key: external_key_example
      asset_properties: null
      properties: null
      type: type_example
      native_type_system:
        # optional
        key: key_example
        model_type: model_type_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        description: description_example
        object_version: 56
        type_mapping_to: null
        type_mapping_from: null
        object_status: 56
        identifier: identifier_example
        types:
        - # required
          model_type: STRUCTURED_TYPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          object_status: 56
          description: description_example
          dt_type: PRIMITIVE
          type_system_name: type_system_name_example
          config_definition:
            # optional
            key: key_example
            model_type: model_type_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            is_contained: true
            object_status: 56
            config_parameter_definitions:
              # optional
              parameter_type:
                # required
                model_type: CONFIGURED_TYPE

                # optional
                wrapped_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                name: name_example
                object_status: 56
                description: description_example
                config_definition:
                  # optional
                  key: key_example
                  model_type: model_type_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  is_contained: true
                  object_status: 56
                  config_parameter_definitions: null
              parameter_name: parameter_name_example
              description: description_example
              default_value: null
              class_field_name: class_field_name_example
              is_static: true
              is_class_field_value: true
      registry_metadata:
        # optional
        aggregator_key: aggregator_key_example
        labels: [ "labels_example" ]
        registry_version: 56
        key: key_example
        is_favorite: true
        created_by_user_id: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
        created_by_user_name: created_by_user_name_example
        updated_by_user_id: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_user_name: updated_by_user_name_example
        time_created: time_created_example
        time_updated: time_updated_example
      metadata:
        # optional
        created_by: created_by_example
        created_by_name: created_by_name_example
        updated_by: updated_by_example
        updated_by_name: updated_by_name_example
        time_created: time_created_example
        time_updated: time_updated_example
        aggregator_key: aggregator_key_example
        aggregator:
          # optional
          type: type_example
          key: key_example
          name: name_example
          identifier: identifier_example
          description: description_example
        identifier_path: identifier_path_example
        info_fields: null
        registry_version: 56
        labels: [ "labels_example" ]
        is_favorite: true
      default_connection:
        # required
        key: key_example
        name: name_example
        identifier: identifier_example

        # optional
        model_version: model_version_example
        model_type: model_type_example
        description: description_example
        object_version: 56
        object_status: 56
        primary_schema:
          # required
          key: key_example
          model_type: model_type_example
          name: name_example
          identifier: identifier_example

          # optional
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          resource_name: resource_name_example
          description: description_example
          object_version: 56
          external_key: external_key_example
          is_has_containers: true
          default_connection: default_connection_example
          object_status: 56
          metadata:
            # optional
            created_by: created_by_example
            created_by_name: created_by_name_example
            updated_by: updated_by_example
            updated_by_name: updated_by_name_example
            time_created: time_created_example
            time_updated: time_updated_example
            aggregator_key: aggregator_key_example
            aggregator:
              # optional
              type: type_example
              key: key_example
              name: name_example
              identifier: identifier_example
              description: description_example
            identifier_path: identifier_path_example
            info_fields: null
            registry_version: 56
            labels: [ "labels_example" ]
            is_favorite: true
        connection_properties:
        - # optional
          name: name_example
          value: value_example
        properties: null
        type: type_example
        is_default: true
        metadata:
          # optional
          created_by: created_by_example
          created_by_name: created_by_name_example
          updated_by: updated_by_example
          updated_by_name: updated_by_name_example
          time_created: time_created_example
          time_updated: time_updated_example
          aggregator_key: aggregator_key_example
          aggregator:
            # optional
            type: type_example
            key: key_example
            name: name_example
            identifier: identifier_example
            description: description_example
          identifier_path: identifier_path_example
          info_fields: null
          registry_version: 56
          labels: [ "labels_example" ]
          is_favorite: true
        registry_metadata:
          # optional
          aggregator_key: aggregator_key_example
          labels: [ "labels_example" ]
          registry_version: 56
          key: key_example
          is_favorite: true
          created_by_user_id: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
          created_by_user_name: created_by_user_name_example
          updated_by_user_id: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
          updated_by_user_name: updated_by_user_name_example
          time_created: time_created_example
          time_updated: time_updated_example
      end_points:
      - # required
        dcms_endpoint_id: "ocid1.dcmsendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        model_type: PRIVATE_END_POINT

        # optional
        pe_id: "ocid1.pe.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dns_proxy_ip: dns_proxy_ip_example
        private_endpoint_ip: private_endpoint_ip_example
        dns_zones: [ "dns_zones_example" ]
        state: ACTIVE
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        description: description_example
        object_version: 56
        object_status: 56
        identifier: identifier_example
        data_assets:
        - # required
          key: key_example
          name: name_example
          identifier: identifier_example

          # optional
          model_version: model_version_example
          model_type: model_type_example
          description: description_example
          object_status: 56
          object_version: 56
          external_key: external_key_example
          asset_properties: null
          properties: null
          type: type_example
          native_type_system: null
          registry_metadata: null
          metadata: null
          default_connection: null
          end_points: [ "end_points_example" ]

- name: Update folder using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_connectivity_folder:
    # required
    name: name_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    model_type: model_type_example
    key: key_example
    model_version: model_version_example
    parent_ref:
      # optional
      parent: parent_example
    description: description_example
    object_status: 56
    object_version: 56
    identifier: identifier_example
    data_assets:
    - # required
      key: key_example
      name: name_example
      identifier: identifier_example

      # optional
      model_version: model_version_example
      model_type: model_type_example
      description: description_example
      object_status: 56
      object_version: 56
      external_key: external_key_example
      asset_properties: null
      properties: null
      type: type_example
      native_type_system:
        # optional
        key: key_example
        model_type: model_type_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        description: description_example
        object_version: 56
        type_mapping_to: null
        type_mapping_from: null
        object_status: 56
        identifier: identifier_example
        types:
        - # required
          model_type: STRUCTURED_TYPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          object_status: 56
          description: description_example
          dt_type: PRIMITIVE
          type_system_name: type_system_name_example
          config_definition:
            # optional
            key: key_example
            model_type: model_type_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            is_contained: true
            object_status: 56
            config_parameter_definitions:
              # optional
              parameter_type:
                # required
                model_type: CONFIGURED_TYPE

                # optional
                wrapped_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                name: name_example
                object_status: 56
                description: description_example
                config_definition:
                  # optional
                  key: key_example
                  model_type: model_type_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  is_contained: true
                  object_status: 56
                  config_parameter_definitions: null
              parameter_name: parameter_name_example
              description: description_example
              default_value: null
              class_field_name: class_field_name_example
              is_static: true
              is_class_field_value: true
      registry_metadata:
        # optional
        aggregator_key: aggregator_key_example
        labels: [ "labels_example" ]
        registry_version: 56
        key: key_example
        is_favorite: true
        created_by_user_id: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
        created_by_user_name: created_by_user_name_example
        updated_by_user_id: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_user_name: updated_by_user_name_example
        time_created: time_created_example
        time_updated: time_updated_example
      metadata:
        # optional
        created_by: created_by_example
        created_by_name: created_by_name_example
        updated_by: updated_by_example
        updated_by_name: updated_by_name_example
        time_created: time_created_example
        time_updated: time_updated_example
        aggregator_key: aggregator_key_example
        aggregator:
          # optional
          type: type_example
          key: key_example
          name: name_example
          identifier: identifier_example
          description: description_example
        identifier_path: identifier_path_example
        info_fields: null
        registry_version: 56
        labels: [ "labels_example" ]
        is_favorite: true
      default_connection:
        # required
        key: key_example
        name: name_example
        identifier: identifier_example

        # optional
        model_version: model_version_example
        model_type: model_type_example
        description: description_example
        object_version: 56
        object_status: 56
        primary_schema:
          # required
          key: key_example
          model_type: model_type_example
          name: name_example
          identifier: identifier_example

          # optional
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          resource_name: resource_name_example
          description: description_example
          object_version: 56
          external_key: external_key_example
          is_has_containers: true
          default_connection: default_connection_example
          object_status: 56
          metadata:
            # optional
            created_by: created_by_example
            created_by_name: created_by_name_example
            updated_by: updated_by_example
            updated_by_name: updated_by_name_example
            time_created: time_created_example
            time_updated: time_updated_example
            aggregator_key: aggregator_key_example
            aggregator:
              # optional
              type: type_example
              key: key_example
              name: name_example
              identifier: identifier_example
              description: description_example
            identifier_path: identifier_path_example
            info_fields: null
            registry_version: 56
            labels: [ "labels_example" ]
            is_favorite: true
        connection_properties:
        - # optional
          name: name_example
          value: value_example
        properties: null
        type: type_example
        is_default: true
        metadata:
          # optional
          created_by: created_by_example
          created_by_name: created_by_name_example
          updated_by: updated_by_example
          updated_by_name: updated_by_name_example
          time_created: time_created_example
          time_updated: time_updated_example
          aggregator_key: aggregator_key_example
          aggregator:
            # optional
            type: type_example
            key: key_example
            name: name_example
            identifier: identifier_example
            description: description_example
          identifier_path: identifier_path_example
          info_fields: null
          registry_version: 56
          labels: [ "labels_example" ]
          is_favorite: true
        registry_metadata:
          # optional
          aggregator_key: aggregator_key_example
          labels: [ "labels_example" ]
          registry_version: 56
          key: key_example
          is_favorite: true
          created_by_user_id: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
          created_by_user_name: created_by_user_name_example
          updated_by_user_id: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
          updated_by_user_name: updated_by_user_name_example
          time_created: time_created_example
          time_updated: time_updated_example
      end_points:
      - # required
        dcms_endpoint_id: "ocid1.dcmsendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        model_type: PRIVATE_END_POINT

        # optional
        pe_id: "ocid1.pe.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dns_proxy_ip: dns_proxy_ip_example
        private_endpoint_ip: private_endpoint_ip_example
        dns_zones: [ "dns_zones_example" ]
        state: ACTIVE
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        description: description_example
        object_version: 56
        object_status: 56
        identifier: identifier_example
        data_assets:
        - # required
          key: key_example
          name: name_example
          identifier: identifier_example

          # optional
          model_version: model_version_example
          model_type: model_type_example
          description: description_example
          object_status: 56
          object_version: 56
          external_key: external_key_example
          asset_properties: null
          properties: null
          type: type_example
          native_type_system: null
          registry_metadata: null
          metadata: null
          default_connection: null
          end_points: [ "end_points_example" ]

- name: Delete folder
  oci_data_connectivity_folder:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    folder_key: folder_key_example
    state: absent

- name: Delete folder using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_connectivity_folder:
    # required
    name: name_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
folder:
    description:
        - Details of the Folder resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        model_type:
            description:
                - The type of the folder.
            returned: on success
            type: str
            sample: model_type_example
        key:
            description:
                - Generated key that can be used in API calls to identify the folder. In scenarios where reference to the folder is required, a value can be
                  passed in create.
            returned: on success
            type: str
            sample: key_example
        model_version:
            description:
                - The model version of an object.
            returned: on success
            type: str
            sample: model_version_example
        parent_ref:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                parent:
                    description:
                        - Key of the parent object.
                    returned: on success
                    type: str
                    sample: parent_example
        name:
            description:
                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                  editable and is restricted to 1000 characters.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - User-defined description of the folder.
            returned: on success
            type: str
            sample: description_example
        object_version:
            description:
                - The version of the object that is used to track changes in the object instance.
            returned: on success
            type: int
            sample: 56
        object_status:
            description:
                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
            returned: on success
            type: int
            sample: 56
        identifier:
            description:
                - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be
                  modified.
            returned: on success
            type: str
            sample: identifier_example
        data_assets:
            description:
                - The list of data assets that belong to the folder.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Currently not used while creating a data asset. Reserved for future.
                    returned: on success
                    type: str
                    sample: key_example
                model_version:
                    description:
                        - The model version of an object.
                    returned: on success
                    type: str
                    sample: model_version_example
                model_type:
                    description:
                        - The type of the object.
                    returned: on success
                    type: str
                    sample: model_type_example
                name:
                    description:
                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value
                          is editable and is restricted to 1000 characters.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - User-defined description of the data asset.
                    returned: on success
                    type: str
                    sample: description_example
                object_status:
                    description:
                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                    returned: on success
                    type: int
                    sample: 56
                object_version:
                    description:
                        - The version of the object that is used to track changes in the object instance.
                    returned: on success
                    type: int
                    sample: 56
                identifier:
                    description:
                        - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value
                          can be modified.
                    returned: on success
                    type: str
                    sample: identifier_example
                external_key:
                    description:
                        - The external key of the object.
                    returned: on success
                    type: str
                    sample: external_key_example
                asset_properties:
                    description:
                        - Additional properties for the data asset.
                    returned: on success
                    type: dict
                    sample: {}
                properties:
                    description:
                        - All the properties for the data asset in a key-value map format.
                    returned: on success
                    type: dict
                    sample: {}
                type:
                    description:
                        - Specific DataAsset Type
                    returned: on success
                    type: str
                    sample: type_example
                native_type_system:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The key of the object.
                            returned: on success
                            type: str
                            sample: key_example
                        model_type:
                            description:
                                - The type of the object.
                            returned: on success
                            type: str
                            sample: model_type_example
                        model_version:
                            description:
                                - The model version of an object.
                            returned: on success
                            type: str
                            sample: model_version_example
                        parent_ref:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                parent:
                                    description:
                                        - Key of the parent object.
                                    returned: on success
                                    type: str
                                    sample: parent_example
                        name:
                            description:
                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters.
                                  The value is editable and is restricted to 1000 characters.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - A user-defined description for the object.
                            returned: on success
                            type: str
                            sample: description_example
                        object_version:
                            description:
                                - The version of the object that is used to track changes in the object instance.
                            returned: on success
                            type: int
                            sample: 56
                        type_mapping_to:
                            description:
                                - The type system to map to.
                            returned: on success
                            type: dict
                            sample: {}
                        type_mapping_from:
                            description:
                                - The type system to map from.
                            returned: on success
                            type: dict
                            sample: {}
                        object_status:
                            description:
                                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                            returned: on success
                            type: int
                            sample: 56
                        identifier:
                            description:
                                - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore.
                                  The value can be modified.
                            returned: on success
                            type: str
                            sample: identifier_example
                        types:
                            description:
                                - An array of types.
                            returned: on success
                            type: complex
                            contains:
                                model_type:
                                    description:
                                        - The property which differentiates the subtypes.
                                    returned: on success
                                    type: str
                                    sample: STRUCTURED_TYPE
                                key:
                                    description:
                                        - The key of the object.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                model_version:
                                    description:
                                        - The model version of an object.
                                    returned: on success
                                    type: str
                                    sample: model_version_example
                                parent_ref:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        parent:
                                            description:
                                                - Key of the parent object.
                                            returned: on success
                                            type: str
                                            sample: parent_example
                                name:
                                    description:
                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                          characters. The value is editable and is restricted to 1000 characters.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                object_status:
                                    description:
                                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                    returned: on success
                                    type: int
                                    sample: 56
                                description:
                                    description:
                                        - A user-defined description for the object.
                                    returned: on success
                                    type: str
                                    sample: description_example
                                dt_type:
                                    description:
                                        - The data type.
                                    returned: on success
                                    type: str
                                    sample: PRIMITIVE
                                type_system_name:
                                    description:
                                        - The data type system name.
                                    returned: on success
                                    type: str
                                    sample: type_system_name_example
                                config_definition:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        key:
                                            description:
                                                - The key of the object.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        model_type:
                                            description:
                                                - The type of the object.
                                            returned: on success
                                            type: str
                                            sample: model_type_example
                                        model_version:
                                            description:
                                                - The model version of an object.
                                            returned: on success
                                            type: str
                                            sample: model_version_example
                                        parent_ref:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                parent:
                                                    description:
                                                        - Key of the parent object.
                                                    returned: on success
                                                    type: str
                                                    sample: parent_example
                                        name:
                                            description:
                                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and
                                                  special characters. The value is editable and is restricted to 1000 characters.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        is_contained:
                                            description:
                                                - Specifies whether the configuration is contained.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        object_status:
                                            description:
                                                - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                  reserved.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        config_parameter_definitions:
                                            description:
                                                - The parameter configuration details.
                                            returned: on success
                                            type: complex
                                            contains:
                                                parameter_type:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        parent_type:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                model_type:
                                                                    description:
                                                                        - The property which differentiates the subtypes.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: STRUCTURED_TYPE
                                                                key:
                                                                    description:
                                                                        - The key of the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: key_example
                                                                model_version:
                                                                    description:
                                                                        - The model version of an object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: model_version_example
                                                                parent_ref:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: ParentReference
                                                                    sample: "null"

                                                                name:
                                                                    description:
                                                                        - Free form text without any restriction on the permitted characters. Name can have
                                                                          letters, numbers, and special characters. The value is editable and is restricted to
                                                                          1000 characters.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: name_example
                                                                object_status:
                                                                    description:
                                                                        - The status of an object that can be set to value 1 for shallow references across
                                                                          objects, other values reserved.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                description:
                                                                    description:
                                                                        - A user-defined description for the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: description_example
                                                                parent_type:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: CompositeType
                                                                    sample: "null"

                                                                elements:
                                                                    description:
                                                                        - An array of elements.
                                                                    returned: on success
                                                                    type: list
                                                                    sample: []
                                                                config_definition:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: ConfigDefinition
                                                                    sample: "null"

                                                        elements:
                                                            description:
                                                                - An array of elements.
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                position:
                                                                    description:
                                                                        - The position of the attribute.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                default_value_string:
                                                                    description:
                                                                        - The default value.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: default_value_string_example
                                                                is_mandatory:
                                                                    description:
                                                                        - Specifies whether the field is mandatory.
                                                                    returned: on success
                                                                    type: bool
                                                                    sample: true
                                                                port_type:
                                                                    description:
                                                                        - The port details of the data asset type.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: DATA
                                                                fields:
                                                                    description:
                                                                        - An array of fields.
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        model_type:
                                                                            description:
                                                                                - The type of the types object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: SHAPE
                                                                        key:
                                                                            description:
                                                                                - The key of the object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: key_example
                                                                        model_version:
                                                                            description:
                                                                                - The model version of an object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: model_version_example
                                                                        parent_ref:
                                                                            description:
                                                                                - ""
                                                                            returned: on success
                                                                            type: ParentReference
                                                                            sample: "null"

                                                                        config_values:
                                                                            description:
                                                                                - ""
                                                                            returned: on success
                                                                            type: ConfigValues
                                                                            sample: "null"

                                                                        object_status:
                                                                            description:
                                                                                - The status of an object that can be set to value 1 for shallow references
                                                                                  across objects, other values reserved.
                                                                            returned: on success
                                                                            type: int
                                                                            sample: 56
                                                                        name:
                                                                            description:
                                                                                - Free form text without any restriction on the permitted characters. Name can
                                                                                  have letters, numbers, and special characters. The value is editable and is
                                                                                  restricted to 1000 characters.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: name_example
                                                                        description:
                                                                            description:
                                                                                - A detailed description of the object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: description_example
                                                                default_value:
                                                                    description:
                                                                        - The default value of the parameter.
                                                                    returned: on success
                                                                    type: dict
                                                                    sample: {}
                                                                root_object_default_value:
                                                                    description:
                                                                        - The default value of the parameter, which can be an object in DIS, such as a data
                                                                          entity.
                                                                    returned: on success
                                                                    type: dict
                                                                    sample: {}
                                                                is_input:
                                                                    description:
                                                                        - Specifies whether the parameter is an input value.
                                                                    returned: on success
                                                                    type: bool
                                                                    sample: true
                                                                is_output:
                                                                    description:
                                                                        - Specifies whether the parameter is an output value.
                                                                    returned: on success
                                                                    type: bool
                                                                    sample: true
                                                                output_aggregation_type:
                                                                    description:
                                                                        - The output aggregation type.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: MIN
                                                                type_name:
                                                                    description:
                                                                        - The type of value the parameter was created for.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: type_name_example
                                                                model_type:
                                                                    description:
                                                                        - The type of the types object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: SHAPE
                                                                key:
                                                                    description:
                                                                        - The key of the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: key_example
                                                                model_version:
                                                                    description:
                                                                        - The model version of an object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: model_version_example
                                                                parent_ref:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        parent:
                                                                            description:
                                                                                - Key of the parent object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: parent_example
                                                                config_values:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        config_param_values:
                                                                            description:
                                                                                - The configuration parameter values.
                                                                            returned: on success
                                                                            type: complex
                                                                            contains:
                                                                                string_value:
                                                                                    description:
                                                                                        - A string value of the parameter.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: string_value_example
                                                                                int_value:
                                                                                    description:
                                                                                        - An integer value of the parameter.
                                                                                    returned: on success
                                                                                    type: int
                                                                                    sample: 56
                                                                                object_value:
                                                                                    description:
                                                                                        - An object value of the parameter.
                                                                                    returned: on success
                                                                                    type: dict
                                                                                    sample: {}
                                                                                ref_value:
                                                                                    description:
                                                                                        - The root object reference value.
                                                                                    returned: on success
                                                                                    type: dict
                                                                                    sample: {}
                                                                                parameter_value:
                                                                                    description:
                                                                                        - Reference to the parameter by its key.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: parameter_value_example
                                                                        parent_ref:
                                                                            description:
                                                                                - ""
                                                                            returned: on success
                                                                            type: complex
                                                                            contains:
                                                                                parent:
                                                                                    description:
                                                                                        - Key of the parent object.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: parent_example
                                                                object_status:
                                                                    description:
                                                                        - The status of an object that can be set to value 1 for shallow references across
                                                                          objects, other values reserved.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                name:
                                                                    description:
                                                                        - Free form text without any restriction on the permitted characters. Name can have
                                                                          letters, numbers, and special characters. The value is editable and is restricted to
                                                                          1000 characters.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: name_example
                                                                description:
                                                                    description:
                                                                        - A detailed description of the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: description_example
                                                                type:
                                                                    description:
                                                                        - The type reference.
                                                                    returned: on success
                                                                    type: dict
                                                                    sample: {}
                                                                labels:
                                                                    description:
                                                                        - Labels are keywords or labels that you can add to data assets, dataflows, and so on.
                                                                          You can define your own labels and use them to categorize content.
                                                                    returned: on success
                                                                    type: list
                                                                    sample: []
                                                                native_shape_field:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        model_type:
                                                                            description:
                                                                                - The type of the types object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: SHAPE
                                                                        key:
                                                                            description:
                                                                                - The key of the object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: key_example
                                                                        model_version:
                                                                            description:
                                                                                - The model version of an object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: model_version_example
                                                                        parent_ref:
                                                                            description:
                                                                                - ""
                                                                            returned: on success
                                                                            type: complex
                                                                            contains:
                                                                                parent:
                                                                                    description:
                                                                                        - Key of the parent object.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: parent_example
                                                                        config_values:
                                                                            description:
                                                                                - ""
                                                                            returned: on success
                                                                            type: complex
                                                                            contains:
                                                                                config_param_values:
                                                                                    description:
                                                                                        - The configuration parameter values.
                                                                                    returned: on success
                                                                                    type: complex
                                                                                    contains:
                                                                                        string_value:
                                                                                            description:
                                                                                                - A string value of the parameter.
                                                                                            returned: on success
                                                                                            type: str
                                                                                            sample: string_value_example
                                                                                        int_value:
                                                                                            description:
                                                                                                - An integer value of the parameter.
                                                                                            returned: on success
                                                                                            type: int
                                                                                            sample: 56
                                                                                        object_value:
                                                                                            description:
                                                                                                - An object value of the parameter.
                                                                                            returned: on success
                                                                                            type: dict
                                                                                            sample: {}
                                                                                        ref_value:
                                                                                            description:
                                                                                                - The root object reference value.
                                                                                            returned: on success
                                                                                            type: dict
                                                                                            sample: {}
                                                                                        parameter_value:
                                                                                            description:
                                                                                                - Reference to the parameter by its key.
                                                                                            returned: on success
                                                                                            type: str
                                                                                            sample: parameter_value_example
                                                                                parent_ref:
                                                                                    description:
                                                                                        - ""
                                                                                    returned: on success
                                                                                    type: complex
                                                                                    contains:
                                                                                        parent:
                                                                                            description:
                                                                                                - Key of the parent object.
                                                                                            returned: on success
                                                                                            type: str
                                                                                            sample: parent_example
                                                                        object_status:
                                                                            description:
                                                                                - The status of an object that can be set to value 1 for shallow references
                                                                                  across objects, other values reserved.
                                                                            returned: on success
                                                                            type: int
                                                                            sample: 56
                                                                        name:
                                                                            description:
                                                                                - Free form text without any restriction on the permitted characters. Name can
                                                                                  have letters, numbers, and special characters. The value is editable and is
                                                                                  restricted to 1000 characters.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: name_example
                                                                        description:
                                                                            description:
                                                                                - A detailed description of the object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: description_example
                                                                        type:
                                                                            description:
                                                                                - The type reference.
                                                                            returned: on success
                                                                            type: dict
                                                                            sample: {}
                                                                        position:
                                                                            description:
                                                                                - The position of the attribute.
                                                                            returned: on success
                                                                            type: int
                                                                            sample: 56
                                                                        default_value_string:
                                                                            description:
                                                                                - The default value.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: default_value_string_example
                                                                        is_mandatory:
                                                                            description:
                                                                                - Specifies whether the field is mandatory.
                                                                            returned: on success
                                                                            type: bool
                                                                            sample: true
                                                        wrapped_type:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                model_type:
                                                                    description:
                                                                        - The property which differentiates the subtypes.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: STRUCTURED_TYPE
                                                                key:
                                                                    description:
                                                                        - The key of the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: key_example
                                                                model_version:
                                                                    description:
                                                                        - The model version of an object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: model_version_example
                                                                parent_ref:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: ParentReference
                                                                    sample: "null"

                                                                name:
                                                                    description:
                                                                        - Free form text without any restriction on the permitted characters. Name can have
                                                                          letters, numbers, and special characters. The value is editable and is restricted to
                                                                          1000 characters.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: name_example
                                                                object_status:
                                                                    description:
                                                                        - The status of an object that can be set to value 1 for shallow references across
                                                                          objects, other values reserved.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                description:
                                                                    description:
                                                                        - A user-defined description for the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: description_example
                                                        config_values:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                config_param_values:
                                                                    description:
                                                                        - The configuration parameter values.
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        string_value:
                                                                            description:
                                                                                - A string value of the parameter.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: string_value_example
                                                                        int_value:
                                                                            description:
                                                                                - An integer value of the parameter.
                                                                            returned: on success
                                                                            type: int
                                                                            sample: 56
                                                                        object_value:
                                                                            description:
                                                                                - An object value of the parameter.
                                                                            returned: on success
                                                                            type: dict
                                                                            sample: {}
                                                                        ref_value:
                                                                            description:
                                                                                - The root object reference value.
                                                                            returned: on success
                                                                            type: dict
                                                                            sample: {}
                                                                        parameter_value:
                                                                            description:
                                                                                - Reference to the parameter by its key.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: parameter_value_example
                                                                parent_ref:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        parent:
                                                                            description:
                                                                                - Key of the parent object.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: parent_example
                                                        dt_type:
                                                            description:
                                                                - The data type.
                                                            returned: on success
                                                            type: str
                                                            sample: PRIMITIVE
                                                        type_system_name:
                                                            description:
                                                                - The data type system name.
                                                            returned: on success
                                                            type: str
                                                            sample: type_system_name_example
                                                        config_definition:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                key:
                                                                    description:
                                                                        - The key of the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: key_example
                                                                model_type:
                                                                    description:
                                                                        - The type of the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: model_type_example
                                                                model_version:
                                                                    description:
                                                                        - The model version of an object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: model_version_example
                                                                parent_ref:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: ParentReference
                                                                    sample: "null"

                                                                name:
                                                                    description:
                                                                        - Free form text without any restriction on the permitted characters. Name can have
                                                                          letters, numbers, and special characters. The value is editable and is restricted to
                                                                          1000 characters.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: name_example
                                                                is_contained:
                                                                    description:
                                                                        - Specifies whether the configuration is contained.
                                                                    returned: on success
                                                                    type: bool
                                                                    sample: true
                                                                object_status:
                                                                    description:
                                                                        - The status of an object that can be set to value 1 for shallow references across
                                                                          objects, other values reserved.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                config_parameter_definitions:
                                                                    description:
                                                                        - The parameter configuration details.
                                                                    returned: on success
                                                                    type: dict
                                                                    sample: {}
                                                        model_type:
                                                            description:
                                                                - The property which differentiates the subtypes.
                                                            returned: on success
                                                            type: str
                                                            sample: STRUCTURED_TYPE
                                                        key:
                                                            description:
                                                                - The key of the object.
                                                            returned: on success
                                                            type: str
                                                            sample: key_example
                                                        model_version:
                                                            description:
                                                                - The model version of an object.
                                                            returned: on success
                                                            type: str
                                                            sample: model_version_example
                                                        parent_ref:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                parent:
                                                                    description:
                                                                        - Key of the parent object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: parent_example
                                                        name:
                                                            description:
                                                                - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                  numbers, and special characters. The value is editable and is restricted to 1000 characters.
                                                            returned: on success
                                                            type: str
                                                            sample: name_example
                                                        object_status:
                                                            description:
                                                                - The status of an object that can be set to value 1 for shallow references across objects,
                                                                  other values reserved.
                                                            returned: on success
                                                            type: int
                                                            sample: 56
                                                        description:
                                                            description:
                                                                - A user-defined description for the object.
                                                            returned: on success
                                                            type: str
                                                            sample: description_example
                                                        schema:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                model_type:
                                                                    description:
                                                                        - The property which differentiates the subtypes.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: STRUCTURED_TYPE
                                                                key:
                                                                    description:
                                                                        - The key of the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: key_example
                                                                model_version:
                                                                    description:
                                                                        - The model version of an object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: model_version_example
                                                                parent_ref:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: ParentReference
                                                                    sample: "null"

                                                                name:
                                                                    description:
                                                                        - Free form text without any restriction on the permitted characters. Name can have
                                                                          letters, numbers, and special characters. The value is editable and is restricted to
                                                                          1000 characters.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: name_example
                                                                object_status:
                                                                    description:
                                                                        - The status of an object that can be set to value 1 for shallow references across
                                                                          objects, other values reserved.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                description:
                                                                    description:
                                                                        - A user-defined description for the object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: description_example
                                                parameter_name:
                                                    description:
                                                        - This object represents the configurable properties for an object type.
                                                    returned: on success
                                                    type: str
                                                    sample: parameter_name_example
                                                description:
                                                    description:
                                                        - A user-defined description for the object.
                                                    returned: on success
                                                    type: str
                                                    sample: description_example
                                                default_value:
                                                    description:
                                                        - The default value for the parameter.
                                                    returned: on success
                                                    type: dict
                                                    sample: {}
                                                class_field_name:
                                                    description:
                                                        - The parameter class field name.
                                                    returned: on success
                                                    type: str
                                                    sample: class_field_name_example
                                                is_static:
                                                    description:
                                                        - Specifies whether the parameter is static.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                                is_class_field_value:
                                                    description:
                                                        - Specifies whether the parameter is a class field.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                registry_metadata:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        aggregator_key:
                            description:
                                - The owning object's key for this object.
                            returned: on success
                            type: str
                            sample: aggregator_key_example
                        labels:
                            description:
                                - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use
                                  them to categorize content.
                            returned: on success
                            type: list
                            sample: []
                        registry_version:
                            description:
                                - The registry version.
                            returned: on success
                            type: int
                            sample: 56
                        key:
                            description:
                                - The identifying key for the object.
                            returned: on success
                            type: str
                            sample: key_example
                        is_favorite:
                            description:
                                - Specifies whether the object is a favorite.
                            returned: on success
                            type: bool
                            sample: true
                        created_by_user_id:
                            description:
                                - The ID of the user who created the object.
                            returned: on success
                            type: str
                            sample: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                        created_by_user_name:
                            description:
                                - The name of the user who created the object.
                            returned: on success
                            type: str
                            sample: created_by_user_name_example
                        updated_by_user_id:
                            description:
                                - The ID of the user who updated the object.
                            returned: on success
                            type: str
                            sample: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                        updated_by_user_name:
                            description:
                                - The name of the user who updated the object.
                            returned: on success
                            type: str
                            sample: updated_by_user_name_example
                        time_created:
                            description:
                                - The date and time that the object was created.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_updated:
                            description:
                                - The date and time that the object was updated.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                metadata:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        created_by:
                            description:
                                - The user that created the object.
                            returned: on success
                            type: str
                            sample: created_by_example
                        created_by_name:
                            description:
                                - The user that created the object.
                            returned: on success
                            type: str
                            sample: created_by_name_example
                        updated_by:
                            description:
                                - The user that updated the object.
                            returned: on success
                            type: str
                            sample: updated_by_example
                        updated_by_name:
                            description:
                                - The user that updated the object.
                            returned: on success
                            type: str
                            sample: updated_by_name_example
                        time_created:
                            description:
                                - The date and time that the object was created.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_updated:
                            description:
                                - The date and time that the object was updated.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        aggregator_key:
                            description:
                                - The owning object key for this object.
                            returned: on success
                            type: str
                            sample: aggregator_key_example
                        aggregator:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - The type of the aggregator.
                                    returned: on success
                                    type: str
                                    sample: type_example
                                key:
                                    description:
                                        - The key of the aggregator object.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                name:
                                    description:
                                        - The name of the aggregator.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                identifier:
                                    description:
                                        - The identifier of the aggregator.
                                    returned: on success
                                    type: str
                                    sample: identifier_example
                                description:
                                    description:
                                        - The description of the aggregator.
                                    returned: on success
                                    type: str
                                    sample: description_example
                        identifier_path:
                            description:
                                - The full path to identify the object.
                            returned: on success
                            type: str
                            sample: identifier_path_example
                        info_fields:
                            description:
                                - Information property fields.
                            returned: on success
                            type: dict
                            sample: {}
                        registry_version:
                            description:
                                - The registry version of the object.
                            returned: on success
                            type: int
                            sample: 56
                        labels:
                            description:
                                - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them
                                  to categorize content.
                            returned: on success
                            type: list
                            sample: []
                        is_favorite:
                            description:
                                - Specifies whether this object is a favorite.
                            returned: on success
                            type: bool
                            sample: true
                default_connection:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is
                                  required, a value can be passed in create.
                            returned: on success
                            type: str
                            sample: key_example
                        model_version:
                            description:
                                - The model version of an object.
                            returned: on success
                            type: str
                            sample: model_version_example
                        model_type:
                            description:
                                - The type of the object.
                            returned: on success
                            type: str
                            sample: model_type_example
                        name:
                            description:
                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters.
                                  The value is editable and is restricted to 1000 characters.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - User-defined description for the connection.
                            returned: on success
                            type: str
                            sample: description_example
                        object_version:
                            description:
                                - The version of the object that is used to track changes in the object instance.
                            returned: on success
                            type: int
                            sample: 56
                        object_status:
                            description:
                                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                            returned: on success
                            type: int
                            sample: 56
                        identifier:
                            description:
                                - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore.
                                  The value can be modified.
                            returned: on success
                            type: str
                            sample: identifier_example
                        primary_schema:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - The object key.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                model_type:
                                    description:
                                        - The object type.
                                    returned: on success
                                    type: str
                                    sample: model_type_example
                                model_version:
                                    description:
                                        - The model version of the object.
                                    returned: on success
                                    type: str
                                    sample: model_version_example
                                parent_ref:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        parent:
                                            description:
                                                - Key of the parent object.
                                            returned: on success
                                            type: str
                                            sample: parent_example
                                name:
                                    description:
                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                          characters. The value is editable and is restricted to 1000 characters.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                resource_name:
                                    description:
                                        - A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000
                                          characters.
                                    returned: on success
                                    type: str
                                    sample: resource_name_example
                                description:
                                    description:
                                        - User-defined description for the schema.
                                    returned: on success
                                    type: str
                                    sample: description_example
                                object_version:
                                    description:
                                        - The version of the object that is used to track changes in the object instance.
                                    returned: on success
                                    type: int
                                    sample: 56
                                external_key:
                                    description:
                                        - The external key of the object.
                                    returned: on success
                                    type: str
                                    sample: external_key_example
                                is_has_containers:
                                    description:
                                        - Specifies whether the schema has containers.
                                    returned: on success
                                    type: bool
                                    sample: true
                                default_connection:
                                    description:
                                        - The default connection key.
                                    returned: on success
                                    type: str
                                    sample: default_connection_example
                                object_status:
                                    description:
                                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                    returned: on success
                                    type: int
                                    sample: 56
                                identifier:
                                    description:
                                        - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or
                                          underscore. The value can be modified.
                                    returned: on success
                                    type: str
                                    sample: identifier_example
                                metadata:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        created_by:
                                            description:
                                                - The user that created the object.
                                            returned: on success
                                            type: str
                                            sample: created_by_example
                                        created_by_name:
                                            description:
                                                - The user that created the object.
                                            returned: on success
                                            type: str
                                            sample: created_by_name_example
                                        updated_by:
                                            description:
                                                - The user that updated the object.
                                            returned: on success
                                            type: str
                                            sample: updated_by_example
                                        updated_by_name:
                                            description:
                                                - The user that updated the object.
                                            returned: on success
                                            type: str
                                            sample: updated_by_name_example
                                        time_created:
                                            description:
                                                - The date and time that the object was created.
                                            returned: on success
                                            type: str
                                            sample: "2013-10-20T19:20:30+01:00"
                                        time_updated:
                                            description:
                                                - The date and time that the object was updated.
                                            returned: on success
                                            type: str
                                            sample: "2013-10-20T19:20:30+01:00"
                                        aggregator_key:
                                            description:
                                                - The owning object key for this object.
                                            returned: on success
                                            type: str
                                            sample: aggregator_key_example
                                        aggregator:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                type:
                                                    description:
                                                        - The type of the aggregator.
                                                    returned: on success
                                                    type: str
                                                    sample: type_example
                                                key:
                                                    description:
                                                        - The key of the aggregator object.
                                                    returned: on success
                                                    type: str
                                                    sample: key_example
                                                name:
                                                    description:
                                                        - The name of the aggregator.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                identifier:
                                                    description:
                                                        - The identifier of the aggregator.
                                                    returned: on success
                                                    type: str
                                                    sample: identifier_example
                                                description:
                                                    description:
                                                        - The description of the aggregator.
                                                    returned: on success
                                                    type: str
                                                    sample: description_example
                                        identifier_path:
                                            description:
                                                - The full path to identify the object.
                                            returned: on success
                                            type: str
                                            sample: identifier_path_example
                                        info_fields:
                                            description:
                                                - Information property fields.
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        registry_version:
                                            description:
                                                - The registry version of the object.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        labels:
                                            description:
                                                - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own
                                                  labels and use them to categorize content.
                                            returned: on success
                                            type: list
                                            sample: []
                                        is_favorite:
                                            description:
                                                - Specifies whether this object is a favorite.
                                            returned: on success
                                            type: bool
                                            sample: true
                        connection_properties:
                            description:
                                - The properties of the connection.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                          characters. The value is editable and is restricted to 1000 characters.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - The value for the connection name property.
                                    returned: on success
                                    type: str
                                    sample: value_example
                        properties:
                            description:
                                - All the properties of the connection in a key-value map format.
                            returned: on success
                            type: dict
                            sample: {}
                        type:
                            description:
                                - Specific Connection Type
                            returned: on success
                            type: str
                            sample: type_example
                        is_default:
                            description:
                                - The default property of the connection.
                            returned: on success
                            type: bool
                            sample: true
                        metadata:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                created_by:
                                    description:
                                        - The user that created the object.
                                    returned: on success
                                    type: str
                                    sample: created_by_example
                                created_by_name:
                                    description:
                                        - The user that created the object.
                                    returned: on success
                                    type: str
                                    sample: created_by_name_example
                                updated_by:
                                    description:
                                        - The user that updated the object.
                                    returned: on success
                                    type: str
                                    sample: updated_by_example
                                updated_by_name:
                                    description:
                                        - The user that updated the object.
                                    returned: on success
                                    type: str
                                    sample: updated_by_name_example
                                time_created:
                                    description:
                                        - The date and time that the object was created.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
                                time_updated:
                                    description:
                                        - The date and time that the object was updated.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
                                aggregator_key:
                                    description:
                                        - The owning object key for this object.
                                    returned: on success
                                    type: str
                                    sample: aggregator_key_example
                                aggregator:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - The type of the aggregator.
                                            returned: on success
                                            type: str
                                            sample: type_example
                                        key:
                                            description:
                                                - The key of the aggregator object.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        name:
                                            description:
                                                - The name of the aggregator.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        identifier:
                                            description:
                                                - The identifier of the aggregator.
                                            returned: on success
                                            type: str
                                            sample: identifier_example
                                        description:
                                            description:
                                                - The description of the aggregator.
                                            returned: on success
                                            type: str
                                            sample: description_example
                                identifier_path:
                                    description:
                                        - The full path to identify the object.
                                    returned: on success
                                    type: str
                                    sample: identifier_path_example
                                info_fields:
                                    description:
                                        - Information property fields.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                registry_version:
                                    description:
                                        - The registry version of the object.
                                    returned: on success
                                    type: int
                                    sample: 56
                                labels:
                                    description:
                                        - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and
                                          use them to categorize content.
                                    returned: on success
                                    type: list
                                    sample: []
                                is_favorite:
                                    description:
                                        - Specifies whether this object is a favorite.
                                    returned: on success
                                    type: bool
                                    sample: true
                        registry_metadata:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                aggregator_key:
                                    description:
                                        - The owning object's key for this object.
                                    returned: on success
                                    type: str
                                    sample: aggregator_key_example
                                labels:
                                    description:
                                        - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels
                                          and use them to categorize content.
                                    returned: on success
                                    type: list
                                    sample: []
                                registry_version:
                                    description:
                                        - The registry version.
                                    returned: on success
                                    type: int
                                    sample: 56
                                key:
                                    description:
                                        - The identifying key for the object.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                is_favorite:
                                    description:
                                        - Specifies whether the object is a favorite.
                                    returned: on success
                                    type: bool
                                    sample: true
                                created_by_user_id:
                                    description:
                                        - The ID of the user who created the object.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                                created_by_user_name:
                                    description:
                                        - The name of the user who created the object.
                                    returned: on success
                                    type: str
                                    sample: created_by_user_name_example
                                updated_by_user_id:
                                    description:
                                        - The ID of the user who updated the object.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                                updated_by_user_name:
                                    description:
                                        - The name of the user who updated the object.
                                    returned: on success
                                    type: str
                                    sample: updated_by_user_name_example
                                time_created:
                                    description:
                                        - The date and time that the object was created.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
                                time_updated:
                                    description:
                                        - The date and time that the object was updated.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
                end_points:
                    description:
                        - The list of endpoints with which this data asset is associated.
                    returned: on success
                    type: complex
                    contains:
                        dcms_endpoint_id:
                            description:
                                - The endpoint ID provided by control plane.
                            returned: on success
                            type: str
                            sample: "ocid1.dcmsendpoint.oc1..xxxxxxEXAMPLExxxxxx"
                        pe_id:
                            description:
                                - The OCID of the private endpoint resource.
                            returned: on success
                            type: str
                            sample: "ocid1.pe.oc1..xxxxxxEXAMPLExxxxxx"
                        compartment_id:
                            description:
                                - The compartmentId of the private endpoint resource.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        dns_proxy_ip:
                            description:
                                - The IP address of the DNS proxy.
                            returned: on success
                            type: str
                            sample: dns_proxy_ip_example
                        private_endpoint_ip:
                            description:
                                - The OCID of the private endpoint resource.
                            returned: on success
                            type: str
                            sample: private_endpoint_ip_example
                        dns_zones:
                            description:
                                - Array of DNS zones to be used during the private endpoint resolution.
                            returned: on success
                            type: list
                            sample: []
                        state:
                            description:
                                - Specifies the private endpoint state.
                            returned: on success
                            type: str
                            sample: ACTIVE
                        model_type:
                            description:
                                - The type of the endpoint.
                            returned: on success
                            type: str
                            sample: PRIVATE_END_POINT
                        key:
                            description:
                                - Generated key that can be used in API calls to identify the endpoint. In scenarios where reference to the endpoint is
                                  required, a value can be passed in create.
                            returned: on success
                            type: str
                            sample: key_example
                        model_version:
                            description:
                                - The model version of an object.
                            returned: on success
                            type: str
                            sample: model_version_example
                        parent_ref:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                parent:
                                    description:
                                        - Key of the parent object.
                                    returned: on success
                                    type: str
                                    sample: parent_example
                        name:
                            description:
                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters.
                                  The value is editable and is restricted to 1000 characters.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - User-defined description of the endpoint.
                            returned: on success
                            type: str
                            sample: description_example
                        object_version:
                            description:
                                - The version of the object that is used to track changes in the object instance.
                            returned: on success
                            type: int
                            sample: 56
                        object_status:
                            description:
                                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                            returned: on success
                            type: int
                            sample: 56
                        identifier:
                            description:
                                - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore.
                                  The value can be modified.
                            returned: on success
                            type: str
                            sample: identifier_example
                        data_assets:
                            description:
                                - The list of data assets that belong to the endpoint.
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - Currently not used while creating a data asset. Reserved for future.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                model_version:
                                    description:
                                        - The model version of an object.
                                    returned: on success
                                    type: str
                                    sample: model_version_example
                                model_type:
                                    description:
                                        - The type of the object.
                                    returned: on success
                                    type: str
                                    sample: model_type_example
                                name:
                                    description:
                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                          characters. The value is editable and is restricted to 1000 characters.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                description:
                                    description:
                                        - User-defined description of the data asset.
                                    returned: on success
                                    type: str
                                    sample: description_example
                                object_status:
                                    description:
                                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                    returned: on success
                                    type: int
                                    sample: 56
                                object_version:
                                    description:
                                        - The version of the object that is used to track changes in the object instance.
                                    returned: on success
                                    type: int
                                    sample: 56
                                identifier:
                                    description:
                                        - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or
                                          underscore. The value can be modified.
                                    returned: on success
                                    type: str
                                    sample: identifier_example
                                external_key:
                                    description:
                                        - The external key of the object.
                                    returned: on success
                                    type: str
                                    sample: external_key_example
                                asset_properties:
                                    description:
                                        - Additional properties for the data asset.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                properties:
                                    description:
                                        - All the properties for the data asset in a key-value map format.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                type:
                                    description:
                                        - Specific DataAsset Type
                                    returned: on success
                                    type: str
                                    sample: type_example
                                native_type_system:
                                    description:
                                        - ""
                                    returned: on success
                                    type: TypeSystem
                                    sample: "null"

                                registry_metadata:
                                    description:
                                        - ""
                                    returned: on success
                                    type: RegistryMetadata
                                    sample: "null"

                                metadata:
                                    description:
                                        - ""
                                    returned: on success
                                    type: ObjectMetadata
                                    sample: "null"

                                default_connection:
                                    description:
                                        - ""
                                    returned: on success
                                    type: Connection
                                    sample: "null"

                                end_points:
                                    description:
                                        - The list of endpoints with which this data asset is associated.
                                    returned: on success
                                    type: list
                                    sample: []
    sample: {
        "model_type": "model_type_example",
        "key": "key_example",
        "model_version": "model_version_example",
        "parent_ref": {
            "parent": "parent_example"
        },
        "name": "name_example",
        "description": "description_example",
        "object_version": 56,
        "object_status": 56,
        "identifier": "identifier_example",
        "data_assets": [{
            "key": "key_example",
            "model_version": "model_version_example",
            "model_type": "model_type_example",
            "name": "name_example",
            "description": "description_example",
            "object_status": 56,
            "object_version": 56,
            "identifier": "identifier_example",
            "external_key": "external_key_example",
            "asset_properties": {},
            "properties": {},
            "type": "type_example",
            "native_type_system": {
                "key": "key_example",
                "model_type": "model_type_example",
                "model_version": "model_version_example",
                "parent_ref": {
                    "parent": "parent_example"
                },
                "name": "name_example",
                "description": "description_example",
                "object_version": 56,
                "type_mapping_to": {},
                "type_mapping_from": {},
                "object_status": 56,
                "identifier": "identifier_example",
                "types": [{
                    "model_type": "STRUCTURED_TYPE",
                    "key": "key_example",
                    "model_version": "model_version_example",
                    "parent_ref": {
                        "parent": "parent_example"
                    },
                    "name": "name_example",
                    "object_status": 56,
                    "description": "description_example",
                    "dt_type": "PRIMITIVE",
                    "type_system_name": "type_system_name_example",
                    "config_definition": {
                        "key": "key_example",
                        "model_type": "model_type_example",
                        "model_version": "model_version_example",
                        "parent_ref": {
                            "parent": "parent_example"
                        },
                        "name": "name_example",
                        "is_contained": true,
                        "object_status": 56,
                        "config_parameter_definitions": {
                            "parameter_type": {
                                "parent_type": {
                                    "model_type": "STRUCTURED_TYPE",
                                    "key": "key_example",
                                    "model_version": "model_version_example",
                                    "parent_ref": null,
                                    "name": "name_example",
                                    "object_status": 56,
                                    "description": "description_example",
                                    "parent_type": null,
                                    "elements": [],
                                    "config_definition": null
                                },
                                "elements": [{
                                    "position": 56,
                                    "default_value_string": "default_value_string_example",
                                    "is_mandatory": true,
                                    "port_type": "DATA",
                                    "fields": [{
                                        "model_type": "SHAPE",
                                        "key": "key_example",
                                        "model_version": "model_version_example",
                                        "parent_ref": null,
                                        "config_values": null,
                                        "object_status": 56,
                                        "name": "name_example",
                                        "description": "description_example"
                                    }],
                                    "default_value": {},
                                    "root_object_default_value": {},
                                    "is_input": true,
                                    "is_output": true,
                                    "output_aggregation_type": "MIN",
                                    "type_name": "type_name_example",
                                    "model_type": "SHAPE",
                                    "key": "key_example",
                                    "model_version": "model_version_example",
                                    "parent_ref": {
                                        "parent": "parent_example"
                                    },
                                    "config_values": {
                                        "config_param_values": {
                                            "string_value": "string_value_example",
                                            "int_value": 56,
                                            "object_value": {},
                                            "ref_value": {},
                                            "parameter_value": "parameter_value_example"
                                        },
                                        "parent_ref": {
                                            "parent": "parent_example"
                                        }
                                    },
                                    "object_status": 56,
                                    "name": "name_example",
                                    "description": "description_example",
                                    "type": {},
                                    "labels": [],
                                    "native_shape_field": {
                                        "model_type": "SHAPE",
                                        "key": "key_example",
                                        "model_version": "model_version_example",
                                        "parent_ref": {
                                            "parent": "parent_example"
                                        },
                                        "config_values": {
                                            "config_param_values": {
                                                "string_value": "string_value_example",
                                                "int_value": 56,
                                                "object_value": {},
                                                "ref_value": {},
                                                "parameter_value": "parameter_value_example"
                                            },
                                            "parent_ref": {
                                                "parent": "parent_example"
                                            }
                                        },
                                        "object_status": 56,
                                        "name": "name_example",
                                        "description": "description_example",
                                        "type": {},
                                        "position": 56,
                                        "default_value_string": "default_value_string_example",
                                        "is_mandatory": true
                                    }
                                }],
                                "wrapped_type": {
                                    "model_type": "STRUCTURED_TYPE",
                                    "key": "key_example",
                                    "model_version": "model_version_example",
                                    "parent_ref": null,
                                    "name": "name_example",
                                    "object_status": 56,
                                    "description": "description_example"
                                },
                                "config_values": {
                                    "config_param_values": {
                                        "string_value": "string_value_example",
                                        "int_value": 56,
                                        "object_value": {},
                                        "ref_value": {},
                                        "parameter_value": "parameter_value_example"
                                    },
                                    "parent_ref": {
                                        "parent": "parent_example"
                                    }
                                },
                                "dt_type": "PRIMITIVE",
                                "type_system_name": "type_system_name_example",
                                "config_definition": {
                                    "key": "key_example",
                                    "model_type": "model_type_example",
                                    "model_version": "model_version_example",
                                    "parent_ref": null,
                                    "name": "name_example",
                                    "is_contained": true,
                                    "object_status": 56,
                                    "config_parameter_definitions": {}
                                },
                                "model_type": "STRUCTURED_TYPE",
                                "key": "key_example",
                                "model_version": "model_version_example",
                                "parent_ref": {
                                    "parent": "parent_example"
                                },
                                "name": "name_example",
                                "object_status": 56,
                                "description": "description_example",
                                "schema": {
                                    "model_type": "STRUCTURED_TYPE",
                                    "key": "key_example",
                                    "model_version": "model_version_example",
                                    "parent_ref": null,
                                    "name": "name_example",
                                    "object_status": 56,
                                    "description": "description_example"
                                }
                            },
                            "parameter_name": "parameter_name_example",
                            "description": "description_example",
                            "default_value": {},
                            "class_field_name": "class_field_name_example",
                            "is_static": true,
                            "is_class_field_value": true
                        }
                    }
                }]
            },
            "registry_metadata": {
                "aggregator_key": "aggregator_key_example",
                "labels": [],
                "registry_version": 56,
                "key": "key_example",
                "is_favorite": true,
                "created_by_user_id": "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx",
                "created_by_user_name": "created_by_user_name_example",
                "updated_by_user_id": "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx",
                "updated_by_user_name": "updated_by_user_name_example",
                "time_created": "2013-10-20T19:20:30+01:00",
                "time_updated": "2013-10-20T19:20:30+01:00"
            },
            "metadata": {
                "created_by": "created_by_example",
                "created_by_name": "created_by_name_example",
                "updated_by": "updated_by_example",
                "updated_by_name": "updated_by_name_example",
                "time_created": "2013-10-20T19:20:30+01:00",
                "time_updated": "2013-10-20T19:20:30+01:00",
                "aggregator_key": "aggregator_key_example",
                "aggregator": {
                    "type": "type_example",
                    "key": "key_example",
                    "name": "name_example",
                    "identifier": "identifier_example",
                    "description": "description_example"
                },
                "identifier_path": "identifier_path_example",
                "info_fields": {},
                "registry_version": 56,
                "labels": [],
                "is_favorite": true
            },
            "default_connection": {
                "key": "key_example",
                "model_version": "model_version_example",
                "model_type": "model_type_example",
                "name": "name_example",
                "description": "description_example",
                "object_version": 56,
                "object_status": 56,
                "identifier": "identifier_example",
                "primary_schema": {
                    "key": "key_example",
                    "model_type": "model_type_example",
                    "model_version": "model_version_example",
                    "parent_ref": {
                        "parent": "parent_example"
                    },
                    "name": "name_example",
                    "resource_name": "resource_name_example",
                    "description": "description_example",
                    "object_version": 56,
                    "external_key": "external_key_example",
                    "is_has_containers": true,
                    "default_connection": "default_connection_example",
                    "object_status": 56,
                    "identifier": "identifier_example",
                    "metadata": {
                        "created_by": "created_by_example",
                        "created_by_name": "created_by_name_example",
                        "updated_by": "updated_by_example",
                        "updated_by_name": "updated_by_name_example",
                        "time_created": "2013-10-20T19:20:30+01:00",
                        "time_updated": "2013-10-20T19:20:30+01:00",
                        "aggregator_key": "aggregator_key_example",
                        "aggregator": {
                            "type": "type_example",
                            "key": "key_example",
                            "name": "name_example",
                            "identifier": "identifier_example",
                            "description": "description_example"
                        },
                        "identifier_path": "identifier_path_example",
                        "info_fields": {},
                        "registry_version": 56,
                        "labels": [],
                        "is_favorite": true
                    }
                },
                "connection_properties": [{
                    "name": "name_example",
                    "value": "value_example"
                }],
                "properties": {},
                "type": "type_example",
                "is_default": true,
                "metadata": {
                    "created_by": "created_by_example",
                    "created_by_name": "created_by_name_example",
                    "updated_by": "updated_by_example",
                    "updated_by_name": "updated_by_name_example",
                    "time_created": "2013-10-20T19:20:30+01:00",
                    "time_updated": "2013-10-20T19:20:30+01:00",
                    "aggregator_key": "aggregator_key_example",
                    "aggregator": {
                        "type": "type_example",
                        "key": "key_example",
                        "name": "name_example",
                        "identifier": "identifier_example",
                        "description": "description_example"
                    },
                    "identifier_path": "identifier_path_example",
                    "info_fields": {},
                    "registry_version": 56,
                    "labels": [],
                    "is_favorite": true
                },
                "registry_metadata": {
                    "aggregator_key": "aggregator_key_example",
                    "labels": [],
                    "registry_version": 56,
                    "key": "key_example",
                    "is_favorite": true,
                    "created_by_user_id": "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx",
                    "created_by_user_name": "created_by_user_name_example",
                    "updated_by_user_id": "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx",
                    "updated_by_user_name": "updated_by_user_name_example",
                    "time_created": "2013-10-20T19:20:30+01:00",
                    "time_updated": "2013-10-20T19:20:30+01:00"
                }
            },
            "end_points": [{
                "dcms_endpoint_id": "ocid1.dcmsendpoint.oc1..xxxxxxEXAMPLExxxxxx",
                "pe_id": "ocid1.pe.oc1..xxxxxxEXAMPLExxxxxx",
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "dns_proxy_ip": "dns_proxy_ip_example",
                "private_endpoint_ip": "private_endpoint_ip_example",
                "dns_zones": [],
                "state": "ACTIVE",
                "model_type": "PRIVATE_END_POINT",
                "key": "key_example",
                "model_version": "model_version_example",
                "parent_ref": {
                    "parent": "parent_example"
                },
                "name": "name_example",
                "description": "description_example",
                "object_version": 56,
                "object_status": 56,
                "identifier": "identifier_example",
                "data_assets": [{
                    "key": "key_example",
                    "model_version": "model_version_example",
                    "model_type": "model_type_example",
                    "name": "name_example",
                    "description": "description_example",
                    "object_status": 56,
                    "object_version": 56,
                    "identifier": "identifier_example",
                    "external_key": "external_key_example",
                    "asset_properties": {},
                    "properties": {},
                    "type": "type_example",
                    "native_type_system": null,
                    "registry_metadata": null,
                    "metadata": null,
                    "default_connection": null,
                    "end_points": []
                }]
            }]
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient
    from oci.data_connectivity.models import CreateFolderDetails
    from oci.data_connectivity.models import UpdateFolderDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FolderHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(FolderHelperGen, self).get_possible_entity_types() + [
            "folder",
            "folders",
            "dataConnectivityfolder",
            "dataConnectivityfolders",
            "folderresource",
            "foldersresource",
            "dataconnectivity",
        ]

    def get_module_resource_id_param(self):
        return "folder_key"

    def get_module_resource_id(self):
        return self.module.params.get("folder_key")

    def get_get_fn(self):
        return self.client.get_folder

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_folder,
            folder_key=summary_model.key,
            registry_id=self.module.params.get("registry_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_folder,
            registry_id=self.module.params.get("registry_id"),
            folder_key=self.module.params.get("folder_key"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "registry_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_folders, **kwargs)

    def get_create_model_class(self):
        return CreateFolderDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_folder,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                create_folder_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateFolderDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_folder,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                folder_key=self.module.params.get("folder_key"),
                update_folder_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_folder,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                folder_key=self.module.params.get("folder_key"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


FolderHelperCustom = get_custom_class("FolderHelperCustom")


class ResourceHelper(FolderHelperCustom, FolderHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            model_type=dict(type="str"),
            key=dict(type="str", no_log=True),
            model_version=dict(type="str"),
            parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
            name=dict(type="str"),
            description=dict(type="str"),
            object_status=dict(type="int"),
            object_version=dict(type="int"),
            identifier=dict(type="str"),
            data_assets=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", required=True, no_log=True),
                    model_version=dict(type="str"),
                    model_type=dict(type="str"),
                    name=dict(type="str", required=True),
                    description=dict(type="str"),
                    object_status=dict(type="int"),
                    object_version=dict(type="int"),
                    identifier=dict(type="str", required=True),
                    external_key=dict(type="str", no_log=True),
                    asset_properties=dict(type="dict"),
                    properties=dict(type="dict"),
                    type=dict(type="str"),
                    native_type_system=dict(
                        type="dict",
                        options=dict(
                            key=dict(type="str", no_log=True),
                            model_type=dict(type="str"),
                            model_version=dict(type="str"),
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
                            ),
                            name=dict(type="str"),
                            description=dict(type="str"),
                            object_version=dict(type="int"),
                            type_mapping_to=dict(type="dict"),
                            type_mapping_from=dict(type="dict"),
                            object_status=dict(type="int"),
                            identifier=dict(type="str"),
                            types=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "STRUCTURED_TYPE",
                                            "DATA_TYPE",
                                            "CONFIGURED_TYPE",
                                            "COMPOSITE_TYPE",
                                            "DERIVED_TYPE",
                                        ],
                                    ),
                                    key=dict(type="str", no_log=True),
                                    model_version=dict(type="str"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
                                    ),
                                    name=dict(type="str"),
                                    object_status=dict(type="int"),
                                    description=dict(type="str"),
                                    dt_type=dict(
                                        type="str", choices=["PRIMITIVE", "STRUCTURED"]
                                    ),
                                    type_system_name=dict(type="str"),
                                    config_definition=dict(
                                        type="dict",
                                        options=dict(
                                            key=dict(type="str", no_log=True),
                                            model_type=dict(type="str"),
                                            model_version=dict(type="str"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                            name=dict(type="str"),
                                            is_contained=dict(type="bool"),
                                            object_status=dict(type="int"),
                                            config_parameter_definitions=dict(
                                                type="dict"
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    registry_metadata=dict(
                        type="dict",
                        options=dict(
                            aggregator_key=dict(type="str", no_log=True),
                            labels=dict(type="list", elements="str"),
                            registry_version=dict(type="int"),
                            key=dict(type="str", no_log=True),
                            is_favorite=dict(type="bool"),
                            created_by_user_id=dict(type="str"),
                            created_by_user_name=dict(type="str"),
                            updated_by_user_id=dict(type="str"),
                            updated_by_user_name=dict(type="str"),
                            time_created=dict(type="str"),
                            time_updated=dict(type="str"),
                        ),
                    ),
                    metadata=dict(
                        type="dict",
                        options=dict(
                            created_by=dict(type="str"),
                            created_by_name=dict(type="str"),
                            updated_by=dict(type="str"),
                            updated_by_name=dict(type="str"),
                            time_created=dict(type="str"),
                            time_updated=dict(type="str"),
                            aggregator_key=dict(type="str", no_log=True),
                            aggregator=dict(
                                type="dict",
                                options=dict(
                                    type=dict(type="str"),
                                    key=dict(type="str", no_log=True),
                                    name=dict(type="str"),
                                    identifier=dict(type="str"),
                                    description=dict(type="str"),
                                ),
                            ),
                            identifier_path=dict(type="str"),
                            info_fields=dict(type="dict"),
                            registry_version=dict(type="int"),
                            labels=dict(type="list", elements="str"),
                            is_favorite=dict(type="bool"),
                        ),
                    ),
                    default_connection=dict(
                        type="dict",
                        options=dict(
                            key=dict(type="str", required=True, no_log=True),
                            model_version=dict(type="str"),
                            model_type=dict(type="str"),
                            name=dict(type="str", required=True),
                            description=dict(type="str"),
                            object_version=dict(type="int"),
                            object_status=dict(type="int"),
                            identifier=dict(type="str", required=True),
                            primary_schema=dict(
                                type="dict",
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    model_type=dict(type="str", required=True),
                                    model_version=dict(type="str"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
                                    ),
                                    name=dict(type="str", required=True),
                                    resource_name=dict(type="str"),
                                    description=dict(type="str"),
                                    object_version=dict(type="int"),
                                    external_key=dict(type="str", no_log=True),
                                    is_has_containers=dict(type="bool"),
                                    default_connection=dict(type="str"),
                                    object_status=dict(type="int"),
                                    identifier=dict(type="str", required=True),
                                    metadata=dict(
                                        type="dict",
                                        options=dict(
                                            created_by=dict(type="str"),
                                            created_by_name=dict(type="str"),
                                            updated_by=dict(type="str"),
                                            updated_by_name=dict(type="str"),
                                            time_created=dict(type="str"),
                                            time_updated=dict(type="str"),
                                            aggregator_key=dict(
                                                type="str", no_log=True
                                            ),
                                            aggregator=dict(
                                                type="dict",
                                                options=dict(
                                                    type=dict(type="str"),
                                                    key=dict(type="str", no_log=True),
                                                    name=dict(type="str"),
                                                    identifier=dict(type="str"),
                                                    description=dict(type="str"),
                                                ),
                                            ),
                                            identifier_path=dict(type="str"),
                                            info_fields=dict(type="dict"),
                                            registry_version=dict(type="int"),
                                            labels=dict(type="list", elements="str"),
                                            is_favorite=dict(type="bool"),
                                        ),
                                    ),
                                ),
                            ),
                            connection_properties=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    name=dict(type="str"), value=dict(type="str")
                                ),
                            ),
                            properties=dict(type="dict"),
                            type=dict(type="str"),
                            is_default=dict(type="bool"),
                            metadata=dict(
                                type="dict",
                                options=dict(
                                    created_by=dict(type="str"),
                                    created_by_name=dict(type="str"),
                                    updated_by=dict(type="str"),
                                    updated_by_name=dict(type="str"),
                                    time_created=dict(type="str"),
                                    time_updated=dict(type="str"),
                                    aggregator_key=dict(type="str", no_log=True),
                                    aggregator=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(type="str"),
                                            key=dict(type="str", no_log=True),
                                            name=dict(type="str"),
                                            identifier=dict(type="str"),
                                            description=dict(type="str"),
                                        ),
                                    ),
                                    identifier_path=dict(type="str"),
                                    info_fields=dict(type="dict"),
                                    registry_version=dict(type="int"),
                                    labels=dict(type="list", elements="str"),
                                    is_favorite=dict(type="bool"),
                                ),
                            ),
                            registry_metadata=dict(
                                type="dict",
                                options=dict(
                                    aggregator_key=dict(type="str", no_log=True),
                                    labels=dict(type="list", elements="str"),
                                    registry_version=dict(type="int"),
                                    key=dict(type="str", no_log=True),
                                    is_favorite=dict(type="bool"),
                                    created_by_user_id=dict(type="str"),
                                    created_by_user_name=dict(type="str"),
                                    updated_by_user_id=dict(type="str"),
                                    updated_by_user_name=dict(type="str"),
                                    time_created=dict(type="str"),
                                    time_updated=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    end_points=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            dcms_endpoint_id=dict(type="str"),
                            pe_id=dict(type="str"),
                            compartment_id=dict(type="str"),
                            dns_proxy_ip=dict(type="str"),
                            private_endpoint_ip=dict(type="str"),
                            dns_zones=dict(type="list", elements="str"),
                            state=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
                            model_type=dict(
                                type="str",
                                required=True,
                                choices=["PRIVATE_END_POINT", "PUBLIC_END_POINT"],
                            ),
                            key=dict(type="str", no_log=True),
                            model_version=dict(type="str"),
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
                            ),
                            name=dict(type="str"),
                            description=dict(type="str"),
                            object_version=dict(type="int"),
                            object_status=dict(type="int"),
                            identifier=dict(type="str"),
                            data_assets=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    model_version=dict(type="str"),
                                    model_type=dict(type="str"),
                                    name=dict(type="str", required=True),
                                    description=dict(type="str"),
                                    object_status=dict(type="int"),
                                    object_version=dict(type="int"),
                                    identifier=dict(type="str", required=True),
                                    external_key=dict(type="str", no_log=True),
                                    asset_properties=dict(type="dict"),
                                    properties=dict(type="dict"),
                                    type=dict(type="str"),
                                    native_type_system=dict(type="TypeSystem"),
                                    registry_metadata=dict(type="RegistryMetadata"),
                                    metadata=dict(type="ObjectMetadata"),
                                    default_connection=dict(type="Connection"),
                                    end_points=dict(type="list", elements="dict"),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            registry_id=dict(type="str", required=True),
            folder_key=dict(type="str", no_log=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="folder",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
