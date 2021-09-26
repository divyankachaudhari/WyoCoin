from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.blockchain_format.program import Program
from chia.types.condition_opcodes import ConditionOpcode
from chia.util.ints import uint64
from chia.util.hash import std_hash

from clvm.casts import int_to_bytes

from cdv.util.load_clvm import load_clvm

WyoCoin_MOD = load_clvm("WyoCoin.clsp","WyoCoin")

# Create a WyoCoin
def create_WyoCoin_puzzle(amount, cash_out_puzhash):
    return WyoCoin_MOD.curry(amount, cash_out_puzhash)

# Generate a solution to contribute to a WyoCoin
def solution_for_WyoCoin(lc_coin, contribution_amount):
    return Program.to([lc_coin.amount, (lc_coin.amount + contribution_amount), lc_coin.puzzle_hash])

# Return the condition to assert the announcement
def WyoCoin_announcement_assertion(lc_coin, contribution_amount):
    return [ConditionOpcode.ASSERT_COIN_ANNOUNCEMENT, std_hash(lc_coin.name() + int_to_bytes((lc_coin.amount + contribution_amount)))]
