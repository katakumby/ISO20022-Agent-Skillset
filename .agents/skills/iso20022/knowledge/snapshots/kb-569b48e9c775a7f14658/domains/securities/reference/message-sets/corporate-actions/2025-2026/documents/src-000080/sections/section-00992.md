---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.128 RejectionReason89Code"]
file_pages: [1237, 1238]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.128 RejectionReason89Code

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1237 to 1238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1237

```text
CodeName Name Definition
(generally used in Dutch Auctions or Bid
Tenders).
DQBI InvalidBidIncrement Bid price / basis points / percentage
increments rejected due to invalid bid
increment for the event (generally used
in Dutch Auctions or Bid Tenders).
DCAN RejectedSinceAlreadyCancelled Cancellation request was rejected since
the instruction has already been
cancelled.
DPRG RejectedSinceInProgress Cancellation request has been rejected
because the instruction process is in
progress or has been processed.
INIR InstructionIrrevocable Instruction is irrevocable.
SHAR ShareholderNumberRejection Unrecognised, missing or invalid
shareholder number.
BSTR BeforeInstructionPeriod Instruction is submitted before instruction
start date.
CTCT MissingContact Contact information is missing.
DUPL DuplicateInstruction Instruction is rejected due to duplicate
business message identifier.
PROI MissingProtectIdentification Protect identification is required for cover
protect instructions.
PROT MissingProtectDate Protect date is required for cover protect
instructions.
PRON NoProtectPrivilege No protect privilege for this event.
TRTI MissingTransactionType Transaction type is missing or invalid for
protect or cover protect instructions.
REJA RejectedByIssuerAgent Instruction rejected by the issuer agent.
IPAW InvalidPaperwork Required paperwork is invalid,
incomplete or missing.
IPED InstructionPriorToEntitlementDate Instruction was received prior to
entitlement date.
16.2.2.128  RejectionReason89Code
Definition: Specifies the reason why the instruction request has a rejected status.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
CERT IncorrectCertification Instruction is rejected since the provided
certification is incorrect or incomplete.
INVA InvalidForTaxAuthorities For tax reclaim, the reclaim is invalid for
the tax authorities.
OPTY InvalidOptionType Invalid option type.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1237 February 2026
```

## File page 1238

```text
CodeName Name Definition
ULNK InvalidReference Linked reference is unknown.
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
(generally used in Dutch Auctions or Bid
Tenders).
DQBI InvalidBidIncrement Bid price / basis points / percentage
increments rejected due to invalid bid
increment for the event (generally used
in Dutch Auctions or Bid Tenders).
SHAR ShareholderNumberRejection Unrecognised, missing or invalid
shareholder number.
ITAX IncorrectTaxRate Tax rate provided is incorrect. It falls
outside the acceptable values for that
investment country.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1238 February 2026
```

