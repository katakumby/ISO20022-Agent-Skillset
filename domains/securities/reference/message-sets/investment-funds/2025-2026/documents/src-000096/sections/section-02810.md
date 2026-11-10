---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>", "55.4.5.20.16 TransactionOverhead <TxOvrhd>", "55.4.5.20.16.1 TotalOverheadApplied <TtlOvrhdApld>"]
file_pages: [3952]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20.16.1 TotalOverheadApplied <TtlOvrhdApld>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3952 to 3952.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3952

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 3964
         Suffix <Sfx> [0..1] Text 3964
         Type <Tp> [1..1]  3964
{Or           Code <Cd> [1..1] CodeSet 3965
Or}           Proprietary <Prtry> [1..1] Text 3966
       Description <Desc> [0..1] Text 3966
     Quantity <Qty> [1..1]  3967
{Or       Quantity <Qty> [1..1] ± C14 3967
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3967
         Quantity <Qty> [1..1] Quantity 3968
         QuantityType <QtyTp> [1..1] Text 3968
         Issuer <Issr> [1..1] Text 3968
         SchemeName <SchmeNm> [0..1] Text 3968
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3968
Constraints
• NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
• TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
55.4.5.20.16.1  TotalOverheadApplied <TtlOvrhdApld>
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
Investment Funds - Maintenance 2025 - 2026 3952 May 2026
```

