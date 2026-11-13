---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.3 Debt <Debt>", "28.4.2.2.1.3.77 PriceRange <PricRg>"]
file_pages: [1626, 1627, 1628, 1629]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.3.77 PriceRange <PricRg>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1626 to 1629.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1626

```text
28.4.2.2.1.3.77  PriceRange <PricRg>
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
28.4.2.2.1.4  Derivative <Deriv>
Presence: [0..1]
Definition: Choice between type of derivatives.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1626 August 2026
```

## File page 1627

```text
Derivative <Deriv> contains the following Derivative4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Future <Futr> [0..1]  1630
     ContractSize <CtrctSz> [0..1] Rate 1632
     ExercisePrice <ExrcPric> [0..1]  1632
       ValueType <ValTp> [0..1] CodeSet 1632
       Value <Val> [1..1] ± 1633
       PriceType <PricTp> [0..1] CodeSet 1633
     FutureDate <FutrDt> [0..1] DateTime 1634
     MinimumSize <MinSz> [0..1] Amount C1, C5 1634
     UnitOfMeasure <UnitOfMeasr> [0..1]  1635
{Or       Code <Cd> [1..1] CodeSet 1635
Or}       Proprietary <Prtry> [1..1] ± 1637
     TimeUnit <TmUnit> [0..1]  1637
{Or       Code <Cd> [1..1] CodeSet 1638
Or}       Proprietary <Prtry> [1..1] ± 1638
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1638
       AllocationPercentage <AllcnPctg> [0..1] Rate 1640
       Quantity <Qty> [0..1]  1640
{Or         Unit <Unit> [1..1] Quantity 1640
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1640
       SettlementType <SttlmTp> [0..1]  1640
{Or         Code <Cd> [1..1] CodeSet 1641
Or}         Proprietary <Prtry> [1..1] ± 1641
       CashAmount <CshAmt> [0..1] Amount C1, C5 1641
       CashType <CshTp> [0..1] Text 1642
       Price <Pric> [0..1]  1642
         ValueType <ValTp> [0..1] CodeSet 1642
         Value <Val> [1..1] ± 1643
         PriceType <PricTp> [0..1] CodeSet 1643
       DirtyPrice <DrtyPric> [0..1]  1644
         ValueType <ValTp> [0..1] CodeSet 1644
         Value <Val> [1..1] ± 1645
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1627 August 2026
```

## File page 1628

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1645
       EndPrice <EndPric> [0..1]  1646
         ValueType <ValTp> [0..1] CodeSet 1646
         Value <Val> [1..1] ± 1647
         PriceType <PricTp> [0..1] CodeSet 1647
       StartValue <StartVal> [0..1] Amount C1, C5 1648
       CurrentValue <CurVal> [0..1] Amount C1, C5 1648
       EndValue <EndVal> [0..1] Amount C1, C5 1649
       AdjustedQuantity <AdjstdQty> [0..1]  1649
{Or         Unit <Unit> [1..1] Quantity 1649
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1650
       ExchangeRate <XchgRate> [0..1] Rate 1650
       CapValue <CapVal> [0..1] Amount C1, C5 1650
   Option <Optn> [0..1]  1650
     OptionSettlementStyle <OptnSttlmStyle> [0..1]  1654
{Or       Code <Cd> [0..*] CodeSet 1654
Or}       Proprietary <Prtry> [1..1] ± 1654
     ConversionDate <ConvsDt> [0..1] DateTime 1654
     StrikePrice <StrkPric> [0..1]  1654
       ValueType <ValTp> [0..1] CodeSet 1655
       Value <Val> [1..1] ± 1655
       PriceType <PricTp> [0..1] CodeSet 1656
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1656
     ConversionPeriod <ConvsPrd> [0..1]  1657
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1657
Or       ToDateTime <ToDtTm> [1..1] DateTime 1657
Or}       DateTimeRange <DtTmRg> [1..1] ± 1657
     OptionStyle <OptnStyle> [0..1]  1658
{Or       Code <Cd> [1..1] CodeSet 1658
Or}       Proprietary <Prtry> [1..1] ± 1658
     OptionType <OptnTp> [0..1] ± 1658
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1628 August 2026
```

## File page 1629

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StrikeValue <StrkVal> [0..1] Quantity 1659
     StrikeMultiplier <StrkMltplr> [0..1] Quantity 1659
     InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1659
{Or       Code <Cd> [1..1] CodeSet 1659
Or}       Proprietary <Prtry> [1..1] ± 1659
     VersionNumber <VrsnNb> [0..1] Quantity 1660
     ExpiryLocation <XpryLctn> [0..1] Text 1660
     Standardisation <Stdstn> [0..1]  1660
{Or       Code <Cd> [1..*] CodeSet 1660
Or}       Proprietary <Prtry> [1..1] ± 1661
     TradingPartyRole <TradgPtyRole> [0..1]  1661
{Or       Code <Cd> [1..*] CodeSet 1661
Or}       Proprietary <Prtry> [1..1] ± 1661
     ContractSize <CtrctSz> [0..1] Rate 1662
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1662
       AllocationPercentage <AllcnPctg> [0..1] Rate 1664
       Quantity <Qty> [0..1]  1664
{Or         Unit <Unit> [1..1] Quantity 1664
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1664
       SettlementType <SttlmTp> [0..1]  1664
{Or         Code <Cd> [1..1] CodeSet 1665
Or}         Proprietary <Prtry> [1..1] ± 1665
       CashAmount <CshAmt> [0..1] Amount C1, C5 1665
       CashType <CshTp> [0..1] Text 1666
       Price <Pric> [0..1]  1666
         ValueType <ValTp> [0..1] CodeSet 1666
         Value <Val> [1..1] ± 1667
         PriceType <PricTp> [0..1] CodeSet 1667
       DirtyPrice <DrtyPric> [0..1]  1668
         ValueType <ValTp> [0..1] CodeSet 1668
         Value <Val> [1..1] ± 1669
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1629 August 2026
```

