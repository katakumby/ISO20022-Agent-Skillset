---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.3 Debt <Debt>", "27.4.2.2.3.77 PriceRange <PricRg>"]
file_pages: [702, 703, 704, 705]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.3.77 PriceRange <PricRg>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 702 to 705.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 702

```text
27.4.2.2.3.77  PriceRange <PricRg>
Presence: [0..1]
Definition: Indicates a search criterion used when looking to buy a bond within a particular price range.
PriceRange <PricRg> contains the following elements (see "AmountOrPercentageRange1" on
page 3003 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 3003
   Term <Term> [0..10]  3003
     Operator <Oprtr> [1..1] CodeSet 3003
     Value <Val> [1..1]  3004
{Or       RateValue <RateVal> [1..1] Rate 3004
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 3004
27.4.2.2.4  Derivative <Deriv>
Presence: [0..1]
Definition: Choice between type of derivatives.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 702 August 2026
```

## File page 703

```text
Derivative <Deriv> contains the following Derivative4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Future <Futr> [0..1]  706
     ContractSize <CtrctSz> [0..1] Rate 708
     ExercisePrice <ExrcPric> [0..1]  708
       ValueType <ValTp> [0..1] CodeSet 708
       Value <Val> [1..1] ± 709
       PriceType <PricTp> [0..1] CodeSet 709
     FutureDate <FutrDt> [0..1] DateTime 710
     MinimumSize <MinSz> [0..1] Amount C1, C5 710
     UnitOfMeasure <UnitOfMeasr> [0..1]  711
{Or       Code <Cd> [1..1] CodeSet 711
Or}       Proprietary <Prtry> [1..1] ± 713
     TimeUnit <TmUnit> [0..1]  713
{Or       Code <Cd> [1..1] CodeSet 714
Or}       Proprietary <Prtry> [1..1] ± 714
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  714
       AllocationPercentage <AllcnPctg> [0..1] Rate 716
       Quantity <Qty> [0..1]  716
{Or         Unit <Unit> [1..1] Quantity 716
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 716
       SettlementType <SttlmTp> [0..1]  716
{Or         Code <Cd> [1..1] CodeSet 717
Or}         Proprietary <Prtry> [1..1] ± 717
       CashAmount <CshAmt> [0..1] Amount C1, C5 717
       CashType <CshTp> [0..1] Text 718
       Price <Pric> [0..1]  718
         ValueType <ValTp> [0..1] CodeSet 718
         Value <Val> [1..1] ± 719
         PriceType <PricTp> [0..1] CodeSet 719
       DirtyPrice <DrtyPric> [0..1]  720
         ValueType <ValTp> [0..1] CodeSet 720
         Value <Val> [1..1] ± 721
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 703 August 2026
```

## File page 704

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 721
       EndPrice <EndPric> [0..1]  722
         ValueType <ValTp> [0..1] CodeSet 722
         Value <Val> [1..1] ± 723
         PriceType <PricTp> [0..1] CodeSet 723
       StartValue <StartVal> [0..1] Amount C1, C5 724
       CurrentValue <CurVal> [0..1] Amount C1, C5 724
       EndValue <EndVal> [0..1] Amount C1, C5 725
       AdjustedQuantity <AdjstdQty> [0..1]  725
{Or         Unit <Unit> [1..1] Quantity 725
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 726
       ExchangeRate <XchgRate> [0..1] Rate 726
       CapValue <CapVal> [0..1] Amount C1, C5 726
   Option <Optn> [0..1]  726
     OptionSettlementStyle <OptnSttlmStyle> [0..1]  730
{Or       Code <Cd> [0..*] CodeSet 730
Or}       Proprietary <Prtry> [1..1] ± 730
     ConversionDate <ConvsDt> [0..1] DateTime 730
     StrikePrice <StrkPric> [0..1]  730
       ValueType <ValTp> [0..1] CodeSet 731
       Value <Val> [1..1] ± 731
       PriceType <PricTp> [0..1] CodeSet 732
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 732
     ConversionPeriod <ConvsPrd> [0..1]  733
{Or       FromDateTime <FrDtTm> [1..1] DateTime 733
Or       ToDateTime <ToDtTm> [1..1] DateTime 733
Or}       DateTimeRange <DtTmRg> [1..1] ± 733
     OptionStyle <OptnStyle> [0..1]  734
{Or       Code <Cd> [1..1] CodeSet 734
Or}       Proprietary <Prtry> [1..1] ± 734
     OptionType <OptnTp> [0..1] ± 734
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 704 August 2026
```

## File page 705

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StrikeValue <StrkVal> [0..1] Quantity 735
     StrikeMultiplier <StrkMltplr> [0..1] Quantity 735
     InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  735
{Or       Code <Cd> [1..1] CodeSet 735
Or}       Proprietary <Prtry> [1..1] ± 735
     VersionNumber <VrsnNb> [0..1] Quantity 736
     ExpiryLocation <XpryLctn> [0..1] Text 736
     Standardisation <Stdstn> [0..1]  736
{Or       Code <Cd> [1..*] CodeSet 736
Or}       Proprietary <Prtry> [1..1] ± 737
     TradingPartyRole <TradgPtyRole> [0..1]  737
{Or       Code <Cd> [1..*] CodeSet 737
Or}       Proprietary <Prtry> [1..1] ± 737
     ContractSize <CtrctSz> [0..1] Rate 738
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  738
       AllocationPercentage <AllcnPctg> [0..1] Rate 740
       Quantity <Qty> [0..1]  740
{Or         Unit <Unit> [1..1] Quantity 740
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 740
       SettlementType <SttlmTp> [0..1]  740
{Or         Code <Cd> [1..1] CodeSet 741
Or}         Proprietary <Prtry> [1..1] ± 741
       CashAmount <CshAmt> [0..1] Amount C1, C5 741
       CashType <CshTp> [0..1] Text 742
       Price <Pric> [0..1]  742
         ValueType <ValTp> [0..1] CodeSet 742
         Value <Val> [1..1] ± 743
         PriceType <PricTp> [0..1] CodeSet 743
       DirtyPrice <DrtyPric> [0..1]  744
         ValueType <ValTp> [0..1] CodeSet 744
         Value <Val> [1..1] ± 745
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 705 August 2026
```

