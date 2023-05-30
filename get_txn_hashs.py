#!/usr/bin/python3

from tqdm import tqdm
import requests
import json


def instruct_daemon(method, params):
    payload = json.dumps({"method": method, "params": params}, skipkeys=False)
    # print(payload)
    headers = {'content-type': "application/json"}
    try:
        response = requests.request("POST", "http://localhost:22023/json_rpc", data=payload, headers=headers)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(e)
    except:
        print('No response from daemon, check daemon is running on this machine')

txn_hashes = []
number_blocks = instruct_daemon('get_block_count', [])["result"]["count"] - 1
print("Number of Blocks: {}".format(number_blocks))


for block in tqdm(range(number_blocks, 1, -1)):
    result = instruct_daemon('get_block', {"height": block})["result"]
    if "tx_hashes" in result:
        txn_hashes.extend(result["tx_hashes"])

# print(txn_hashes)

# txn_hashes = ["172ad560100ae827ccad0dd7c015e192dc8c46fd333906025159fa1d38366036",
              # "e68d059e4f37fac4455a7530f69d348519b9ad928577b9686f09cff7e9165631",
              # "00c554125ab85cf70134118a32265c21e829b5777c5e1b81c8a8d1cf75f13458",
              # "a092d0d9aa3db7bd2ffe83fe315f216cad9f84767a1bcc0e7621b793611f954c",
              # "d4e1daa8aee4b6c12fd2a50a025e2161c751202eb883733ce8eeb1de9176b226",
              # "3e662dd1fb38bab4d29734c91eb332bcb1571865ff5263fb0ba1354e61a8e4c6",
              # "033f1000cb8ccbd66d52e271c32c07e4254f438d0ee8c084e259e2b596dbf2f7",
              # "1657cb923b181d91a3c369dc6fdd2c9a0ebd35cef4310c8373bb7eb3b8eb54da",
              # "bc2a51e5c76ba89d94210ccab7f243f0dec40fdf142afcf9f16e7c452a9d9fa0",
              # "4067b6b7078c21e6129e2a6bba4c310b0e4026b3efc29ebda5ca77470d851d66",
              # "f6e3e13d2235524d5084103f94fd3997458c311c37b6768d7420d806db25003e",
              # "3939820b52a86938110ad651ab7a18866c77de57f6bee3dfc508acc11f071e11",
              # "beabfca8c6808359f91cf6e97dc3adc16e511db19347a1c63df8fd4650414773",
              # "f80bf0a9ccfed2588a41c5b08081d3325825d60e6a34b9a51d2a0e35ed5d6d57",
              # "d5010e233b196ba36e245544e94087143e238945fab5413804917b2dd1a39b74",
              # "ea48fd1d2def890677070879ae8f2be3fca373b78d8dd054447fefdb03fc0cc8",
              # "d7506256f57e242116fe8bac82f5afc1060265b3af3d962efc51fe1fccf8ff1d",
              # "2b6df418bbaffa0cf30c96c16535a86061a5adf2d14f0417bf95246da7119596",
              # "ef3d2022c7fc1a8a41bb531524032f795ab964b1c5b1e34955a1f5f1b0bd4397",
              # "2f01aa0ed633f0c49a1f4bcffd61099a3481f07842b0ab91426d558fd4f85222",
              # "99513e1a4fa77d8fdfd14d4cc251b8650150fe154f1620de43d37ec9f993ed08",
              # "76c1bed470025fa34e400daabf3a6d551af25108fe64762043371dc67bce7d8c",
              # "575d1a3cd0f84329a00a86cb0619c8d358ab27c2bca40647495a87e0bc87c974",
              # "c5cc73d333815349d0fd0ed812aa06c3f69a5d02d7d6eee1183d3519132fd07c",
              # "6dbc41a4ec37c5dcd3a7961794a285ae84772305b821b1599d30c133c8d0c33a",
              # "0692c239079912cef1b44b7ecff46ace1bdeaeedbe1ed90cf02328e8dc3874d5",
              # "aa0803d8543f559b5996de70e3e10d13576bcdc7d539d4640cc89233f658f48b",
              # "aa4da6fc4115237e132e30e22e860cd2870e66dbf2df057558a57474153e0962",
              # "ba9858fb255f6652f08b7081eb791ea59e1af36f83ca10a2daa16d9e48b1a9ef",
              # "cf90ca3ba4e77f09d6df4b2375ab7b123afda3d89a7ff4261a24078015791932",
              # "e21efa337388a00fb0587ddd221bad2d567d9d97e877e49636aca9569446b847",
              # "0c54a9a158b45d9bc70f1ceca35526bca6abd996256b78bf9c784cfe38eb18d8",
              # "dc9749ed0d306f6cece000716886a8737d95b08b9e4189d2cd29cf01dce1304a",
              # "2a5d16859c227038e01d673585f44f0a0408ddb8f020bb545dca41e1d6a29813",
              # "c2801052b4878488c012a03cfe35aa0b035782d9305887b7b379233d22dd3790",
              # "81614c69c542b4f65e943c590e9cf3113622a096e3c41c93a5fdcf6e89bae709",
              # "e352aa025d3948b9b3480880714bc357727d8333a095906c0e01a25e8b7b3e88",
              # "2e17644bf932d281e30b6188d3239dc58ee411b2e3c44f48acd95b5d7cad0764",
              # "147aba7f6ad51ae4d1e78bb34760019134ef14cb7a0df3bd97b3c6e2b8f11841",
              # "8a1a137a3f138b2fde936a2bea06fd612882f11f8c40cfeed70d0f7a2d18d0ba",
              # "2189fa3bc6e3aad6bdd98d8066ad92e0915752b644919f1be2f3ac1118f22ea6",
              # "5150dc438726547a19545896f74accf03b911653e72d266ce7ef5e4753b746e0",
              # "205397bb796b9bdfb34ec8198ad649e595935f99eeca46b295e542adf6d156fc",
              # "e18c4aa3ffb1156aff0767727324eaeaf602492821ca1abf8ac9c299b329fdeb"]

transaction_save_file = open('transaction-dump.json', 'w+')
json.dump(txn_hashes, transaction_save_file)

