---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.12 InstructionStatus <InstrSts>", "14.4.3.5.3.3.7.12.12.9 Returned <Rtrd>", "14.4.3.5.3.3.7.12.12.9.2 Reason <Rsn>", "14.4.3.5.3.3.7.12.12.9.2.1 ReasonCode <RsnCd>", "14.4.3.5.3.3.7.12.12.9.2.1.1 Code <Cd>"]
file_pages: [806]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.12.9.2.1.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 806 to 806.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 806

```text
ReasonCode <RsnCd> contains one of the following ReturnedReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 806
Or}   Proprietary <Prtry> [1..1] ± 806
14.4.3.5.3.3.7.12.12.9.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Returned reason specified as a code.
Datatype: "ReturnedStatus1Code" on page 1241
CodeName Name Definition
NARR NarrativeReason See narrative field for reason.
PROR Prorated Shares returned due to prorated
acceptance.
14.4.3.5.3.3.7.12.12.9.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Returned reason specified as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
14.4.3.5.3.3.7.12.12.9.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Additional information about the returned status.
Datatype: "Max210Text" on page 1249
14.4.3.5.3.4  BlockedBalance <BlckdBal>
Presence: [0..1]
Definition: Balance of financial instruments that are blocked.
BlockedBalance <BlckdBal> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 806 February 2026
```

