---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.19 BidRangeType1Choice", "16.1.15.19.2 Proprietary <Prtry>"]
file_pages: [919]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.19.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 919 to 919.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 919

```text
CodeName Name Definition
DIVI Divisible All values (including minimum and
maximum prices) are divisible by the bid
interval.
INCR Incremental No values within the bid range are
divisible by the bid interval including the
minimum and maximum prices. Each
value between the minimum and
maximum prices is incremented by the
bid interval.
MULT InMultiple Minimum and maximum prices are not
divisible by the bid interval. All
successive values between the minimum
and maximum prices are in multiples of
the bid interval.
16.1.15.19.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Bid range type expressed as a proprietary value.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.20  ConsentTypeFormat4Choice
Definition: Choice between a standard code or proprietary code to specify the consent type format
required.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 919
Or}   Proprietary <Prtry> [1..1] ± 920
16.1.15.20.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the consent type required.
Datatype: "ConsentType1Code" on page 1166
CodeName Name Definition
CTRM ChangeInTerms Change in the terms and conditions of
the bond.
DUPY DueAndPayable Change in the due and payable
conditions.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 919 February 2026
```

