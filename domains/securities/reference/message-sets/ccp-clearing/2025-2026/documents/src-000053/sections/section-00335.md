---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>", "12.1.11.1.7.3 OtherMargin <OthrMrgn>", "12.1.11.1.7.3.1 Type <Tp>"]
file_pages: [428]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.7.3.1 Type <Tp>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 428 to 428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 428

```text
If the margin amount calculation is to be shown in more details (with for example, the
MarkToMarketNetted or MarkToMarketGross amounts), then it is recommended to use the element
variation margin that is present at a higher level in the message.
12.1.11.1.7.3.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of margin that is calculated.
Type <Tp> contains one of the following MarginType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 428
Or}   Proprietary <Prtry> [1..1] ± 429
12.1.11.1.7.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Provides the margin type using a code.
Datatype: MarginType1Code on page 478
CodeName Name Definition
SEMA SettlementRiskMargin Margin required to cover the risk of non
settlement of the underlying. Also used
to cover the risk linked to the non
settlement on payment platforms (for
example TARGET2 vs CLS).
ADFM AdditionalDefaultFundMargin Additional margin required to cover the
daily risk encountered by the central
counterparty before the clearing member
is actually called to cover the default
fund. Indeed, central counterparty
calculates the margin on the default fund
on a daily basis but only calls the
clearing member at the end of the
month.
SCMA ShortChargeMargin Margin required to cover the
concentration risk linked to the default of
the seller of the "protection" (for example
CDS seller).
COMA CouponMargin Margin required to cover the non
payment of the monthly premium (for
credit derivatives).
UFMA UpfrontMargin Margin required to cover the non
payment of the upfront premium (for
credit derivatives).
CEMA CreditEventMargin Margin required to cover the risk of any
event linked to the underlying (for
example the payment default by the
issuer of a debt).
INDE InitialDeposit Margin required to enable a member to
start trading on a specific market where
high risks and amounts are involved.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 428
```

