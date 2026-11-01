# @perrylink/dsh-plugin-kit

> **Non-official companion tool.** Part of the DSH standards family; not a certification, accreditation, security audit, or official endorsement. Standard: https://github.com/PerryLink/dsh-standards. The `dsh.standards` block is a `not-run` placeholder, not a pass.


```sh
dsh plugin --profile <name> add @perrylink/dsh-plugin-kit
```


Shared **zero-runtime-dependency** toolkit for the PerryLink DSH plugin repositories. The per-project audit found 20+ plugins hand-rolling the same Provider seam and duplicating the same sanitize/pricing/verdict shapes, so this package extracts all of it — the pluggable Provider seam, the fail-closed approval and adaptive session-event gates, the mechanical verify scripts, and the shared sanitize/pricing/judge pure modules — into one ESM + TypeScript package.

> **Package name.** This project publishes to npm as **`@perrylink/dsh-plugin-kit`**. The bare npm name `dsh-plugin-kit` belongs to a different, unrelated project — installing it does not install this package.

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add @perrylink/dsh-plugin-kit` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking).

[![npm version](https://img.shields.io/npm/v/@perrylink/dsh-plugin-kit)](https://www.npmjs.com/package/@perrylink/dsh-plugin-kit)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)
[![DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)
[![Node](https://img.shields.io/badge/node-%5E22.19%20%7C%7C%20%3E%3D24-brightgreen.svg)](#)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/dsh-plugin-kit)
[![CI](https://img.shields.io/github/actions/workflow/status/PerryLink/dsh-plugin-kit/ci.yml?branch=main&label=CI)](https://github.com/PerryLink/dsh-plugin-kit/actions)
[![Version](https://img.shields.io/github/v/tag/PerryLink/dsh-plugin-kit?label=version)](https://github.com/PerryLink/dsh-plugin-kit/releases)
[![npm downloads](https://img.shields.io/npm/dm/@perrylink/dsh-plugin-kit)](https://www.npmjs.com/package/@perrylink/dsh-plugin-kit)
[![dshfind](https://dshfind.com/api/badge/PerryLink/dsh-plugin-kit?metric=downloads)](https://dshfind.com/plugins/PerryLink/dsh-plugin-kit?ref=badge)

**English** | [简体中文](README-zh.md) | [Español](README-es.md) | [Português](README-pt.md) | [हिन्दी](README-hi.md)

Shared **zero-runtime-dependency** toolkit for the PerryLink DSH plugin
repositories. The per-project audit found 20+ plugins hand-rolling
the same Provider seam and duplicating the same sanitize/pricing/verdict
shapes, so this package extracts all of it — the pluggable Provider seam, the
fail-closed approval and adaptive session-event gates, the mechanical verify
scripts, and the shared sanitize/pricing/judge pure modules — into one
ESM + TypeScript package.

## Install & uninstall

As a library, install is `pnpm add` (see Quick start). The package also ships an
intentionally empty `dsh.bundle.patch` layer (`cordis.patch.yml`), so it flows
through the harness bundle channel when a profile wants the kit mounted as a
package:

```sh
# npm channel (published releases)
dsh plugin --profile web add @perrylink/dsh-plugin-kit

