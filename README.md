# Proving-time scenarios

Read [Mandatory Proofs: Proving Times](https://jsign.github.io/proving-time-scenarios/).

The documentation source is in [`docs/`](docs/).

## Check the book

Install the documentation dependencies:

```sh
python3 -m pip install --requirement requirements-docs.txt
```

Run the local checks:

```sh
npx --yes markdownlint-cli2@0.23.2 "README.md" "docs/**/*.md"
python3 scripts/check_diagrams.py
mkdocs build --strict
```

Start the local site for a visual review:

```sh
mkdocs serve
```
