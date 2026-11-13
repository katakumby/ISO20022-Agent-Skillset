---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.4 Message Building Blocks", "15.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "15.4.2.2 Identification <Id>", "15.4.2.2.2 AssetClassAndSubClass <AsstClssAndSubClss>"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.4.2.2.2 AssetClassAndSubClass <AsstClssAndSubClss>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
15.4.2.2.2  AssetClassAndSubClass <AsstClssAndSubClss>
Presence: [1..1]
Definition: Identifies the asset class and sub-class of non-equity instruments to which the result relates
AssetClassAndSubClass <AsstClssAndSubClss> contains the following
AssetClassAndSubClassIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AssetClass <AsstClss> [1..1] CodeSet 237
   DerivativeSubClass <DerivSubClss> [0..1]  237
     Description <Desc> [0..1] Text 238
     SegmentationCriteria <SgmttnCrit> [1..*]  238
       CriteriaName <CritNm> [1..1] CodeSet 238
       CriteriaValue <CritVal> [1..1] Text 240
   FinancialInstrumentClassification <FinInstrmClssfctn> [0..1] CodeSet 240
15.4.2.2.2.1  AssetClass <AsstClss>
Presence: [1..1]
Definition: Asset class of non-equity instruments to which the result relates
Datatype: "NonEquityAssetClass1Code" on page 439
CodeName Name Definition
SDRV SecuritisedDerivative Securitised derivative.
IRDV InterestRateDerivative Interest rate derivative.
FEXD ForeignExchangeDerivative Foreign exchange derivative.
EQDV EquityDerivative Equity derivative.
EADV EmissionAllowanceDerivative Emission allowance derivative.
EMAL EmissionAllowance Emission allowance.
CRDV CreditDerivative Credit derivative.
CFDS ContractForDifference Contract for difference.
COMD CommodityDerivative Commodity derivative.
C10D C10Derivative C10 derivative.
BOND Bond Bond.
ETCS ExchangeTradedCommodities Exchange traded commodities.
ETNS ExchangeTradedNote Exchange traded note.
SFPS StructuredFinanceProduct Structured finance product.
15.4.2.2.2.2  DerivativeSubClass <DerivSubClss>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
237 July 2025
```

