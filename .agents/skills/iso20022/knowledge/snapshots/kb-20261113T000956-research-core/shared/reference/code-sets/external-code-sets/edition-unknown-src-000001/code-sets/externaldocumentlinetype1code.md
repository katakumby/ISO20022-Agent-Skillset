---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalDocumentLineType1Code"]
code_set: "ExternalDocumentLineType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalDocumentLineType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalDocumentLineType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the document line type as published in an external document type code list.
*`ADPI`-Line item reference is an additional product identification assigned by the manufacturer.
*`AISB`-Line item reference is an alternate International Standard Book Number (ISBN).
*`ASNB`-Line item reference is an asset number.
*`CTNB`-Line item reference is a catalog number.
*`DBSP`-Line item reference is Dun & Bradstreet Standard Product and Service code.
*`EANN`-Line item reference is an European Article Number (EAN).
*`EINB`-Line item reference is an equipment identification number.
*`GSNB`-Line item reference is a general specification number.
*`HIBC`-Line item reference is a Health Care Industry Bar Code (HIBC)
*`ISBN`-Line item reference is an International Standard Book Number (ISBN).
*`LTNB`-Line item reference is a lot number.
*`MDNB`-Line item reference is a model number
*`PRNB`-Line item reference is a part reference number.
*`PTCD`-Line item reference is a product type code.
*`SKNB`-Line item reference is a stock number.
*`STNB`-Line item reference is a style number.
*`TONB`-Line item reference is a technical order number.
*`UPCC`-Line item reference is an UPC consumer package code.
*`UPNB`-Line item reference is an Universal Product Number.

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
| 1 | ADPI |
| 2 | AISB |
| 3 | ASNB |
| 4 | CTNB |
| 5 | DBSP |
| 6 | EANN |
| 7 | EINB |
| 8 | GSNB |
| 9 | HIBC |
| 10 | ISBN |
| 11 | LTNB |
| 12 | MDNB |
| 13 | PRNB |
| 14 | PTCD |
| 15 | SKNB |
| 16 | STNB |
| 17 | TONB |
| 18 | UPCC |
| 19 | UPNB |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
