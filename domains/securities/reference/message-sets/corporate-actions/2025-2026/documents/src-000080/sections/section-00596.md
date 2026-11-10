---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.1 TotalInstructedBalance <TtlInstdBal>"]
file_pages: [783]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.1 TotalInstructedBalance <TtlInstdBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 783 to 783.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 783

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             ReasonCode <RsnCd> [1..1]  805
{Or               Code <Cd> [1..1] CodeSet 806
Or}               Proprietary <Prtry> [1..1] ± 806
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 806
14.4.3.5.3.3.1  TotalInstructedBalance <TtlInstdBal>
Presence: [1..1]
Definition: Provides information about the total instructed balance.
TotalInstructedBalance <TtlInstdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
14.4.3.5.3.3.2  TotalAcceptedInstructionBalance <TtlAccptdInstrBal>
Presence: [0..1]
Definition: Daily total of all accepted instructions for given day. Cover protect instructions will be
included in this total balance.
TotalAcceptedInstructionBalance <TtlAccptdInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.3.3  TotalCancelledInstructionBalance <TtlCancInstrBal>
Presence: [0..1]
Definition: Daily total of cancelled instructions for a given day.
TotalCancelledInstructionBalance <TtlCancInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 783 February 2026
```

