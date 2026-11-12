---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalMandateReason1Code"]
code_set: "ExternalMandateReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalMandateReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalMandateReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external mandate processing reason code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`AC01`-Format of the account number specified is not correct
*`AC04`-Account number specified has been closed on the Receiver's books
*`AC06`-Account specified is blocked, prohibiting posting of transactions against it.
*`AG01`-Transaction forbidden on this type of account (formerly NoAgreement)
*`AG02`-Bank Operation code specified in the message is not valid for receiver
*`AM02`-Specific transaction/message amount is greater than allowed maximum
*`AM03`-Specified message amount is a non processable currency outside of existing agreement
*`AM05`-Duplication.
*`BE01`-Identification of end customer is not consistent with associated account number. (formerly CreditorConsistency).
*`BE04`-Specification of creditor's address, which is required for payment, is missing/not correct (formerly IncorrectCreditorAddress).
*`BE05`-Party who initiated the message is not recognised by the end customer
*`BE06`-End customer specified is not known at associated Sort/National Bank Code or does no longer exist in the books
*`BE07`-Specification of debtor's address, which is required for payment, is missing/not correct.
*`DT01`-Invalid date (eg, wrong settlement date)
*`FF01`-File format incomplete or invalid
*`MD01`-No Mandate
*`MD02`-Mandate related information data required by the scheme is missing.
*`MD07`-End customer is deceased.
*`MD08`-Receiving agent does not offer specified Mandate services
*`MD09`-Account is not open to specified Mandates services
*`MD10`-Account is not open to specified Mandates services for this particular creditor
*`MD11`-Agent to whom the message needs to be forwarded cannot be located
*`MD12`-Mandate identification is not unique to the creditor
*`MD13`-There is a problem with the customer authentication
*`MD14`-Agent in the payment workflow is incorrect
*`MD15`-Currency of the transaction is incorrect
*`MD16`-Cancellation/amendment requested by the debtor
*`MD17`-Cancellation/amendment requested by the creditor
*`MD18`-Cancellation/amendment requested by the creditor and the debtor
*`MD19`-Mandate cancellation following early reimbursement of the debit by the debtor
*`MD20`-Mandate cancellation following validity expiration
*`MD21`-Mandate cancellation due to suspected fraud
*`MD22`-Mandate cancellation following mandate initiation cancellation
*`MD23`-Mandate cancellation following mandate amendment cancellation
*`MS02`-Reason has not been specified by end customer
*`MS03`-Reason has not been specified by agent.
*`NARR`-Reason is provided as narrative information in the additional reason information.
*`RC01`-Bank Identifier code specified in the message has an incorrect format (formerly IncorrectFormatForRoutingCode).
*`RF01`-Transaction reference is not unique within the message.
*`RR01`-Specification of the debtor’s account or unique identification needed for reasons of regulatory requirements is insufficient or missing
*`RR02`-Specification of the debtor’s name and/or address needed for regulatory requirements is insufficient or missing.
*`RR03`-Specification of the creditor’s name and/or address needed for regulatory requirements is insufficient or missing.
*`RR04`-Regulatory Reason
*`SL01`-Due to specific service offered by the Debtor Agent
*`SL11`-Whitelisting service offered by the Debtor Agent; Debtor has not included the Creditor on its “Whitelist” (yet). In the Whitelist the Debtor may list all allowed Creditors to debit Debtor bank account.
*`SL12`-Blacklisting service offered by the Debtor Agent; Debtor included the Creditor on his “Blacklist”. In the Blacklist the Debtor may list all Creditors not allowed to debit Debtor bank account.
*`SL13`-Due to Maximum allowed Direct Debit Transactions per period service offered by the Debtor Agent.
*`SL14`-Due to Maximum allowed Direct Debit Transaction amount service offered by the Debtor Agent.

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
| 2 | AC04 |
| 3 | AC06 |
| 4 | AG01 |
| 5 | AG02 |
| 6 | AM02 |
| 7 | AM03 |
| 8 | AM05 |
| 9 | BE01 |
| 10 | BE04 |
| 11 | BE05 |
| 12 | BE06 |
| 13 | BE07 |
| 14 | DT01 |
| 15 | FF01 |
| 16 | MD01 |
| 17 | MD02 |
| 18 | MD07 |
| 19 | MD08 |
| 20 | MD09 |
| 21 | MD10 |
| 22 | MD11 |
| 23 | MD12 |
| 24 | MD13 |
| 25 | MD14 |
| 26 | MD15 |
| 27 | MD16 |
| 28 | MD17 |
| 29 | MD18 |
| 30 | MD19 |
| 31 | MD20 |
| 32 | MD21 |
| 33 | MD22 |
| 34 | MD23 |
| 35 | MS02 |
| 36 | MS03 |
| 37 | NARR |
| 38 | RC01 |
| 39 | RF01 |
| 40 | RR01 |
| 41 | RR02 |
| 42 | RR03 |
| 43 | RR04 |
| 44 | SL01 |
| 45 | SL11 |
| 46 | SL12 |
| 47 | SL13 |
| 48 | SL14 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
