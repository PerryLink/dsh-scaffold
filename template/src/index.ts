/**
 * <PLUGIN_NAME> — <one-line purpose>.
 *
 * This file is the single Host face of the plugin (function-plugin contract:
 * `name` / `inject` / `Config` / `apply`, no default export). It demonstrates
 * the three roles that make a complete capability seam:
 *
 *   1. Service Definition — the interface (and its schema) both sides agree on.
 *   2. Service Provider   — registers implementations into a ProviderRegistry;
 *                           `register` returns a disposer, so every
 *                           registration is a reversible side effect.
 *   3. Consumer           — resolves the active implementation and uses it.
 *
 * Copy this directory and replace every <PLACEHOLDER> token.
 */

import { ProviderRegistry } from 'dsh-scaffold/seam'

/** Minimal structural Cordis context surface (substitute the real `Context`). */
interface Ctx {
  /** Register a side effect that returns its disposer. */
  effect(cb: () => () => void): void
  /** The plugin config as loaded from cordis.patch.yml. */
  config: Config
}

// ---------------------------------------------------------------------------
// Service Definition
// ---------------------------------------------------------------------------

/** The capability interface every provider implements. */
export interface MyCapability {
  /** Transform one input string. */
  run(input: string): string
}

// ---------------------------------------------------------------------------
// Service Provider
// ---------------------------------------------------------------------------

/** The default, zero-dependency implementation. */
class DefaultCapability implements MyCapability {
  run(input: string): string {
    return `default:${input}`
  }
}

/** An alternative implementation a deployment may opt into. */
class FastCapability implements MyCapability {
  run(input: string): string {
    return `fast:${input}`
  }
}

/** Raw plugin config; defaults are applied in {@link resolveConfig}. */
export interface Config {
  /** Which provider to activate. */
  readonly provider?: string
}

/** Explicit resolution step: apply defaults here, fail loud on invalid input. */
export function resolveConfig(config: Config): { readonly provider: string } {
  return { provider: config.provider ?? 'default' }
}

/** Plugin identity (the Loader unwraps `exports.default ?? exports`). */
export const name = '<PLUGIN_NAME>'

/** Hard service dependencies; optional services are read via `ctx.get`. */
export const inject: readonly string[] = []

/**
 * Host face: build the seam and wire it into the runtime.
 * @param ctx - the Cordis context.
 */
export function apply(ctx: Ctx): void {
  const resolved = resolveConfig(ctx.config)

  // Provider seam: one registry per capability. The default implementation is
  // injected up front; optional backends register themselves through
  // `ctx.effect`, whose returned disposer removes them on stop/update.
  const registry = new ProviderRegistry<MyCapability>({
    default: { name: 'default', impl: new DefaultCapability() },
  })
  ctx.effect(() => registry.register('fast', new FastCapability()))

  // -------------------------------------------------------------------------
  // Consumer
  // -------------------------------------------------------------------------

  // Resolve the active implementation (the configured provider name) and use it.
  const capability = registry.use(resolved.provider) ?? registry.use()
  if (capability === undefined) throw new Error(`no capability provider "${resolved.provider}"`)
  const output = capability.run('hello')
  void output
}
