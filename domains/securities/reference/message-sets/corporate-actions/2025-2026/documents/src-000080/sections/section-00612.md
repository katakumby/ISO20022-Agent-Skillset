---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.4 Rejected <Rjctd>", "14.4.3.5.3.3.7.12.12.4.2 Reason <Rsn>", "14.4.3.5.3.3.7.12.12.4.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [801]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.4.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 801 to 801.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 801

```text
Definition: Rejection reason specified as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
14.4.3.5.3.3.7.12.12.4.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Additional information about the rejection status.
Datatype: "Max210Text" on page 1249
14.4.3.5.3.3.7.12.12.5  Pending <Pdg>
Presence: [1..1]
Definition: Instruction has not been completed.
Pending <Pdg> contains one of the following PendingStatus85Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 801
Or}   Reason <Rsn> [1..*]  C4 801
     ReasonCode <RsnCd> [1..1]  802
{Or       Code <Cd> [1..1] CodeSet 802
Or}       Proprietary <Prtry> [1..1] ± 803
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
14.4.3.5.3.3.7.12.12.5.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
14.4.3.5.3.3.7.12.12.5.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the pending status.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 801 February 2026
```

