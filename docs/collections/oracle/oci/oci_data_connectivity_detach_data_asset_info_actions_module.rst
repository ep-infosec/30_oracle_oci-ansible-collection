.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na

.. Anchors

.. _ansible_collections.oracle.oci.oci_data_connectivity_detach_data_asset_info_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_data_connectivity_detach_data_asset_info_actions -- Perform actions on a DetachDataAssetInfo resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.4.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_data_connectivity_detach_data_asset_info_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on a DetachDataAssetInfo resource in Oracle Cloud Infrastructure
- For *action=create_detach_data_asset*, detaches a list of data assets to the given endpoint.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 3.6
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="11">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>create_detach_data_asset</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the DetachDataAssetInfo.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-api_user"></div>
                    <b>api_user</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_ID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user&#x27;s OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_fingerprint"></div>
                    <b>api_user_fingerprint</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_fingerprint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair&#x27;s fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_key_file"></div>
                    <b>api_user_key_file</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_key_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_key_pass_phrase"></div>
                    <b>api_user_key_pass_phrase</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_key_pass_phrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-auth_purpose"></div>
                    <b>auth_purpose</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_purpose" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>service_principal</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The auth purpose which can be used in conjunction with &#x27;auth_type=instance_principal&#x27;. The default auth_purpose for instance_principal is None.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-auth_type"></div>
                    <b>auth_type</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                                                                                                                                <li>instance_obo_user</li>
                                                                                                                                                                                                <li>resource_principal</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-cert_bundle"></div>
                    <b>cert_bundle</b>
                    <a class="ansibleOptionLink" href="#parameter-cert_bundle" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The full path to a CA certificate bundle to be used for SSL verification. This will override the default CA certificate bundle. If not set, then the value of the OCI_ANSIBLE_CERT_BUNDLE variable, if any, is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-config_file_location"></div>
                    <b>config_file_location</b>
                    <a class="ansibleOptionLink" href="#parameter-config_file_location" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-config_profile_name"></div>
                    <b>config_profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-config_profile_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets"></div>
                    <b>data_assets</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The array of DataAsset keys.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/asset_properties"></div>
                    <b>asset_properties</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/asset_properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Additional properties for the data asset.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection"></div>
                    <b>default_connection</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/connection_properties"></div>
                    <b>connection_properties</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/connection_properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The properties of the connection.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/connection_properties/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/connection_properties/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/connection_properties/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/connection_properties/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The value for the connection name property.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User-defined description for the connection.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/is_default"></div>
                    <b>is_default</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/is_default" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The default property of the connection.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is required, a value can be passed in create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata"></div>
                    <b>metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/aggregator"></div>
                    <b>aggregator</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/aggregator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/aggregator/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/aggregator/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The description of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/aggregator/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/aggregator/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The identifier of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/aggregator/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/aggregator/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the aggregator object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/aggregator/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/aggregator/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/aggregator/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/aggregator/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the aggregator.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/aggregator_key"></div>
                    <b>aggregator_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/aggregator_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The owning object key for this object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/created_by"></div>
                    <b>created_by</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/created_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/created_by_name"></div>
                    <b>created_by_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/created_by_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/identifier_path"></div>
                    <b>identifier_path</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/identifier_path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The full path to identify the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/info_fields"></div>
                    <b>info_fields</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/info_fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Information property fields.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/is_favorite"></div>
                    <b>is_favorite</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/is_favorite" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether this object is a favorite.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/registry_version"></div>
                    <b>registry_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/registry_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The registry version of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/time_created" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/time_updated" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was updated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/updated_by"></div>
                    <b>updated_by</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/updated_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that updated the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/metadata/updated_by_name"></div>
                    <b>updated_by_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/metadata/updated_by_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that updated the object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/object_version"></div>
                    <b>object_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/object_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The version of the object that is used to track changes in the object instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema"></div>
                    <b>primary_schema</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/default_connection"></div>
                    <b>default_connection</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/default_connection" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default connection key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User-defined description for the schema.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/external_key"></div>
                    <b>external_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/external_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The external key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/is_has_containers"></div>
                    <b>is_has_containers</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/is_has_containers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the schema has containers.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata"></div>
                    <b>metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/aggregator"></div>
                    <b>aggregator</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/aggregator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/aggregator/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/aggregator/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The description of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/aggregator/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/aggregator/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The identifier of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/aggregator/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/aggregator/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the aggregator object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/aggregator/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/aggregator/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/aggregator/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/aggregator/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the aggregator.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/aggregator_key"></div>
                    <b>aggregator_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/aggregator_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The owning object key for this object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/created_by"></div>
                    <b>created_by</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/created_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/created_by_name"></div>
                    <b>created_by_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/created_by_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/identifier_path"></div>
                    <b>identifier_path</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/identifier_path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The full path to identify the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/info_fields"></div>
                    <b>info_fields</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/info_fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Information property fields.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/is_favorite"></div>
                    <b>is_favorite</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/is_favorite" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether this object is a favorite.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/registry_version"></div>
                    <b>registry_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/registry_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The registry version of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/time_created" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/time_updated" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was updated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/updated_by"></div>
                    <b>updated_by</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/updated_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that updated the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/metadata/updated_by_name"></div>
                    <b>updated_by_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/metadata/updated_by_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that updated the object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/object_version"></div>
                    <b>object_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/object_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The version of the object that is used to track changes in the object instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/primary_schema/resource_name"></div>
                    <b>resource_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/primary_schema/resource_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000 characters.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/properties"></div>
                    <b>properties</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>All the properties of the connection in a key-value map format.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata"></div>
                    <b>registry_metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/aggregator_key"></div>
                    <b>aggregator_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/aggregator_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The owning object&#x27;s key for this object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/created_by_user_id"></div>
                    <b>created_by_user_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/created_by_user_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ID of the user who created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/created_by_user_name"></div>
                    <b>created_by_user_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/created_by_user_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the user who created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/is_favorite"></div>
                    <b>is_favorite</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/is_favorite" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the object is a favorite.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The identifying key for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/registry_version"></div>
                    <b>registry_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/registry_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The registry version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/time_created" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/time_updated" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was updated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/updated_by_user_id"></div>
                    <b>updated_by_user_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/updated_by_user_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ID of the user who updated the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/registry_metadata/updated_by_user_name"></div>
                    <b>updated_by_user_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/registry_metadata/updated_by_user_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the user who updated the object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/default_connection/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/default_connection/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specific Connection Type</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User-defined description of the data asset.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points"></div>
                    <b>end_points</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of endpoints with which this data asset is associated.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The compartmentId of the private endpoint resource.</div>
                                            <div>Applicable when model_type is &#x27;PRIVATE_END_POINT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets"></div>
                    <b>data_assets</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of data assets that belong to the endpoint.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/asset_properties"></div>
                    <b>asset_properties</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/asset_properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Additional properties for the data asset.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/default_connection"></div>
                    <b>default_connection</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/default_connection" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User-defined description of the data asset.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/end_points"></div>
                    <b>end_points</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/end_points" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of endpoints with which this data asset is associated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/external_key"></div>
                    <b>external_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/external_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The external key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Currently not used while creating a data asset. Reserved for future.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/metadata"></div>
                    <b>metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/native_type_system"></div>
                    <b>native_type_system</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/native_type_system" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/object_version"></div>
                    <b>object_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/object_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The version of the object that is used to track changes in the object instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/properties"></div>
                    <b>properties</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>All the properties for the data asset in a key-value map format.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/registry_metadata"></div>
                    <b>registry_metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/registry_metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/data_assets/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/data_assets/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specific DataAsset Type</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/dcms_endpoint_id"></div>
                    <b>dcms_endpoint_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/dcms_endpoint_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The endpoint ID provided by control plane.</div>
                                            <div>Required when model_type is &#x27;PRIVATE_END_POINT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User-defined description of the endpoint.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/dns_proxy_ip"></div>
                    <b>dns_proxy_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/dns_proxy_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IP address of the DNS proxy.</div>
                                            <div>Applicable when model_type is &#x27;PRIVATE_END_POINT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/dns_zones"></div>
                    <b>dns_zones</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/dns_zones" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Array of DNS zones to be used during the private endpoint resolution.</div>
                                            <div>Applicable when model_type is &#x27;PRIVATE_END_POINT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Generated key that can be used in API calls to identify the endpoint. In scenarios where reference to the endpoint is required, a value can be passed in create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PRIVATE_END_POINT</li>
                                                                                                                                                                                                <li>PUBLIC_END_POINT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the endpoint.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/object_version"></div>
                    <b>object_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/object_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The version of the object that is used to track changes in the object instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;PRIVATE_END_POINT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/pe_id"></div>
                    <b>pe_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/pe_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the private endpoint resource.</div>
                                            <div>Applicable when model_type is &#x27;PRIVATE_END_POINT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/private_endpoint_ip"></div>
                    <b>private_endpoint_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/private_endpoint_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the private endpoint resource.</div>
                                            <div>Applicable when model_type is &#x27;PRIVATE_END_POINT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/end_points/state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/end_points/state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ACTIVE</li>
                                                                                                                                                                                                <li>INACTIVE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies the private endpoint state.</div>
                                            <div>Applicable when model_type is &#x27;PRIVATE_END_POINT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/external_key"></div>
                    <b>external_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/external_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The external key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Currently not used while creating a data asset. Reserved for future.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata"></div>
                    <b>metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/aggregator"></div>
                    <b>aggregator</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/aggregator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/aggregator/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/aggregator/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The description of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/aggregator/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/aggregator/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The identifier of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/aggregator/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/aggregator/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the aggregator object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/aggregator/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/aggregator/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the aggregator.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/aggregator/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/aggregator/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the aggregator.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/aggregator_key"></div>
                    <b>aggregator_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/aggregator_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The owning object key for this object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/created_by"></div>
                    <b>created_by</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/created_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/created_by_name"></div>
                    <b>created_by_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/created_by_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/identifier_path"></div>
                    <b>identifier_path</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/identifier_path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The full path to identify the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/info_fields"></div>
                    <b>info_fields</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/info_fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Information property fields.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/is_favorite"></div>
                    <b>is_favorite</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/is_favorite" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether this object is a favorite.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/registry_version"></div>
                    <b>registry_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/registry_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The registry version of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/time_created" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/time_updated" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was updated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/updated_by"></div>
                    <b>updated_by</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/updated_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that updated the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/metadata/updated_by_name"></div>
                    <b>updated_by_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/metadata/updated_by_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user that updated the object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system"></div>
                    <b>native_type_system</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/object_version"></div>
                    <b>object_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/object_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The version of the object that is used to track changes in the object instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/type_mapping_from"></div>
                    <b>type_mapping_from</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/type_mapping_from" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type system to map from.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/type_mapping_to"></div>
                    <b>type_mapping_to</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/type_mapping_to" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type system to map to.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types"></div>
                    <b>types</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of types.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition"></div>
                    <b>config_definition</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions"></div>
                    <b>config_parameter_definitions</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The parameter configuration details.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/class_field_name"></div>
                    <b>class_field_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/class_field_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The parameter class field name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/default_value"></div>
                    <b>default_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/default_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value for the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/is_class_field_value"></div>
                    <b>is_class_field_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/is_class_field_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the parameter is a class field.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/is_static"></div>
                    <b>is_static</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/is_static" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the parameter is static.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_name"></div>
                    <b>parameter_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This object represents the configurable properties for an object type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type"></div>
                    <b>parameter_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition"></div>
                    <b>config_definition</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is one of [&#x27;DATA_TYPE&#x27;, &#x27;CONFIGURED_TYPE&#x27;, &#x27;COMPOSITE_TYPE&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/config_parameter_definitions"></div>
                    <b>config_parameter_definitions</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/config_parameter_definitions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The parameter configuration details.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/is_contained"></div>
                    <b>is_contained</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/is_contained" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the configuration is contained.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_definition/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/dt_type"></div>
                    <b>dt_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/dt_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PRIMITIVE</li>
                                                                                                                                                                                                <li>STRUCTURED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The data type.</div>
                                            <div>Applicable when model_type is &#x27;DATA_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements"></div>
                    <b>elements</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of elements.</div>
                                            <div>Applicable when model_type is &#x27;COMPOSITE_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/default_value"></div>
                    <b>default_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/default_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/default_value_string"></div>
                    <b>default_value_string</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/default_value_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value.</div>
                                            <div>Applicable when model_type is &#x27;NATIVE_SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A detailed description of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields"></div>
                    <b>fields</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of fields.</div>
                                            <div>Applicable when model_type is one of [&#x27;INPUT_PORT&#x27;, &#x27;OUTPUT_PORT&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A detailed description of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/fields/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/is_input"></div>
                    <b>is_input</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/is_input" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the parameter is an input value.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/is_mandatory"></div>
                    <b>is_mandatory</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/is_mandatory" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the field is mandatory.</div>
                                            <div>Applicable when model_type is &#x27;NATIVE_SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/is_output"></div>
                    <b>is_output</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/is_output" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the parameter is an output value.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OUTPUT_PORT</li>
                                                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>INPUT_PORT</li>
                                                                                                                                                                                                <li>PARAMETER</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field"></div>
                    <b>native_shape_field</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/default_value_string"></div>
                    <b>default_value_string</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/default_value_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A detailed description of the object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/is_mandatory"></div>
                    <b>is_mandatory</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/is_mandatory" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the field is mandatory.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                            <div>Required when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/native_shape_field/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type reference.</div>
                                            <div>Required when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/output_aggregation_type"></div>
                    <b>output_aggregation_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/output_aggregation_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>MIN</li>
                                                                                                                                                                                                <li>MAX</li>
                                                                                                                                                                                                <li>COUNT</li>
                                                                                                                                                                                                <li>SUM</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The output aggregation type.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/port_type"></div>
                    <b>port_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/port_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DATA</li>
                                                                                                                                                                                                <li>CONTROL</li>
                                                                                                                                                                                                <li>MODEL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The port details of the data asset type.</div>
                                            <div>Applicable when model_type is one of [&#x27;INPUT_PORT&#x27;, &#x27;OUTPUT_PORT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                            <div>Applicable when model_type is &#x27;NATIVE_SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/root_object_default_value"></div>
                    <b>root_object_default_value</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/root_object_default_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value of the parameter, which can be an object in DIS, such as a data entity.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is one of [&#x27;SHAPE&#x27;, &#x27;SHAPE_FIELD&#x27;, &#x27;PARAMETER&#x27;]</div>
                                            <div>Required when model_type is &#x27;NATIVE_SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which differentiates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type_name"></div>
                    <b>type_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/elements/type_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of value the parameter was created for.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which differentiates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type"></div>
                    <b>parent_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;COMPOSITE_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/config_definition"></div>
                    <b>config_definition</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/config_definition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/elements"></div>
                    <b>elements</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/elements" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of elements.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which differentiates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/parent_type"></div>
                    <b>parent_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/parent_type/parent_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema"></div>
                    <b>schema</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;STRUCTURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which differentiates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/schema/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/type_system_name"></div>
                    <b>type_system_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/type_system_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The data type system name.</div>
                                            <div>Applicable when model_type is &#x27;DATA_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type"></div>
                    <b>wrapped_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which differentiates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/config_parameter_definitions/parameter_type/wrapped_type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/is_contained"></div>
                    <b>is_contained</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/is_contained" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the configuration is contained.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/config_definition/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/config_definition/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/dt_type"></div>
                    <b>dt_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/dt_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PRIMITIVE</li>
                                                                                                                                                                                                <li>STRUCTURED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The data type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which differentiates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/native_type_system/types/type_system_name"></div>
                    <b>type_system_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/native_type_system/types/type_system_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The data type system name.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/object_version"></div>
                    <b>object_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/object_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The version of the object that is used to track changes in the object instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/properties"></div>
                    <b>properties</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>All the properties for the data asset in a key-value map format.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata"></div>
                    <b>registry_metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/aggregator_key"></div>
                    <b>aggregator_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/aggregator_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The owning object&#x27;s key for this object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/created_by_user_id"></div>
                    <b>created_by_user_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/created_by_user_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ID of the user who created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/created_by_user_name"></div>
                    <b>created_by_user_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/created_by_user_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the user who created the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/is_favorite"></div>
                    <b>is_favorite</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/is_favorite" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the object is a favorite.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The identifying key for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/registry_version"></div>
                    <b>registry_version</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/registry_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The registry version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/time_created" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/time_updated" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date and time that the object was updated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/updated_by_user_id"></div>
                    <b>updated_by_user_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/updated_by_user_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ID of the user who updated the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="9">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/registry_metadata/updated_by_user_name"></div>
                    <b>updated_by_user_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/registry_metadata/updated_by_user_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the user who updated the object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="10">
                    <div class="ansibleOptionAnchor" id="parameter-data_assets/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_assets/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specific DataAsset Type</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-endpoint_id"></div>
                    <b>endpoint_id</b>
                    <a class="ansibleOptionLink" href="#parameter-endpoint_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DCMS endpoint ID.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#parameter-region" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-registry_id"></div>
                    <b>registry_id</b>
                    <a class="ansibleOptionLink" href="#parameter-registry_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The registry OCID.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="11">
                    <div class="ansibleOptionAnchor" id="parameter-tenancy"></div>
                    <b>tenancy</b>
                    <a class="ansibleOptionLink" href="#parameter-tenancy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Attributes


.. Notes

Notes
-----

.. note::
   - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Perform action create_detach_data_asset on detach_data_asset_info
      oci_data_connectivity_detach_data_asset_info_actions:
        # required
        registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"
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
        action: create_detach_data_asset





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-detach_data_asset_info"></div>
                    <b>detach_data_asset_info</b>
                    <a class="ansibleOptionLink" href="#return-detach_data_asset_info" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the DetachDataAssetInfo resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;reference_info&#x27;: {&#x27;error_msg&#x27;: &#x27;error_msg_example&#x27;, &#x27;status&#x27;: &#x27;ERROR&#x27;}}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-detach_data_asset_info/reference_info"></div>
                    <b>reference_info</b>
                    <a class="ansibleOptionLink" href="#return-detach_data_asset_info/reference_info" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Mapping the DataAsset name as the key to the results as the value.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-detach_data_asset_info/reference_info/error_msg"></div>
                    <b>error_msg</b>
                    <a class="ansibleOptionLink" href="#return-detach_data_asset_info/reference_info/error_msg" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Error text for validation failure.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">error_msg_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-detach_data_asset_info/reference_info/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-detach_data_asset_info/reference_info/status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Status of the validation result execution.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ERROR</div>
                                    </td>
            </tr>
                    
                    
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Oracle (@oracle)



.. Parsing errors