# git channel (latest master)
dsh plugin --profile web add github:PerryLink/dsh-plugin-kit
```

Remove with:

```sh
pnpm remove @perrylink/dsh-plugin-kit
```

Nothing registers global state: uninstall is exactly the reverse of install.

## What is dsh-plugin-kit?

Shared **zero-runtime-dependency** toolkit for the PerryLink DSH plugin repositories. The per-project audit found 20+ plugins hand-rolling the same Provider seam and duplicating the same sanitize/pricing/verdict shapes, so this package extracts all of it — the pluggable Provider seam, the fail-closed approval and adaptive session-event gates, the mechanical verify scripts, and the shared sanitize/pricing/judge pure modules — into one ESM + TypeScript package.

![Workflow diagram for dsh-plugin-kit: call → plugin → result.](docs/assets/dsh-plugin-kit-flow.svg)

*Workflow overview: call → plugin → result. The examples below use the real command surface.*



## Compatibility

- **DSH harness**: the kit imports nothing from `@deepseek-ai/*` at runtime.
  `@deepseek-ai/cordis` (`^4.0.5-alpha.1`), `@deepseek-ai/schemastery`
  (`^3.18.5-alpha.1`), and the `@deepseek-ai/dsh-*` packages are **optional**
  peer dependencies in the `>=0.1.2-rc.1 <0.2.0 || >=0.1.5-alpha.1 <0.2.0 || >=0.1.6-0 <0.2.0 || >=0.1.7-0 <0.2.0 || >=0.2.0-0 <0.3.0 || >=0.2.1-0 <0.3.0`
  band the PerryLink plugin repos share; they exist only for type
  interop. Verified 2026-09-11 against the dsh-v0.1.7-alpha.1 master checkout
  (full gate chain + profile install smoke), and re-verified 2026-10-05 against
  the `dsh-v0.2.1-alpha.1` checkout (full gate chain + profile install smoke).
- **Node**: `^22.19.0 || >=24.0.0`, ESM only.
- **Wire compatibility**: names and shapes mirror `dsh-mask` (sanitize),
  `dsh-budget` (pricing), and `dsh-auto-review` (judge and the
  `fallbackPolicy` vocabulary), so migration is mechanical.

## What you get

- **Zero runtime dependencies** — the pure core (`seam`, `gates`, `shared`)
  is browser-safe.
- **ESM + strict TypeScript** — JSDoc contracts on every module; `strict`,
  `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`.
- **Fail-closed and adaptive gates** — approval never defaults to a grant;
  session-event appends degrade gracefully on hosts that reject unknown event
  types.
- **A new-plugin skeleton** — `template/` with `cordis.yml`, a three-role
  `src/index.ts` (Service Definition / Provider / Consumer), a test, and the
  shared Renovate preset.

## Quick start

```sh
dsh plugin --profile web add github:PerryLink/dsh-plugin-kit
```

From npm:

```sh
pnpm add @perrylink/dsh-plugin-kit
```

From git (the `prepare` script builds `lib/` using only production
dependencies):

```sh
pnpm add github:PerryLink/dsh-plugin-kit
```

Replace a hand-rolled registry in one step:

```ts
import { ProviderRegistry } from '@perrylink/dsh-plugin-kit/seam'

const registry = new ProviderRegistry<Detector>({
  default: { name: 'regex', impl: new RegexDetector() },
})
ctx.effect(() => registry.register('ner', new NerDetector()))
const active = registry.use('ner') ?? registry.use()
```

### Examples

These are the plugin's real entry points; install once, then call one.

#### Detailed example

**Command**

~~~sh
import { createStripper } from '@perrylink/dsh-plugin-kit/shared'
createStripper().strip('call 13800138000 or email a@b.com')
~~~

**Output**

~~~text
call <PHONE_1> or email <EMAIL_1>
~~~

*Observed from `README.md:153 (shared sanitize); src/shared/sanitize.ts:268; test/sanitize.test.ts:8-19`*

#### Failure branch

**Input**

~~~text
const r = new ProviderRegistry(); r.register('openai', impl); r.register('openai', impl)  // second call
~~~

**Output**

~~~text
Error: Provider "openai" is already registered
~~~

*Observed from `plugins/dsh-plugin-kit/lib/seam/provider.js:55-58; plugins/dsh-plugin-kit/test/seam.test.ts:27-30; plugins/dsh-plugin-kit/README.md:164`*

#### Brief examples

- `applyFailClosed`
- `parseVerdict`

## Configuration

No runtime configuration: the gates and helpers are pure functions. The only
configuration surface is `cordis.patch.yml`, the bundle-patch layer shipped
for harness profile composition; it mounts no plugin row (the kit is a
library) and documents how consuming plugins add their own rows.

## Tools & surfaces

| Subpath | Purpose |
|---|---|
| `seam` | `ProviderRegistry<T>` — reversible, fail-loud named provider registry. |
| `gates` | `applyFailClosed`; `makeEventGate` / `maybeAppendSessionEvent` / `probeIgnorableAppend`. |
| `shared` | `sanitize` (`Stripper`, `redactText`, `redactMapping`, `sanitizeText`, `sanitizeUrl`), `pricing` (`BUILTIN_PRICES`, `estimateUsageCost`, `tokenCarbon`, `latencyStats`, `formatMoney`, `formatTokens`), `judge` (`parseVerdict`, `VERDICT_SCHEMA`, `riskExceeds`). |
| `verify` | Mechanical CI gates (`verify-license`, `verify-readme-languages`, `verify-seam`) with a `VerifyReport` and a non-zero-exit CLI: `node lib/verify/cli.js all .` |
| `template/` | New-plugin skeleton (`cordis.yml`, three-role plugin, test, README, `renovate.json5`). |
| root barrel | Re-exports all of the above. |

## Permissions & data

The kit performs no I/O, no network access, and no subprocess spawns on its
own. `Stripper` keeps placeholder→original mappings in memory only, and
`stats()`/`redactMapping()` never emit plaintext; a consumer that persists a
mapping owns that decision and its storage permissions.

## Security boundaries

- `sanitize`/`redact*` are **display hygiene**, not a security boundary: they
  reduce leakage into logs and results, they do not authenticate or authorize.
- Approval gates are fail closed by default (`rejected`); the only grant path
  is an explicit `allow-once` opt-in.
- Session-event appends the host refuses are skipped, never retried in a way
  that could break session resume.
- Report vulnerabilities via GitHub Security Advisories — see `SECURITY.md`.

## Known limitations

- Hosts whose `Session.append` third argument is a `SurfaceIntent`
  (`0.1.2-rc.1`) throw `validateNext` on the ignorable-envelope probe; the
  gate degrades to skip-unknown, so audit events are dropped (fail closed)
  rather than logged on those hosts.
- 0.1.2-rc.1 (adapted 2026-09-02): the session envelope keeps its ignorable field for stored-log read compatibility only - Session.append still cannot stamp it, so audit-gate behavior is unchanged.
- The kit ships no browser UI half; it is a library consumed by the Host (and
  optionally Client) halves of other plugins.

## Development

```sh
pnpm install
pnpm run typecheck        # tsc --noEmit
pnpm run typecheck:ci     # CI face: tsc -p tsconfig.ci.json --noEmit
pnpm test                 # vitest unit tests
pnpm run build            # emit lib/ + declarations (also run by prepare)
pnpm run verify:self-contained
pnpm run verify:artifacts
```

## Topics

This repository is also the maintenance hub for the ecosystem:
`scripts/sync-peer-range.mjs` re-pins the shared peer band across every repo in
the target directory in
one command, `renovate/default.json5` is the shared Renovate preset every repo
extends, `.github/workflows/npm-publish.yml` is a reusable tag-triggered
publish workflow (needs only an `NPM_TOKEN` secret), and `data/repos.json` is
the ecosystem registry consumed by the portal. Read that file for the roster; the per-plugin READMEs carry the collapsed list. See
[docs/ecosystem-tooling.md](docs/ecosystem-tooling.md).

Keywords: dsh, dsh-plugin, deepseek-harness, deepseek, cordis, perrylink,
provider, seam, approval, sanitize, pricing, judge.

## Contributors

Maintained by [PerryLink](https://github.com/PerryLink) with contributions
from the DSH plugin ecosystem.

## PerryLink DSH Plugin Family

This project is part of the DeepSeek Harness plugin family from [PerryLink](https://github.com/PerryLink). The roster stays collapsed below so every README keeps a short first screen; expand it to see every row and its status.

<details>
<summary>Expand all plugins</summary>

| Plugin | Status |
|---|---|
| **[dsh-aqua-input-check](https://github.com/PerryLink/dsh-aqua-input-check)** |  |
| **[dsh-archive-check](https://github.com/PerryLink/dsh-archive-check)** |  |
| **[dsh-auto-review](https://github.com/PerryLink/dsh-auto-review)** |  |
| **[dsh-autotier](https://github.com/PerryLink/dsh-autotier)** | 🧊 FROZEN — see the repo README |
| **[dsh-bid-ca-precheck](https://github.com/PerryLink/dsh-bid-ca-precheck)** |  |
| **[dsh-bid-qual-check](https://github.com/PerryLink/dsh-bid-qual-check)** |  |
| **[dsh-cert-mcp](https://github.com/PerryLink/dsh-cert-mcp)** | 🧊 FROZEN — see the repo README |
| **[dsh-checkpoint-rewind](https://github.com/PerryLink/dsh-checkpoint-rewind)** |  |
| **[dsh-click](https://github.com/PerryLink/dsh-click)** |  |
| **[dsh-composer-history](https://github.com/PerryLink/dsh-composer-history)** |  |
| **[dsh-contract-stance](https://github.com/PerryLink/dsh-contract-stance)** |  |
| **[dsh-customs-doc-check](https://github.com/PerryLink/dsh-customs-doc-check)** |  |
| **[dsh-data-quality](https://github.com/PerryLink/dsh-data-quality)** |  |
| **[dsh-demurrage-ledger](https://github.com/PerryLink/dsh-demurrage-ledger)** |  |
| **[dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck)** |  |
| **[dsh-drill-script-check](https://github.com/PerryLink/dsh-drill-script-check)** |  |
| **[dsh-eia-guide-check](https://github.com/PerryLink/dsh-eia-guide-check)** |  |
| **[dsh-emergency-plan](https://github.com/PerryLink/dsh-emergency-plan)** |  |
| **[dsh-essay-rubric-check](https://github.com/PerryLink/dsh-essay-rubric-check)** |  |
| **[dsh-evidence-check](https://github.com/PerryLink/dsh-evidence-check)** |  |
| **[dsh-export-ctl-check](https://github.com/PerryLink/dsh-export-ctl-check)** |  |
| **[dsh-fast](https://github.com/PerryLink/dsh-fast)** |  |
| **[dsh-fmea-table-check](https://github.com/PerryLink/dsh-fmea-table-check)** |  |
| **[dsh-forecast-penalty](https://github.com/PerryLink/dsh-forecast-penalty)** |  |
| **[dsh-fund-research](https://github.com/PerryLink/dsh-fund-research)** |  |
| **[dsh-github](https://github.com/PerryLink/dsh-github)** |  |
| **[dsh-gongwen-flow-check](https://github.com/PerryLink/dsh-gongwen-flow-check)** |  |
| **[dsh-gongwen-word-check](https://github.com/PerryLink/dsh-gongwen-word-check)** |  |
| **[dsh-guard-plan-qc](https://github.com/PerryLink/dsh-guard-plan-qc)** |  |
| **[dsh-hazchem-check](https://github.com/PerryLink/dsh-hazchem-check)** |  |
| **[dsh-hazplan-check](https://github.com/PerryLink/dsh-hazplan-check)** |  |
| **[dsh-hidden-risk-map](https://github.com/PerryLink/dsh-hidden-risk-map)** |  |
| **[dsh-hs-classify](https://github.com/PerryLink/dsh-hs-classify)** |  |
| **[dsh-icd-rule-check](https://github.com/PerryLink/dsh-icd-rule-check)** |  |
| **[dsh-industry-research](https://github.com/PerryLink/dsh-industry-research)** |  |
| **[dsh-lawcite-adapter](https://github.com/PerryLink/dsh-lawcite-adapter)** |  |
| **[dsh-laya](https://github.com/PerryLink/dsh-laya)** |  |
| **[dsh-lc-doc-check](https://github.com/PerryLink/dsh-lc-doc-check)** |  |
| **[dsh-learning-gap-check](https://github.com/PerryLink/dsh-learning-gap-check)** |  |
| **[dsh-library](https://github.com/PerryLink/dsh-library)** |  |
| **[dsh-local-ai](https://github.com/PerryLink/dsh-local-ai)** |  |
| **[dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions)** |  |
| **[dsh-mask](https://github.com/PerryLink/dsh-mask)** |  |
| **[dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel)** |  |
| **[dsh-medrec-qc](https://github.com/PerryLink/dsh-medrec-qc)** |  |
| **[dsh-memento](https://github.com/PerryLink/dsh-memento)** |  |
| **[dsh-nsfc-form-check](https://github.com/PerryLink/dsh-nsfc-form-check)** |  |
| **[dsh-nurse-record-check](https://github.com/PerryLink/dsh-nurse-record-check)** |  |
| **[dsh-observe](https://github.com/PerryLink/dsh-observe)** |  |
| **[dsh-origin-rvc-check](https://github.com/PerryLink/dsh-origin-rvc-check)** |  |
| **[dsh-ota-review-check](https://github.com/PerryLink/dsh-ota-review-check)** |  |
| **[dsh-output-styles](https://github.com/PerryLink/dsh-output-styles)** |  |
| **[dsh-paper-doc-adapter](https://github.com/PerryLink/dsh-paper-doc-adapter)** |  |
| **[dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules)** |  |
| **[dsh-permit-report-check](https://github.com/PerryLink/dsh-permit-report-check)** |  |
| **[dsh-pipeline-check](https://github.com/PerryLink/dsh-pipeline-check)** |  |
| **[dsh-pleading-draft](https://github.com/PerryLink/dsh-pleading-draft)** |  |
| **[dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor)** |  |
| **[dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide)** |  |
| **[dsh-plugin-kit](https://github.com/PerryLink/dsh-plugin-kit)** |  |
| **[dsh-plugin-upgrade](https://github.com/PerryLink/dsh-plugin-upgrade)** |  |
| **[dsh-policy-brief-draft](https://github.com/PerryLink/dsh-policy-brief-draft)** |  |
| **[dsh-power-loss-split](https://github.com/PerryLink/dsh-power-loss-split)** |  |
| **[dsh-power-ticket-check](https://github.com/PerryLink/dsh-power-ticket-check)** |  |
| **[dsh-ppap-check](https://github.com/PerryLink/dsh-ppap-check)** |  |
| **[dsh-protest-deadline](https://github.com/PerryLink/dsh-protest-deadline)** |  |
| **[dsh-railway-window](https://github.com/PerryLink/dsh-railway-window)** |  |
| **[dsh-repair-order-qc](https://github.com/PerryLink/dsh-repair-order-qc)** |  |
| **[dsh-research-report](https://github.com/PerryLink/dsh-research-report)** |  |
| **[dsh-review-reply-check](https://github.com/PerryLink/dsh-review-reply-check)** |  |
| **[dsh-rulefile-check](https://github.com/PerryLink/dsh-rulefile-check)** |  |
| **[dsh-safety-brief-check](https://github.com/PerryLink/dsh-safety-brief-check)** |  |
| **[dsh-score](https://github.com/PerryLink/dsh-score)** |  |
| **[dsh-session-sync](https://github.com/PerryLink/dsh-session-sync)** |  |
| **[dsh-site-log-check](https://github.com/PerryLink/dsh-site-log-check)** |  |
| **[dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security)** |  |
| **[dsh-soe-decision-check](https://github.com/PerryLink/dsh-soe-decision-check)** |  |
| **[dsh-soilwater-check](https://github.com/PerryLink/dsh-soilwater-check)** |  |
| **[dsh-sop-sync-check](https://github.com/PerryLink/dsh-sop-sync-check)** |  |
| **[dsh-spc-gbt-adapter](https://github.com/PerryLink/dsh-spc-gbt-adapter)** |  |
| **[dsh-talk](https://github.com/PerryLink/dsh-talk)** |  |
| **[dsh-tender-extract](https://github.com/PerryLink/dsh-tender-extract)** |  |
| **[dsh-tender-matrix](https://github.com/PerryLink/dsh-tender-matrix)** |  |
| **[dsh-test-drive](https://github.com/PerryLink/dsh-test-drive)** |  |
| **[dsh-ticktick](https://github.com/PerryLink/dsh-ticktick)** |  |
| **[dsh-translate](https://github.com/PerryLink/dsh-translate)** |  |
| **[dsh-warranty-calc](https://github.com/PerryLink/dsh-warranty-calc)** |  |
| **[dsh-community-bench](https://github.com/PerryLink/dsh-community-bench)** | 🧊 FROZEN — see the repo README |
| **[dsh-budget](https://github.com/PerryLink/dsh-budget)** | 🧊 FROZEN — see the repo README |
| **[dsh-claude-move](https://github.com/PerryLink/dsh-claude-move)** | 🧊 FROZEN — see the repo README |
| **[dsh-defend](https://github.com/PerryLink/dsh-defend)** | 🧊 FROZEN — see the repo README |
| **[dsh-draw](https://github.com/PerryLink/dsh-draw)** | 🧊 FROZEN — see the repo README |
| **[dsh-reach](https://github.com/PerryLink/dsh-reach)** | 🧊 FROZEN — see the repo README |
| **[dsh-background-agents](https://github.com/PerryLink/dsh-background-agents)** | 🚫 RETIRED — see the repo README |
| **[dsh-session-pin](https://github.com/PerryLink/dsh-session-pin)** | 🚫 RETIRED — see the repo README |
| **[dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms)** | 🚫 RETIRED — see the repo README |

</details>

## License

Apache-2.0 — see [LICENSE](LICENSE).
