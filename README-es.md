# dsh-scaffold

> **Renamed:** previously `@perrylink/dsh-plugin-kit`; now **`dsh-scaffold`**. Old repo stays as a pointer/backup. New home: https://github.com/PerryLink/dsh-scaffold


Kit compartido **sin dependencias en tiempo de ejecución** para los repositorios de plugins DSH de PerryLink. La auditoría por proyecto detectó que más de 20 plugins reimplementan el mismo seam Provider y duplican las mismas formas de sanitización, precios y veredictos, así que este paquete lo extrae todo — el seam Provider enchufable, las puertas de aprobación fail-closed y de eventos de sesión adaptativos, los scripts de verificación mecánica y los módulos puros sanitize/pricing/judge — en un único paquete ESM + TypeScript.

> **Nombre del paquete.** Este proyecto se publica en npm como **`dsh-scaffold`**. El nombre simple `dsh-scaffold` pertenece a otro proyecto no relacionado: instalarlo no instala este paquete.

- **Canal de la tienda 1024**: primero `npm i -g dsh1024`, luego `dsh1024 plugin --profile web add dsh-scaffold` (cuenta para el ranking de instalaciones de [deepseek1024.com](https://deepseek1024.com)).

[![npm version](https://img.shields.io/npm/v/dsh-scaffold)](https://www.npmjs.com/package/dsh-scaffold)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)
[![DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)
[![Node](https://img.shields.io/badge/node-%5E22.19%20%7C%7C%20%3E%3D24-brightgreen.svg)](#)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/dsh-scaffold)
[![CI](https://img.shields.io/github/actions/workflow/status/PerryLink/dsh-scaffold/ci.yml?branch=main&label=CI)](https://github.com/PerryLink/dsh-scaffold/actions)
[![Version](https://img.shields.io/github/v/tag/PerryLink/dsh-scaffold?label=version)](https://github.com/PerryLink/dsh-scaffold/releases)
[![npm downloads](https://img.shields.io/npm/dm/dsh-scaffold)](https://www.npmjs.com/package/dsh-scaffold)
[![dshfind](https://dshfind.com/api/badge/PerryLink/dsh-scaffold?metric=downloads&lang=es)](https://dshfind.com/es/plugins/PerryLink/dsh-scaffold?ref=badge)

[English](README.md) | [简体中文](README-zh.md) | **Español** | [Português](README-pt.md) | [हिन्दी](README-hi.md)

```sh
dsh plugin --profile <name> add dsh-scaffold
```


Kit compartido **sin dependencias en tiempo de ejecución** para los
repositorios de plugins DSH de PerryLink. La auditoría por proyecto detectó
que más de 20 plugins reimplementan el mismo seam Provider y
duplican las mismas formas de sanitización, precios y veredictos, así que este
paquete lo extrae todo — el seam Provider enchufable, las puertas de aprobación
fail-closed y de eventos de sesión adaptativos, los scripts de verificación
mecánica y los módulos puros sanitize/pricing/judge — en un único paquete
ESM + TypeScript.

## Instalación y desinstalación

La instalación es `pnpm add` (ver Inicio rápido). El paquete también incluye una capa `dsh.bundle.patch` deliberadamente vacía (`cordis.patch.yml`), así que también fluye por el canal bundle del harness cuando un perfil quiere montar el kit como paquete:

```sh
# canal npm (versiones publicadas)
dsh plugin --profile web add dsh-scaffold

# canal git (último master)
dsh plugin --profile web add github:PerryLink/dsh-scaffold
```

Para eliminar:

```sh
pnpm remove dsh-scaffold
```

Nada registra estado global: desinstalar es exactamente lo inverso de instalar.

## What is dsh-scaffold?

Kit compartido **sin dependencias en tiempo de ejecución** para los repositorios de plugins DSH de PerryLink. La auditoría por proyecto detectó que más de 20 plugins reimplementan el mismo seam Provider y duplican las mismas formas de sanitización, precios y veredictos, así que este paquete lo extrae todo — el seam Provider enchufable, las puertas de aprobación fail-closed y de eventos de sesión adaptativos, los scripts de verificación mecánica y los módulos puros sanitize/pricing/judge — en un único paquete ESM + TypeScript.

![Diagrama de flujo de dsh-scaffold: llamada → plugin → resultado.](docs/assets/dsh-scaffold-flow.svg)

*Resumen del flujo: llamada → plugin → resultado. Los ejemplos siguientes usan la superficie de comandos real.*


*La misma ejecución, animada.*

## Compatibilidad

- **DSH harness**: el kit no importa nada de `@deepseek-ai/*` en tiempo de
  ejecución. `@deepseek-ai/cordis` (`^4.0.5-alpha.1`), `@deepseek-ai/schemastery`
  (`^3.18.5-alpha.1`) y los paquetes `@deepseek-ai/dsh-*` son peer dependencies
  **opcionales** en la banda `>=0.1.2-rc.1 <0.2.0 || >=0.1.5-alpha.1 <0.2.0 || >=0.1.6-0 <0.2.0 || >=0.1.7-0 <0.2.0 || >=0.2.0-0 <0.3.0 || >=0.2.1-0 <0.3.0` compartida por los repos de plugins de PerryLink;
  solo existen para interoperar tipos. Verificado el 2026-09-11 contra
  el checkout master `dsh-v0.1.7-alpha.1` (cadena completa de puertas + smoke
  de instalación de perfil), y re-verificado el 2026-10-05 contra el checkout
  `dsh-v0.2.1-alpha.1` (cadena completa de puertas + smoke de instalación de perfil).
- **Node**: `^22.19.0 || >=24.0.0`, solo ESM.
- **Compatibilidad de formato**: nombres y formas reflejan `dsh-mask`
  (sanitize), `dsh-budget` (pricing) y `dsh-auto-review` (judge y el
  vocabulario `fallbackPolicy`), así que la migración es mecánica.

## Qué obtienes

- **Cero dependencias en tiempo de ejecución** — el núcleo puro (`seam`,
  `gates`, `shared`) es seguro para el navegador.
- **ESM + TypeScript estricto** — contratos JSDoc en cada módulo; `strict`,
  `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`.
- **Puertas fail-closed y adaptativas** — la aprobación nunca concede por
  defecto; los eventos de sesión degradan con elegancia en hosts que rechazan
  tipos de evento desconocidos.
- **Plantilla de plugin** — `template/` con `cordis.yml`, un `src/index.ts` de
  tres roles (Service Definition / Provider / Consumer), un test y el preset
  compartido de Renovate.

## Inicio rápido

```sh
dsh plugin --profile web add github:PerryLink/dsh-scaffold
```

Desde npm:

```sh
pnpm add dsh-scaffold
```

Desde git (el script `prepare` construye `lib/` usando solo dependencias de
producción):

```sh
pnpm add github:PerryLink/dsh-scaffold
```

Reemplaza un registro escrito a mano en un paso:

```ts
import { ProviderRegistry } from 'dsh-scaffold/seam'

const registry = new ProviderRegistry<Detector>({
  default: { name: 'regex', impl: new RegexDetector() },
})
ctx.effect(() => registry.register('ner', new NerDetector()))
const active = registry.use('ner') ?? registry.use()
```

### Ejemplos

Son los puntos de entrada reales; instala y llama a uno.

#### Ejemplo detallado

**Comando**

~~~sh
import { createStripper } from 'dsh-scaffold/shared'
createStripper().strip('call 13800138000 or email a@b.com')
~~~

**Salida**

~~~text
call <PHONE_1> or email <EMAIL_1>
~~~

*Observado en `README.md:153 (shared sanitize); src/shared/sanitize.ts:268; test/sanitize.test.ts:8-19`*

#### Rama de fallo

**Entrada**

~~~text
const r = new ProviderRegistry(); r.register('openai', impl); r.register('openai', impl)  // second call
~~~

**Salida**

~~~text
Error: Provider "openai" is already registered
~~~

*Observado en `plugins/dsh-scaffold/lib/seam/provider.js:55-58; plugins/dsh-scaffold/test/seam.test.ts:27-30; plugins/dsh-scaffold/README.md:164`*

#### Ejemplos breves

- `applyFailClosed`
- `parseVerdict`

## Configuración

Sin configuración en tiempo de ejecución: las puertas y utilidades son
funciones puras. La única superficie de configuración es `cordis.patch.yml`,
la capa de parche de bundle que se distribuye para la composición de perfiles
del harness; no monta ninguna fila de plugin (el kit es una biblioteca) y
documenta cómo los plugins consumidores añaden las suyas.

## Herramientas y superficies

| Subruta | Propósito |
|---|---|
| `seam` | `ProviderRegistry<T>` — registro de providers nombrado, reversible y que falla en voz alta. |
| `gates` | `applyFailClosed`; `makeEventGate` / `maybeAppendSessionEvent` / `probeIgnorableAppend`. |
| `shared` | `sanitize` (`Stripper`, `redactText`, `redactMapping`, `sanitizeText`, `sanitizeUrl`), `pricing` (`BUILTIN_PRICES`, `estimateUsageCost`, `tokenCarbon`, `latencyStats`, `formatMoney`, `formatTokens`), `judge` (`parseVerdict`, `VERDICT_SCHEMA`, `riskExceeds`). |
| `verify` | Puertas CI mecánicas (`verify-license`, `verify-readme-languages`, `verify-seam`) con `VerifyReport` y CLI con salida no cero: `node lib/verify/cli.js all .` |
| `template/` | Plantilla de plugin nuevo (`cordis.yml`, plugin de tres roles, test, README, `renovate.json5`). |
| barrel raíz | Reexporta todo lo anterior. |

## Permisos y datos

El kit no realiza E/S, acceso a red ni subprocesos por sí mismo. `Stripper`
mantiene los mapeos placeholder→original solo en memoria, y
`stats()`/`redactMapping()` nunca emiten texto plano; un consumidor que
persista un mapeo es dueño de esa decisión y de sus permisos de almacenamiento.

## Límites de seguridad

- `sanitize`/`redact*` son **higiene de presentación**, no un límite de
  seguridad: reducen la fuga en logs y resultados, no autentican ni autorizan.
- Las puertas de aprobación son fail-closed por defecto (`rejected`); la única
  vía de concesión es una opción explícita `allow-once`.
- Los eventos de sesión que el host rechaza se omiten, nunca se reintentan de
  forma que pueda romper la reanudación de la sesión.
- Reporta vulnerabilidades vía GitHub Security Advisories — ver `SECURITY.md`.

## Limitaciones conocidas

- Los hosts cuyo tercer argumento de `Session.append` es un `SurfaceIntent`
  (`0.1.2-rc.1`) lanzan `validateNext` ante la sonda del sobre ignorable;
  la puerta degrada a omitir-desconocido, de modo que los eventos de auditoría
  se descartan (fail closed) en esos hosts en lugar de registrarse.
- 0.1.2-rc.1 (adaptado el 2026-09-02): el sobre de sesión conserva su campo ignorable solo para compatibilidad de lectura de logs almacenados - Session.append aún no puede estamparlo, por lo que el comportamiento de la puerta no cambia.
- El kit no trae mitad de UI de navegador: es una biblioteca consumida por las
  mitades Host (y opcionalmente Client) de otros plugins.

## Desarrollo

```sh
pnpm install
pnpm run typecheck        # tsc --noEmit
pnpm run typecheck:ci     # cara CI: tsc -p tsconfig.ci.json --noEmit
pnpm test                 # tests unitarios vitest
pnpm run build            # emite lib/ y declaraciones (también lo hace prepare)
pnpm run verify:self-contained
pnpm run verify:artifacts
```

## Temas

Este repositorio es también el centro de mantenimiento del ecosistema:
plugins: `scripts/sync-peer-range.mjs` repinnea la banda de peers compartida
en todos los repos con un comando, `renovate/default.json5` es el preset de
Renovate compartido que todos extienden, `.github/workflows/npm-publish.yml`
es un flujo de publicación reutilizable disparado por tag (solo necesita un
secreto `NPM_TOKEN`), y `data/repos.json` es el registro del ecosistema que
consume el portal. Ver [docs/ecosystem-tooling.md](docs/ecosystem-tooling.md).

Palabras clave: dsh, dsh-plugin, deepseek-harness, deepseek, cordis, perrylink,
provider, seam, approval, sanitize, pricing, judge.

## Contribuidores

Mantenido por [PerryLink](https://github.com/PerryLink) con contribuciones
del ecosistema de plugins DSH.

## Licencia

Apache-2.0 — ver [LICENSE](LICENSE).

## PerryLink DSH Plugin Family

Este proyecto forma parte de la familia de plugins de DeepSeek Harness de [PerryLink](https://github.com/PerryLink). El registro permanece plegado abajo para que cada README conserve una primera pantalla corta; expándelo para ver cada fila y su estado.

<details>
<summary>Expandir todos los plugins</summary>

| Plugin | Estado |
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
| **[dsh-budget](https://github.com/PerryLink/dsh-budget)** | 🧊 CONGELADO — ver el README del repositorio |
| **[dsh-claude-move](https://github.com/PerryLink/dsh-claude-move)** | 🧊 CONGELADO — ver el README del repositorio |
| **[dsh-defend](https://github.com/PerryLink/dsh-defend)** | 🧊 CONGELADO — ver el README del repositorio |
| **[dsh-draw](https://github.com/PerryLink/dsh-draw)** | 🧊 CONGELADO — ver el README del repositorio |
| **[dsh-reach](https://github.com/PerryLink/dsh-reach)** | 🧊 CONGELADO — ver el README del repositorio |
| **[dsh-background-agents](https://github.com/PerryLink/dsh-background-agents)** | 🚫 RETIRADO — ver el README del repositorio |
| **[dsh-session-pin](https://github.com/PerryLink/dsh-session-pin)** | 🚫 RETIRADO — ver el README del repositorio |
| **[dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms)** | 🚫 RETIRADO — ver el README del repositorio |

</details>
