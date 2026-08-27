# Mandatory Proofs: Proving Times

## Scope

A mandatory execution proof is a proof that the protocol requires for block validity or fork choice.
This guide compares three hypothetical designs for these proofs on Ethereum.

The baseline assumes a post-Glamsterdam protocol with ePBS from
[EIP-7732](https://eips.ethereum.org/EIPS/eip-7732).
The [Glamsterdam meta EIP](https://eips.ethereum.org/EIPS/eip-7773) schedules EIP-7732 for inclusion.

The other scenarios add [EIP-7862](https://eips.ethereum.org/EIPS/eip-7862) or
[EIP-7886](https://eips.ethereum.org/EIPS/eip-7886) to this baseline.
Neither EIP defines mandatory execution proofs.
Therefore, every scenario in this guide is hypothetical.

This guide assumes that each payload builder also generates the execution proof for its payload.
Independent proof producers are outside the scope.

## Read the guide

<div class="grid cards" markdown>

- **Foundations**

    ---

    Learn the actors, ePBS slot timing, proving-time terms, and builder proof model.

    [Read the foundations](foundations.md){ .md-button }

- **Three scenarios**

    ---

    Compare the [ePBS baseline](scenarios/epbs-baseline.md),
    [delayed state root](scenarios/delayed-state-root.md), and
    [delayed execution](scenarios/delayed-execution.md).

- **Evaluation**

    ---

    Examine gas-limit implications, timing conditions, and proof responsibilities.

    [Compare the designs](evaluation.md){ .md-button }

</div>
