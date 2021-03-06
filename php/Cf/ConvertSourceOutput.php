<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cf/cf.proto

namespace Cf;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>cf.ConvertSourceOutput</code>
 */
class ConvertSourceOutput extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>string all_sources_info = 1;</code>
     */
    private $all_sources_info = '';
    /**
     * Generated from protobuf field <code>string teo_string = 2;</code>
     */
    private $teo_string = '';
    /**
     * Generated from protobuf field <code>string input_fuel = 3;</code>
     */
    private $input_fuel = '';
    /**
     * Generated from protobuf field <code>string output_fuel = 4;</code>
     */
    private $output_fuel = '';
    /**
     * Generated from protobuf field <code>string output = 5;</code>
     */
    private $output = '';
    /**
     * Generated from protobuf field <code>string input = 6;</code>
     */
    private $input = '';
    /**
     * Generated from protobuf field <code>string n_supply_list = 7;</code>
     */
    private $n_supply_list = '';
    /**
     * Generated from protobuf field <code>string teo_capacity_factor_group = 8;</code>
     */
    private $teo_capacity_factor_group = '';
    /**
     * Generated from protobuf field <code>string teo_dhn = 9;</code>
     */
    private $teo_dhn = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $all_sources_info
     *     @type string $teo_string
     *     @type string $input_fuel
     *     @type string $output_fuel
     *     @type string $output
     *     @type string $input
     *     @type string $n_supply_list
     *     @type string $teo_capacity_factor_group
     *     @type string $teo_dhn
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Cf\Cf::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>string all_sources_info = 1;</code>
     * @return string
     */
    public function getAllSourcesInfo()
    {
        return $this->all_sources_info;
    }

    /**
     * Generated from protobuf field <code>string all_sources_info = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setAllSourcesInfo($var)
    {
        GPBUtil::checkString($var, True);
        $this->all_sources_info = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string teo_string = 2;</code>
     * @return string
     */
    public function getTeoString()
    {
        return $this->teo_string;
    }

    /**
     * Generated from protobuf field <code>string teo_string = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setTeoString($var)
    {
        GPBUtil::checkString($var, True);
        $this->teo_string = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string input_fuel = 3;</code>
     * @return string
     */
    public function getInputFuel()
    {
        return $this->input_fuel;
    }

    /**
     * Generated from protobuf field <code>string input_fuel = 3;</code>
     * @param string $var
     * @return $this
     */
    public function setInputFuel($var)
    {
        GPBUtil::checkString($var, True);
        $this->input_fuel = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string output_fuel = 4;</code>
     * @return string
     */
    public function getOutputFuel()
    {
        return $this->output_fuel;
    }

    /**
     * Generated from protobuf field <code>string output_fuel = 4;</code>
     * @param string $var
     * @return $this
     */
    public function setOutputFuel($var)
    {
        GPBUtil::checkString($var, True);
        $this->output_fuel = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string output = 5;</code>
     * @return string
     */
    public function getOutput()
    {
        return $this->output;
    }

    /**
     * Generated from protobuf field <code>string output = 5;</code>
     * @param string $var
     * @return $this
     */
    public function setOutput($var)
    {
        GPBUtil::checkString($var, True);
        $this->output = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string input = 6;</code>
     * @return string
     */
    public function getInput()
    {
        return $this->input;
    }

    /**
     * Generated from protobuf field <code>string input = 6;</code>
     * @param string $var
     * @return $this
     */
    public function setInput($var)
    {
        GPBUtil::checkString($var, True);
        $this->input = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string n_supply_list = 7;</code>
     * @return string
     */
    public function getNSupplyList()
    {
        return $this->n_supply_list;
    }

    /**
     * Generated from protobuf field <code>string n_supply_list = 7;</code>
     * @param string $var
     * @return $this
     */
    public function setNSupplyList($var)
    {
        GPBUtil::checkString($var, True);
        $this->n_supply_list = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string teo_capacity_factor_group = 8;</code>
     * @return string
     */
    public function getTeoCapacityFactorGroup()
    {
        return $this->teo_capacity_factor_group;
    }

    /**
     * Generated from protobuf field <code>string teo_capacity_factor_group = 8;</code>
     * @param string $var
     * @return $this
     */
    public function setTeoCapacityFactorGroup($var)
    {
        GPBUtil::checkString($var, True);
        $this->teo_capacity_factor_group = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string teo_dhn = 9;</code>
     * @return string
     */
    public function getTeoDhn()
    {
        return $this->teo_dhn;
    }

    /**
     * Generated from protobuf field <code>string teo_dhn = 9;</code>
     * @param string $var
     * @return $this
     */
    public function setTeoDhn($var)
    {
        GPBUtil::checkString($var, True);
        $this->teo_dhn = $var;

        return $this;
    }

}

