# dsh-scaffold

> **Renamed:** previously `@perrylink/dsh-plugin-kit`; now **`dsh-scaffold`**. Old repo stays as a pointer/backup. New home: https://github.com/PerryLink/dsh-scaffold


Kit compartilhado **sem dependências em tempo de execução** para os repositórios de plugins DSH da PerryLink. A auditoria por projeto encontrou mais de 20 plugins reimplementando o mesmo seam Provider e duplicando as mesmas formas de sanitização, precificação e veredicto, então este pacote extrai tudo isso — o seam Provider plugável, as portas de aprovação fail-closed e de eventos de sessão adaptativos, os scripts de verificação mecânica e os módulos puros sanitize/pricing/judge — em um único pacote ESM + TypeScript.

> **Nome do pacote.** Este projeto é publicado no npm como **`dsh-scaffold`**. O nome simples `dsh-scaffold` pertence a outro projeto não relacionado — instalá-lo não instala este pacote.

- **Canal da loja 1024**: primeiro `npm i -g dsh1024`, depois `dsh1024 plugin --profile web add dsh-scaffold` (conta para o ranking de instalações do [deepseek1024.com](https://deepseek1024.com)).

[![npm version](https://img.shields.io/npm/v/dsh-scaffold)](https://www.npmjs.com/package/dsh-scaffold)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)
[![DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)
[![Node](https://img.shields.io/badge/node-%5E22.19%20%7C%7C%20%3E%3D24-brightgreen.svg)](#)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/dsh-scaffold)
[![CI](https://img.shields.io/github/actions/workflow/status/PerryLink/dsh-scaffold/ci.yml?branch=main&label=CI)](https://github.com/PerryLink/dsh-scaffold/actions)
[![Version](https://img.shields.io/github/v/tag/PerryLink/dsh-scaffold?label=version)](https://github.com/PerryLink/dsh-scaffold/releases)
[![npm downloads](https://img.shields.io/npm/dm/dsh-scaffold)](https://www.npmjs.com/package/dsh-scaffold)
[![dshfind](https://dshfind.com/api/badge/PerryLink/dsh-scaffold?metric=downloads&lang=pt)](https://dshfind.com/pt/plugins/PerryLink/dsh-scaffold?ref=badge)

[English](README.md) | [简体中文](README-zh.md) | [Español](README-es.md) | **Português** | [हिन्दी](README-hi.md)

```sh
dsh plugin --profile <name> add dsh-scaffold
```


Kit compartilhado **sem dependências em tempo de execução** para os
repositórios de plugins DSH da PerryLink. A auditoria por projeto encontrou
mais de 20 plugins reimplementando o mesmo seam Provider e duplicando
as mesmas formas de sanitização, precificação e veredicto, então este pacote
extrai tudo isso — o seam Provider plugável, as portas de aprovação
fail-closed e de eventos de sessão adaptativos, os scripts de verificação
mecânica e os módulos puros sanitize/pricing/judge — em um único pacote
ESM + TypeScript.

## What is dsh-scaffold?

Kit compartilhado **sem dependências em tempo de execução** para os repositórios de plugins DSH da PerryLink. A auditoria por projeto encontrou mais de 20 plugins reimplementando o mesmo seam Provider e duplicando as mesmas formas de sanitização, precificação e veredicto, então este pacote extrai tudo isso — o seam Provider plugável, as portas de aprovação fail-closed e de eventos de sessão adaptativos, os scripts de verificação mecânica e os módulos puros sanitize/pricing/judge — em um único pacote ESM + TypeScript.

![Diagrama de fluxo de dsh-scaffold: chamada → plugin → resultado.](docs/assets/dsh-scaffold-flow.svg)

*Visão geral do fluxo: chamada → plugin → resultado. Os exemplos abaixo usam a superfície real de comandos.*


*A mesma execução, animada.*

## Compatibilidade

- **DSH harness**: o kit não importa nada de `@deepseek-ai/*` em tempo de
  execução. `@deepseek-ai/cordis` (`^4.0.5-alpha.1`), `@deepseek-ai/schemastery`
  (`^3.18.5-alpha.1`) e os pacotes `@deepseek-ai/dsh-*` são peer dependencies
  **opcionais** na faixa `>=0.1.2-rc.1 <0.2.0 || >=0.1.5-alpha.1 <0.2.0 || >=0.1.6-0 <0.2.0 || >=0.1.7-0 <0.2.0 || >=0.2.0-0 <0.3.0 || >=0.2.1-0 <0.3.0` compartilhada pelos repos de plugins da PerryLink;
  existem apenas para interoperação de tipos. Verificado em 2026-09-11 contra
  o checkout master `dsh-v0.1.7-alpha.1` (cadeia completa de portas + smoke
  de instalação de perfil), e re-verificado em 2026-10-05 contra o checkout
  `dsh-v0.2.1-alpha.1` (cadeia completa de portas + smoke de instalação de perfil).
- **Node**: `^22.19.0 || >=24.0.0`, somente ESM.
- **Compatibilidade de formato**: nomes e formas espelham `dsh-mask`
  (sanitize), `dsh-budget` (pricing) e `dsh-auto-review` (judge e o
  vocabulário `fallbackPolicy`), então a migração é mecânica.

## O que você recebe

- **Zero dependências em tempo de execução** — o núcleo puro (`seam`,
  `gates`, `shared`) é seguro para o navegador.
- **ESM + TypeScript estrito** — contratos JSDoc em cada módulo; `strict`,
  `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`.
- **Portas fail-closed e adaptativas** — a aprovação nunca concede por
  padrão; os eventos de sessão degradam com elegância em hosts que rejeitam
  tipos de evento desconhecidos.
- **Esqueleto de plugin** — `template/` com `cordis.yml`, um `src/index.ts`
  de três papéis (Service Definition / Provider / Consumer), um teste e o
  preset compartilhado do Renovate.

## Início rápido

```sh
dsh plugin --profile web add github:PerryLink/dsh-scaffold
```

Pelo npm:

```sh
pnpm add dsh-scaffold
```

Pelo git (o script `prepare` constrói `lib/` usando apenas dependências de
produção):

```sh
pnpm add github:PerryLink/dsh-scaffold
```

Substitua um registro escrito à mão em um passo:

```ts
import { ProviderRegistry } from 'dsh-scaffold/seam'

const registry = new ProviderRegistry<Detector>({
  default: { name: 'regex', impl: new RegexDetector() },
})
ctx.effect(() => registry.register('ner', new NerDetector()))
const active = registry.use('ner') ?? registry.use()
```

## Instalar e desinstalar

A instalação é `pnpm add` (ver Início rápido). O pacote também traz uma camada `dsh.bundle.patch` deliberadamente vazia (`cordis.patch.yml`), então ele também flui pelo canal bundle do harness quando um perfil quer montar o kit como pacote:

```sh
# canal npm (versões publicadas)
dsh plugin --profile web add dsh-scaffold

# canal git (master mais recente)
dsh plugin --profile web add github:PerryLink/dsh-scaffold
```

Para remover:

```sh
pnpm remove dsh-scaffold
```

Nada registra estado global: desinstalar é exatamente o inverso de instalar.

### Exemplos

São os pontos de entrada reais; instale e chame um.

#### Exemplo detalhado

**Comando**

~~~sh
import { createStripper } from 'dsh-scaffold/shared'
createStripper().strip('call 13800138000 or email a@b.com')
~~~

**Saída**

~~~text
call <PHONE_1> or email <EMAIL_1>
~~~

*Observado em `README.md:153 (shared sanitize); src/shared/sanitize.ts:268; test/sanitize.test.ts:8-19`*

#### Ramo de falha

**Entrada**

~~~text
const r = new ProviderRegistry(); r.register('openai', impl); r.register('openai', impl)  // second call
~~~

**Saída**

~~~text
Error: Provider "openai" is already registered
~~~

*Observado em `plugins/dsh-scaffold/lib/seam/provider.js:55-58; plugins/dsh-scaffold/test/seam.test.ts:27-30; plugins/dsh-scaffold/README.md:164`*

#### Exemplos breves

- `applyFailClosed`
- `parseVerdict`

## Configuração

Sem configuração em tempo de execução: as portas e utilitários são funções
puras. A única superfície de configuração é `cordis.patch.yml`, a camada de
patch de bundle distribuída para a composição de perfis do harness; ela não
monta nenhuma linha de plugin (o kit é uma biblioteca) e documenta como
plugins consumidores adicionam as suas.

## Ferramentas e superfícies

| Subcaminho | Propósito |
|---|---|
| `seam` | `ProviderRegistry<T>` — registro nomeado de providers, reversível e que falha em voz alta. |
| `gates` | `applyFailClosed`; `makeEventGate` / `maybeAppendSessionEvent` / `probeIgnorableAppend`. |
| `shared` | `sanitize` (`Stripper`, `redactText`, `redactMapping`, `sanitizeText`, `sanitizeUrl`), `pricing` (`BUILTIN_PRICES`, `estimateUsageCost`, `tokenCarbon`, `latencyStats`, `formatMoney`, `formatTokens`), `judge` (`parseVerdict`, `VERDICT_SCHEMA`, `riskExceeds`). |
| `verify` | Portas CI mecânicas (`verify-license`, `verify-readme-languages`, `verify-seam`) com `VerifyReport` e CLI com saída não zero: `node lib/verify/cli.js all .` |
| `template/` | Esqueleto de plugin novo (`cordis.yml`, plugin de três papéis, teste, README, `renovate.json5`). |
| barrel raiz | Reexporta tudo acima. |

## Permissões e dados

O kit não faz E/S, acesso à rede nem subprocessos por conta própria. O
`Stripper` mantém os mapeamentos placeholder→original apenas em memória, e
`stats()`/`redactMapping()` nunca emitem texto puro; um consumidor que
persista um mapeamento é dono dessa decisão e das permissões de armazenamento.

## Limites de segurança

- `sanitize`/`redact*` são **higiene de exibição**, não um limite de
  segurança: reduzem vazamentos em logs e resultados, não autenticam nem
  autorizam.
- As portas de aprovação são fail-closed por padrão (`rejected`); o único
  caminho de concessão é uma opção explícita `allow-once`.
- Eventos de sessão que o host recusa são pulados, nunca tentados de novo de
  forma que possa quebrar a retomada da sessão.
- Reporte vulnerabilidades via GitHub Security Advisories — ver `SECURITY.md`.

## Limitações conhecidas

- Hosts cujo terceiro argumento de `Session.append` é um `SurfaceIntent`
  (`0.1.2-rc.1`) lançam `validateNext` na sonda do envelope ignorable; a
  porta degrada para pular-desconhecido, então eventos de auditoria são
  descartados (fail closed) nesses hosts em vez de registrados.
- 0.1.2-rc.1 (adaptado em 2026-09-02): o envelope de sessão mantém seu campo ignorable apenas para compatibilidade de leitura de logs armazenados - o Session.append ainda não consegue estampá-lo, então o comportamento da porta não muda.
- O kit não traz metade de UI de navegador: é uma biblioteca consumida pelas
  metades Host (e opcionalmente Client) de outros plugins.

## Desenvolvimento

```sh
pnpm install
pnpm run typecheck        # tsc --noEmit
pnpm run typecheck:ci     # face CI: tsc -p tsconfig.ci.json --noEmit
pnpm test                 # testes unitários vitest
pnpm run build            # emite lib/ e declarações (prepare também faz)
pnpm run verify:self-contained
pnpm run verify:artifacts
```

## Tópicos

Este repositório também é o hub de manutenção do ecossistema:
`scripts/sync-peer-range.mjs` reaponta a faixa de peers compartilhada em todos
os repos com um comando, `renovate/default.json5` é o preset compartilhado do
Renovate que todos estendem, `.github/workflows/npm-publish.yml` é um fluxo de
publicação reutilizável disparado por tag (precisa apenas de um segredo
`NPM_TOKEN`), e `data/repos.json` é o registro do ecossistema consumido pelo
portal. Ver [docs/ecosystem-tooling.md](docs/ecosystem-tooling.md).

Palavras-chave: dsh, dsh-plugin, deepseek-harness, deepseek, cordis, perrylink,
provider, seam, approval, sanitize, pricing, judge.

## Contribuidores

Mantido por [PerryLink](https://github.com/PerryLink) com contribuições do
ecossistema de plugins DSH.

## Licença

Apache-2.0 — ver [LICENSE](LICENSE).

## PerryLink DSH Plugin Family

Este projeto faz parte da família de plugins do DeepSeek Harness da [PerryLink](https://github.com/PerryLink). O registro fica recolhido abaixo para que cada README mantenha uma primeira tela curta; expanda para ver cada linha e seu status.

<details>
<summary>Expandir todos os plugins</summary>

| Plugin | Status |
|---|---|
| **[dsh-aqua-input-check](https://github.com/PerryLink/dsh-aqua-input-check)** |  |
| **[dsh-archive-check](https://github.com/PerryLink/dsh-archive-check)** |  |
| **[dsh-auto-review](https://github.com/PerryLink/dsh-auto-review)** |  |
| **[dsh-autotier](https://github.com/PerryLink/dsh-autotier)** |  |
| **[dsh-bid-ca-precheck](https://github.com/PerryLink/dsh-bid-ca-precheck)** |  |
| **[dsh-bid-qual-check](https://github.com/PerryLink/dsh-bid-qual-check)** |  |
| **[dsh-cert-mcp](https://github.com/PerryLink/dsh-cert-mcp)** |  |
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
| **[dsh-scaffold](https://github.com/PerryLink/dsh-scaffold)** |  |
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
| **[dsh-budget](https://github.com/PerryLink/dsh-budget)** | 🧊 CONGELADO — ver o README do repositório |
| **[dsh-claude-move](https://github.com/PerryLink/dsh-claude-move)** | 🧊 CONGELADO — ver o README do repositório |
| **[dsh-defend](https://github.com/PerryLink/dsh-defend)** | 🧊 CONGELADO — ver o README do repositório |
| **[dsh-draw](https://github.com/PerryLink/dsh-draw)** | 🧊 CONGELADO — ver o README do repositório |
| **[dsh-reach](https://github.com/PerryLink/dsh-reach)** | 🧊 CONGELADO — ver o README do repositório |
| **[dsh-background-agents](https://github.com/PerryLink/dsh-background-agents)** | 🚫 RETIRADO — ver o README do repositório |
| **[dsh-session-pin](https://github.com/PerryLink/dsh-session-pin)** | 🚫 RETIRADO — ver o README do repositório |
| **[dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms)** | 🚫 RETIRADO — ver o README do repositório |

</details>
