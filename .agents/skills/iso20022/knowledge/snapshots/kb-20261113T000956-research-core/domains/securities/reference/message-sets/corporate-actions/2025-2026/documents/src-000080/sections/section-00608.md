---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.2 Cancelled <Canc>"]
file_pages: [797]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.2 Cancelled <Canc>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 797 to 797.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 797

```text
Accepted <Accptd> contains the following elements (see "NoSpecifiedReason1" on page 1144 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
14.4.3.5.3.3.7.12.12.2  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction cancelled by client cancellation instruction.
Cancelled <Canc> contains one of the following elements (see "CancelledStatus12Choice" on
page 1146 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1147
Or}   Reason <Rsn> [1..*]  C2 1147
     ReasonCode <RsnCd> [1..1]  1147
{Or       Code <Cd> [1..1] CodeSet 1148
Or}       Proprietary <Prtry> [1..1] ± 1148
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1148
14.4.3.5.3.3.7.12.12.3  AcceptedForFurtherProcessing <AccptdForFrthrPrcg>
Presence: [1..1]
Definition: Provides status information related to an instruction request that is accepted. This means
that the instruction has been received, is processable and has been validated for further processing.
AcceptedForFurtherProcessing <AccptdForFrthrPrcg> contains the following elements (see
"NoSpecifiedReason1" on page 1144 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
14.4.3.5.3.3.7.12.12.4  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction rejected by the receiver.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 797 February 2026
```

