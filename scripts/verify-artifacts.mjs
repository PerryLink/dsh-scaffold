// Verify the built artifacts after `pnpm run build`: syntax-check the ESM
// entry, import it under plain Node, and assert the shipped files exist.
// Guards against TypeScript-only syntax leaking into shipped output and
// against a tarball missing the bundle patch.
import { execFileSync } from 'node:child_process'
import { existsSync, readFileSync } from 'node:fs'
import path from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)))

const required = [
  'lib/index.js',
  'lib/index.d.ts',
  'cordis.patch.yml',
  'LICENSE',
]
for (const rel of required) {
  if (!existsSync(path.join(root, rel))) throw new Error(`missing artifact: ${rel}`)
}

// 1. Syntax-check the ESM entry (plain Node parse; no execution).
execFileSync(process.execPath, ['--check', path.join(root, 'lib/index.js')], { stdio: 'inherit' })

// 2. The library face must import under plain Node (no tsx, no checkout paths).
const index = await import(pathToFileURL(path.join(root, 'lib/index.js')).href)
if (typeof index.makeEventGate !== 'function' || typeof index.applyFailClosed !== 'function') {
  throw new Error('lib/index.js exports an unexpected library face')
}

// 3. The bundle patch must reference the package by its own name.
const patch = readFileSync(path.join(root, 'cordis.patch.yml'), 'utf8')
if (!patch.includes('dsh-toolkit')) {
  throw new Error('cordis.patch.yml does not reference dsh-toolkit')
}

console.log('artifacts OK: syntax + ESM import + bundle patch present')
