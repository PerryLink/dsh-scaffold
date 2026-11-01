# dsh-toolkit

> **Renamed:** previously `@perrylink/dsh-plugin-kit`; now **`dsh-toolkit`**. Old repo stays as a pointer/backup. New home: https://github.com/PerryLink/dsh-toolkit


[English](README.md) · [简体中文](README-zh.md) · [Español](README-es.md) · [Português](README-pt.md) · [हिन्दी](README-hi.md)

```sh
dsh plugin --profile <name> add dsh-toolkit
```


PerryLink DSH प्लगइन रिपॉज़िटरीज़ के लिए साझा **शून्य-रनटाइम-निर्भरता** टूलकिट। प्रति-प्रोजेक्ट ऑडिट में पाया गया कि 20+ प्लगइन एक ही Provider seam हाथ से लिखते हैं और एक जैसी sanitize/pricing/निर्णय आकृतियाँ दोहराते हैं, इसलिए यह पैकेज वह सब — प्लगेबल Provider seam, fail-closed अनुमोदन और अनुकूली सत्र-घटना गेट, यांत्रिक verify स्क्रिप्ट और साझा sanitize/pricing/judge शुद्ध मॉड्यूल — एक ESM + TypeScript पैकेज में निकालता है।

> **पैकेज नाम।** यह प्रोजेक्ट npm पर **`dsh-toolkit`** के रूप में प्रकाशित होता है। सादा नाम `dsh-toolkit` किसी असंबंधित प्रोजेक्ट का है — उसे इंस्टॉल करने से यह पैकेज इंस्टॉल नहीं होता।

