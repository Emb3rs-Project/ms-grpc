<?php
// GENERATED CODE -- DO NOT EDIT!

namespace Market;

/**
 */
class MarketModuleClient extends \Grpc\BaseStub {

    /**
     * @param string $hostname hostname
     * @param array $opts channel options
     * @param \Grpc\Channel $channel (optional) re-use channel object
     */
    public function __construct($hostname, $opts, $channel = null) {
        parent::__construct($hostname, $opts, $channel);
    }

    /**
     * @param \Market\MarketInputRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     */
    public function RunShortTermMarket(\Market\MarketInputRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/market.MarketModule/RunShortTermMarket',
        $argument,
        ['\Market\ShortTermMarketResponse', 'decode'],
        $metadata, $options);
    }

    /**
     * @param \Market\MarketInput $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     */
    public function RunShortTermMarketDirect(\Market\MarketInput $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/market.MarketModule/RunShortTermMarketDirect',
        $argument,
        ['\Market\ShortTermMarketResponse', 'decode'],
        $metadata, $options);
    }

    /**
     * @param \Market\MarketInputRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     */
    public function RunLongTermMarket(\Market\MarketInputRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/market.MarketModule/RunLongTermMarket',
        $argument,
        ['\Market\LongTermMarketResponse', 'decode'],
        $metadata, $options);
    }

    /**
     * @param \Market\MarketInput $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     */
    public function RunLongTermMarketDirect(\Market\MarketInput $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/market.MarketModule/RunLongTermMarketDirect',
        $argument,
        ['\Market\LongTermMarketResponse', 'decode'],
        $metadata, $options);
    }

}
