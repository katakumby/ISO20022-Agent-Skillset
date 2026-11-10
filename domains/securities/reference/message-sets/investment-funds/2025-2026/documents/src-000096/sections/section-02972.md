---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.11 NewDetails <NewDtls>"]
file_pages: [4167]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.11 NewDetails <NewDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4167 to 4167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4167

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
56.4.3.2.11  NewDetails <NewDtls>
Presence: [0..1]
Definition: Expected execution information.
Impacted by: C10 "DateElementRule"
NewDetails <NewDtls> contains the following ExpectedExecutionDetails5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExpectedTradeDateTime <XpctdTradDtTm> [0..1] ± 4167
   ExpectedCashSettlementDate <XpctdCshSttlmDt> [0..1] Date 4167
Constraints
• DateElementRule
Either ExpectedTradeDateTime or ExpectedCashSettlementDate must be present. Both may be
present.
56.4.3.2.11.1  ExpectedTradeDateTime <XpctdTradDtTm>
Presence: [0..1]
Definition: Expected date or expected date and time at which a price will be applied according to the
terms of the prospectus.
ExpectedTradeDateTime <XpctdTradDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
56.4.3.2.11.2  ExpectedCashSettlementDate <XpctdCshSttlmDt>
Presence: [0..1]
Definition: Date of a payment, for example, a prepayment date.
Datatype: "ISODate" on page 5388
56.4.3.2.12  GatingOrHoldBackDetails <GtgOrHldBckDtls>
Presence: [0..1]
Definition: Information about gating and hold back of redemption proceeds.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4167 May 2026
```

