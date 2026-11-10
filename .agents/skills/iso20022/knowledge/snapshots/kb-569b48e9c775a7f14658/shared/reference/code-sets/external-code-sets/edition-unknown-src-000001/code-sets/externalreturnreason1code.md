---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalReturnReason1Code"]
code_set: "ExternalReturnReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalReturnReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalReturnReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the return reason, as published in an external return reason code list.
External code sets can be downloaded from www.iso20022.org.
*`AC01`-Format of the account number specified is not correct
*`AC03`-Wrong IBAN in SCT
*`AC04`-Account number specified has been closed on the bank of account's books
*`AC06`-Account specified is blocked, prohibiting posting of transactions against it.
*`AC13`-Debtor account type is missing or invalid
*`AC14`-An agent in the payment chain is invalid.
*`AC15`-Account details have changed.
*`AC16`-Account is in sequestration.
*`AC17`-Account is in liquidation.
*`AG01`-Transaction forbidden on this type of account (formerly NoAgreement)
*`AG02`-Bank Operation code specified in the message is not valid for receiver
*`AM01`-Specified message amount is equal to zero
*`AM02`-Specific transaction/message amount is greater than allowed maximum
*`AM03`-Specified message amount is an non processable currency outside of existing agreement
*`AM04`-Amount of funds available to cover specified message amount is insufficient.
*`AM05`-Duplication
*`AM06`-Specified transaction amount is less than agreed minimum.
*`AM07`-Amount specified in message has been blocked by regulatory authorities.
*`AM09`-Amount received is not the amount agreed or expected
*`AM10`-Sum of instructed amounts does not equal the control sum.
*`ARDT`-Already returned original SCT
*`BE01`-Identification of end customer is not consistent with associated account number, organisation ID or private ID.
*`BE04`-Specification of creditor's address, which is required for payment, is missing/not correct (formerly IncorrectCreditorAddress).
*`BE05`-Party who initiated the message is not recognised by the end customer
*`BE06`-End customer specified is not known at associated Sort/National Bank Code or does no longer exist in the books
*`BE07`-Specification of debtor's address, which is required for payment, is missing/not correct.
*`BE08`-Returned as a result of a bank error.
*`CN01`-Authorisation is cancelled.
*`CNOR`-Creditor bank is not registered under this BIC in the CSM
*`CNPC`-Cash not picked up by Creditor or cash could not be delivered to Creditor
*`CURR`-Currency of the payment is incorrect
*`CUST`-Cancellation requested by the Debtor
*`DNOR`-Debtor bank is not registered under this BIC in the CSM
*`DS28`-Return following technical problems resulting in erroneous transaction.
*`DT01`-Invalid date (eg, wrong settlement date)
*`DT02`-Cheque has been issued but not deposited and is considered expired.
*`ED01`-Correspondent bank not possible.
*`ED03`-Balance of payments complementary info is requested
*`ED05`-Settlement of the transaction has failed.
*`EMVL`-The card payment is fraudulent and was not processed with EMV technology for an EMV card.
*`ERIN`-The Extended Remittance Information (ERI) option is not supported.
*`FF05`-Local Instrument code is missing or invalid
*`FOCR`-Return following a cancellation request
*`FR01`-Returned as a result of fraud.
*`FRTR`-Final response/tracking is recalled as mandate is cancelled.
*`MD01`-No Mandate
*`MD02`-Mandate related information data required by the scheme is missing.
*`MD06`-Return of funds requested by end customer
*`MD07`-End customer is deceased.
*`MS02`-Reason has not been specified by end customer
*`MS03`-Reason has not been specified by agent.
*`NARR`-Reason is provided as narrative information in the additional reason information.
*`NOAS`-No response from Beneficiary
*`NOCM`-Customer account is not compliant with regulatory requirements, for example FICA (in South Africa) or any other regulatory requirements which render an account inactive for certain processing.
*`NOOR`-Original SCT never received
*`PINL`-The card payment is fraudulent (lost and stolen fraud) and was processed as EMV transaction without PIN verification.
*`RC01`-Bank Identifier code specified in the message has an incorrect format (formerly IncorrectFormatForRoutingCode).
*`RC07`-Incorrrect BIC of the beneficiary Bank in the SCTR
*`RF01`-Transaction reference is not unique within the message.
*`RR01`-Specification of the debtor’s account or unique identification needed for reasons of regulatory requirements is insufficient or missing
*`RR02`-Specification of the debtor’s name and/or address needed for regulatory requirements is insufficient or missing.
*`RR03`-Specification of the creditor’s name and/or address needed for regulatory requirements is insufficient or missing.
*`RR04`-Regulatory Reason
*`RUTA`-Return following investigation request and no remediation possible.
*`SL01`-Due to specific service offered by the Debtor Agent
*`SL02`-Due to specific service offered by the Creditor Agent
*`SL11`-Whitelisting service offered by the Debtor Agent; Debtor has not included the Creditor on its “Whitelist” (yet). In the Whitelist the Debtor may list all allowed Creditors to debit Debtor bank account.
*`SL12`-Blacklisting service offered by the Debtor Agent; Debtor included the Creditor on his “Blacklist”. In the Blacklist the Debtor may list all Creditors not allowed to debit Debtor bank account.
*`SL13`-Due to Maximum allowed Direct Debit Transactions per period service offered by the Debtor Agent.
*`SL14`-Due to Maximum allowed Direct Debit Transaction amount service offered by the Debtor Agent.
*`SP01`-Payment is stopped by account holder.
*`SP02`-Previously stopped by means of a stop payment advise.
*`SVNR`-The card payment is returned since a cash amount rendered was not correct or goods or a service was not rendered to the customer, e.g. in an e-commerce situation.
*`TM01`-Associated message was received after agreed processing cut-off time.
*`TRAC`-Return following direct debit being removed from tracking process.
*`UPAY`-Payment is not justified.
*`AGNT`-Agent in the payment workflow is incorrect.
*`FF06`-Category Purpose code is missing or invalid.
*`RC08`-ClearingSystemMemberidentifier is invalid or missing.
Generic usage if cannot specify between debit or credit account.
*`BE11`-Creditor country code is missing or invalid.
*`BE17`-Creditor or Ultimate Creditor identification code missing or invalid.
*`AC02`-Debtor account number invalid or missing.
*`RR11`-Invalid or missing identification of a bank proprietary service.
*`BE10`-Debtor country code is missing or invalid.
*`BE16`-Debtor or Ultimate Debtor identification code missing or invalid.
*`RC11`-Intermediary Agent is invalid or missing.
*`RR12`-Invalid or missing identification required within a particular country or payment type.
*`FF03`-Payment Type Information is missing or invalid.
Generic usage if cannot specify Service Level or Local Instrument code.
*`FF07`-Purpose is missing or invalid.
*`FF04`-Service Level code is missing or invalid.
*`RR09`-Structured creditor reference invalid or missing.
*`RR05`-Regulatory or Central Bank Reporting information missing, incomplete or invalid.
*`RR07`-Remittance information structure does not comply with rules for payment type.
*`RR08`-Remittance information truncated to comply with rules for payment type.
*`RR06`-Tax information missing, incomplete or invalid.
*`AG07`-Debtor account cannot be debited for a generic reason.
Usage: Code value may be used in general purposes and as a replacement for AM04 if debtor bank does not reveal its customer's insufficient funds for privacy reasons.
*`G004`-In a FIToFI Customer Credit Transfer: Credit to the creditor’s account is pending, status Originator is waiting for funds provided via a cover. Update will follow from the Status Originator.
*`MD05`-Creditor or creditor's agent should not have collected the direct debit.
*`AC07`-Creditor account number closed.
*`DC04`-Return of Covering Settlement due to the underlying Credit Transfer details not being received.
*`RC04`-Creditor bank identifier is invalid or missing.
*`DT04`-Future date not supported.
*`DUPL`-Payment is a duplicate of another payment.
*`RC03`-Debtor bank identifier is invalid or missing.

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
| 2 | AC03 |
| 3 | AC04 |
| 4 | AC06 |
| 5 | AC13 |
| 6 | AC14 |
| 7 | AC15 |
| 8 | AC16 |
| 9 | AC17 |
| 10 | AG01 |
| 11 | AG02 |
| 12 | AM01 |
| 13 | AM02 |
| 14 | AM03 |
| 15 | AM04 |
| 16 | AM05 |
| 17 | AM06 |
| 18 | AM07 |
| 19 | AM09 |
| 20 | AM10 |
| 21 | ARDT |
| 22 | BE01 |
| 23 | BE04 |
| 24 | BE05 |
| 25 | BE06 |
| 26 | BE07 |
| 27 | BE08 |
| 28 | CN01 |
| 29 | CNOR |
| 30 | CNPC |
| 31 | CURR |
| 32 | CUST |
| 33 | DNOR |
| 34 | DS28 |
| 35 | DT01 |
| 36 | DT02 |
| 37 | ED01 |
| 38 | ED03 |
| 39 | ED05 |
| 40 | EMVL |
| 41 | ERIN |
| 42 | FF05 |
| 43 | FOCR |
| 44 | FR01 |
| 45 | FRTR |
| 46 | MD01 |
| 47 | MD02 |
| 48 | MD06 |
| 49 | MD07 |
| 50 | MS02 |
| 51 | MS03 |
| 52 | NARR |
| 53 | NOAS |
| 54 | NOCM |
| 55 | NOOR |
| 56 | PINL |
| 57 | RC01 |
| 58 | RC07 |
| 59 | RF01 |
| 60 | RR01 |
| 61 | RR02 |
| 62 | RR03 |
| 63 | RR04 |
| 64 | RUTA |
| 65 | SL01 |
| 66 | SL02 |
| 67 | SL11 |
| 68 | SL12 |
| 69 | SL13 |
| 70 | SL14 |
| 71 | SP01 |
| 72 | SP02 |
| 73 | SVNR |
| 74 | TM01 |
| 75 | TRAC |
| 76 | UPAY |
| 77 | AGNT |
| 78 | FF06 |
| 79 | RC08 |
| 80 | BE11 |
| 81 | BE17 |
| 82 | AC02 |
| 83 | RR11 |
| 84 | BE10 |
| 85 | BE16 |
| 86 | RC11 |
| 87 | RR12 |
| 88 | FF03 |
| 89 | FF07 |
| 90 | FF04 |
| 91 | RR09 |
| 92 | RR05 |
| 93 | RR07 |
| 94 | RR08 |
| 95 | RR06 |
| 96 | AG07 |
| 97 | G004 |
| 98 | MD05 |
| 99 | AC07 |
| 100 | DC04 |
| 101 | RC04 |
| 102 | DT04 |
| 103 | DUPL |
| 104 | RC03 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