- **1024 स्टोर चैनल**: पहले `npm i -g dsh1024`, फिर `dsh1024 plugin --profile web add dsh-toolkit` ([deepseek1024.com](https://deepseek1024.com) इंस्टॉल रैंकिंग में गिना जाता है)।

[![npm version](https://img.shields.io/npm/v/dsh-toolkit)](https://www.npmjs.com/package/dsh-toolkit)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)
[![DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)
[![Node](https://img.shields.io/badge/node-%5E22.19%20%7C%7C%20%3E%3D24-brightgreen.svg)](#)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/dsh-toolkit)
[![CI](https://img.shields.io/github/actions/workflow/status/PerryLink/dsh-toolkit/ci.yml?branch=main&label=CI)](https://github.com/PerryLink/dsh-toolkit/actions)
[![Version](https://img.shields.io/github/v/tag/PerryLink/dsh-toolkit?label=version)](https://github.com/PerryLink/dsh-toolkit/releases)
[![npm downloads](https://img.shields.io/npm/dm/dsh-toolkit)](https://www.npmjs.com/package/dsh-toolkit)
[![dshfind](https://dshfind.com/api/badge/PerryLink/dsh-toolkit?metric=downloads&lang=hi)](https://dshfind.com/hi/plugins/PerryLink/dsh-toolkit?ref=badge)

[English](README.md) | [简体中文](README-zh.md) | [Español](README-es.md) | [Português](README-pt.md) | **हिन्दी**

PerryLink DSH प्लगइन रिपॉज़िटरीज़ के लिए साझा **शून्य-रनटाइम-निर्भरता** टूलकिट।
प्रति-प्रोजेक्ट ऑडिट में पाया गया कि 20+ प्लगइन एक ही Provider seam
हाथ से लिखते हैं और एक जैसी sanitize/pricing/निर्णय आकृतियाँ दोहराते हैं, इसलिए
यह पैकेज वह सब — प्लगेबल Provider seam, fail-closed अनुमोदन और अनुकूली
सत्र-घटना गेट, यांत्रिक verify स्क्रिप्ट और साझा sanitize/pricing/judge शुद्ध
मॉड्यूल — एक ESM + TypeScript पैकेज में निकालता है।

## इंस्टॉल और अनइंस्टॉल (Install & uninstall)

इंस्टॉल `pnpm add` है (त्वरित शुरुआत देखें)। यह पैकेज जान-बूझकर खाली `dsh.bundle.patch` परत (`cordis.patch.yml`) भी लाता है, इसलिए जब कोई profile kit को पैकेज के रूप में माउंट करना चाहे तो यह harness के bundle चैनल से भी जाता है:

```sh
# npm चैनल (प्रकाशित रिलीज़)
dsh plugin --profile web add dsh-toolkit

# git चैनल (नवीनतम master)
dsh plugin --profile web add github:PerryLink/dsh-toolkit
```

हटाने के लिए:

```sh
pnpm remove dsh-toolkit
```

कुछ भी वैश्विक स्थिति पंजीकृत नहीं करता: अनइंस्टॉल इंस्टॉल का ठीक उल्टा है।

## What is dsh-toolkit?

PerryLink DSH प्लगइन रिपॉज़िटरीज़ के लिए साझा **शून्य-रनटाइम-निर्भरता** टूलकिट। प्रति-प्रोजेक्ट ऑडिट में पाया गया कि 20+ प्लगइन एक ही Provider seam हाथ से लिखते हैं और एक जैसी sanitize/pricing/निर्णय आकृतियाँ दोहराते हैं, इसलिए यह पैकेज वह सब — प्लगेबल Provider seam, fail-closed अनुमोदन और अनुकूली सत्र-घटना गेट, यांत्रिक verify स्क्रिप्ट और साझा sanitize/pricing/judge शुद्ध मॉड्यूल — एक ESM + TypeScript पैकेज में निकालता है।

![dsh-toolkit कार्यप्रवाह आरेख: कॉल → प्लगइन → परिणाम।](docs/assets/dsh-toolkit-flow.svg)

*कार्यप्रवाह: कॉल → प्लगइन → परिणाम। नीचे के उदाहरण वास्तविक कमांड सतह का उपयोग करते हैं।*


*वही रन, एनिमेटेड।*

## अनुकूलता (Compatibility)

- **DSH harness**: किट रनटाइम पर `@deepseek-ai/*` से कुछ भी import नहीं करता।
  `@deepseek-ai/cordis` (`^4.0.5-alpha.1`), `@deepseek-ai/schemastery` (`^3.18.5-alpha.1`) और
  `@deepseek-ai/dsh-*` पैकेज PerryLink प्लगइन रिपोज़ की साझा `>=0.1.2-rc.1 <0.2.0 || >=0.1.5-alpha.1 <0.2.0 || >=0.1.6-0 <0.2.0 || >=0.1.7-0 <0.2.0 || >=0.2.0-0 <0.3.0 || >=0.2.1-0 <0.3.0` बैंड में
  **वैकल्पिक** peer dependencies हैं; वे केवल टाइप इंटरऑप के लिए हैं।
  2026-09-11 को `dsh-v0.1.7-alpha.1` master checkout के विरुद्ध सत्यापित
  (पूर्ण गेट शृंखला + profile इंस्टॉल स्मोक), और 2026-10-05 को `dsh-v0.2.1-alpha.1`
  checkout के विरुद्ध पुनः सत्यापित (पूर्ण गेट शृंखला + profile इंस्टॉल स्मोक)।
- **Node**: `^22.19.0 || >=24.0.0`, केवल ESM।
- **वायर अनुकूलता**: नाम और आकृतियाँ `dsh-mask` (sanitize), `dsh-budget`
  (pricing) और `dsh-auto-review` (judge व `fallbackPolicy` शब्दावली) का दर्पण
  हैं, इसलिए माइग्रेशन यांत्रिक है।

## आपको क्या मिलता है (What you get)

- **शून्य रनटाइम निर्भरताएँ** — शुद्ध कोर (`seam`, `gates`, `shared`)
  ब्राउज़र-सुरक्षित है।
- **ESM + सख्त TypeScript** — हर मॉड्यूल पर JSDoc अनुबंध; `strict`,
  `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`।
- **Fail-closed और अनुकूली गेट** — अनुमोदन कभी डिफ़ॉल्ट से अनुदान नहीं देता;
  अज्ञात घटना प्रकार अस्वीकार करने वाले होस्ट पर सत्र-घटनाएँ सुंदरता से
  अपमानित होती हैं।
- **नया-प्लगइन कंकाल** — `template/` में `cordis.yml`, तीन-भूमिका वाला
  `src/index.ts` (Service Definition / Provider / Consumer), एक टेस्ट और साझा
  Renovate प्रीसेट।

## त्वरित शुरुआत (Quick start)

```sh
dsh plugin --profile web add github:PerryLink/dsh-toolkit
```

npm से:

```sh
pnpm add dsh-toolkit
```

git से (`prepare` स्क्रिप्ट केवल उत्पादन निर्भरताओं से `lib/` बनाती है):

```sh
pnpm add github:PerryLink/dsh-toolkit
```

हाथ से लिखी रजिस्ट्री एक चरण में बदलें:

```ts
import { ProviderRegistry } from 'dsh-toolkit/seam'

const registry = new ProviderRegistry<Detector>({
  default: { name: 'regex', impl: new RegexDetector() },
})
ctx.effect(() => registry.register('ner', new NerDetector()))
const active = registry.use('ner') ?? registry.use()
```

## कॉन्फ़िगरेशन (Configuration)

रनटाइम कॉन्फ़िगरेशन नहीं है: गेट और सहायक शुद्ध फ़ंक्शन हैं। एकमात्र
कॉन्फ़िगरेशन सतह `cordis.patch.yml` है — harness प्रोफ़ाइल संयोजन के लिए
वितरित bundle-patch परत; यह कोई प्लगइन पंक्ति नहीं जोड़ती (किट एक लाइब्रेरी
है) और बताती है कि उपभोक्ता प्लगइन अपनी पंक्तियाँ कैसे जोड़ें।

## उपकरण और सतहें (Tools & surfaces)

| उपपथ | उद्देश्य |
|---|---|
| `seam` | `ProviderRegistry<T>` — प्रतिवर्ती, नामित provider रजिस्ट्री जो ज़ोर से विफल होती है। |
| `gates` | `applyFailClosed`; `makeEventGate` / `maybeAppendSessionEvent` / `probeIgnorableAppend`। |
| `shared` | `sanitize` (`Stripper`, `redactText`, `redactMapping`, `sanitizeText`, `sanitizeUrl`), `pricing` (`BUILTIN_PRICES`, `estimateUsageCost`, `tokenCarbon`, `latencyStats`, `formatMoney`, `formatTokens`), `judge` (`parseVerdict`, `VERDICT_SCHEMA`, `riskExceeds`)। |
| `verify` | यांत्रिक CI गेट (`verify-license`, `verify-readme-languages`, `verify-seam`) `VerifyReport` और गैर-शून्य निकास CLI के साथ: `node lib/verify/cli.js all .` |
| `template/` | नए प्लगइन का कंकाल (`cordis.yml`, तीन-भूमिका प्लगइन, टेस्ट, README, `renovate.json5`)। |
| मूल barrel | उपरोक्त सब पुनः निर्यात करता है। |

## अनुमतियाँ और डेटा (Permissions & data)

किट स्वयं कोई I/O, नेटवर्क एक्सेस या सबप्रोसेस नहीं करता। `Stripper`
placeholder→original मैपिंग केवल मेमोरी में रखता है, और
`stats()`/`redactMapping()` कभी प्लेनटेक्स्ट नहीं देते; मैपिंग को स्थायी करने
वाला उपभोक्ता उस निर्णय और उसकी स्टोरेज अनुमतियों का स्वामी है।

## सुरक्षा सीमाएँ (Security boundaries)

- `sanitize`/`redact*` **प्रदर्शन स्वच्छता** हैं, सुरक्षा सीमा नहीं: वे लॉग और
  परिणामों में रिसाव घटाते हैं, प्रमाणित या अधिकृत नहीं करते।
- अनुमोदन गेट डिफ़ॉल्ट से fail closed हैं (`rejected`); अनुदान का एकमात्र रास्ता
  स्पष्ट `allow-once` विकल्प है।
- होस्ट द्वारा अस्वीकृत सत्र-घटनाएँ छोड़ दी जाती हैं, कभी ऐसे पुनर्प्रयास नहीं
  किए जाते जो सत्र रिज़्यूम तोड़ सकें।
- कमज़ोरियाँ GitHub Security Advisories से रिपोर्ट करें — `SECURITY.md` देखें।

## ज्ञात सीमाएँ (Known limitations)

- जिन होस्ट का `Session.append` तीसरा तर्क `SurfaceIntent` है
  (`0.1.2-rc.1`), वे ignorable-लिफ़ाफ़ा जाँच पर `validateNext` फेंकते हैं;
  गेट अज्ञात-छोड़ने में अपमानित होता है, इसलिए ऐसे होस्ट पर ऑडिट घटनाएँ लिखे
  जाने के बजाय छोड़ दी जाती हैं (fail closed)।
- 0.1.2-rc.1 (2026-09-02 को अनुकूलित): सत्र लिफ़ाफ़ा अपना ignorable फ़ील्ड केवल संग्रहीत-लॉग पठन संगतता के लिए रखता है - Session.append अभी भी इसे स्टैम्प नहीं कर सकता, इसलिए गेट व्यवहार अपरिवर्तित है।
- किट में ब्राउज़र UI आधा नहीं है: यह एक लाइब्रेरी है जिसे अन्य प्लगइन के Host
  (और वैकल्पिक Client) आधे उपभोग करते हैं।

## विकास (Development)

```sh
pnpm install
pnpm run typecheck        # tsc --noEmit
pnpm run typecheck:ci     # CI चेहरा: tsc -p tsconfig.ci.json --noEmit
pnpm test                 # vitest यूनिट टेस्ट
pnpm run build            # lib/ व घोषणाएँ उत्सर्जित करता है (prepare भी)
pnpm run verify:self-contained
pnpm run verify:artifacts
```

## विषय (Topics)

यह रिपॉज़िटरी पूरे इकोसिस्टम का रखरखाव केंद्र भी है:
`scripts/sync-peer-range.mjs` एक कमांड में सभी रिपोज़ की साझा peer बैंड फिर से
पिन करता है, `renovate/default.json5` वह साझा Renovate प्रीसेट है जिसे हर
रिपो विस्तारित करता है, `.github/workflows/npm-publish.yml` एक पुन: प्रयोज्य
tag-ट्रिगर प्रकाशन वर्कफ़्लो है (केवल एक `NPM_TOKEN` सीक्रेट चाहिए), और
`data/repos.json` पोर्टल द्वारा उपभोग की जाने वाली इकोसिस्टम रजिस्ट्री है।
[docs/ecosystem-tooling.md](docs/ecosystem-tooling.md) देखें।

कीवर्ड: dsh, dsh-plugin, deepseek-harness, deepseek, cordis, perrylink,
provider, seam, approval, sanitize, pricing, judge।

## योगदानकर्ता (Contributors)

[PerryLink](https://github.com/PerryLink) द्वारा अनुरक्षित, DSH प्लगइन
इकोसिस्टम के योगदान के साथ।

## लाइसेंस (License)

Apache-2.0 — [LICENSE](LICENSE) देखें।

## PerryLink DSH Plugin Family

यह प्रोजेक्ट [PerryLink](https://github.com/PerryLink) के DeepSeek Harness प्लगइन परिवार का हिस्सा है। पूरी सूची नीचे संक्षिप्त रखी गई है ताकि हर README की पहली स्क्रीन छोटी रहे; हर पंक्ति और उसकी स्थिति देखने के लिए इसे खोलें।

<details>
<summary>सभी प्लगइन खोलें</summary>

| प्लगइन | स्थिति |
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
| **[dsh-toolkit](https://github.com/PerryLink/dsh-toolkit)** |  |
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
| **[dsh-budget](https://github.com/PerryLink/dsh-budget)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-claude-move](https://github.com/PerryLink/dsh-claude-move)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-defend](https://github.com/PerryLink/dsh-defend)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-draw](https://github.com/PerryLink/dsh-draw)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-reach](https://github.com/PerryLink/dsh-reach)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-background-agents](https://github.com/PerryLink/dsh-background-agents)** | 🚫 सेवानिवृत्त — रिपॉज़िटरी README देखें |
| **[dsh-session-pin](https://github.com/PerryLink/dsh-session-pin)** | 🚫 सेवानिवृत्त — रिपॉज़िटरी README देखें |
| **[dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms)** | 🚫 सेवानिवृत्त — रिपॉज़िटरी README देखें |

</details>

### उदाहरण

ये वास्तविक प्रवेश बिंदु हैं; इंस्टॉल के बाद एक चलाएँ।

#### विस्तृत उदाहरण

**कमांड**

~~~sh
import { createStripper } from 'dsh-toolkit/shared'
createStripper().strip('call 13800138000 or email a@b.com')
~~~

**आउटपुट**

~~~text
call <PHONE_1> or email <EMAIL_1>
~~~

*स्रोत `README.md:153 (shared sanitize); src/shared/sanitize.ts:268; test/sanitize.test.ts:8-19`*

#### विफलता शाखा

**इनपुट**

~~~text
const r = new ProviderRegistry(); r.register('openai', impl); r.register('openai', impl)  // second call
~~~

**आउटपुट**

~~~text
Error: Provider "openai" is already registered
~~~

*स्रोत `plugins/dsh-toolkit/lib/seam/provider.js:55-58; plugins/dsh-toolkit/test/seam.test.ts:27-30; plugins/dsh-toolkit/README.md:164`*

#### संक्षिप्त उदाहरण

- `applyFailClosed`
- `parseVerdict`

