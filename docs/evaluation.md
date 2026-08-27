# Evaluation

This chapter compares the timing effects of the three scenarios.

## Gas-limit implications

Ethereum used has a 60M gas limit. This analysis uses hypothetical targets of 200M, 300M, 500M, and 1 Ggas.

The table gives illustrative average rates of proof generation before all overheads.

| Reference interval | Timing basis | 60M baseline | 200M target | 300M target | 500M target | 1 Ggas target |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 6 seconds | `t=6` payload deadline to `t=12` next proposal | 10.0 Mgas/s | 33.3 Mgas/s | 50.0 Mgas/s | 83.3 Mgas/s | 166.7 Mgas/s |
| 9 seconds | Rounded proof start at `t≈0` to assumed availability at `t=9` | 6.7 Mgas/s | 22.2 Mgas/s | 33.3 Mgas/s | 55.6 Mgas/s | 111.1 Mgas/s |

The calculation is `gas limit / reference interval`.
If the actual proof start or deadline changes, the required rate also changes.
Overheads reduce net proving time. Therefore, the required proving rate increases.

We assume that gas is proportional to zkVM proving work. This requires zkEVM-aware gas repricing or a zkEVM dimension in a multidimensional gas model.

## Proving-time comparison

The assessment considers mandatory-proof timing only. It does not evaluate other protocol benefits.

| Scenario | Timing result | Work or responsibility | Main limit |
| --- | --- | --- | --- |
| ePBS baseline | The 9-second reference requires the explicit `t≈0` and `t=9` assumptions. | It does not reduce proof work. | ePBS defines validation budgets, not a proof window. |
| Delayed state root | It adds no proving time. | It can remove an estimated 8% from the hot path if proof `N` does not require root `N`. | The estimate was done under a specific zkEVM for mainnet blocks, and might change after Glamsterdam. Note that two proofs can add aggregation overhead. |
| Delayed execution | The builder-owned model gains no time. The next-slot model has at most 6 seconds before overheads. | Candidate builders for `N+1` repeat proof `N` and give it to the beacon proposer. | The design shifts proof responsibility to slot `N+1`, which might have second-order effects. |
