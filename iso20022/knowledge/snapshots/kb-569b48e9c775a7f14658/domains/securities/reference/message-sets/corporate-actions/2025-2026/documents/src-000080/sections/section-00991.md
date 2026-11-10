---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.123 RateType14Code"]
file_pages: [1235, 1236]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.123 RateType14Code

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1235 to 1236.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1235

```text
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
NILP NilPayment Rate will not be paid.
16.2.2.123  RateType14Code
Definition: Specifies the type of rate.
Type: CodeSet
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
JLID IssuerDiscretion Indicates that there will not be a uniform
proration rate that applies to all
instructions or accounts.
16.2.2.124  RateType5Code
Definition: Specifies the type of rate.
Type: CodeSet
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.2.2.125  RateType7Code
Definition: Specifies the type of rate.
Type: CodeSet
CodeName Name Definition
SCHD Scheduled Rate of the scheduled payment.
USCD Unscheduled Rate of the unscheduled payment.
16.2.2.126  RateValueType7Code
Definition: Specifies the value of a rate.
Type: CodeSet
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.2.2.127  RejectionReason86Code
Definition: Specifies the reason why the instruction request has a rejected status.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1235 February 2026
```

## File page 1236

```text
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
CERT IncorrectCertification Instruction is rejected since the provided
certification is incorrect or incomplete.
INVA InvalidForTaxAuthorities For tax reclaim, the reclaim is invalid for
the tax authorities.
OPTY InvalidOptionType Invalid option type.
ULNK InvalidReference Linked reference is unknown.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
LACK LackofSecurities Instructed position exceeds the eligible
balance.
LATE MarketDeadlineMissed Received after market deadline.
NMTY Mismatch Mismatch between option number and
option type.
FULL MissingBeneficiaryOwnerDetails Rejected due to missing beneficiary
owner details.
CANC OptionCancelled Option is not valid; it has been cancelled
by the market or service provider, and
cannot be responded to. Any responses
already processed against this option
are considered void and new responses
will be required.
INTV OptionInactive Option is not active and can no longer be
responded to. Any responses already
processed against this option will remain
valid, for example, expired option.
OPNM OptionNumberRejection Unrecognised option number.
OTHR Other Other. See Narrative.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
REFT RefusedByTaxAuthorities Reclaim is refused by the tax authorities.
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
EVNM UnrecognisedIdentification Unrecognised event number.
DQCS AmountRejection Unrecognised or invalid instructed cash
amount.
DQCC CurrencyRejection Invalid instructed currency.
DQAM InstructionTypeRejection Invalid use of instructed amount (QCAS)
or of instructed quantity (QINS)
qualifiers.
IRDQ InvalidUseRoundUpQuantity Instruction is rejected due to invalid use
of the additional round up quantity.
DQBV InvalidBidValue Bid price / basis points / percentage falls
outside of bid range for the event
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1236 February 2026
```

