---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalDocumentType1Code"]
code_set: "ExternalDocumentType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalDocumentType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalDocumentType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the document type as published in an external document type code list.
External code sets can be downloaded from www.iso20022.org.
*`CINV`-Document is an invoice.
*`CNFA`-Document is a credit note for the final amount settled for a commercial transaction.
*`CONT`-Document is a contract evidencing an agreement between the seller and buyer for the supply of goods and/or services.
*`CREN`-Document is a credit note.
*`DEBN`-Document is a debit note.
*`DISP`-Document is an advice of dispatch of the goods.
*`DNFA`-Document is a debit note for the final amount settled for a commercial transaction.
*`HIRI`-Document is an invoice for the hiring of human resources or renting goods or equipment.
*`INVS`-Document is a signed invoice.
*`MSIN`-Document is an invoice claiming payment for the supply of metered services, eg. Gas or electricity, supplied to a fixed meter.
*`PROF`-In trade transactions, a pro forma invoice is a document that states a commitment from the seller to sell goods to the buyer at specified prices and terms. It is used to declare the value of the trade. It is not a true invoice, because it is not used to record accounts receivable for the seller and accounts payable for the buyer.
*`PUOR`-Document is a purchase order.
*`QUOT`-Document is a quotation setting out the conditions under which the goods and/or services are offered.
*`SBIN`-Document is a statement of the transactions posted to the debtor's account at the supplier.
*`SPRR`-Document is a document presented by the seller in support of the procurement of goods and/or services.
*`TISH`-Document is a timesheet recording times for the provision of services and/or delivery of goods.
*`USAR`-Document is a usage report indicating the consumption pattern for designated goods and/or services.
*`AROI`-Document is a payment that applies to a specific source document.
*`BOLD`-Document is a shipping notice.
*`CMCN`-Document is an agreement between the parties, stipulating the terms and conditions of the delivery of goods or services.
*`SOAC`-Document is a statement of the transactions posted to the debtor's account at the supplier.
*`TSUT`-Document is a transaction identifier as assigned by the Trade Services Utility.
*`VCHR`-Document is an electronic payment document.

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
| 1 | CINV |
| 2 | CNFA |
| 3 | CONT |
| 4 | CREN |
| 5 | DEBN |
| 6 | DISP |
| 7 | DNFA |
| 8 | HIRI |
| 9 | INVS |
| 10 | MSIN |
| 11 | PROF |
| 12 | PUOR |
| 13 | QUOT |
| 14 | SBIN |
| 15 | SPRR |
| 16 | TISH |
| 17 | USAR |
| 18 | AROI |
| 19 | BOLD |
| 20 | CMCN |
| 21 | SOAC |
| 22 | TSUT |
| 23 | VCHR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
