---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.2 OptionType <OptnTp>"]
file_pages: [787]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.2 OptionType <OptnTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 787 to 787.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 787

```text
14.4.3.5.3.3.7.2  OptionType <OptnTp>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
OptionType <OptnTp> contains one of the following elements (see "CorporateActionOption30Choice"
on page 881 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 882
Or}   Proprietary <Prtry> [1..1] ± 883
14.4.3.5.3.3.7.3  InstructedBalance <InstdBal>
Presence: [1..1]
Definition: Balance of instructed position.
InstructedBalance <InstdBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
14.4.3.5.3.3.7.4  DefaultAction <DfltActn>
Presence: [0..1]
Definition: Indicates the default action related to a corporate action event.
DefaultAction <DfltActn> contains one of the following elements (see
"DefaultProcessingOrStandingInstruction2Choice" on page 998 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DefaultOptionIndicator <DfltOptnInd> [1..1] Indicator 998
Or}   StandingInstructionIndicator <StgInstrInd> [1..1] Indicator 998
14.4.3.5.3.3.7.5  OptionAcceptedInstructedBalance <OptnAccptdInstdBal>
Presence: [0..1]
Definition: Daily total of accepted instructions received for a given option.
OptionAcceptedInstructedBalance <OptnAccptdInstdBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 787 February 2026
```

