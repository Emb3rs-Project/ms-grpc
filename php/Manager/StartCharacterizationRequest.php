<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manager/manager.proto

namespace Manager;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>manager.StartCharacterizationRequest</code>
 */
class StartCharacterizationRequest extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>string entity_id = 1;</code>
     */
    private $entity_id = '';
    /**
     * Generated from protobuf field <code>string entity_data = 2;</code>
     */
    private $entity_data = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $entity_id
     *     @type string $entity_data
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Manager\Manager::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>string entity_id = 1;</code>
     * @return string
     */
    public function getEntityId()
    {
        return $this->entity_id;
    }

    /**
     * Generated from protobuf field <code>string entity_id = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setEntityId($var)
    {
        GPBUtil::checkString($var, True);
        $this->entity_id = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string entity_data = 2;</code>
     * @return string
     */
    public function getEntityData()
    {
        return $this->entity_data;
    }

    /**
     * Generated from protobuf field <code>string entity_data = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setEntityData($var)
    {
        GPBUtil::checkString($var, True);
        $this->entity_data = $var;

        return $this;
    }

}

