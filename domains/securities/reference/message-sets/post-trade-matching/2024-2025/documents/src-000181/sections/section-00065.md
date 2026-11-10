---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.7 UnderlyingFinancialInstrument <UndrlygFinInstrm>", "3.4.7.2 Attributes <Attrbts>", "3.4.7.2.30 PercentageOfDebtClaims <PctgOfDebtClms>"]
file_pages: [89]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.7.2.30 PercentageOfDebtClaims <PctgOfDebtClms>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 89 to 89.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
price of the instrument is indexed to the price of an underlying benchmark.
Datatype: "PercentageRate" on page 667
3.4.7.2.30  PercentageOfDebtClaims <PctgOfDebtClms>
Presence: [0..1]
Definition: Percentage of the underlying assets of a fund that represents a debt, for example, in the
context of the EU Savings directive.
Datatype: "PercentageRate" on page 667
3.4.7.2.31  CouponAttachedNumber <CpnAttchdNb>
Presence: [0..1]
Definition: Number of the coupon attached to the physical security.
CouponAttachedNumber <CpnAttchdNb> contains one of the following elements (see
"Number1Choice" on page 310 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NumberIdentification <NbId> [1..1] Text 310
Or}   Proprietary <Prtry> [1..1] ± 310
3.4.7.2.32  PoolNumber <PoolNb>
Presence: [0..1]
Definition: Number identifying a group of underlying assets assigned by the issuer of a factored
security.
PoolNumber <PoolNb> contains the following elements (see "GenericIdentification37" on page 280 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 280
   Issuer <Issr> [0..1] Text 280
3.4.7.2.33  VersionNumber <VrsnNb>
Presence: [0..1]
Definition: Number allocated by options exchanges to record that an option has undergone a change in
its contract specifications (particularly adjustment of the strike price).
VersionNumber <VrsnNb> contains one of the following elements (see "Number1Choice" on
page 310 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NumberIdentification <NbId> [1..1] Text 310
Or}   Proprietary <Prtry> [1..1] ± 310
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 89 February 2025
```

