<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market/market.proto

namespace Market;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>market.ShortTermMarketResponse</code>
 */
class ShortTermMarketResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>string Gn = 1;</code>
     */
    protected $Gn = '';
    /**
     * Generated from protobuf field <code>string Ln = 2;</code>
     */
    protected $Ln = '';
    /**
     * Generated from protobuf field <code>string Pn = 3;</code>
     */
    protected $Pn = '';
    /**
     * Generated from protobuf field <code>string QoE = 4;</code>
     */
    protected $QoE = '';
    /**
     * Generated from protobuf field <code>string optimal = 5;</code>
     */
    protected $optimal = '';
    /**
     * Generated from protobuf field <code>string plot_market_clearing = 6;</code>
     */
    protected $plot_market_clearing = '';
    /**
     * Generated from protobuf field <code>string settlement = 7;</code>
     */
    protected $settlement = '';
    /**
     * Generated from protobuf field <code>string social_welfare_h = 8;</code>
     */
    protected $social_welfare_h = '';
    /**
     * Generated from protobuf field <code>string shadow_price = 9;</code>
     */
    protected $shadow_price = '';
    /**
     * Generated from protobuf field <code>string Tnm = 10;</code>
     */
    protected $Tnm = '';
    /**
     * Generated from protobuf field <code>string agent_operational_cost = 11;</code>
     */
    protected $agent_operational_cost = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $Gn
     *     @type string $Ln
     *     @type string $Pn
     *     @type string $QoE
     *     @type string $optimal
     *     @type string $plot_market_clearing
     *     @type string $settlement
     *     @type string $social_welfare_h
     *     @type string $shadow_price
     *     @type string $Tnm
     *     @type string $agent_operational_cost
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Market\Market::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>string Gn = 1;</code>
     * @return string
     */
    public function getGn()
    {
        return $this->Gn;
    }

    /**
     * Generated from protobuf field <code>string Gn = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setGn($var)
    {
        GPBUtil::checkString($var, True);
        $this->Gn = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string Ln = 2;</code>
     * @return string
     */
    public function getLn()
    {
        return $this->Ln;
    }

    /**
     * Generated from protobuf field <code>string Ln = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setLn($var)
    {
        GPBUtil::checkString($var, True);
        $this->Ln = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string Pn = 3;</code>
     * @return string
     */
    public function getPn()
    {
        return $this->Pn;
    }

    /**
     * Generated from protobuf field <code>string Pn = 3;</code>
     * @param string $var
     * @return $this
     */
    public function setPn($var)
    {
        GPBUtil::checkString($var, True);
        $this->Pn = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string QoE = 4;</code>
     * @return string
     */
    public function getQoE()
    {
        return $this->QoE;
    }

    /**
     * Generated from protobuf field <code>string QoE = 4;</code>
     * @param string $var
     * @return $this
     */
    public function setQoE($var)
    {
        GPBUtil::checkString($var, True);
        $this->QoE = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string optimal = 5;</code>
     * @return string
     */
    public function getOptimal()
    {
        return $this->optimal;
    }

    /**
     * Generated from protobuf field <code>string optimal = 5;</code>
     * @param string $var
     * @return $this
     */
    public function setOptimal($var)
    {
        GPBUtil::checkString($var, True);
        $this->optimal = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string plot_market_clearing = 6;</code>
     * @return string
     */
    public function getPlotMarketClearing()
    {
        return $this->plot_market_clearing;
    }

    /**
     * Generated from protobuf field <code>string plot_market_clearing = 6;</code>
     * @param string $var
     * @return $this
     */
    public function setPlotMarketClearing($var)
    {
        GPBUtil::checkString($var, True);
        $this->plot_market_clearing = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string settlement = 7;</code>
     * @return string
     */
    public function getSettlement()
    {
        return $this->settlement;
    }

    /**
     * Generated from protobuf field <code>string settlement = 7;</code>
     * @param string $var
     * @return $this
     */
    public function setSettlement($var)
    {
        GPBUtil::checkString($var, True);
        $this->settlement = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string social_welfare_h = 8;</code>
     * @return string
     */
    public function getSocialWelfareH()
    {
        return $this->social_welfare_h;
    }

    /**
     * Generated from protobuf field <code>string social_welfare_h = 8;</code>
     * @param string $var
     * @return $this
     */
    public function setSocialWelfareH($var)
    {
        GPBUtil::checkString($var, True);
        $this->social_welfare_h = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string shadow_price = 9;</code>
     * @return string
     */
    public function getShadowPrice()
    {
        return $this->shadow_price;
    }

    /**
     * Generated from protobuf field <code>string shadow_price = 9;</code>
     * @param string $var
     * @return $this
     */
    public function setShadowPrice($var)
    {
        GPBUtil::checkString($var, True);
        $this->shadow_price = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string Tnm = 10;</code>
     * @return string
     */
    public function getTnm()
    {
        return $this->Tnm;
    }

    /**
     * Generated from protobuf field <code>string Tnm = 10;</code>
     * @param string $var
     * @return $this
     */
    public function setTnm($var)
    {
        GPBUtil::checkString($var, True);
        $this->Tnm = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string agent_operational_cost = 11;</code>
     * @return string
     */
    public function getAgentOperationalCost()
    {
        return $this->agent_operational_cost;
    }

    /**
     * Generated from protobuf field <code>string agent_operational_cost = 11;</code>
     * @param string $var
     * @return $this
     */
    public function setAgentOperationalCost($var)
    {
        GPBUtil::checkString($var, True);
        $this->agent_operational_cost = $var;

        return $this;
    }

}

