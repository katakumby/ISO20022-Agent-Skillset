---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.9 UnaffirmedReason3Choice", "7.1.28.9.2 Proprietary <Prtry>"]
file_pages: [595]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.9.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 595 to 595.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 595

```text
CodeName Name Definition
NAFF CounterpartyNotAffirmed Specifies the reason the counterparty
has not affirmed.
7.1.28.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a unaffirmed status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.10  AffirmationStatus10Choice
Definition: Choice of format for the affirmation status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 595
Or}   Proprietary <Prtry> [1..1] ± 595
7.1.28.10.1  Code <Cd>
Presence: [1..1]
Definition: Status of affirmation of a trade.
Datatype: "AffirmationStatus1Code" on page 614
CodeName Name Definition
AFFI Affirmed Status of the transaction is affirmed.
NAFI Unaffirmed Status of the transaction is unaffirmed.
7.1.28.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade has been unaffirmed.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 595 February 2025
```

