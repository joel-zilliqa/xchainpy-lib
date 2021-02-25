import json
import http3


def to_sochain_network(net: str):
    return 'LTCTEST' if net == 'testnet' else 'LTC'

async def get_balance(sochain_url:str, net:str, address:str):
    """Get address balance
    https://sochain.com/api#get-balance

    :param net: mainnet or testnet
    :type net: str
    :param address: wallet address
    :type address: str
    :returns: The fees with memo
    """
    try:
        api_url = f'{sochain_url}/get_address_balance/{to_sochain_network(net)}/{address}'

        client = http3.AsyncClient()
        response = await client.get(api_url)

        if response.status_code == 200:
            balance_response = json.loads(response.content.decode('utf-8'))['data']
            confirmed = float(balance_response['confirmed_balance'])
            unconfirmed = float(balance_response['unconfirmed_balance'])
            total = confirmed + unconfirmed
            return total
        else:
            return None
    except Exception as err:
        raise Exception(str(err))


async def get_tx(sochain_url:str, net: str, hash: str):
    """Get transaction by hash
    https://sochain.com/api#get-tx

    :param net: mainnet or testnet
    :type net: str
    :param hash: The transaction hash
    :type hash: str
    :returns: The fees with memo
    """
    try:
        api_url = f'{sochain_url}/get_tx/{to_sochain_network(net)}/{hash}'

        client = http3.AsyncClient()
        response = await client.get(api_url)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))['data']
        else:
            return None
    except Exception as err:
        raise Exception(str(err))


async def get_suggested_tx_fee():
    """Get Litecoin suggested transaction fee

    Note: sochain does not provide fee rate related data
    So use Bitgo API for fee estimation
    Refer: https://app.bitgo.com/docs/#operation/v2.tx.getfeeestimate

    :returns: The Litecoin suggested transaction fee per bytes in sat
    """
    try:
        api_url = 'https://app.bitgo.com/api/v2/ltc/tx/fee'

        client = http3.AsyncClient()
        response = await client.get(api_url)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))['fastestFee']
        else:
            return None
    except Exception as err:
        raise Exception(str(err))