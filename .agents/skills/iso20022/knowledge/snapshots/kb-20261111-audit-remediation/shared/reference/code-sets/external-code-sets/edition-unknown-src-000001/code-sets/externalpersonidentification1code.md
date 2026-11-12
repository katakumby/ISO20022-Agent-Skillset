---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPersonIdentification1Code"]
code_set: "ExternalPersonIdentification1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPersonIdentification1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPersonIdentification1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external person identification scheme name code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`ARNU`-Number assigned by a social security agency to identify a non-resident person.
*`CCPT`-Number assigned by an authority to identify the passport number of a person.
*`CUST`-Number assigned by an issuer to identify a customer.
*`DRLC`-Number assigned by an authority to identify a driver's license.
*`EMPL`-Number assigned by a registration authority to an employee.
*`NIDN`-Number assigned by an authority to identify the national identity number of a person.
*`SOSE`-Number assigned by an authority to identify the social security number of a person.
*`TELE`-Number assigned by a telephone or mobile phone operator to identify a person. A person may have multiple phone numbers.
*`TXID`-Number assigned by a tax authority to identify a person.
*`POID`-Commercial identification of the person.
*`BANK`-Unique and unambiguous assignment made by a specific bank or similar financial institution to identify a relationship as defined between the bank and its client.

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
| 1 | ARNU |
| 2 | CCPT |
| 3 | CUST |
| 4 | DRLC |
| 5 | EMPL |
| 6 | NIDN |
| 7 | SOSE |
| 8 | TELE |
| 9 | TXID |
| 10 | POID |
| 11 | BANK |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
