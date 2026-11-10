---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.31 SecuritiesTradeDetails100", "35.1.16.31.1 TradeDate <TradDt>"]
file_pages: [1563]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.31.1 TradeDate <TradDt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1563 to 1563.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1563

```text
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if InstructionProcessingAdditionalDetails
is present, then it must not contain information that can be provided in a structured field.
• TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time of the
place of trade, for example, of the stock exchange, or of the selling broker for OTC.
35.1.16.31.1  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.16.31.2  OpeningSettlementDate <OpngSttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
OpeningSettlementDate <OpngSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.16.31.3  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days on which the interest rate accrues (daily accrual note).
Impacted by: C20 "NumberRule"
Datatype: "Max3Number" on page 2189
Constraints
• NumberRule
If Number is negative, then Sign must be present.
35.1.16.31.4  InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1563 March 2026
```

