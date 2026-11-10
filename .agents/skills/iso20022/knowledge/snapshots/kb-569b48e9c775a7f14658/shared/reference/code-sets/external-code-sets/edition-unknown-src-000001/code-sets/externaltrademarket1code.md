---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalTradeMarket1Code"]
code_set: "ExternalTradeMarket1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalTradeMarket1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalTradeMarket1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external trade market code in the format of character string with a maximum length of 4 characters.
External code sets can be downloaded from www.iso20022.org.

*`FDMS`-Factoring service provider, Factoring client and third party in the same country
*`FEXP`-Factoring service provider, Factoring client in the same country, third party in another country
*`FFDM`-Factoring client and third party in the same country, Factoring service provider in another country
*`FFDT`-Factoring service provider, Factoring client and third party in the same country, but factoring client has an exceptional VAT ruling, for example if it’s overseas
*`FIMP`-Factoring service provider and third party in the same country, Factoring client in another country
*`FREX`-Factoring service provider, Factoring client and third party in three different countries

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
| 1 | FDMS |
| 2 | FEXP |
| 3 | FFDM |
| 4 | FFDT |
| 5 | FIMP |
| 6 | FREX |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
