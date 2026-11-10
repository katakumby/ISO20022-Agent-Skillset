---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.17 AggregateBalancePerSafekeepingPlace44", "82.1.5.17.4 AggregateBalance <AggtBal>"]
file_pages: [2901]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.17.4 AggregateBalance <AggtBal>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2901 to 2901.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2901

```text
Pledgee <Pldgee> contains the following elements (see "Pledgee3" on page 3063 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PledgeeTypeAndIdentification <PldgeeTpAndId> [0..1]  3064
{Or     TypeAndIdentification <TpAndId> [1..1]  3064
       Identification <Id> [1..1] IdentifierSet C2 3064
       PledgeeType <PldgeeTp> [1..1] CodeSet 3065
Or     Identification <Id> [1..1]  3065
       Identification <Id> [0..1] Text 3065
       PledgeeType <PldgeeTp> [1..1] CodeSet 3065
Or}     Proprietary <Prtry> [1..1] ± 3066
   LEI <LEI> [0..1] IdentifierSet 3066
Constraints
• PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
Following Must be True
    /PledgeeTypeAndIdentification Must be present
 Or    /LEI Must be present
82.1.5.17.4  AggregateBalance <AggtBal>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
AggregateBalance <AggtBal> contains the following elements (see "Balance6" on page 2857 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 2857
   Quantity <Qty> [1..1] ± 2858
82.1.5.17.5  AvailableBalance <AvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is available.
AvailableBalance <AvlblBal> contains the following elements (see "Balance8" on page 2863 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 2863
   Quantity <Qty> [1..1] ± 2863
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2901 August 2026
```

