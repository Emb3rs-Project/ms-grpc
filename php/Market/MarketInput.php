<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market/market.proto

namespace Market;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>market.MarketInput</code>
 */
class MarketInput extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>string input = 1;</code>
     */
    protected $input = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $input
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Market\Market::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>string input = 1;</code>
     * @return string
     */
    public function getInput()
    {
        return $this->input;
    }

    /**
     * Generated from protobuf field <code>string input = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setInput($var)
    {
        GPBUtil::checkString($var, True);
        $this->input = $var;

        return $this;
    }

}

