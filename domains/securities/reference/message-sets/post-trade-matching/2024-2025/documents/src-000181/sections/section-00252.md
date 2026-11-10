---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.20 Reversible2Choice", "7.1.19.20.2 Proprietary <Prtry>"]
file_pages: [310]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.20.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 310 to 310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
CodeName Name Definition
REVL Reversible Securities lending contract can be ended
by the borrower before the expiration
date.
FIXD Fixed Securities lending contract can not be
ended by the borrower before the
expiration date.
CABK CallBack Securities lending contract can be ended
by the lender before the expiration date.
7.1.19.20.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Closing of the securities lending contract expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.21  Number1Choice
Definition: Choice of format for the number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NumberIdentification <NbId> [1..1] Text 310
Or}   Proprietary <Prtry> [1..1] ± 310
7.1.19.21.1  NumberIdentification <NbId>
Presence: [1..1]
Definition: Number of maximum 3 numeric text.
Datatype: "Max3NumericText" on page 669
7.1.19.21.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary number format.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 310 February 2025
```

