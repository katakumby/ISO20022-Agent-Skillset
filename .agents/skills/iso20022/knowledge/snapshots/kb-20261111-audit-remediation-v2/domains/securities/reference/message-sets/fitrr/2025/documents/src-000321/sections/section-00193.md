---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.4 Message Building Blocks", "15.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "15.4.2.2 Identification <Id>", "15.4.2.2.1 ISINAndSubClass <ISINAndSubClss>", "15.4.2.2.1.2 DerivativeSubClass <DerivSubClss>", "15.4.2.2.1.2.2 SegmentationCriteria <SgmttnCrit>", "15.4.2.2.1.2.2.2 CriteriaValue <CritVal>"]
file_pages: [236]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.4.2.2.1.2.2.2 CriteriaValue <CritVal>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 236 to 236.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 236

```text
CodeName Name Definition
ISPT SovereignAndPublicTypeIssuer Issuer of sovereign and public type.
SRTC SpecificRouteTimeCharterAverage Specific route time charter average.
SACL SubAssetClass Sub-asset class.
SBPD SubProduct Sub product.
TTMS SwapTimeToMaturityBucket Time to maturity bucket of the swap.
NCSW SwaptionNotionalCurrency Notional currency of the swaption.
TTMB TimeToMaturityBucket Time to maturity bucket.
IOUB UnderlyingBondIssuer Issuer of the underlying bond.
TOUB UnderlyingBondTerm Term of the underlying bond.
UISC UnderlyingIndexCDSSubClassIdentification Sub class of the underlying index credit
default swap (CDS).
UIDX UnderlyingIndexIdentification Underlying index identification such as
an ISIN or an index name.
UINS UnderlyingInstrumentIdentification Underlying instrument identification,
such as an ISIN code.
UIRT UnderlyingInterestRate Underlying interest rate.
REOU UnderlyingReferenceEntity Underlying reference entity.
UTYP UnderlyingType Underlying type.
15.4.2.2.1.2.2.2  CriteriaValue <CritVal>
Presence: [1..1]
Definition: Value identifying the sub class with respect to a segmentation criteria as per local regulation.
Datatype: "Max1000Text" on page 454
15.4.2.2.1.3  FinancialInstrumentClassification <FinInstrmClssfctn>
Presence: [0..1]
Definition: Identification of non-equity financial instruments.
Datatype: "NonEquityInstrumentReportingClassification1Code" on page 440
CodeName Name Definition
SFPS StructuredFinanceProduct Contract is of type structured finance
products (SFPs).
SDRV SecuritisedDerivative Contract is of type securitised
derivatives.
DERV Derivative Contract is of type derivative.
EMAL EmissionAllowance Contract is of type emission allowances.
BOND Bond Contract is of type bonds.
ETCS ExchangeTradedCommodities Contract is of type exchange traded
commodities.
ETNS ExchangeTradedNote Contract is of type exchange traded
note.
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
236 July 2025
```

