---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.5 Pending <Pdg>", "14.4.3.5.3.3.7.12.12.5.2 Reason <Rsn>", "14.4.3.5.3.3.7.12.12.5.2.1 ReasonCode <RsnCd>", "14.4.3.5.3.3.7.12.12.5.2.1.2 Proprietary <Prtry>"]
file_pages: [803]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.5.2.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 803 to 803.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 803

```text
CodeName Name Definition
MONY InsufficientMoney Insufficient money in your account.
IPAW InvalidPaperwork Required paperwork is invalid,
incomplete or missing.
LACK LackOfSecurities Insufficient financial instruments in your
account.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
MCER MissingCertification Awaiting receipt of adequate
certification.
MTAX MissingTaxRate Tax rate is missing.
OTHR Other Other. See Narrative.
FULL PendingBeneficiaryOwnerDetails Pending receipt of beneficiary owner
details.
PENR PendingReceipt Instruction is pending receipt of
securities, for example, from a purchase
or loan.
DQUA QuantityDisagreement Quantity of financial instruments does
not match.
SNAV SystemNotAvailable System is not available. Instruction is
sent outside of business hours.
CERT WrongCertificatesNumbers Certificate number error.
14.4.3.5.3.3.7.12.12.5.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Pending reason specified as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
14.4.3.5.3.3.7.12.12.5.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the processed instruction.
Datatype: "Max210Text" on page 1249
14.4.3.5.3.3.7.12.12.6  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Cancellation instruction is pending.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 803 February 2026
```

