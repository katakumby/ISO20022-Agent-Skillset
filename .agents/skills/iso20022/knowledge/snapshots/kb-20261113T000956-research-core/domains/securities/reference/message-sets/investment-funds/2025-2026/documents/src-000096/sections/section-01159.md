---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.10 UnitsDetails <UnitsDtls>", "40.4.15.11.10.8 TransactionOverhead <TxOvrhd>", "40.4.15.11.10.8.1 TotalOverheadApplied <TtlOvrhdApld>"]
file_pages: [1619]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.10.8.1 TotalOverheadApplied <TtlOvrhdApld>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1619 to 1619.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1619

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 1631
         Suffix <Sfx> [0..1] Text 1631
         Type <Tp> [1..1]  1631
{Or           Code <Cd> [1..1] CodeSet 1632
Or}           Proprietary <Prtry> [1..1] Text 1633
       Description <Desc> [0..1] Text 1633
     Quantity <Qty> [1..1]  1634
{Or       Quantity <Qty> [1..1] ± C23 1634
Or}       ProprietaryQuantity <PrtryQty> [1..1]  1634
         Quantity <Qty> [1..1] Quantity 1635
         QuantityType <QtyTp> [1..1] Text 1635
         Issuer <Issr> [1..1] Text 1635
         SchemeName <SchmeNm> [0..1] Text 1635
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1635
Constraints
• NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
• TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
40.4.15.11.10.8.1  TotalOverheadApplied <TtlOvrhdApld>
Presence: [0..1]
Definition: Total amount of overhead applied to the transaction that impacts the settlement amount.
Impacted by: C1 "ActiveCurrency", C18 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1619 May 2026
```

