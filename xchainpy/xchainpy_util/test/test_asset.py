import pytest
from xchainpy.xchainpy_util.asset import Asset


class TestAsset:
    def test_create_asset(self):
        asset = Asset('BNB', 'RUNE-67C')
        assert asset.chain == 'BNB'
        assert asset.symbol == 'RUNE-67C'
        assert asset.ticker == 'RUNE'

    def test_invalid_chain(self):
        with pytest.raises(Exception) as err:
            Asset('invalid chain', 'BNB', 'BNB')
        assert str(err.value) == "the chain is invalid"

    def test_asset_to_string(self):
        asset = Asset('BNB', 'RUNE-67C', 'RUNE')
        assert str(asset) == 'BNB.RUNE-67C'

    def test_asset_equal(self):
        asset = Asset('BNB', 'RUNE-67C', 'RUNE')
        asset2 = Asset('BNB', 'RUNE-67C', 'RUNE')
        assert asset == asset2

    def test_string_to_asset(self):
        asset_str = 'BNB.RUNE-67C'
        asset = Asset.from_str(asset_str)
        assert asset["chain"] == 'BNB'
        assert asset["symbol"] == 'RUNE-67C'
        assert asset["ticker"] == 'RUNE'



