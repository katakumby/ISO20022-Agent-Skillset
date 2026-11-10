---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.9 OutForRegistrationBalance <OutForRegnBal>"]
file_pages: [808]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.9 OutForRegistrationBalance <OutForRegnBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 808 to 808.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 808

```text
14.4.3.5.3.9  OutForRegistrationBalance <OutForRegnBal>
Presence: [0..1]
Definition: Balance of financial instruments currently being processed by the institution responsible for
registering the new beneficial owner (or nominee).
OutForRegistrationBalance <OutForRegnBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.10  SettlementPositionBalance <SttlmPosBal>
Presence: [0..1]
Definition: Balance of securities representing only settled transactions; pending transactions not
included.
SettlementPositionBalance <SttlmPosBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.11  StreetPositionBalance <StrtPosBal>
Presence: [0..1]
Definition: Balance of financial instruments that remain registered in the name of the prior beneficial
owner.
StreetPositionBalance <StrtPosBal> contains the following elements (see "SignedQuantityFormat10"
on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.12  TradeDatePositionBalance <TradDtPosBal>
Presence: [0..1]
Definition: Balance of securities based on trade date, for example, includes all pending transactions in
addition to the balance of settled transactions.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 808 February 2026
```

