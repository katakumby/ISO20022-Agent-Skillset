---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalOrganisationIdentification1Code"]
code_set: "ExternalOrganisationIdentification1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalOrganisationIdentification1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalOrganisationIdentification1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external organisation identification scheme name code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`BANK`-Unique and unambiguous assignment made by a specific bank or similar financial institution to identify a relationship as defined between the bank and its client.
*`CBID`-A unique identification number assigned by a central bank to identify an organisation.
*`CHID`-A unique identification number assigned by a clearing house to identify an organisation
*`CINC`-A unique identification number assigned by a designated authority to a certificate of incorporation and used to identify an organisation.
*`COID`-Country authority given organisation identification (e.g., corporate registration number)
*`CUST`-Number assigned by an issuer to identify a customer.
Number assigned by a party to identify a creditor or debtor relationship.
*`DUNS`-A unique identification number provided by Dun & Bradstreet to identify an organisation.
*`EMPL`-Number assigned by a registration authority to an employer.
*`GS1G`-Global Location Number. A non-significant reference number used to identify legal entities, functional entities, or physical entities according to GS1 numbering scheme rules.The number is used to retrieve detailed information that is linked to it.
*`SREN`-The SIREN number is a 9 digit code assigned by INSEE, the French National Institute for Statistics and Economic Studies, to identify an organisation in France.
*`SRET`-The SIRET number is a 14 digit code assigned by INSEE, the French National Institute for Statistics and Economic Studies, to identify an organisation unit in France. It consists of the SIREN number, followed by a five digit classification number, to identify the local geographical unit of that entity
*`TXID`-Number assigned by a tax authority to identify an organisation.
*`BDID`-Identifier of the business domain in which the organisation is active.
*`BOID`-Other identification of the organisation.
*`USID`-Unique identifier assigned to a pension/superannuation fund, product, or scheme to which a superannuation contribution payment is directed.

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
| 1 | BANK |
| 2 | CBID |
| 3 | CHID |
| 4 | CINC |
| 5 | COID |
| 6 | CUST |
| 7 | DUNS |
| 8 | EMPL |
| 9 | GS1G |
| 10 | SREN |
| 11 | SRET |
| 12 | TXID |
| 13 | BDID |
| 14 | BOID |
| 15 | USID |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
