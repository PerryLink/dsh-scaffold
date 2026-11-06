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
`package.json`, `src/index.ts`, this README and `cordis.patch.yml`;
`<plugin-id>` in `cordis.patch.yml`; `<One-line purpose.>` in `package.json`
and this README.

## Standards (fill before publishing)

The optional `dsh.standards` block in `package.json` starts as a placeholder, not a claim.
Run `npx dsh-standards@1.2.2 . --scope entry --entry-claim static --format json --out entry.json`
and replace it with the recorded output.
With no evidence, keep `not-run` / `not-measured`; never write `PASS` without a recorded gate, journey or benchmark.

The same statuses live in `standards.json`. The three levels are adoption
depths, not grades or certification; the public teaching copy is
[dsh-plugin-guide/guide/standards.md](https://github.com/PerryLink/dsh-plugin-guide/blob/main/guide/standards.md).
