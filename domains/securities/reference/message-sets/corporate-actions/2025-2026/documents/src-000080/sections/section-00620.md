---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.13 InTransshipmentBalance <InTrnsShipmntBal>"]
file_pages: [809]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.13 InTransshipmentBalance <InTrnsShipmntBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 809 to 809.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 809

```text
TradeDatePositionBalance <TradDtPosBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.13  InTransshipmentBalance <InTrnsShipmntBal>
Presence: [0..1]
Definition: Balance of physical securities that are in the process of being transferred from one
depository/agent to another.
InTransshipmentBalance <InTrnsShipmntBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.14  RegisteredBalance <RegdBal>
Presence: [0..1]
Definition: Balance of financial instruments that are registered (in the name of a nominee name or of the
beneficial owner).
RegisteredBalance <RegdBal> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.15  ObligatedBalance <OblgtdBal>
Presence: [0..1]
Definition: Position that account holders should return to the account servicer to participate in the event
or to fulfil their obligation for the event to be complete, for example, return of securities for late
announced drawing.
ObligatedBalance <OblgtdBal> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 809 February 2026
```

