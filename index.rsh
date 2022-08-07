'reach 0.1'
export const main = Reach.App(() => {
    const Alice = Participant('Alice', {
        start_program: Fun([], Null),
    })
    const Bob_accs = API('Bob_accs', {
        optin_acc: Fun([], Null)
    })
    init()
    Alice.only(() => {
        interact.start_program()
    })

    Alice.publish()

    const [start_count] =
        parallelReduce([0])
            .invariant(balance() == 0)
            .while(start_count < 6)
            .api(Bob_accs.optin_acc,
                (k) => {
                    k(null);
                    return [start_count + 1];
                })

    commit()
    exit()
})
