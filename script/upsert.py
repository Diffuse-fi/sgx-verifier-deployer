import subprocess
import os
import argparse
from utils.network import *
from enum import Enum

class CA(Enum):
    ROOT = "0"
    PROCESSOR = "1"
    PLATFORM = "2"
    SIGNING = "3"


def upsert(network):

    # script uses hardcoded inputs that I took from transactions in automata testnet
    # https://explorer-testnet.ata.network/address/0xcf171ACd6c0a776f9d3E1F6Cac8067c982Ac6Ce1
    #
    attributes = [
        # requested here in qpl-tool https://github.com/automata-network/automata-dcap-qpl/blob/4c02528b898ca95692303013034021e2f9b64ba1/automata-dcap-qpl-tool/src/contracts.rs#L223
        # https://certificates.trustedservices.intel.com/Intel_SGX_Attestation_RootCA.pem
        ['upsertPcsCertificates(uint8 ca, bytes cert)', CA.ROOT.value, '0x3082028f30820234a003020102021422650cd65a9d3489f383b49552bf501b392706ac300a06082a8648ce3d0403023068311a301806035504030c11496e74656c2053475820526f6f74204341311a3018060355040a0c11496e74656c20436f72706f726174696f6e3114301206035504070c0b53616e746120436c617261310b300906035504080c024341310b3009060355040613025553301e170d3138303532313130343531305a170d3439313233313233353935395a3068311a301806035504030c11496e74656c2053475820526f6f74204341311a3018060355040a0c11496e74656c20436f72706f726174696f6e3114301206035504070c0b53616e746120436c617261310b300906035504080c024341310b30090603550406130255533059301306072a8648ce3d020106082a8648ce3d030107034200040ba9c4c0c0c86193a3fe23d6b02cda10a8bbd4e88e48b4458561a36e705525f567918e2edc88e40d860bd0cc4ee26aacc988e505a953558c453f6b0904ae7394a381bb3081b8301f0603551d2304183016801422650cd65a9d3489f383b49552bf501b392706ac30520603551d1f044b30493047a045a043864168747470733a2f2f6365727469666963617465732e7472757374656473657276696365732e696e74656c2e636f6d2f496e74656c534758526f6f7443412e646572301d0603551d0e0416041422650cd65a9d3489f383b49552bf501b392706ac300e0603551d0f0101ff04040302010630120603551d130101ff040830060101ff020101300a06082a8648ce3d0403020349003046022100e5bfe50911f92f428920dc368a302ee3d12ec5867ff622ec6497f78060c13c20022100e09d25ac7a0cb3e5e8e68fec5fa3bd416c47440bd950639d450edcbea4576aa2'],

        # not requested, can be downloaded here, https://certificates.trustedservices.intel.com/IntelSGXRootCA.der
        ['upsertRootCACrl(bytes rootcacrl)', '0x308201223081c8020101300a06082a8648ce3d0403023068311a301806035504030c11496e74656c2053475820526f6f74204341311a3018060355040a0c11496e74656c20436f72706f726174696f6e3114301206035504070c0b53616e746120436c617261310b300906035504080c024341310b3009060355040613025553170d3234303332303139313933305a170d3235303430333139313933305aa02f302d300a0603551d140403020101301f0603551d2304183016801422650cd65a9d3489f383b49552bf501b392706ac300a06082a8648ce3d0403020349003046022100e7606fef2da68785a0c39bc34ac344c9e2d6ed4b0223e79a6c6297d421b73784022100fc1587aece4296d5e9370fd6a444a72d03c598cb21dc8104c55b127b766ea82b'],

        # not requested, without it upsert pck crl fails txn[upsert_pck_crl] meet error: Revert(Bytes(0x4e487b710000000000000000000000000000000000000000000000000000000000000032))
        ['upsertPcsCertificates(uint8 ca, bytes cert)', CA.PLATFORM.value, '0x308202963082023da003020102021500956f5dcdbd1be1e94049c9d4f433ce01570bde54300a06082a8648ce3d0403023068311a301806035504030c11496e74656c2053475820526f6f74204341311a3018060355040a0c11496e74656c20436f72706f726174696f6e3114301206035504070c0b53616e746120436c617261310b300906035504080c024341310b3009060355040613025553301e170d3138303532313130353031305a170d3333303532313130353031305a30703122302006035504030c19496e74656c205347582050434b20506c6174666f726d204341311a3018060355040a0c11496e74656c20436f72706f726174696f6e3114301206035504070c0b53616e746120436c617261310b300906035504080c024341310b30090603550406130255533059301306072a8648ce3d020106082a8648ce3d0301070342000435207feeddb595748ed82bb3a71c3be1e241ef61320c6816e6b5c2b71dad5532eaea12a4eb3f948916429ea47ba6c3af82a15e4b19664e52657939a2d96633dea381bb3081b8301f0603551d2304183016801422650cd65a9d3489f383b49552bf501b392706ac30520603551d1f044b30493047a045a043864168747470733a2f2f6365727469666963617465732e7472757374656473657276696365732e696e74656c2e636f6d2f496e74656c534758526f6f7443412e646572301d0603551d0e04160414956f5dcdbd1be1e94049c9d4f433ce01570bde54300e0603551d0f0101ff04040302010630120603551d130101ff040830060101ff020100300a06082a8648ce3d040302034700304402205ec5648b4c3e8ba558196dd417fdb6b9a5ded182438f551e9c0f938c3d5a8b970220261bd520260f9c647d3569be8e14a32892631ac358b994478088f4d2b27cf37e'],

        # https://github.com/automata-network/automata-dcap-qpl/blob/4c02528b898ca95692303013034021e2f9b64ba1/automata-dcap-qpl-tool/src/contracts.rs#L242
        ['upsertPcsCertificates(uint8 ca, bytes cert)', CA.SIGNING.value, '0x3082028b30820232a00302010202147e3882d5fb55294a40498e458403e91491bdf455300a06082a8648ce3d0403023068311a301806035504030c11496e74656c2053475820526f6f74204341311a3018060355040a0c11496e74656c20436f72706f726174696f6e3114301206035504070c0b53616e746120436c617261310b300906035504080c024341310b3009060355040613025553301e170d3138303532313130353031305a170d3235303532313130353031305a306c311e301c06035504030c15496e74656c2053475820544342205369676e696e67311a3018060355040a0c11496e74656c20436f72706f726174696f6e3114301206035504070c0b53616e746120436c617261310b300906035504080c024341310b30090603550406130255533059301306072a8648ce3d020106082a8648ce3d0301070342000443451bcc73c9d5917caf766e61af3fe98087dd4f13257b261e851897799dd13d6811fb47713803bb9bae587fccddc2e31be9a28b86962acc6daf96da58eeca96a381b53081b2301f0603551d2304183016801422650cd65a9d3489f383b49552bf501b392706ac30520603551d1f044b30493047a045a043864168747470733a2f2f6365727469666963617465732e7472757374656473657276696365732e696e74656c2e636f6d2f496e74656c534758526f6f7443412e646572301d0603551d0e041604147e3882d5fb55294a40498e458403e91491bdf455300e0603551d0f0101ff0404030206c0300c0603551d130101ff04023000300a06082a8648ce3d040302034700304402201f42f3038037f226c43b46002576e3a29caa36a064e47493272dc81aec1862550220237ed6eb346b0653c607db5d5d46260da0f3eed7d669ff37bc26686e8c1d2807'],

        # https://github.com/automata-network/automata-dcap-qpl/blob/4c02528b898ca95692303013034021e2f9b64ba1/automata-dcap-qpl-tool/src/helper.rs#L250
        ['upsertPckCrl(uint8 ca, bytes calldata crl)', CA.PLATFORM.value, '0x30820a6230820a08020101300a06082a8648ce3d04030230703122302006035504030c19496e74656c205347582050434b20506c6174666f726d204341311a3018060355040a0c11496e74656c20436f72706f726174696f6e3114301206035504070c0b53616e746120436c617261310b300906035504080c024341310b3009060355040613025553170d3235303331373132343532335a170d3235303431363132343532335a30820934303302146fc34e5023e728923435d61aa4b83c618166ad35170d3235303331373132343532335a300c300a0603551d1504030a01013034021500efae6e9715fca13b87e333e8261ed6d990a926ad170d3235303331373132343532335a300c300a0603551d1504030a01013034021500fd608648629cba73078b4d492f4b3ea741ad08cd170d3235303331373132343532335a300c300a0603551d1504030a010130340215008af924184e1d5afddd73c3d63a12f5e8b5737e56170d3235303331373132343532335a300c300a0603551d1504030a01013034021500b1257978cfa9ccdd0759abf8c5ca72fae3a78a9b170d3235303331373132343532335a300c300a0603551d1504030a01013033021474fea614a972be0e2843f2059835811ed872f9b3170d3235303331373132343532335a300c300a0603551d1504030a01013034021500f9c4ef56b3ab48d577e108baedf4bf88014214b9170d3235303331373132343532335a300c300a0603551d1504030a010130330214071de0778f9e5fc4f2878f30d6b07c9a30e6b30b170d3235303331373132343532335a300c300a0603551d1504030a01013034021500cde2424f972cea94ff239937f4d80c25029dd60b170d3235303331373132343532335a300c300a0603551d1504030a0101303302146c3319e5109b64507d3cf1132ce00349ef527319170d3235303331373132343532335a300c300a0603551d1504030a01013034021500df08d756b66a7497f43b5bb58ada04d3f4f7a937170d3235303331373132343532335a300c300a0603551d1504030a01013033021428af485b6cf67e409a39d5cb5aee4598f7a8fa7b170d3235303331373132343532335a300c300a0603551d1504030a01013034021500fb8b2daec092cada8aa9bc4ff2f1c20d0346668c170d3235303331373132343532335a300c300a0603551d1504030a01013034021500cd4850ac52bdcc69a6a6f058c8bc57bbd0b5f864170d3235303331373132343532335a300c300a0603551d1504030a01013034021500994dd3666f5275fb805f95dd02bd50cb2679d8ad170d3235303331373132343532335a300c300a0603551d1504030a0101303302140702136900252274d9035eedf5457462fad0ef4c170d3235303331373132343532335a300c300a0603551d1504030a01013033021461f2bf73e39b4e04aa27d801bd73d24319b5bf80170d3235303331373132343532335a300c300a0603551d1504030a0101303302143992be851b96902eff38959e6c2eff1b0651a4b5170d3235303331373132343532335a300c300a0603551d1504030a0101303302140fda43a00b68ea79b7c2deaeac0b498bdfb2af90170d3235303331373132343532335a300c300a0603551d1504030a010130330214639f139a5040fdcff191e8a4fb1bf086ed603971170d3235303331373132343532335a300c300a0603551d1504030a01013034021500959d533f9249dc1e513544cdc830bf19b7f1f301170d3235303331373132343532335a300c300a0603551d1504030a0101303302147ae37748a9f912f4c63ba7ab07c593ce1d1d1181170d3235303331373132343532335a300c300a0603551d1504030a01013033021413884b33269938c195aa170fca75da177538df0b170d3235303331373132343532335a300c300a0603551d1504030a0101303402150085d3c9381b77a7e04d119c9e5ad6749ff3ffab87170d3235303331373132343532335a300c300a0603551d1504030a0101303402150093887ca4411e7a923bd1fed2819b2949f201b5b4170d3235303331373132343532335a300c300a0603551d1504030a0101303302142498dc6283930996fd8bf23a37acbe26a3bed457170d3235303331373132343532335a300c300a0603551d1504030a010130340215008a66f1a749488667689cc3903ac54c662b712e73170d3235303331373132343532335a300c300a0603551d1504030a01013034021500afc13610bdd36cb7985d106481a880d3a01fda07170d3235303331373132343532335a300c300a0603551d1504030a01013034021500efe04b2c33d036aac96ca673bf1e9a47b64d5cbb170d3235303331373132343532335a300c300a0603551d1504030a0101303402150083d9ac8d8bb509d1c6c809ad712e8430559ed7f3170d3235303331373132343532335a300c300a0603551d1504030a0101303302147931fd50b5071c1bbfc5b7b6ded8b45b9d8b8529170d3235303331373132343532335a300c300a0603551d1504030a0101303302141fa20e2970bde5d57f7b8ddf8339484e1f1d0823170d3235303331373132343532335a300c300a0603551d1504030a0101303302141e87b2c3b32d8d23e411cef34197b95af0c8adf5170d3235303331373132343532335a300c300a0603551d1504030a010130340215009afd2ee90a473550a167d996911437c7502d1f09170d3235303331373132343532335a300c300a0603551d1504030a0101303302144481b0f11728a13b696d3ea9c770a0b15ec58dda170d3235303331373132343532335a300c300a0603551d1504030a01013034021500a7859f57982ef0e67d37bc8ef2ef5ac835ff1aa9170d3235303331373132343532335a300c300a0603551d1504030a010130340215009d67753b81e47090aea763fbec4c4549bcdb9933170d3235303331373132343532335a300c300a0603551d1504030a01013033021434bfbb7a1d9c568147e118b614f7b76ed3ef68df170d3235303331373132343532335a300c300a0603551d1504030a0101303302142c3cc6fe9279db1516d5ce39f2a898cda5a175e1170d3235303331373132343532335a300c300a0603551d1504030a010130330214717948687509234be979e4b7dce6f31bef64b68c170d3235303331373132343532335a300c300a0603551d1504030a010130340215009d76ef2c39c136e8658b6e7396b1d7445a27631f170d3235303331373132343532335a300c300a0603551d1504030a01013034021500c3e025fca995f36f59b48467939e3e34e6361a6f170d3235303331373132343532335a300c300a0603551d1504030a010130340215008c5f6b3257da05b17429e2e61ba965d67330606a170d3235303331373132343532335a300c300a0603551d1504030a01013034021500a17c51722ec1e0c3278fe8bdf052059cbec4e648170d3235303331373132343532335a300c300a0603551d1504030a0101a02f302d300a0603551d140403020101301f0603551d23041830168014956f5dcdbd1be1e94049c9d4f433ce01570bde54300a06082a8648ce3d0403020348003045022100ca60f2f57e2977366546b4a2527fa01c6955a45d1fad0c88258eb5c4d5d99f1302207131ac991f56db3d018e01769ca8819da49ee95cd6d3682df55f14a90f461e45']
    ]


    with open('addresses/' + network.dirname + '/PCS_DAO', 'r') as file:
        PCS_DAO = file.read().strip()

    for i in range(len(attributes)):
        print('==================================================================\n', i)
        cmd = ['cast', 'send', PCS_DAO]
        for attr in attributes[i]:
            cmd.append(attr)
        cmd.append('--private-key=' + os.getenv("PRIVATE_KEY"))
        cmd.append('--rpc-url=' + network.rpc_url)
        cmd.append('--legacy')

        subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data feeder parameters")
    parser.add_argument('-n', '--network', type=network_class, required=True, help="Choose network")
    args = parser.parse_args()

    upsert(args.network)