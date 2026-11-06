# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| 0.0.x | Yes |

This plugin is pre-1.0: only the latest published release receives security
fixes. Upgrade before reporting, and name the exact version you tested.

## Reporting a vulnerability

Report privately through GitHub Security Advisories on
`https://github.com/<OWNER>/<PLUGIN_NAME>/security/advisories/new`.
Do not open a public issue for a vulnerability.

Include the plugin version, the DSH version, the impact, and a minimal
reproduction. Expect an initial response within 7 days; coordinated disclosure
within 90 days.

## Scope

- credential handling in the plugin itself;
- outbound requests the plugin makes;
- tool output that reaches a prompt, a shell, or a renderer;
- lifecycle scripts — this template ships none, and that is the expectation.

## Out of scope

- vulnerabilities in DSH, Cordis, or a dependency: report them to the owning
  project;
- the host's sandbox. A plugin runs in-process with the user's permissions, and
  a static check is not containment.

## Not a security audit

This policy describes how to report a problem; it does not certify the plugin.
Static checks can miss runtime behavior, so do not read a PASS as "secure".
