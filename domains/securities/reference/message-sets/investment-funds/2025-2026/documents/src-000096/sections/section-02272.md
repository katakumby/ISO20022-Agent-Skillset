---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.28 RelatedPartyDetails <RltdPtyDtls>", "50.4.4.9.28.1 Identification <Id>"]
file_pages: [3179]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.28.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3179 to 3179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3179

```text
RelatedPartyDetails <RltdPtyDtls> contains the following Intermediary50 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3179
   Account <Acct> [0..1]  3179
     Identification <Id> [1..1] Text 3179
     AccountServicer <AcctSvcr> [0..1] ± 3180
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3180
   Role <Role> [0..1] ± 3180
Constraints
• OrderOriginatorEligibility1Rule
OrderOriginatorEligibility may only be present if Role is either UCL1 (UnderlyingClient1) or UCL2
(UnderlyingClient2).
50.4.4.9.28.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of the intermediary.
Identification <Id> contains the following elements (see "PartyIdentification139" on page 5043 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
50.4.4.9.28.2  Account <Acct>
Presence: [0..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Account <Acct> contains the following Account35 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 3179
   AccountServicer <AcctSvcr> [0..1] ± 3180
50.4.4.9.28.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3179 May 2026
```

