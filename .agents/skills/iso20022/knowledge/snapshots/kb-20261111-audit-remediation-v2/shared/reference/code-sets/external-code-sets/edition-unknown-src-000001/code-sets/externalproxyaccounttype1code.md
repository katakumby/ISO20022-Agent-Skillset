---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalProxyAccountType1Code"]
code_set: "ExternalProxyAccountType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalProxyAccountType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalProxyAccountType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external proxy account type code, as published in the proxy account type external code set.
External code sets can be downloaded from www.iso20022.org.
*`TELE`-A telephone number in the format specified by the 'The international public telecommunication numbering plan ITU-T E.164.
*`EMAL`-Internationalised address of an electronic mail box for internet messages.
*`DNAM`-Internationalised internet domain name.
*`CINC`-Corporate Identification issued by a national  institution or regulator, used as account proxy. 
(applied for corporate account proxy).
*`COTX`-Unique government-issued tax Identification used as account proxy to identify the corporate (for example for government tax) and typically linked to the corporate bank account (applied for corporate account proxy).
*`COID`-Identification issued by a national  institution or regulator (different from a national scheme like a clearing provider), used as account proxy (applied for corporate or individual account proxy).
*`CUST`-Any other customer identification number issued by a corporate, bank or other organization, used as account proxy.
(applied for corporate or individual account proxy).
*`DRLC`-Unique government-issued Identification used as account proxy to  identify the individual  (for example for government charges, road taxes and tolls,vaccination charges) and typically linked to the individual's bank account (applied for  individual account proxy).
*`EIDN`-Government-issued Identification (different from a passport Identification or a national Identification). Used as account proxy to  identify the individual (for example for public benefits) and typically linked to the individual's bank account (applied for  individual account proxy).
*`EWAL`-Market-adopted prepaid instruments like e-Wallets, payments to / from e-wallets from / to bank accounts (applied for corporate or individual account proxy).
*`PVTX`-Unique government-issued  tax Identification  used as account proxy to  identify the individual  for example for government tax) and typically linked to the individual's bank account (applied for  individual account proxy).
*`LEIC`-Legal Entity Identifier used as account proxy (applied for corporate account proxy).
Use cases: Can be used by corporates as a "government-issued" Identification for registration with payment schemes as a proxy. The proxy may be further used for payments and collections using the underlying instant payment rails for a variety of corporate use cases.
*`MBNO`-Mobile phone number in the format specified by the “The international public telecommunication numbering plan ITU- T E 164" (applied for corporate or individual account proxy).
*`NIDN`-Unique government-issued Identification  used as account proxy to  identify the individual  or corporate for example for public benefits, government subsidies) and typically linked to the individual's / corporate bank account.
(applied for corporate or individual account proxy).
*`CCPT`-Unique government-issued Identification  used as account proxy to  identify the individual  (for example for government charges, road taxes, vaccination charges) and typically linked to the individual's bank account
(applied for  individual account proxy).
*`SHID`-Account proxy issued by a payment scheme (applied for corporate or individual account proxy).
Use cases: Any proxies issued by clearing systems, for example VPA (India), FPS Identifier (Hong Kong), Jompay (Malaysia) CCIN (Canada).
*`SOSE`-Unique government-issued Identification  used as account proxy to identify the individual  (for example for public benefits) and typically linked to the individual's bank account (applied for individual account proxy).
*`TOKN`-Electronic Identification used, for example, to mask an account number as a means of data secrecy.
(applied for corporate or individual account proxy).
*`UBIL`-Subscriber Identification for utilities and services. As opposed to a biller Identification, this identification is used for the subscriber of the service (applied for corporate or individual account proxy).
*`VIPN`-Account proxy for receiving insurance claims, pay insurance premium, road tax payments, traffic tickets etc.(applied for corporate or individual account proxy).
*`BIID`-Billers of specific utilities could register for a Biller Identification as supported in the clearing scheme, and use this identification for collections (applied for corporate account proxy).
*`OSID`-Additional scheme identifier used to complement the primary scheme identification so that banks can apply respective validations of the proxy value as per the Type code provided.

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
| 1 | TELE |
| 2 | EMAL |
| 3 | DNAM |
| 4 | CINC |
| 5 | COTX |
| 6 | COID |
| 7 | CUST |
| 8 | DRLC |
| 9 | EIDN |
| 10 | EWAL |
| 11 | PVTX |
| 12 | LEIC |
| 13 | MBNO |
| 14 | NIDN |
| 15 | CCPT |
| 16 | SHID |
| 17 | SOSE |
| 18 | TOKN |
| 19 | UBIL |
| 20 | VIPN |
| 21 | BIID |
| 22 | OSID |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
