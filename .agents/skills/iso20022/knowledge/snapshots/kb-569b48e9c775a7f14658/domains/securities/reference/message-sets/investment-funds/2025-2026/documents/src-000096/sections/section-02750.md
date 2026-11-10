---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.18 TransactionOverhead <TxOvrhd>", "55.4.5.19.18.1 TotalOverheadApplied <TtlOvrhdApld>"]
file_pages: [3880]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.18.1 TotalOverheadApplied <TtlOvrhdApld>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3880 to 3880.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3880

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 3892
         Suffix <Sfx> [0..1] Text 3892
         Type <Tp> [1..1]  3892
{Or           Code <Cd> [1..1] CodeSet 3893
Or}           Proprietary <Prtry> [1..1] Text 3894
       Description <Desc> [0..1] Text 3894
     Quantity <Qty> [1..1]  3895
{Or       Quantity <Qty> [1..1] ± C14 3895
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3895
         Quantity <Qty> [1..1] Quantity 3896
         QuantityType <QtyTp> [1..1] Text 3896
         Issuer <Issr> [1..1] Text 3896
         SchemeName <SchmeNm> [0..1] Text 3896
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3896
Constraints
• NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
• TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
55.4.5.19.18.1  TotalOverheadApplied <TtlOvrhdApld>
Presence: [0..1]
Definition: Total amount of overhead applied to the transaction that impacts the settlement amount.
Impacted by: C2 "ActiveCurrency", C8 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3880 May 2026
```

