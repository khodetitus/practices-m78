class DiscountError(Exception):
    pass


def apply_discount(price_org: int, discount: float) -> int:
    try:
        price_total = int(price_org * (1 - discount))
        print(price_total)
        assert 0 <= price_total <= price_org
    except Exception:
        raise DiscountError("gheymat asli nabayd bishtar az gheymat ba takhfif bashad")


# arguman dovom bayad float va beyne 0 ta 1 bashad
# agar bekhahim fals shavad bayad az 1 bishtar be dahim

apply_discount(9, 0.5)
# def apply_discount(price: int, discount: float) -> int:
#     """This Function Calculated Final Price"""
#
#     result = int(price * (1 - discount))
#     assert 0 <= result <= price
#     return result
# in kar eshtebah hast chon nabayd ba assert validation data ra anjam dahim
# pas mitavanim be rahati ann ra dakhele try except gharar dahim ke agar gheymat kol az gheymat asli kamtar bod va az 0 bishatr bod ok dahad va agar nabod error monaseb ra chap konad...
