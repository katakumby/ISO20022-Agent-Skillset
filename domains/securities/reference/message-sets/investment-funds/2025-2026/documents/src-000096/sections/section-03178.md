---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.6 Cancellation Right", "66.1.6.1 DateFormat1Choice", "66.1.6.1.2 Code <Cd>"]
file_pages: [4408]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.6.1.2 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4408 to 4408.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4408

```text
66.1.6.1.2  Code <Cd>
Presence: [1..1]
Definition: Date expressed as a code.
Datatype: "SettlementDate1Code" on page 5362
CodeName Name Definition
ASAP AsSoonAsPossible Transfer is to be effected as soon as
possible.
ENDC AtEndOfContract Transfer is to be effected at the end of
the contract.
WHIF WhenAndIfIssued Settlement takes place when the
financial instrument is issued by the
issuer.
66.1.6.1.3  DateTime <DtTm>
Presence: [1..1]
Definition: Date expressed as a calendar date and time.
Datatype: "ISODateTime" on page 5388
66.1.7 Cash
66.1.7.1  CashOutForecast6
Definition: Cash movements out of a fund as a result of investment funds transactions, eg, redemptions
or switch-out.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4409
   SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4409
   SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4409
   ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4409
   AdditionalBalance <AddtlBal> [0..1] ± 4410
Constraints
• AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list (AdditionalBalance/
TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders, AdditionalBalance/
TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders) must be present.
On Condition
    /AdditionalBalance is present
Following Must be True
    /AdditionalBalance/TotalUnitsFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalUnitsFromCashOrders Must be present
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4408 May 2026
```

