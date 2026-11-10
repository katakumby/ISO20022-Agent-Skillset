---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties78", "7.1.26.1.1 Depository <Dpstry>"]
file_pages: [455]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.1 Depository <Dpstry>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 455 to 455.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 455

```text
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
7.1.26.1.1  Depository <Dpstry>
Presence: [0..1]
Definition: First party in the settlement chain. In a plain vanilla settlement, it is the Central Securities
Depository where the counterparty requests to receive the financial instrument or from where the
counterparty delivers the financial instruments.
Depository <Dpstry> contains the following elements (see "PartyIdentification148" on page 420 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  420
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C2 420
Or     NameAndAddress <NmAndAdr> [1..1] ± 420
Or}     Country <Ctry> [1..1] CodeSet C3 421
   LEI <LEI> [0..1] IdentifierSet 421
   ProcessingIdentification <PrcgId> [0..1] Text 421
7.1.26.1.2  Party1 <Pty1>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the depository.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 455 March 2026
```

