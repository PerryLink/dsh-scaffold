# <PLUGIN_NAME>

<One-line purpose.>

## Seam roles

- **Service Definition** — `src/index.ts` (`MyCapability` interface).
- **Service Provider** — `src/index.ts` (default + `fast` implementations registered via `ProviderRegistry`).
- **Consumer** — `src/index.ts` (`apply` resolves and uses the active provider).

## Configuration

See `cordis.patch.yml` for the Config fields. Keep that exact filename:
`package.json` lists it in `files` and points `dsh.bundle.patch` at it.

## Capabilities and labels

`dsh.capabilities` and `dsh.labels` ship as empty arrays because this skeleton
does not call a Harness host surface yet. Declare only the capability IDs the
plugin actually uses (`fs:read`, `fs:write`, `shell`, `subprocess`,
`network:egress`, `network:ingress`, `credentials:read`, `credentials:list`,
`credentials:provider`, `llm:adapter`, `sessions:read`, `system-prompt:write`,
`tools:register`, `remote:expose`, `plugin:install`): every undeclared static
trigger is a C-11 failure. Leave `dsh.labels` empty unless a disclosure label
applies (`prompt-modification`, `red-team`, `third-party-model-provider`,
`remote-access`, `mirror`).

## Development

```sh
pnpm install
pnpm test
```

Replace every `<PLACEHOLDER>` token before publishing: `<PLUGIN_NAME>` in
`package.json`, `src/index.ts`, this README, `cordis.patch.yml` and
`SECURITY.md`; `<OWNER>` in `SECURITY.md`; `<plugin-id>` in
`cordis.patch.yml`; `<One-line purpose.>` in `package.json` and this README.

## Security

A DSH plugin runs in the host's process, as your user, with your permissions:
there is no runtime sandbox around loaded plugin code, and `dsh.capabilities` is
a declaration the host does not enforce. Treat the manifest as disclosure, not
as a boundary.

- **Least privilege.** `dsh.capabilities` ships as `[]` and
  `security.permissions` declares no files, network, credentials, shell, or
  subprocess use — both are true only while the skeleton stays this small. Add
  the capability ID and the permission entry as soon as you touch a surface;
  deleting a declaration does not remove the ability.
- **Credentials.** Resolve per operation with
  `ctx.credentials.resolve(credentialRef('NAME'))`; use `describe()` for a UI.
  Never log, persist, put in `argv`, or forward a value. Never read
  `~/.ssh`, `~/.aws`, `~/.netrc`, `.npmrc`, or the credential backing file.
- **Egress.** Keep a constant `https` allowlist, fetch no URL supplied by a
  model or a tool result, check redirects hop by hop, and disclose third-party
  endpoints. The host has no egress policy; this is the plugin's own discipline.
- **Output is untrusted.** Tool results, web pages, files, and session text are
  data, not instructions. Validate against `output.schema` and wrap external
  text before it reaches a prompt; escape it before it reaches HTML or a shell.
- **Lifecycle scripts.** The template has no `preinstall`/`install`/
  `postinstall`/`prepare`. Keep it that way; `--ignore-scripts` stops install
  scripts only, not the code the host loads.
- **Disclosure.** `security.permissions` is a draft, non-host field: it is not
  read or enforced. `dsh.commitments` and `dsh.disclosure` are optional — leave
  them out rather than filling in claims you cannot support.
- **Reporting.** `SECURITY.md` names the private advisory channel and the
  supported versions. Report privately; do not open a public issue.

The full boundary and the proposed `DSC-15`–`DSC-22` checks are in
[dsh-plugin-guide/docs/security.md](https://github.com/PerryLink/dsh-plugin-guide/blob/main/docs/security.md).

## Standards (fill before publishing)

The optional `dsh.standards` block in `package.json` starts as a placeholder, not a claim.
Run `npx dsh-standards@1.2.2 . --scope entry --entry-claim static --format json --out entry.json`
and replace it with the recorded output.
With no evidence, keep `not-run` / `not-measured`; never write `PASS` without a recorded gate, journey or benchmark.

The same statuses live in `standards.json`. The three levels are adoption
depths, not grades or certification; the public teaching copy is
[dsh-plugin-guide/guide/standards.md](https://github.com/PerryLink/dsh-plugin-guide/blob/main/guide/standards.md).
