---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.1 Accepted <Accptd>"]
file_pages: [796]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.1 Accepted <Accptd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 796 to 796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 796

```text
InstructionStatus <InstrSts> contains one of the following InstructionProcessingStatus62Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Accepted <Accptd> [1..1] ± 796
Or   Cancelled <Canc> [1..1] ± 797
Or   AcceptedForFurtherProcessing <AccptdForFrthrPrcg> [1..1] ± 797
Or   Rejected <Rjctd> [1..1]  797
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 798
Or}     Reason <Rsn> [1..*]  C3 798
       ReasonCode <RsnCd> [1..1]  798
{Or         Code <Cd> [1..1] CodeSet 799
Or}         Proprietary <Prtry> [1..1] ± 800
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 801
Or   Pending <Pdg> [1..1]  801
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 801
Or}     Reason <Rsn> [1..*]  C4 801
       ReasonCode <RsnCd> [1..1]  802
{Or         Code <Cd> [1..1] CodeSet 802
Or}         Proprietary <Prtry> [1..1] ± 803
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
Or   PendingCancellation <PdgCxl> [1..1] ± 803
Or   Covered <Cvrd> [1..1] ± 804
Or   Uncovered <Ucvrd> [1..1] ± 804
Or}   Returned <Rtrd> [1..1]  804
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 805
Or}     Reason <Rsn> [1..*]  C6 805
       ReasonCode <RsnCd> [1..1]  805
{Or         Code <Cd> [1..1] CodeSet 806
Or}         Proprietary <Prtry> [1..1] ± 806
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 806
14.4.3.5.3.3.7.12.12.1  Accepted <Accptd>
Presence: [1..1]
Definition: Instruction is accepted.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 796 February 2026
```

