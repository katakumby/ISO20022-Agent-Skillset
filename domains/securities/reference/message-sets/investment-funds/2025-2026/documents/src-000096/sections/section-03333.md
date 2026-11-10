---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.3 InvestmentAccount74", "66.1.24.3.34 OpeningDate <OpngDt>"]
file_pages: [4572]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.3.34 OpeningDate <OpngDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4572 to 4572.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4572

```text
66.1.24.3.34  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Legal opening date for the account.
OpeningDate <OpngDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4467
Or}   DateTime <DtTm> [1..1] DateTime 4467
66.1.24.3.35  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Legal closing date for the account.
ClosingDate <ClsgDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4467
Or}   DateTime <DtTm> [1..1] DateTime 4467
66.1.24.3.36  NegativeIndicator <NegInd>
Presence: [0..1]
Definition: Indicates whether the account can hold a negative position in a security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.24.3.37  ProcessingOrder <PrcgOrdr>
Presence: [0..1]
Definition: Order in which securities are moved from the account.
Datatype: "PositionEffect3Code" on page 5343
CodeName Name Definition
FIFO Fifo First in, first out. Results in a position
obtained after having sold in priority the
securities bought chronologically.
LIFO Lifo Last in, last out. Results in a position
obtained after having sold in priority the
securities bought chronologically.
66.1.24.3.38  Liability <Lblty>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4572 May 2026
```

