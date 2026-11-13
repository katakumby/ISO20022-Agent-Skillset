---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.34 NegativeIndicator <NegInd>"]
file_pages: [4631]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.34 NegativeIndicator <NegInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4631 to 4631.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4631

```text
66.1.24.9.34  NegativeIndicator <NegInd>
Presence: [0..1]
Definition: Indicates whether the account can hold a negative position in a security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.24.9.35  ProcessingOrder <PrcgOrdr>
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
66.1.24.9.36  Liability <Lblty>
Presence: [0..1]
Definition: Specifies whether the investor assumes responsibility for the liability.
Liability <Lblty> contains one of the following elements (see "Liability1Choice" on page 4870 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4870
Or}   Proprietary <Prtry> [1..1] ± 4870
66.1.24.9.37  InvestorProfile <InvstrPrfl>
Presence: [0..*]
Definition: Information used to determine fees and types of operations that can be carried out on the
account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4631 May 2026
```

