---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.23 InvestorProfile2", "66.1.28.23.5 MarketMaker <MktMakr>", "66.1.28.23.5.2 Compliance <Cmplc>"]
file_pages: [4854]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.23.5.2 Compliance <Cmplc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4854 to 4854.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4854

```text
ContractPeriod <CtrctPrd> contains the following elements (see "DateTimePeriod2" on page 4465 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 4466
   ToDateTime <ToDtTm> [0..1] DateTime 4466
66.1.28.23.5.2  Compliance <Cmplc>
Presence: [0..1]
Definition: Indicates whether the market maker is obligated to comply with the requirements of the
contract it holds with the exchange or is exempt from these obligations.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.23.5.3  MaximumSpread <MaxSprd>
Presence: [0..1]
Definition: Percentage of the variation between the maximum accepted minimum and maximum value
of an action.
Datatype: "PercentageRate" on page 5401
66.1.28.23.5.4  Discount <Dscnt>
Presence: [0..1]
Definition: Rate of discount.
Datatype: "PercentageRate" on page 5401
66.1.28.24  ResidualCash2
Definition: Specifies how the cash in the account that is awaiting investment is to be dealt with.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4854
   Currency <Ccy> [0..1] CodeSet C1 4855
66.1.28.24.1  Indicator <Ind>
Presence: [1..1]
Definition: Indicates whether the cash in the account awaiting investment is to be transferred.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4854 May 2026
```

