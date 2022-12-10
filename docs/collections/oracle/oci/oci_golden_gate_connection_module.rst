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

.. _ansible_collections.oracle.oci.oci_golden_gate_connection_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_golden_gate_connection -- Manage a Connection resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.4.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_golden_gate_connection`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a Connection resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new Connection.
- This resource has the following action operations in the :ref:`oracle.oci.oci_golden_gate_connection_actions <ansible_collections.oracle.oci.oci_golden_gate_connection_actions_module>` module: change_compartment.


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
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-additional_attributes"></div>
                    <b>additional_attributes</b>
                    <a class="ansibleOptionLink" href="#parameter-additional_attributes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of name-value pair attribute entries. Used as additional parameters in connection string.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-additional_attributes/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-additional_attributes/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the property entry.</div>
                                            <div>Required when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-additional_attributes/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-additional_attributes/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The value of the property entry.</div>
                                            <div>Required when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-bootstrap_servers"></div>
                    <b>bootstrap_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-bootstrap_servers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: `&quot;server1.example.com:9092,server2.example.com:9092&quot;`</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bootstrap_servers/host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-bootstrap_servers/host" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name or address of a host.</div>
                                            <div>Required when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bootstrap_servers/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-bootstrap_servers/port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The port of an endpoint usually specified for a connection.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bootstrap_servers/private_ip"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-bootstrap_servers/private_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The private IP address of the connection&#x27;s endpoint in the customer&#x27;s VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment being referenced.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>Required for delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-connection_id"></div>
                    <b>connection_id</b>
                    <a class="ansibleOptionLink" href="#parameter-connection_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of a Connection.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-connection_string"></div>
                    <b>connection_string</b>
                    <a class="ansibleOptionLink" href="#parameter-connection_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-connection_type"></div>
                    <b>connection_type</b>
                    <a class="ansibleOptionLink" href="#parameter-connection_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>MYSQL</li>
                                                                                                                                                                                                <li>OCI_OBJECT_STORAGE</li>
                                                                                                                                                                                                <li>KAFKA</li>
                                                                                                                                                                                                <li>ORACLE</li>
                                                                                                                                                                                                <li>GOLDENGATE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The connection type.</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with connection_id present.</div>
                                            <div>Applicable when connection_type is one of [&#x27;MYSQL&#x27;, &#x27;OCI_OBJECT_STORAGE&#x27;, &#x27;KAFKA&#x27;, &#x27;GOLDENGATE&#x27;, &#x27;ORACLE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-consumer_properties"></div>
                    <b>consumer_properties</b>
                    <a class="ansibleOptionLink" href="#parameter-consumer_properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The base64 encoded content of the consumer.properties file.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database_id"></div>
                    <b>database_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the database being referenced.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database_name"></div>
                    <b>database_name</b>
                    <a class="ansibleOptionLink" href="#parameter-database_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the database.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;MYSQL&#x27;</div>
                                            <div>Required when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-db_system_id"></div>
                    <b>db_system_id</b>
                    <a class="ansibleOptionLink" href="#parameter-db_system_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the database system being referenced.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Tags defined for this resource. Each key is predefined and scoped to a namespace.</div>
                                            <div>Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deployment_id"></div>
                    <b>deployment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-deployment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the deployment being referenced.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;GOLDENGATE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Metadata about this specific object.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object&#x27;s Display Name.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Applicable when connection_type is one of [&#x27;MYSQL&#x27;, &#x27;OCI_OBJECT_STORAGE&#x27;, &#x27;KAFKA&#x27;, &#x27;GOLDENGATE&#x27;, &#x27;ORACLE&#x27;]</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-force_create"></div>
                    <b>force_create</b>
                    <a class="ansibleOptionLink" href="#parameter-force_create" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn&#x27;t create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.</div>
                                            <div>Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-host" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name or address of a host.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is one of [&#x27;MYSQL&#x27;, &#x27;GOLDENGATE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-key_by"></div>
                    <b>key_by</b>
                    <a class="ansibleOptionLink" href="#parameter-key_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource are used to uniquely identify a resource.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-key_id"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-key_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the customer &quot;Master&quot; key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-key_store"></div>
                    <b>key_store</b>
                    <a class="ansibleOptionLink" href="#parameter-key_store" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The base64 encoded content of the KeyStore file.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-key_store_password"></div>
                    <b>key_store_password</b>
                    <a class="ansibleOptionLink" href="#parameter-key_store_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The KeyStore password.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-nsg_ids"></div>
                    <b>nsg_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-nsg_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when connection_type is one of [&#x27;MYSQL&#x27;, &#x27;ORACLE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The port of an endpoint usually specified for a connection.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is one of [&#x27;MYSQL&#x27;, &#x27;GOLDENGATE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-private_ip"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-private_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The private IP address of the connection&#x27;s endpoint in the customer&#x27;s VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is one of [&#x27;MYSQL&#x27;, &#x27;GOLDENGATE&#x27;, &#x27;ORACLE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-private_key_file"></div>
                    <b>private_key_file</b>
                    <a class="ansibleOptionLink" href="#parameter-private_key_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint. See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;OCI_OBJECT_STORAGE&#x27;</div>
                                            <div>Required when connection_type is &#x27;OCI_OBJECT_STORAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-producer_properties"></div>
                    <b>producer_properties</b>
                    <a class="ansibleOptionLink" href="#parameter-producer_properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The base64 encoded content of the producer.properties file.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-public_key_fingerprint"></div>
                    <b>public_key_fingerprint</b>
                    <a class="ansibleOptionLink" href="#parameter-public_key_fingerprint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The fingerprint of the API Key of the user specified by the userId. See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;OCI_OBJECT_STORAGE&#x27;</div>
                                            <div>Required when connection_type is &#x27;OCI_OBJECT_STORAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                            <div>The name of the region. e.g.: us-ashburn-1</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;OCI_OBJECT_STORAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-security_protocol"></div>
                    <b>security_protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-security_protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Security Type for MySQL.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is one of [&#x27;MYSQL&#x27;, &#x27;KAFKA&#x27;]</div>
                                            <div>Required when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-session_mode"></div>
                    <b>session_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-session_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The mode of the database connection session to be established by the data client. &#x27;REDIRECT&#x27; - for a RAC database, &#x27;DIRECT&#x27; - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_ca"></div>
                    <b>ssl_ca</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_ca" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Database Certificate - The base64 encoded content of mysql.pem file containing the server public key (for 1 and 2-way SSL).</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_cert"></div>
                    <b>ssl_cert</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_cert" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Client Certificate - The base64 encoded content of client-cert.pem file containing the client public key (for 2-way SSL).</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_crl"></div>
                    <b>ssl_crl</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_crl" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Certificates revoked by certificate authorities (CA). Server certificate must not be on this list (for 1 and 2-way SSL). Note: This is an optional and that too only applicable if TLS/MTLS option is selected.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_key"></div>
                    <b>ssl_key</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Client Key - The client-key.pem containing the client private key (for 2-way SSL).</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_key_password"></div>
                    <b>ssl_key_password</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_key_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The password for the cert inside of of the KeyStore. In case it differs from the KeyStore password, it should be provided.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_mode"></div>
                    <b>ssl_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SSL modes for MySQL.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The state of the Connection.</div>
                                            <div>Use <em>state=present</em> to create or update a Connection.</div>
                                            <div>Use <em>state=absent</em> to delete a Connection.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-stream_pool_id"></div>
                    <b>stream_pool_id</b>
                    <a class="ansibleOptionLink" href="#parameter-stream_pool_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the stream pool being referenced.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the subnet being referenced.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-technology_type"></div>
                    <b>technology_type</b>
                    <a class="ansibleOptionLink" href="#parameter-technology_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The MySQL technology type.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-tenancy_id"></div>
                    <b>tenancy_id</b>
                    <a class="ansibleOptionLink" href="#parameter-tenancy_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the related OCI tenancy.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;OCI_OBJECT_STORAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-trust_store"></div>
                    <b>trust_store</b>
                    <a class="ansibleOptionLink" href="#parameter-trust_store" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The base64 encoded content of the TrustStore file.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-trust_store_password"></div>
                    <b>trust_store_password</b>
                    <a class="ansibleOptionLink" href="#parameter-trust_store_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The TrustStore password.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;KAFKA&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-user_id"></div>
                    <b>user_id</b>
                    <a class="ansibleOptionLink" href="#parameter-user_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;OCI_OBJECT_STORAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when connection_type is one of [&#x27;MYSQL&#x27;, &#x27;ORACLE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-vault_id"></div>
                    <b>vault_id</b>
                    <a class="ansibleOptionLink" href="#parameter-vault_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wait"></div>
                    <b>wait</b>
                    <a class="ansibleOptionLink" href="#parameter-wait" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to wait for create or delete operation to complete.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wait_timeout"></div>
                    <b>wait_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-wait_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Time, in seconds, to wait when <em>wait=yes</em>. Defaults to 1200 for most of the services but some services might have a longer wait timeout.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wallet"></div>
                    <b>wallet</b>
                    <a class="ansibleOptionLink" href="#parameter-wallet" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The wallet contents Oracle GoldenGate uses to make connections to a database.  This attribute is expected to be base64 encoded.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when connection_type is &#x27;ORACLE&#x27;</div>
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

    
    - name: Create connection with connection_type = MYSQL
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        technology_type: technology_type_example
        connection_type: MYSQL

        # optional
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        database_name: database_name_example
        ssl_mode: ssl_mode_example
        ssl_ca: ssl_ca_example
        ssl_crl: ssl_crl_example
        ssl_cert: ssl_cert_example
        ssl_key: ssl_key_example
        additional_attributes:
        - # required
          name: name_example
          value: value_example
        db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        security_protocol: security_protocol_example
        username: username_example
        password: example-password
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        host: host_example
        port: 56
        private_ip: private_ip_example

    - name: Create connection with connection_type = OCI_OBJECT_STORAGE
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        technology_type: technology_type_example
        connection_type: OCI_OBJECT_STORAGE

        # optional
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        region: us-phoenix-1
        user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        private_key_file: private_key_file_example
        public_key_fingerprint: public_key_fingerprint_example
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]

    - name: Create connection with connection_type = KAFKA
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        technology_type: technology_type_example
        connection_type: KAFKA

        # optional
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
        bootstrap_servers:
        - # required
          host: host_example

          # optional
          port: 56
          private_ip: private_ip_example
        security_protocol: security_protocol_example
        username: username_example
        password: example-password
        trust_store: trust_store_example
        trust_store_password: example-password
        key_store: key_store_example
        key_store_password: example-password
        ssl_key_password: example-password
        consumer_properties: consumer_properties_example
        producer_properties: producer_properties_example
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]

    - name: Create connection with connection_type = ORACLE
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        technology_type: technology_type_example
        connection_type: ORACLE

        # optional
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        connection_string: connection_string_example
        wallet: wallet_example
        session_mode: session_mode_example
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        username: username_example
        password: example-password
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        private_ip: private_ip_example

    - name: Create connection with connection_type = GOLDENGATE
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        technology_type: technology_type_example
        connection_type: GOLDENGATE

        # optional
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        host: host_example
        port: 56
        private_ip: private_ip_example

    - name: Update connection with connection_type = MYSQL
      oci_golden_gate_connection:
        # required
        connection_type: MYSQL

        # optional
        database_name: database_name_example
        ssl_mode: ssl_mode_example
        ssl_ca: ssl_ca_example
        ssl_crl: ssl_crl_example
        ssl_cert: ssl_cert_example
        ssl_key: ssl_key_example
        additional_attributes:
        - # required
          name: name_example
          value: value_example
        db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        security_protocol: security_protocol_example
        username: username_example
        password: example-password
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        host: host_example
        port: 56
        private_ip: private_ip_example

    - name: Update connection with connection_type = OCI_OBJECT_STORAGE
      oci_golden_gate_connection:
        # required
        connection_type: OCI_OBJECT_STORAGE

        # optional
        tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        region: us-phoenix-1
        user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        private_key_file: private_key_file_example
        public_key_fingerprint: public_key_fingerprint_example
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]

    - name: Update connection with connection_type = KAFKA
      oci_golden_gate_connection:
        # required
        connection_type: KAFKA

        # optional
        stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
        bootstrap_servers:
        - # required
          host: host_example

          # optional
          port: 56
          private_ip: private_ip_example
        security_protocol: security_protocol_example
        username: username_example
        password: example-password
        trust_store: trust_store_example
        trust_store_password: example-password
        key_store: key_store_example
        key_store_password: example-password
        ssl_key_password: example-password
        consumer_properties: consumer_properties_example
        producer_properties: producer_properties_example
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]

    - name: Update connection with connection_type = ORACLE
      oci_golden_gate_connection:
        # required
        connection_type: ORACLE

        # optional
        connection_string: connection_string_example
        wallet: wallet_example
        session_mode: session_mode_example
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        username: username_example
        password: example-password
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        private_ip: private_ip_example

    - name: Update connection with connection_type = GOLDENGATE
      oci_golden_gate_connection:
        # required
        connection_type: GOLDENGATE

        # optional
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        host: host_example
        port: 56
        private_ip: private_ip_example

    - name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = MYSQL
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type: MYSQL

        # optional
        database_name: database_name_example
        ssl_mode: ssl_mode_example
        ssl_ca: ssl_ca_example
        ssl_crl: ssl_crl_example
        ssl_cert: ssl_cert_example
        ssl_key: ssl_key_example
        additional_attributes:
        - # required
          name: name_example
          value: value_example
        db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        security_protocol: security_protocol_example
        username: username_example
        password: example-password
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        host: host_example
        port: 56
        private_ip: private_ip_example

    - name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = OCI_OBJECT_STORAGE
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type: OCI_OBJECT_STORAGE

        # optional
        tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        region: us-phoenix-1
        user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        private_key_file: private_key_file_example
        public_key_fingerprint: public_key_fingerprint_example
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]

    - name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = KAFKA
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type: KAFKA

        # optional
        stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
        bootstrap_servers:
        - # required
          host: host_example

          # optional
          port: 56
          private_ip: private_ip_example
        security_protocol: security_protocol_example
        username: username_example
        password: example-password
        trust_store: trust_store_example
        trust_store_password: example-password
        key_store: key_store_example
        key_store_password: example-password
        ssl_key_password: example-password
        consumer_properties: consumer_properties_example
        producer_properties: producer_properties_example
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]

    - name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = ORACLE
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type: ORACLE

        # optional
        connection_string: connection_string_example
        wallet: wallet_example
        session_mode: session_mode_example
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        username: username_example
        password: example-password
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        private_ip: private_ip_example

    - name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = GOLDENGATE
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type: GOLDENGATE

        # optional
        display_name: display_name_example
        description: description_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids: [ "nsg_ids_example" ]
        deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        host: host_example
        port: 56
        private_ip: private_ip_example

    - name: Delete connection
      oci_golden_gate_connection:
        # required
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

    - name: Delete connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_golden_gate_connection:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        state: absent





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
                    <div class="ansibleOptionAnchor" id="return-connection"></div>
                    <b>connection</b>
                    <a class="ansibleOptionLink" href="#return-connection" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Connection resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;additional_attributes&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}], &#x27;bootstrap_servers&#x27;: [{&#x27;host&#x27;: &#x27;host_example&#x27;, &#x27;port&#x27;: 56, &#x27;private_ip&#x27;: &#x27;private_ip_example&#x27;}], &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;connection_string&#x27;: &#x27;connection_string_example&#x27;, &#x27;connection_type&#x27;: &#x27;GOLDENGATE&#x27;, &#x27;database_id&#x27;: &#x27;ocid1.database.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;database_name&#x27;: &#x27;database_name_example&#x27;, &#x27;db_system_id&#x27;: &#x27;ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;deployment_id&#x27;: &#x27;ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;host&#x27;: &#x27;host_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;ingress_ips&#x27;: [{&#x27;ingress_ip&#x27;: &#x27;ingress_ip_example&#x27;}], &#x27;key_id&#x27;: &#x27;ocid1.key.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;nsg_ids&#x27;: [], &#x27;port&#x27;: 56, &#x27;private_ip&#x27;: &#x27;private_ip_example&#x27;, &#x27;region&#x27;: &#x27;us-phoenix-1&#x27;, &#x27;security_protocol&#x27;: &#x27;SSL&#x27;, &#x27;session_mode&#x27;: &#x27;DIRECT&#x27;, &#x27;ssl_mode&#x27;: &#x27;DISABLED&#x27;, &#x27;stream_pool_id&#x27;: &#x27;ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;subnet_id&#x27;: &#x27;ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;system_tags&#x27;: {}, &#x27;technology_type&#x27;: &#x27;GOLDENGATE&#x27;, &#x27;tenancy_id&#x27;: &#x27;ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;user_id&#x27;: &#x27;ocid1.user.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;username&#x27;: &#x27;username_example&#x27;, &#x27;vault_id&#x27;: &#x27;ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/additional_attributes"></div>
                    <b>additional_attributes</b>
                    <a class="ansibleOptionLink" href="#return-connection/additional_attributes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of name-value pair attribute entries. Used as additional parameters in connection string.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-connection/additional_attributes/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-connection/additional_attributes/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the property entry.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-connection/additional_attributes/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-connection/additional_attributes/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The value of the property entry.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/bootstrap_servers"></div>
                    <b>bootstrap_servers</b>
                    <a class="ansibleOptionLink" href="#return-connection/bootstrap_servers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: `&quot;server1.example.com:9092,server2.example.com:9092&quot;`</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-connection/bootstrap_servers/host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#return-connection/bootstrap_servers/host" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name or address of a host.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">host_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-connection/bootstrap_servers/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-connection/bootstrap_servers/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The port of an endpoint usually specified for a connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-connection/bootstrap_servers/private_ip"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#return-connection/bootstrap_servers/private_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The private IP address of the connection&#x27;s endpoint in the customer&#x27;s VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">private_ip_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/connection_string"></div>
                    <b>connection_string</b>
                    <a class="ansibleOptionLink" href="#return-connection/connection_string" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">connection_string_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/connection_type"></div>
                    <b>connection_type</b>
                    <a class="ansibleOptionLink" href="#return-connection/connection_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The connection type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GOLDENGATE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/database_id"></div>
                    <b>database_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/database_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the database being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.database.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/database_name"></div>
                    <b>database_name</b>
                    <a class="ansibleOptionLink" href="#return-connection/database_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">database_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/db_system_id"></div>
                    <b>db_system_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/db_system_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the database system being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-connection/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Tags defined for this resource. Each key is predefined and scoped to a namespace.</div>
                                            <div>Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/deployment_id"></div>
                    <b>deployment_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/deployment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the deployment being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-connection/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Metadata about this specific object.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-connection/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An object&#x27;s Display Name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-connection/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.</div>
                                            <div>Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#return-connection/host" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name or address of a host.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">host_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-connection/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the connection being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/ingress_ips"></div>
                    <b>ingress_ips</b>
                    <a class="ansibleOptionLink" href="#return-connection/ingress_ips" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of ingress IP addresses, from where the GoldenGate deployment connects to this connection&#x27;s privateIp.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-connection/ingress_ips/ingress_ip"></div>
                    <b>ingress_ip</b>
                    <a class="ansibleOptionLink" href="#return-connection/ingress_ips/ingress_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A Private Endpoint IPv4 or IPv6 Address created in the customer&#x27;s subnet.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ingress_ip_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/key_id"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/key_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the customer &quot;Master&quot; key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.key.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-connection/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Describes the object&#x27;s current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-connection/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Possible lifecycle states for connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/nsg_ids"></div>
                    <b>nsg_ids</b>
                    <a class="ansibleOptionLink" href="#return-connection/nsg_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-connection/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The port of an endpoint usually specified for a connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/private_ip"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#return-connection/private_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The private IP address of the connection&#x27;s endpoint in the customer&#x27;s VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">private_ip_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#return-connection/region" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the region. e.g.: us-ashburn-1</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">us-phoenix-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/security_protocol"></div>
                    <b>security_protocol</b>
                    <a class="ansibleOptionLink" href="#return-connection/security_protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Kafka security protocol.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SSL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/session_mode"></div>
                    <b>session_mode</b>
                    <a class="ansibleOptionLink" href="#return-connection/session_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The mode of the database connection session to be established by the data client. &#x27;REDIRECT&#x27; - for a RAC database, &#x27;DIRECT&#x27; - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">DIRECT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/ssl_mode"></div>
                    <b>ssl_mode</b>
                    <a class="ansibleOptionLink" href="#return-connection/ssl_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>SSL modes for MySQL.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">DISABLED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/stream_pool_id"></div>
                    <b>stream_pool_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/stream_pool_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the stream pool being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/subnet_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the subnet being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-connection/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{orcl-cloud: {free-tier-retain: true}}`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/technology_type"></div>
                    <b>technology_type</b>
                    <a class="ansibleOptionLink" href="#return-connection/technology_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The GoldenGate technology type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GOLDENGATE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/tenancy_id"></div>
                    <b>tenancy_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/tenancy_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the related OCI tenancy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-connection/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the resource was created. The format is defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>, such as `2016-08-25T21:10:29.600Z`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-connection/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the resource was last updated. The format is defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>, such as `2016-08-25T21:10:29.600Z`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/user_id"></div>
                    <b>user_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/user_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.user.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#return-connection/username" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">username_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-connection/vault_id"></div>
                    <b>vault_id</b>
                    <a class="ansibleOptionLink" href="#return-connection/vault_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx</div>
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

