---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.1 OptionNumber <OptnNb>"]
file_pages: [582]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.1 OptionNumber <OptnNb>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 582 to 582.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 582

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       TaxOnIncome <TaxOnIncm> [0..1] ± 658
       TaxOnProfits <TaxOnPrfts> [0..1] Rate 658
       TaxReclaimRate <TaxRclmRate> [0..1] Rate 658
       EqualisationRate <EqulstnRate> [0..1] Amount C1 658
       DeemedRate <DmdRate> [0..*] ± 659
     PriceDetails <PricDtls> [0..1]  C22 659
       GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 660
       GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 660
       CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 661
8.4.12.1  OptionNumber <OptnNb>
Presence: [1..1]
Definition: Number identifying the available corporate action options.
OptionNumber <OptnNb> contains one of the following elements (see "OptionNumber1Choice" on
page 970 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Text 970
Or}   Code <Cd> [1..1] CodeSet 970
8.4.12.2  OptionType <OptnTp>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
OptionType <OptnTp> contains one of the following elements (see "CorporateActionOption33Choice"
on page 944 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 944
Or}   Proprietary <Prtry> [1..1] ± 945
8.4.12.3  OptionFeatures <OptnFeatrs>
Presence: [0..*]
Definition: Specifies the features that may apply to a corporate action option.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 582 February 2026
```

