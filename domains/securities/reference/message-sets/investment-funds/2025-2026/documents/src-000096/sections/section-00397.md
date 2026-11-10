---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.6.16 UnitsDetails <UnitsDtls>", "26.4.6.16.8 TransactionOverhead <TxOvrhd>", "26.4.6.16.8.1 TotalOverheadApplied <TtlOvrhdApld>"]
file_pages: [552]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.6.16.8.1 TotalOverheadApplied <TtlOvrhdApld>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 552 to 552.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 552

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 564
         Suffix <Sfx> [0..1] Text 564
         Type <Tp> [1..1]  564
{Or           Code <Cd> [1..1] CodeSet 565
Or}           Proprietary <Prtry> [1..1] Text 566
       Description <Desc> [0..1] Text 566
     Quantity <Qty> [1..1]  567
{Or       Quantity <Qty> [1..1] ± C14 567
Or}       ProprietaryQuantity <PrtryQty> [1..1]  567
         Quantity <Qty> [1..1] Quantity 568
         QuantityType <QtyTp> [1..1] Text 568
         Issuer <Issr> [1..1] Text 568
         SchemeName <SchmeNm> [0..1] Text 568
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 568
Constraints
• NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
• TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
26.4.6.16.8.1  TotalOverheadApplied <TtlOvrhdApld>
Presence: [0..1]
Definition: Total amount of overhead applied to the transaction that impacts the settlement amount.
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 552 May 2026
```

