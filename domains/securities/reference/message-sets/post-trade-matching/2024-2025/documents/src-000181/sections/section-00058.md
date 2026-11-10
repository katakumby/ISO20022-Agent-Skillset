---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.7 UnderlyingFinancialInstrument <UndrlygFinInstrm>", "3.4.7.2 Attributes <Attrbts>"]
file_pages: [80, 81, 82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.7.2 Attributes <Attrbts>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 80 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
Identification <Id> contains the following elements (see "SecurityIdentification19" on page 270 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 271
   OtherIdentification <OthrId> [0..*]  271
     Identification <Id> [1..1] Text 271
     Suffix <Sfx> [0..1] Text 271
     Type <Tp> [1..1] ± 271
   Description <Desc> [0..1] Text 271
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
3.4.7.2  Attributes <Attrbts>
Presence: [0..1]
Definition: Underlying financial instrument attributes to which an trade confirmation is related.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 80 February 2025
```

## File page 81

```text
Impacted by: C3 "AdditionalDetailsRule", C40 "PlaceOfListingRule"
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 81 February 2025
```

## File page 82

```text
Attributes <Attrbts> contains the following FinancialInstrumentAttributes124 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   InterestRate <IntrstRate> [0..1] Rate 88
   NextInterestRate <NxtIntrstRate> [0..1] Rate 88
   IndexRateBasis <IndxRateBsis> [0..1] Rate 88
   PercentageOfDebtClaims <PctgOfDebtClms> [0..1] Rate 89
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 82 February 2025
```

