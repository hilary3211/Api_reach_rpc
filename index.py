from threading import Thread
from reach_rpc import mk_rpc
import time
def main():
    rpc, rpc_callbacks = mk_rpc()

    starting_balance = rpc("/stdlib/parseCurrency", 100)
    name = 'Alice'
    acc_alice = rpc("/stdlib/newTestAccount", starting_balance)
    acc_bob1 = rpc("/stdlib/newTestAccount", starting_balance)
    acc_bob2 = rpc("/stdlib/newTestAccount", starting_balance)
    acc_bob3 = rpc("/stdlib/newTestAccount", starting_balance)
    acc_bob4 = rpc("/stdlib/newTestAccount", starting_balance)
    acc_bob5 = rpc("/stdlib/newTestAccount", starting_balance)
    acc_bob6 = rpc("/stdlib/newTestAccount", starting_balance)

    

    def fmt(x):
        return rpc("/stdlib/formatCurrency", x, 4)

    def get_balance(w):
        return fmt(rpc("/stdlib/balanceOf", w))

    before_alice = get_balance(acc_alice)
    before_bob1 = get_balance(acc_bob1)
    before_bob2 = get_balance(acc_bob2)
    before_bob3 = get_balance(acc_bob3)
    before_bob4 = get_balance(acc_bob4)
    before_bob5 = get_balance(acc_bob5)

    ctc_alice = rpc("/acc/contract", acc_alice)

    def play_alice():
        def start_program():
            print('program has started')
        rpc_callbacks(
            "/backend/Alice",
            ctc_alice,
            dict(
                start_program = start_program
            ),
        )
    alice = Thread(target=play_alice)
    alice.start()

    def play_bob(accc):
        ctc_bob = rpc("/acc/contract", accc, rpc("/ctc/getInfo", ctc_alice))
        rpc('/ctc/apis/Bob_accs/optin_acc', ctc_bob)
        rpc("/forget/ctc", ctc_bob)
    bob1 = Thread(target=play_bob(acc_bob1))
    bob1.start()
    bob2 = Thread(target=play_bob(acc_bob2))
    bob2.start()
    bob3 = Thread(target=play_bob(acc_bob3))
    bob3.start()
    bob4 = Thread(target=play_bob(acc_bob4))
    bob4.start()
    bob5 = Thread(target=play_bob(acc_bob5))
    bob5.start()
    bob6 = Thread(target=play_bob(acc_bob6))
    bob6.start()


    alice.join()
    bob1.join()
    bob2.join()
    bob3.join()
    bob4.join()
    bob5.join()
    bob6.join()

    rpc("/forget/acc", acc_alice, acc_bob1,acc_bob2,acc_bob3,acc_bob4,acc_bob5)
    rpc("/forget/ctc", ctc_alice)


if __name__ == "__main__":
    main()
