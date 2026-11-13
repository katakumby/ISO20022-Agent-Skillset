---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.4 Rejected <Rjctd>", "14.4.3.5.3.3.7.12.12.4.2 Reason <Rsn>", "14.4.3.5.3.3.7.12.12.4.2.1 ReasonCode <RsnCd>", "14.4.3.5.3.3.7.12.12.4.2.1.2 Proprietary <Prtry>"]
file_pages: [800]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.4.2.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 800 to 800.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 800

```text
CodeName Name Definition
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
14.4.3.5.3.3.7.12.12.4.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 800 February 2026
```

