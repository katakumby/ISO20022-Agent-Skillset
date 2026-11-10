---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>", "3.4.6.50 FaceAmount <FaceAmt>"]
file_pages: [77, 78]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.6.50 FaceAmount <FaceAmt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 77 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
MinimumExercisableMultipleQuantity <MinExrcblMltplQty> contains one of the following elements
(see "FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
3.4.6.50  FaceAmount <FaceAmt>
Presence: [0..1]
Definition: Signed face amount and amortised value of security.
Datatype: "ImpliedCurrencyAndAmount" on page 613
3.4.6.51  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
ContractSize <CtrctSz> contains one of the following elements (see
"FinancialInstrumentQuantity18Choice" on page 518 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 518
Or}   FaceAmount <FaceAmt> [1..1] Amount 518
3.4.6.52  FinancialInstrumentAttributeAdditionalDetails <FinInstrmAttrAddtlDtls>
Presence: [0..1]
Definition: Provides additional information about the financial instrument in narrative form.
Datatype: "Max350Text" on page 669
3.4.7 UnderlyingFinancialInstrument <UndrlygFinInstrm>
Presence: [0..*]
Definition: Underlying financial instrument to which an trade confirmation is related.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 77 February 2025
```

## File page 78

```text
UnderlyingFinancialInstrument <UndrlygFinInstrm> contains the following
UnderlyingFinancialInstrument7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± C19,
C20,
C27,
C28,
C34
79
   Attributes <Attrbts> [0..1]  C3, C40 80
     PlaceOfListing <PlcOfListg> [0..1] ± 83
     Rating <Ratg> [0..1] ± 84
     CertificateNumber <CertNb> [0..1] Text 84
     DayCountBasis <DayCntBsis> [0..1] ± 84
     RegistrationForm <RegnForm> [0..1] ± 84
     PaymentFrequency <PmtFrqcy> [0..1] ± 85
     VariableRateChangeFrequency
<VarblRateChngFrqcy>
[0..1] ± 85
     ClassificationType <ClssfctnTp> [0..1] ± 85
     OptionStyle <OptnStyle> [0..1] ± 85
     OptionType <OptnTp> [0..1] ± 86
     DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 86
     CouponDate <CpnDt> [0..1] Date 86
     ExpiryDate <XpryDt> [0..1] Date 86
     FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 87
     MaturityDate <MtrtyDt> [0..1] Date 87
     IssueDate <IsseDt> [0..1] Date 87
     NextCallableDate <NxtCllblDt> [0..1] Date 87
     ConversionDate <ConvsDt> [0..1] Date 87
     PutableDate <PutblDt> [0..1] Date 87
     DatedDate <DtdDt> [0..1] Date 87
     FirstPaymentDate <FrstPmtDt> [0..1] Date 87
     NextFactorDate <NxtFctrDt> [0..1] Date 88
     PreviousFactor <PrvsFctr> [0..1] Rate 88
     CurrentFactor <CurFctr> [0..1] Rate 88
     NextFactor <NxtFctr> [0..1] Rate 88
     EndFactor <EndFctr> [0..1] Rate 88
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 78 February 2025
```

