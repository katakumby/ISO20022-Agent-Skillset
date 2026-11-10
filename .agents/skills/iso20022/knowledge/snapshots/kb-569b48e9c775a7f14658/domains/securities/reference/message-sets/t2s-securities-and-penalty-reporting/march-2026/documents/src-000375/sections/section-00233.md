---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.15 AggregateBalancePerSafekeepingPlace44", "7.1.5.15.4 AggregateBalance <AggtBal>"]
file_pages: [309]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.15.4 AggregateBalance <AggtBal>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 309 to 309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
Pledgee <Pldgee> contains the following elements (see "Pledgee3" on page 417 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PledgeeTypeAndIdentification <PldgeeTpAndId> [0..1]  417
{Or     TypeAndIdentification <TpAndId> [1..1]  418
       Identification <Id> [1..1] IdentifierSet C2 418
       PledgeeType <PldgeeTp> [1..1] CodeSet 418
Or     Identification <Id> [1..1]  419
       Identification <Id> [0..1] Text 419
       PledgeeType <PldgeeTp> [1..1] CodeSet 419
Or}     Proprietary <Prtry> [1..1] ± 419
   LEI <LEI> [0..1] IdentifierSet 420
Constraints
• PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
Following Must be True
    /PledgeeTypeAndIdentification Must be present
 Or    /LEI Must be present
7.1.5.15.4  AggregateBalance <AggtBal>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
AggregateBalance <AggtBal> contains the following elements (see "Balance6" on page 267 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 268
   Quantity <Qty> [1..1] ± 268
7.1.5.15.5  AvailableBalance <AvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is available.
AvailableBalance <AvlblBal> contains the following elements (see "Balance8" on page 271 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 271
   Quantity <Qty> [1..1] ± 271
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 309 March 2026
```

