---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalDocumentAmountType1Code"]
code_set: "ExternalDocumentAmountType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalDocumentAmountType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalDocumentAmountType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the nature, or use, of the amount, as published in an external document amount type code set.
External code sets can be downloaded from www.iso20022.org.
*`APDS`-Addition discount based on third-party agreed business promotional activity, i.e., extra 10 percent discount for 15 days)
*`STDS`-Discount based on volume purchased.
*`TMDS`-Discount based on terms negotiated for payment within a specified time period, i.e., 2/10 Net 30 (2 percent discount if paid in 10 days; otherwise, net amount is due in 30 days).
*`CITY`-Tax accessed by city jurisdictions within a country.
*`CNTY`-Tax accessed by county jurisdictions within a country.
*`LOCL`-Tax accessed by local jurisdictions within a country.
*`PROV`-Tax accessed by province jurisdictions within a country.
*`STAT`-Tax accessed by state jurisdictions within a country.
*`CREN`-Amount is a credit note.
*`DUPA`-Amount is due payable.
*`PRIN`-Amount is the outstanding principal.
*`TOTA`-Amount is the total.
*`INTE`-Amount is the interest.
*`ESCO`-Amount is in escrow.
*`TAXS`-Amount is tax.
*`INSU`-Amount is insurance.
*`OBAL`-Amount is the outstanding balance.
*`SBAL`-Amount is the statement balance.
*`MIDU`-Amount is the minimum due.
*`PADU`-Amount is past due.
*`CRTL`-Amount is available credit.
*`PBAL`-Amount is the previous balance.
*`CHAR`-Amount is new charges, for example new charges on a credit card.
*`FEES`-Amount is fees.
*`INTC`-Amount is interest charges, or example interest charges on a credit card.
*`REMI`-Amount remitted.
*`DISC`-Discount Applied. Generic usage if cannot be specified by any other discount code.

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
| 1 | APDS |
| 2 | STDS |
| 3 | TMDS |
| 4 | CITY |
| 5 | CNTY |
| 6 | LOCL |
| 7 | PROV |
| 8 | STAT |
| 9 | CREN |
| 10 | DUPA |
| 11 | PRIN |
| 12 | TOTA |
| 13 | INTE |
| 14 | ESCO |
| 15 | TAXS |
| 16 | INSU |
| 17 | OBAL |
| 18 | SBAL |
| 19 | MIDU |
| 20 | PADU |
| 21 | CRTL |
| 22 | PBAL |
| 23 | CHAR |
| 24 | FEES |
| 25 | INTC |
| 26 | REMI |
| 27 | DISC |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
