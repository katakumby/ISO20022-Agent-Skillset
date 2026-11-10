---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCashAccountType1Code"]
code_set: "ExternalCashAccountType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCashAccountType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCashAccountType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the nature, or use, of the cash account in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`CACC`-Account used to post debits and credits when no specific account has been nominated.
*`CARD`-Account used for credit card payments.
*`CASH`-Account used for the payment of cash.
*`CHAR`-Account used for charges if different from the account for
payment.
*`CISH`-Account used for payment of income if different from the current cash account
*`COMM`-Account used for commission if different from the account
for payment.
*`CPAC`-Account used to post settlement debit and credit entries on behalf of a designated Clearing Participant.
*`LLSV`-Account used for savings with special interest and withdrawal terms.
*`LOAN`-Account used for loans.
*`MGLD`-Account used for a marginal lending facility.
*`MOMA`-Account used for money markets if different from the cash
account.
*`NREX`-Account used for non-resident external.
*`ODFT`-Account is used for overdrafts.
*`ONDP`-Account used for overnight deposits.
*`OTHR`-Account not otherwise specified.
*`SACC`-Account used to post debit and credit entries, as a result of transactions cleared and settled through a specific clearing and settlement system.
*`SLRY`-Accounts used for salary payments.
*`SVGS`-Account used for savings.
*`TAXE`-Account used for taxes if different from the account for
payment.
*`TRAN`-A transacting account is the most basic type of bank account that you can get. The main difference between transaction and cheque accounts is that you usually do not get a cheque book with your transacting account and neither are you offered an overdraft facility.
*`TRAS`-Account used for trading if different from the current cash account.
*`VACC`-Account created virtually to facilitate collection and reconciliation.
*`NFCA`-Non-Resident Individual / Entity Foreign Current held domestically.
*`RFCA`-Resident Individual Foreign Currency held domestically.
*`REFC`-Resident Entity Foreign Currency held domestically.
*`NLCY`-Non-Resident domestic currency account.
*`RLCY`-Resident domestic currency account.
*`ODEP`-Account used as ordinary deposit for everyday deposits and withdrawals.

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
| 1 | CACC |
| 2 | CARD |
| 3 | CASH |
| 4 | CHAR |
| 5 | CISH |
| 6 | COMM |
| 7 | CPAC |
| 8 | LLSV |
| 9 | LOAN |
| 10 | MGLD |
| 11 | MOMA |
| 12 | NREX |
| 13 | ODFT |
| 14 | ONDP |
| 15 | OTHR |
| 16 | SACC |
| 17 | SLRY |
| 18 | SVGS |
| 19 | TAXE |
| 20 | TRAN |
| 21 | TRAS |
| 22 | VACC |
| 23 | NFCA |
| 24 | RFCA |
| 25 | REFC |
| 26 | NLCY |
| 27 | RLCY |
| 28 | ODEP |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
