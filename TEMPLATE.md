# Template Usage

This is a template repository, however the template does not transfer issues. Here is how to transfer it:

## Pre-requisites

- Copilot CLI (https://github.com/features/copilot/cli)
- Github CLI (https://cli.github.com/)
- Authenticated through Github CLI (`gh auth login`)

## Get started

1. Use repository as a template.
2. Copy the link to the repository you made (e.g. https://github.com/aryxenv/contoso-finance-ai-tour-26)
3. Clone your repo

```bash
git clone <YOUR_REPO_URL> # replace with your repo url (e.g. https://github.com/aryxenv/contoso-finance-ai-tour-26)
```

4. Clone the template repo & navigate to it

```bash
git clone https://github.com/aryxenv/contoso-finance
cd contoso-finance
```

5. Start Copilot CLI

```bash
copilot
```

6. Transfer prompt (on Plan Mode - `shift+tab` to switch) -> NOTE: REPLACE `<USER>` AND `<YOUR_REPO_NAME>`

```txt
Read all the issues available on the current git repo. these issues must be copied over to (NOT TRANSFERED) to
https://github.com/<USER>/<YOUR_REPO_NAME>, I am the owner of this so it should be possible through gh
cli. Include closed issues and update cross-references in issue bodies. Try to do as much in parallel as possible, where safe.
```

7. (optional) It may ask you some questions, select what you believe is best.
8. Select `autopilot + /fleet` option.
9. Let Copilot CLI do it's magic!

> [!TIP]
> To reduce agent hallucination, delete this file when doing the demo.
