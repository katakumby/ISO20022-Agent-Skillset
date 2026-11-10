---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>", "12.1.11.1.7.3 OtherMargin <OthrMrgn>", "12.1.11.1.7.3.1 Type <Tp>", "12.1.11.1.7.3.1.2 Proprietary <Prtry>"]
file_pages: [429]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.7.3.1.2 Proprietary <Prtry>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 429 to 429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 429

```text
CodeName Name Definition
NEMA NegociationMargin Margin calculated on the same basis as
for the variation margin but the margin is
kept by the central counterparty and not
"paid " to the other clearing member.
INMA InitialMargin Margin required for absorbing future
market price fluctuations (market risks)
occurring between the default of a
member and close-out of unsettled
securities positions by the central
counterparty.
VAMA VariationMargin Margin required to cover the risk linked
to the price fluctuations occurred on the
unsettled exposures towards central
counterparty.
INCA IncreaseCoverageAmount Additional margin required to cover a risk
increase (expressed in the reporting
currency). This results from a risk
management decision depending on
central counterparty specific criteria.
12.1.11.1.7.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the margin type using a proprietary format.
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
12.1.11.1.7.3.2  Amount <Amt>
Presence: [1..1]
Definition: Provides the margin amount in the reporting currency and optionally in the original currency.
Amount <Amt> contains the following Amount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
429
   ReportingAmount <RptgAmt> [1..1] Amount 430
12.1.11.1.7.3.2.1  OriginalCurrencyAmount <OrgnlCcyAmt>
Presence: [0..1]
Definition: Amount expressed in the original currency.
Impacted by:   'C1 ActiveCurrency  ',   'C7 CurrencyAmount  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 429
```

