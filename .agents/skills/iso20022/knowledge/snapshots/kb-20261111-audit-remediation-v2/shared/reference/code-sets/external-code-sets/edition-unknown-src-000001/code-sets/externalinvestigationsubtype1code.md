---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationSubType1Code"]
code_set: "ExternalInvestigationSubType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationSubType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationSubType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the investigation sub type, as published in an external investigation sub type code set.
External code sets can be downloaded from www.iso20022.org.
*`AMLI`-Investigation relates to anti-money laundering.
*`SANC`-Investigation relates to sanctions.
*`FRAD`-Investigation relates to fraud.
*`UTEX`-Investigation relates to a transaction that cannot be executed.
*`FCCI`-Investigation relates to financial crimes compliance.
*`FWTR`-Investigation relates to funds/wire transfer regulation.
*`RQUF`-Use of funds on an entry is requested.
*`RQDA`-Debit authorisation on an entry is requested.
*`RQVA`-Revaluation of an entry is requested.
*`RQCH`-Investigation relating to charges that have been taken or are requested.
*`OTHR`-Other

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
| 1 | AMLI |
| 2 | SANC |
| 3 | FRAD |
| 4 | UTEX |
| 5 | FCCI |
| 6 | FWTR |
| 7 | RQUF |
| 8 | RQDA |
| 9 | RQVA |
| 10 | RQCH |
| 11 | OTHR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
