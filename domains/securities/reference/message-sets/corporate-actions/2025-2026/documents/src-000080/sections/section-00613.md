---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.5 Pending <Pdg>", "14.4.3.5.3.3.7.12.12.5.2 Reason <Rsn>", "14.4.3.5.3.3.7.12.12.5.2.1 ReasonCode <RsnCd>"]
file_pages: [802]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.5.2.1 ReasonCode <RsnCd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 802 to 802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 802

```text
Reason <Rsn> contains the following PendingStatusReason35 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  802
{Or     Code <Cd> [1..1] CodeSet 802
Or}     Proprietary <Prtry> [1..1] ± 803
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
14.4.3.5.3.3.7.12.12.5.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Specifies the reason why the instruction's processing is pending.
ReasonCode <RsnCd> contains one of the following PendingReason82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 802
Or}   Proprietary <Prtry> [1..1] ± 803
14.4.3.5.3.3.7.12.12.5.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Pending reason specified as a code.
Datatype: "PendingReason38Code" on page 1229
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
BSTR BeforeInstructionPeriod Instruction is submitted before instruction
start date.
DQCS DisagreementOnCashAmount Unrecognised or invalid instructed cash
amount.
NTAX InconsistentTaxRate Tax rate is not consistent with the
documentation in place.
ITAX IncorrectTaxRate Tax rate provided is incorrect. It falls
outside the acceptable values for that
investment country.
IPED InstructionPriorToEntitlementDate Instruction was received prior to
entitlement date.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 802 February 2026
```

