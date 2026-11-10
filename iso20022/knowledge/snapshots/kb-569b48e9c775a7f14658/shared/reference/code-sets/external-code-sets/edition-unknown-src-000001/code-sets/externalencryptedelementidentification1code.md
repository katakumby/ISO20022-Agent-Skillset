---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalEncryptedElementIdentification1Code"]
code_set: "ExternalEncryptedElementIdentification1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalEncryptedElementIdentification1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalEncryptedElementIdentification1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the element that has been encrypted, as published in an external data to encrypt type code set.
External code sets can be downloaded from www.iso20022.org.

These codes have the same value as the tag assignments shown in ISO 13492 for the data encryption dataset.  The codes are variable in length and conform to ISO/IEC 8825-1.
*`8A`-Primary Account Number
*`8C`-Track1
*`8D`-Track2
*`8E`-Track3
*`8F`-Visible Card Security Code
*`89`-Pre-agreed structure for encrypting data. Permits combination of data elements as per bilateral agreement.
*`90`-Expiry Date
*`91`-Payment Account Reference (PAR)
*`92`-Payer Customer Identification.
*`93`-Payer Customer Name
*`94`-Payer Customer Address
*`95`-Payer Customer Credentials Alien Registration Number
*`96`-Payer Customer Credentials Driver Licence Identification
*`97`-Payer Customer Credentials National Identifier
*`98`-Payer Customer Credentials Passport Number
*`99`-Payer Customer Credentials Social Security Number
*`9A`-Payee Customer Identification.
*`9B`-Payee Customer Name.
*`9C`-Payee Customer Address
*`9D`-Payee Customer Credentials Alien Registration Number
*`9E`-Payee Customer Credentials Driver Licence Identification
*`9F1F`-Payee Customer Credentials National Identifier
*`9F20`-Payee Customer Credentials Passport Number
*`9F21`-Payee Customer Credentials Social Security Number
*`9F22`-Customer Device Identification
*`9F23`-Customer Device Location
*`9F24`-Customer Device Internet Protocol Address
*`9F25`-Customer Device E-mail
*`9F26`-Token Payment Token
*`9F27`-Token Token Requestor Identification
*`9F28`-Cardholder Name
*`9F29`-Cardholder Identification Customer Identification
*`9F2A`-Cardholder Identification Alien Registration Number
*`9F2B`-Cardholder Identification Driver Licence Identification
*`9F2C`-Cardholder Identification Email
*`9F2D`-Cardholder Identification NatinalIdentifier
*`9F2E`-Cardholder Identification Passport Number
*`9F2F`-Cardholder Identification PhoneNumber
*`9F30`-Cardholder Identification Social Security Number
*`9F31`-Cardholder Identification Address
*`9F32`-Cardholder Contact Information Name
*`9F33`-Cardholder Contact Information Home Phone Number
*`9F34`-Cardholder Contact Information Business Phone Number
*`9F35`-Cardholder Contact Information Mobile Phone Number
*`9F36`-Cardholder Contact Information Other Phone Number
*`9F37`-Cardholder Contact Information Personal Email Address
*`9F38`-Cardholder Contact Information Business Email Address
*`9F39`-Cardholder Contact Information Other Email Address
*`9F3A`-Cardholder Address Digits
*`9F3B`-Cardholder Billing Address
*`9F3C`-Cardholder Birth Date
*`9F3D`-Cardholder Place Of Birth
*`9F3E`-Cardholder Employee Identification Number
*`9F3F`-Cardholder Employer Identification Number
*`9F40`-Cardholder Password
*`9F41`-Cardholder Postal Code
*`9F42`-Cardholder Shipping Address
*`9F43`-Cardholder Shipping Address From
*`9F44`-Cardholder Shipping Address To
*`9F45`-Cardholder Tax Identification Number
*`9F46`-Account From Account Identification
*`9F47`-Account To Account Identification

## Source constraints

```json
{
  "type": "string",
  "pattern": "^([0-9A-F][0-9A-F]){1,3}$"
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | 8A |
| 2 | 8C |
| 3 | 8D |
| 4 | 8E |
| 5 | 8F |
| 6 | 89 |
| 7 | 90 |
| 8 | 91 |
| 9 | 92 |
| 10 | 93 |
| 11 | 94 |
| 12 | 95 |
| 13 | 96 |
| 14 | 97 |
| 15 | 98 |
| 16 | 99 |
| 17 | 9A |
| 18 | 9B |
| 19 | 9C |
| 20 | 9D |
| 21 | 9E |
| 22 | 9F1F |
| 23 | 9F20 |
| 24 | 9F21 |
| 25 | 9F22 |
| 26 | 9F23 |
| 27 | 9F24 |
| 28 | 9F25 |
| 29 | 9F26 |
| 30 | 9F27 |
| 31 | 9F28 |
| 32 | 9F29 |
| 33 | 9F2A |
| 34 | 9F2B |
| 35 | 9F2C |
| 36 | 9F2D |
| 37 | 9F2E |
| 38 | 9F2F |
| 39 | 9F30 |
| 40 | 9F31 |
| 41 | 9F32 |
| 42 | 9F33 |
| 43 | 9F34 |
| 44 | 9F35 |
| 45 | 9F36 |
| 46 | 9F37 |
| 47 | 9F38 |
| 48 | 9F39 |
| 49 | 9F3A |
| 50 | 9F3B |
| 51 | 9F3C |
| 52 | 9F3D |
| 53 | 9F3E |
| 54 | 9F3F |
| 55 | 9F40 |
| 56 | 9F41 |
| 57 | 9F42 |
| 58 | 9F43 |
| 59 | 9F44 |
| 60 | 9F45 |
| 61 | 9F46 |
| 62 | 9F47 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
