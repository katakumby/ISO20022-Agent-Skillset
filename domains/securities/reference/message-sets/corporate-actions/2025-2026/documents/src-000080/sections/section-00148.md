---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.11 AmountDetails <AmtDtls>", "3.4.11.25.11.1 GrossAmount <GrssAmt>"]
file_pages: [211]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.11.1 GrossAmount <GrssAmt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 211 to 211.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 211

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalAmount <OrgnlAmt> [0..1] Amount C2, C18 223
   PrincipalOrCorpus <PrncplOrCrps> [0..1] Amount C2, C18 223
   RedemptionPremiumAmount <RedPrmAmt> [0..1] Amount C2, C18 224
   IncomePortion <IncmPrtn> [0..1] Amount C2, C18 224
   StockExchangeTax <StockXchgTax> [0..1] Amount C2, C18 225
   EUTaxRetentionAmount <EUTaxRtntnAmt> [0..1] Amount C2, C18 225
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C2, C18 225
   EqualisationAmount <EqulstnAmt> [0..1] Amount C2, C18 226
   FATCATaxAmount <FATCATaxAmt> [0..1] Amount C2, C18 226
   NRATaxAmount <NRATaxAmt> [0..1] Amount C2, C18 227
   BackUpWithholdingTaxAmount
<BckUpWhldgTaxAmt>
[0..1] Amount C2, C18 227
   TaxOnIncomeAmount <TaxOnIncmAmt> [0..1] Amount C2, C18 227
   TransactionTax <TxTax> [0..1] Amount C2, C18 228
   DeemedAmount <DmdAmt> [0..1] Amount C2, C18 228
   ForeignIncomeAmount <FrgnIncmAmt> [0..1] Amount C2, C18 229
   DeemedDividendAmount <DmdDvddAmt> [0..1] Amount C2, C18 229
   DeemedFundAmount <DmdFndAmt> [0..1] Amount C2, C18 229
   DeemedInterestAmount <DmdIntrstAmt> [0..1] Amount C2, C18 230
   DeemedRoyaltiesAmount <DmdRyltsAmt> [0..1] Amount C2, C18 230
   BuyUpAmount <BuyUpAmt> [0..1] Amount C2, C18 231
3.4.11.25.11.1  GrossAmount <GrssAmt>
Presence: [0..1]
Definition: Amount of money before any tax deductions have been made.
Impacted by: C2 "ActiveCurrency", C18 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 211 February 2026
```

