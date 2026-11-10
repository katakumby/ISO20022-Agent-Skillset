---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.2 SequenceRange1Choice", "6.1.15.2.3 FromToSequence <FrToSeq>"]
file_pages: [844]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.2.3 FromToSequence <FrToSeq>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 844 to 844.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 844

```text
Datatype: "Max35Text" on page 916
6.1.15.2.3  FromToSequence <FrToSeq>
Presence: [1..*]
Definition: Particular sequence range specified between a start sequence and an end sequence.
FromToSequence <FrToSeq> contains the following SequenceRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromSequence <FrSeq> [1..1] Text 844
   ToSequence <ToSeq> [1..1] Text 844
6.1.15.2.3.1  FromSequence <FrSeq>
Presence: [1..1]
Definition: Start sequence of the range.
Datatype: "Max35Text" on page 916
6.1.15.2.3.2  ToSequence <ToSeq>
Presence: [1..1]
Definition: End sequence of the range.
Datatype: "Max35Text" on page 916
6.1.15.2.4  EqualSequence <EQSeq>
Presence: [1..*]
Definition: Specified sequence to match.
Datatype: "Max35Text" on page 916
6.1.15.2.5  NotEqualSequence <NEQSeq>
Presence: [1..*]
Definition: Specified sequence to be excluded.
Datatype: "Max35Text" on page 916
6.1.15.3  Pagination1
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 844
   LastPageIndicator <LastPgInd> [1..1] Indicator 845
6.1.15.3.1  PageNumber <PgNb>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
844 March 2026
```

