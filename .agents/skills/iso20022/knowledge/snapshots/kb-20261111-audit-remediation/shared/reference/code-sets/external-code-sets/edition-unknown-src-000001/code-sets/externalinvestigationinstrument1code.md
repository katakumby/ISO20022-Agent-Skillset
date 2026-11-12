---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationInstrument1Code"]
code_set: "ExternalInvestigationInstrument1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationInstrument1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationInstrument1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the type of instrument or product to which the investigation refers, as published in an external investigation instrument code set.
External code sets can be downloaded from www.iso20022.org.
*`CHQB`-Investigation is related to a cheque.
*`INST`-Investigation is related to an instant credit transfer.
*`XBCT`-Investigation is related to a cross border payment.
*`ACHP`-Investigation is related to an ACH or mass payment.
*`DDTP`-Investigation is related to a direct debit.
*`CARD`-Investigation is related to a card transaction.
*`URGP`-Investigation is related to a wire/high value payment.
*`STAT`-Investigation is related to a statement entry.
*`DRFT`-Investigation is related to a draft.
*`SRTP`-Investigation is related to a request to pay.
*`OTHR`-Other underlying instrument.

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
| 1 | CHQB |
| 2 | INST |
| 3 | XBCT |
| 4 | ACHP |
| 5 | DDTP |
| 6 | CARD |
| 7 | URGP |
| 8 | STAT |
| 9 | DRFT |
| 10 | SRTP |
| 11 | OTHR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
