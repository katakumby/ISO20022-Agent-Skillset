---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalVerificationReason1Code"]
code_set: "ExternalVerificationReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalVerificationReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalVerificationReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external verification reason code, as published in an external verification code set.
External code sets can be downloaded from www.iso20022.org.
*`AC01`-Account number provided in the request is invalid or missing.
*`AGNT`-Agent identification provided in the request is incorrect
*`DUPL`-Request is a duplicate of another request
*`AG01`-Transaction forbidden on this type of account (Payment cannot be made to this account for example not open for deposits, blocked, closed).
*`BNOR`-PSP is not registered under this Scheme.
*`DS28`-Return following technical problems resulting in erroneous transaction.
*`FF01`-File format incomplete or invalid.
*`MS03`-Reason has not been specified by agent.
*`NORR`-No response on request within timeframe.
*`NR01`-PSP not able to confirm details and no reason is stated.
*`RC03`-Debtor bank identifier is invalid or missing.
*`RC04`-Creditor bank identifier is invalid or missing.
*`TM01`-Associated message was received after agreed processing cut-off time.
*`PN01`-Account Owner name and Payment Account number do not match.
*`PN02`-Account Owner name and Payment Account number is a close match.
*`PI01`-Account Owner Identification and Payment Account number do not match.

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
| 1 | AC01 |
| 2 | AGNT |
| 3 | DUPL |
| 4 | AG01 |
| 5 | BNOR |
| 6 | DS28 |
| 7 | FF01 |
| 8 | MS03 |
| 9 | NORR |
| 10 | NR01 |
| 11 | RC03 |
| 12 | RC04 |
| 13 | TM01 |
| 14 | PN01 |
| 15 | PN02 |
| 16 | PI01 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
