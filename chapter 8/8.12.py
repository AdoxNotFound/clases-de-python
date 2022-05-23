def make_sandwich(*items):
    print("\nyour sandwich has:")
    for item in items:
        print(f"-{item}")

make_sandwich('tomaco')
make_sandwich('onion', 'chipotle', 'tortiya')
make_sandwich('brrrr', 'flow', 'lettuce')