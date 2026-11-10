---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.4 Rejected <Rjctd>", "14.4.3.5.3.3.7.12.12.4.2 Reason <Rsn>", "14.4.3.5.3.3.7.12.12.4.2.1 ReasonCode <RsnCd>", "14.4.3.5.3.3.7.12.12.4.2.1.1 Code <Cd>"]
file_pages: [799]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.4.2.1.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 799 to 799.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 799

```text
ReasonCode <RsnCd> contains one of the following RejectedReason58Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 799
Or}   Proprietary <Prtry> [1..1] ± 800
14.4.3.5.3.3.7.12.12.4.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Rejection reason specified as a code.
Datatype: "RejectionReason86Code" on page 1235
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
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 799 February 2026
```

