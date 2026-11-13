---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.4 Message Building Blocks", "15.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "15.4.2.2 Identification <Id>", "15.4.2.2.2 AssetClassAndSubClass <AsstClssAndSubClss>", "15.4.2.2.2.2 DerivativeSubClass <DerivSubClss>", "15.4.2.2.2.2.1 Description <Desc>"]
file_pages: [238, 239]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.4.2.2.2.2.1 Description <Desc>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 238 to 239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 238

```text
Definition: Sub class of non-equity instruments to which the result relates, as defined in the local
regulation.
DerivativeSubClass <DerivSubClss> contains the following NonEquitySubClass1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Description <Desc> [0..1] Text 238
   SegmentationCriteria <SgmttnCrit> [1..*]  238
     CriteriaName <CritNm> [1..1] CodeSet 238
     CriteriaValue <CritVal> [1..1] Text 240
15.4.2.2.2.2.1  Description <Desc>
Presence: [0..1]
Definition: Description of the derivative sub-class.
Datatype: "Max1000Text" on page 454
15.4.2.2.2.2.2  SegmentationCriteria <SgmttnCrit>
Presence: [1..*]
Definition: Criteria used to segment classes of derivative instruments into sub classes as per local
regulation.
SegmentationCriteria <SgmttnCrit> contains the following
NonEquitySubClassSegmentationCriterion1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CriteriaName <CritNm> [1..1] CodeSet 238
   CriteriaValue <CritVal> [1..1] Text 240
15.4.2.2.2.2.2.1  CriteriaName <CritNm>
Presence: [1..1]
Definition: Criteria used to segment classes of derivative instruments into sub classes as per local
regulation.
Datatype: "NonEquitySubClassSegmentationCriteria1Code" on page 440
CodeName Name Definition
ASCL AssetClass Asset class.
BSPD BaseProduct Base product.
CNC1 CFDNotionalCurrency1 Contract for difference notional currency
1.
CNC2 CFDNotionalCurrency2 Contract for difference notional currency
2.
NCCO CommodityNotionalCurrency Commodity derivative notional currency.
CTYP ContractType Contract type.
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
238 July 2025
```

## File page 239

```text
CodeName Name Definition
NCCR CreditNotionalCurrency Credit derivative notional currency.
DCSL DeliveryCashLocation Delivery cash settlement location.
DTYP DeliverySettlementType Delivery settlement type.
EQUT EquityUnderlyingType Equity derivative underlying type.
FNC1 FEXNotionalCurrency1 Foreign exchange derivative notional
currency 1.
FNC2 FEXNotionalCurrency2 Foreign exchange derivative notional
currency 2.
FSPD FurtherSubProduct Further sub product.
IIND InflationIndexCodeName Inflation index code or name.
IRTC InterestRateTermOfContract Interest rate term of contract.
INC1 IRDNotionalCurrency1 Interest rate derivative notional currency
1.
INC2 IRDNotionalCurrency2 Interest rate derivative notional currency
2.
ISIN ISIN Instrument identification.
TTMO OptionTimeToMaturityBucket Time to maturity bucket of the option.
PRMT Parameter Parameter.
SSRF SizeSpecificationRelatedToFreightSubtype Size specification related to freight
subtype.
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
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
239 July 2025
```

