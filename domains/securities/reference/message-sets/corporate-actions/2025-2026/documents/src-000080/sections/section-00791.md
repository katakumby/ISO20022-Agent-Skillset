---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.63 IntermediateSecuritiesDistributionTypeFormat19Choice"]
file_pages: [986]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.63 IntermediateSecuritiesDistributionTypeFormat19Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 986 to 986.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 986

```text
Definition: Unique reference identifying the beneficial owner the refund applies to, as assigned by the
account owner to the tax documentation sent to the account servicer for processing.
Datatype: "Max35Text" on page 1251
16.1.15.63  IntermediateSecuritiesDistributionTypeFormat19Choice
Definition: Choice between a standard code or proprietary code to specify the type of intermediate
securities distribution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 986
Or}   Proprietary <Prtry> [1..1] ± 987
16.1.15.63.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of intermediate security distribution.
Datatype: "IntermediateSecurityDistributionType6Code" on page 1217
CodeName Name Definition
BIDS ReverseRights Offer to existing holders by the issuing
company to repurchase its own
securities. The objective of the offer is to
reduce the number of outstanding
securities.
DRIP DividendReinvestment Dividend payment where holders can
keep cash or have the cash reinvested in
the market by the issuer into additional
shares in the issuing company. To be
distinguished from DVOP as the
company invests the dividend in the
market rather than creating new share
capital in exchange for the dividend.
DVCA CashDividend Distribution of cash to shareholders, in
proportion to their equity holding.
Ordinary dividends are recurring and
regular. Shareholder must take cash and
may be offered a choice of currency.
DVOP DividendOption Distribution of dividend option.
EXRI SubscriptionRights Call or exercise on nil paid securities or
intermediate securities resulting from an
intermediate securities distribution
(RHDI). This code is used for the second
event, when an intermediate securities'
issue (rights/coupons) is composed of
two events, the first event being the
distribution of intermediate securities.
PRIO OpenOfferRights Form of open or public offer where, due
to a limited amount of securities
available, priority is given to existing
shareholders.
DVSC ScripDividendOrPayment Dividend or interest paid in the form of
scrip.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 986 February 2026
```

