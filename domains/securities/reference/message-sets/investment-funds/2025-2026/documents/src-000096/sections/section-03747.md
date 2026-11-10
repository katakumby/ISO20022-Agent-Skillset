---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.39 Intermediary49", "66.1.30.39.3 OrderOriginatorEligibility <OrdrOrgtrElgblty>"]
file_pages: [5033]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.39.3 OrderOriginatorEligibility <OrdrOrgtrElgblty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5033 to 5033.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5033

```text
66.1.30.39.3  OrderOriginatorEligibility <OrdrOrgtrElgblty>
Presence: [0..1]
Definition: Counterparties eligibility as defined by article 24 of the EU MiFID Directive applicable to
transactions executed by investment firms for eligible counterparties.
Datatype: "OrderOriginatorEligibility1Code" on page 5332
CodeName Name Definition
ELIG Eligible Eligible counterparty - MiFID
classification of counterparty. Eligible
customers are the most sophisticated
level of investor, able to opt out of some
the protections afforded by conduct of
business rules defined under MiFID.
RETL Retail Retail client - MiFID classification of
counterparty. Retail customers are the
least sophisticated level of investor.
PROF Professional Professional client - MiFID classification
of counterparty. Professional customers
are, for example, investment firms, credit
institutions, insurance companies.
66.1.30.39.4  TradingPartyCapacity <TradgPtyCpcty>
Presence: [0..1]
Definition: Capacity of the party executing an order.
Datatype: "TradingCapacity8Code" on page 5378
CodeName Name Definition
AGEN Agent Trading as Agent on behalf of a
customer.
PRIN Principal Trading as Principal.
66.1.30.39.5  Role <Role>
Presence: [0..1]
Definition: Function performed by the intermediary.
Role <Role> contains one of the following elements (see "InvestmentFundRole2Choice" on page 4779
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4779
Or}   Proprietary <Prtry> [1..1] ± 4780
66.1.30.40  CRSForm1Choice
Definition: Choice of formats for the type of Common Reporting Standard (CRS) form.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5033 May 2026
```

