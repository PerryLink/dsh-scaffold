import { existsSync, readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'

const templateUrl = (name) => new URL(`../template/${name}`, import.meta.url)
const readJson = (name) => JSON.parse(readFileSync(templateUrl(name), 'utf8'))
const readText = (name) => readFileSync(templateUrl(name), 'utf8')

const PLACEHOLDER_STATUSES = {
  entry: 'not-run',
  flow: 'not-run',
  boost: 'not-measured',
}
const LEVELS = Object.keys(PLACEHOLDER_STATUSES)

describe('template placeholders', () => {
  const pkg = readJson('package.json')
  const standards = readJson('standards.json')

  it('ships dsh.standards as a not-run placeholder, not a claim', () => {
    expect(pkg.dsh.standards.schema).toBe('dsh-levels/1')
    for (const level of LEVELS) {
      expect(standards.levels[level].status).toBe(PLACEHOLDER_STATUSES[level])
      expect(pkg.dsh.standards[level]).toEqual({
        status: standards.levels[level].status,
        evidence: standards.levels[level].evidence,
      })
      expect(pkg.dsh.standards[level].evidence).toBeNull()
    }
    expect(JSON.stringify(pkg.dsh.standards)).not.toMatch(/PASS|certified|official|recommended|secure/iu)
  })

  it('declares license, engines.dsh and the files the entry standard requires', () => {
    expect(pkg.license).toBe('Apache-2.0')
    expect(pkg.engines?.dsh).toBe('>=0.2.2-0 <0.3.0')
    expect(pkg.files).toContain('LICENSE')
    expect(pkg.files).toContain('cordis.patch.yml')
    expect(pkg.files).toContain('SECURITY.md')
    expect(existsSync(templateUrl('LICENSE'))).toBe(true)
    expect(existsSync(templateUrl('SECURITY.md'))).toBe(true)
    // The policy must name a private channel and the supported versions.
    const policy = readText('SECURITY.md')
    expect(policy).toMatch(/security\/advisories\/new/)
    expect(policy).toMatch(/Supported versions/i)
  })

  it('ships the full Apache-2.0 text as template/LICENSE', () => {
    const license = readText('LICENSE')
    expect(license).toContain('Apache License')
    expect(license).toContain('Version 2.0, January 2004')
    expect(license).toContain('limitations under the License')
  })

  it('points dsh.bundle.patch at a patch file that exists', () => {
    expect(pkg.dsh.bundle.patch).toBe('./cordis.patch.yml')
    expect(existsSync(templateUrl('cordis.patch.yml'))).toBe(true)
    expect(existsSync(templateUrl('cordis.yml'))).toBe(false)
  })

  it('declares empty capabilities/labels and explains the empty capabilities list', () => {
    expect(Array.isArray(pkg.dsh.capabilities)).toBe(true)
    expect(pkg.dsh.capabilities).toEqual([])
    expect(pkg.dsh.labels).toEqual([])
    // The skeleton uses no Harness host surface, so the empty array is real
    // (not an omission); the README must say how to fill it.
    expect(readText('README.md')).toMatch(/dsh\.capabilities/)

    // No install-time lifecycle scripts: the template must not opt into
    // running code on the user's machine at install time.
    for (const name of ['preinstall', 'install', 'postinstall', 'prepare']) {
      expect(pkg.scripts?.[name]).toBeUndefined()
    }

    // Permissions are disclosure only, in a draft shape the host does not read.
    expect(pkg.security.status).toBe('draft')
    expect(pkg.security.note).toMatch(/not enforced/i)
    expect(pkg.security.permissions).toEqual({
      files: [],
      network: [],
      credentials: [],
      shell: false,
      subprocess: false,
    })
  })

  it('depends on the published dsh-scaffold package instead of the 404 dsh-toolkit', () => {
    expect(pkg.dependencies['dsh-scaffold']).toMatch(/^\^0\.2\./)
    expect(pkg.dependencies['dsh-toolkit']).toBeUndefined()
    const source = readText('src/index.ts')
    expect(source).toContain("from 'dsh-scaffold/seam'")
    expect(source).not.toContain('dsh-plugin-kit')
  })

  it('ships an advisory entry-check workflow pinned to Node 24.9 and dsh-standards 1.2.2', () => {
    const workflowFile = '.github/workflows/entry-check.yml'
    expect(existsSync(templateUrl(workflowFile))).toBe(true)
    const workflow = readText(workflowFile)
    expect(workflow).toMatch(/continue-on-error:\s*true/)
    expect(workflow).toMatch(/node-version:\s*['"]?24\.9/)
    expect(workflow).toContain('npm i -D dsh-standards@1.2.2')
    expect(workflow).toContain('npx dsh-standards . --scope entry --entry-claim static --format json --out entry.json')
    expect(workflow).toContain('actions/upload-artifact')
    expect(workflow).toMatch(/if:\s*always\(\)/)
  })
})
