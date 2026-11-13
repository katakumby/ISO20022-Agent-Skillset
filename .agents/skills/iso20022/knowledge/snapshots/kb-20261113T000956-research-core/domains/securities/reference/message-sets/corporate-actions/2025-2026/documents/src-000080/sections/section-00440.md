---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.8 PriceDetails <PricDtls>", "8.4.12.8.2 OverSubscriptionDepositPrice <OverSbcptDpstPric>"]
file_pages: [592]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.8.2 OverSubscriptionDepositPrice <OverSbcptDpstPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 592 to 592.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 592

```text
CashInLieuOfSharePrice <CshInLieuOfShrPric> contains one of the following elements (see
"PriceFormat77Choice" on page 1064 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1064
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1065
     PriceValue <PricVal> [1..1] Rate 1065
Or}   AmountPrice <AmtPric> [1..1] ± 1065
8.4.12.8.2  OverSubscriptionDepositPrice <OverSbcptDpstPric>
Presence: [0..1]
Definition: Amount of money required per over-subscribed equity as defined by the issuer.
OverSubscriptionDepositPrice <OverSbcptDpstPric> contains one of the following elements (see
"PriceFormat77Choice" on page 1064 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1064
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1065
     PriceValue <PricVal> [1..1] Rate 1065
Or}   AmountPrice <AmtPric> [1..1] ± 1065
8.4.12.9  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Place where the trade was executed.
Impacted by: C41 "MarketTypeAndIdentificationRule"
PlaceOfTrade <PlcOfTrad> contains the following elements (see "MarketIdentification84" on
page 884 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 884
   Type <Tp> [1..1] ± 885
Constraints
• MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 592 February 2026
```

