---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalUndertakingType1Code"]
code_set: "ExternalUndertakingType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalUndertakingType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalUndertakingType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external undertaking type code in the format of a character string with a maximum length of 4 characters. The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`APAY`-Undertaking in support of an advance payment obligation.
*`COMM`-Undertaking in support of a commercial obligation.
*`CUST`-Undertaking in support of a customs duty obligation.
*`DPAY`-Undertaking representing the primary means of payment.
*`FINC`-Undertaking in support of a financial obligation.
*`INSU`-Undertaking in support of a insurance obligation.
*`IRBO`-Undertaking in support of an Industrial Revenue Board (IRB) obligation.
*`MAIN`-Undertaking in support of a maintenance obligation.
*`PAYM`-Undertaking in support of a payment obligation.
*`PERF`-Undertaking in support of a performance obligation.
*`RETN`-Undertaking in support of a monetary retention obligation.
*`SHIP`-Undertaking in support of a sea transportation obligation.
*`TEND`-Undertaking in support of a tender or bid obligation.
*`WARR`-Undertaking in support of a warranty obligation.

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | APAY |
| 2 | COMM |
| 3 | CUST |
| 4 | DPAY |
| 5 | FINC |
| 6 | INSU |
| 7 | IRBO |
| 8 | MAIN |
| 9 | PAYM |
| 10 | PERF |
| 11 | RETN |
| 12 | SHIP |
| 13 | TEND |
| 14 | WARR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
