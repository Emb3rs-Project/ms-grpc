<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cf/cf.proto

namespace Cf;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>cf.ConvertPinchOutput</code>
 */
class ConvertPinchOutput extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>string co2_optimization = 1;</code>
     */
    private $co2_optimization = '';
    /**
     * Generated from protobuf field <code>string energy_recovered_optimization = 2;</code>
     */
    private $energy_recovered_optimization = '';
    /**
     * Generated from protobuf field <code>string energy_investment_optimization = 3;</code>
     */
    private $energy_investment_optimization = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $co2_optimization
     *     @type string $energy_recovered_optimization
     *     @type string $energy_investment_optimization
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Cf\Cf::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>string co2_optimization = 1;</code>
     * @return string
     */
    public function getCo2Optimization()
    {
        return $this->co2_optimization;
    }

    /**
     * Generated from protobuf field <code>string co2_optimization = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setCo2Optimization($var)
    {
        GPBUtil::checkString($var, True);
        $this->co2_optimization = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string energy_recovered_optimization = 2;</code>
     * @return string
     */
    public function getEnergyRecoveredOptimization()
    {
        return $this->energy_recovered_optimization;
    }

    /**
     * Generated from protobuf field <code>string energy_recovered_optimization = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setEnergyRecoveredOptimization($var)
    {
        GPBUtil::checkString($var, True);
        $this->energy_recovered_optimization = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string energy_investment_optimization = 3;</code>
     * @return string
     */
    public function getEnergyInvestmentOptimization()
    {
        return $this->energy_investment_optimization;
    }

    /**
     * Generated from protobuf field <code>string energy_investment_optimization = 3;</code>
     * @param string $var
     * @return $this
     */
    public function setEnergyInvestmentOptimization($var)
    {
        GPBUtil::checkString($var, True);
        $this->energy_investment_optimization = $var;

        return $this;
    }

}

