---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.6.14 TotalUnitsNumber <TtlUnitsNb>", "26.4.6.14.1 UnitsNumber <UnitsNb>"]
file_pages: [546, 547, 548]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.6.14.1 UnitsNumber <UnitsNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 546 to 548.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 546

```text
TotalUnitsNumber <TtlUnitsNb> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 546
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 546
26.4.6.14.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
26.4.6.14.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
26.4.6.15  TransferRate <TrfRate>
Presence: [0..1]
Definition: Quantity of securities transferred as a percentage of the holding.
Datatype: "PercentageRate" on page 5401
26.4.6.16  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units transferred.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 546 May 2026
```

## File page 547

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  549
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 549
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 549
   OrderDate <OrdrDt> [0..1] Date 549
   AcquisitionDate <AcqstnDt> [0..1] Date 549
   CertificateNumber <CertNb> [0..*] Text 549
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 549
   Reference <Ref> [0..1] Text 550
   PriceDetails <PricDtls> [0..1] ± 550
   TransactionOverhead <TxOvrhd> [0..1]  C24,
C35
550
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 552
     TotalFees <TtlFees> [0..1] Amount C1, C10 553
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 553
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 553
     IndividualFee <IndvFee> [0..*]  C6 554
       Type <Tp> [1..1]  554
{Or         Code <Cd> [1..1] CodeSet 555
Or}         Proprietary <Prtry> [1..1] ± 556
       Basis <Bsis> [0..1]  556
{Or         Code <Cd> [1..1] CodeSet 556
Or}         Proprietary <Prtry> [1..1] ± 557
       StandardAmount <StdAmt> [0..1] Amount C1, C10 557
       StandardRate <StdRate> [0..1] Rate 557
       DiscountDetails <DscntDtls> [0..1]  C15 558
         Amount <Amt> [0..1] Amount C1, C10 558
         Rate <Rate> [0..1] Rate 559
         Basis <Bsis> [0..1]  559
{Or           Code <Cd> [1..1] CodeSet 559
Or}           Proprietary <Prtry> [1..1] ± 559
       AppliedAmount <ApldAmt> [0..1] Amount C1, C10 560
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 547 May 2026
```

## File page 548

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 560
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 560
       RecipientIdentification <RcptId> [0..1] ± 560
       InformativeIndicator <InftvInd> [1..1] Indicator 561
     IndividualTax <IndvTax> [0..*] ± 561
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  561
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C21,
C22,
C25
562
         ISIN <ISIN> [0..1] IdentifierSet 564
         OtherIdentification <OthrId> [0..*]  564
           Identification <Id> [1..1] Text 564
           Suffix <Sfx> [0..1] Text 564
           Type <Tp> [1..1]  564
{Or             Code <Cd> [1..1] CodeSet 565
Or}             Proprietary <Prtry> [1..1] Text 566
         Description <Desc> [0..1] Text 566
       Quantity <Qty> [1..1]  567
{Or         Quantity <Qty> [1..1] ± C14 567
Or}         ProprietaryQuantity <PrtryQty> [1..1]  567
           Quantity <Qty> [1..1] Quantity 568
           QuantityType <QtyTp> [1..1] Text 568
           Issuer <Issr> [1..1] Text 568
           SchemeName <SchmeNm> [0..1] Text 568
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 568
   OtherAmount <OthrAmt> [0..*]  568
     Type <Tp> [1..1]  569
{Or       Code <Cd> [1..1] CodeSet 569
Or}       ProprietaryCode <PrtryCd> [1..1] ± 569
     Amount <Amt> [1..1] Amount C1, C10 569
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 548 May 2026
```

