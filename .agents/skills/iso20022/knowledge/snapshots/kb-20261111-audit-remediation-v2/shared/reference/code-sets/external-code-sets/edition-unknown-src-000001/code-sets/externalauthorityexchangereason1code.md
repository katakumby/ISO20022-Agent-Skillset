---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalAuthorityExchangeReason1Code"]
code_set: "ExternalAuthorityExchangeReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalAuthorityExchangeReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalAuthorityExchangeReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason for the exchange with the national competent authority, as published in an external category purpose code list.
External code sets can be downloaded from www.iso20022.org.
*`ADHR`-Ad hoc request.
*`CABB`-Competent Authority for Buyer Branch.
*`CABC`-Competent Authority for Basket Constituant.
*`CABT`-Competent Authority for Buyer Transmitting Firm.
*`CADB`-Competent Authority for Decision Making Branch.
*`CADU`-Competent Authority for Direct Underlying.
*`CAEB`-Competent Authority for Executing Branch.
*`CAFI`-Competent Authority for Instrument.
*`CAIX`-Competent Authority for Index.
*`CAMB`-Competent Authority for Membership Branch.
*`CASB`-Competent Authority for Seller Branch.
*`CAST`-Competent Authority for Seller Transmitting Firm.
*`CATV`-Competent Authority for Trading Venue.

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
| 1 | ADHR |
| 2 | CABB |
| 3 | CABC |
| 4 | CABT |
| 5 | CADB |
| 6 | CADU |
| 7 | CAEB |
| 8 | CAFI |
| 9 | CAIX |
| 10 | CAMB |
| 11 | CASB |
| 12 | CAST |
| 13 | CATV |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
