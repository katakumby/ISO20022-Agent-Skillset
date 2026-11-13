---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalRatesAndTenors1Code"]
code_set: "ExternalRatesAndTenors1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalRatesAndTenors1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalRatesAndTenors1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external rates and tenors code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`EURI`-Euro interbank offered rate (3 months, 6 months and other tenors).
*`ESOI`-Euro Overnight Index Swap (ESTROIS) 1 day, 1 week, other tenors.
*`ESTR`-Euro short-term rate.
*`GBPO`-Pound sterling London inter-bank offered rate (3 months, 6 months, other tenors) and the respective successor rate.
*`OTHR`-Other floating rates and tenors.
*`SOFR`-Secured overnight financing rate (1 months, 3 months, other tenors).
*`USOI`-US dollar overnight index swap (1 day, 1 week, other tenors), USDOIS.
*`USPO`-US dollar London inter-bank offered rate (3 months, 6 months, other tenors) and the respective successor rate.

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
| 1 | EURI |
| 2 | ESOI |
| 3 | ESTR |
| 4 | GBPO |
| 5 | OTHR |
| 6 | SOFR |
| 7 | USOI |
| 8 | USPO |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
