---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.5 MasterReference <MstrRef>", "24.4.6.11 Quantity <Qty>", "24.4.6.11.1 TotalUnitsNumber <TtlUnitsNb>"]
file_pages: [458, 459, 460]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.6.11.1 TotalUnitsNumber <TtlUnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 458 to 460.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 458

```text
Quantity <Qty> contains one of the following Quantity82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TotalUnitsNumber <TtlUnitsNb> [1..1]  458
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 458
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 458
Or}   TransferRate <TrfRate> [1..1] Rate 458
24.4.6.11.1  TotalUnitsNumber <TtlUnitsNb>
Presence: [1..1]
Definition: Total quantity of securities to be transferred.
TotalUnitsNumber <TtlUnitsNb> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 458
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 458
24.4.6.11.1.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
24.4.6.11.1.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
24.4.6.11.2  TransferRate <TrfRate>
Presence: [1..1]
Definition: Quantity of securities to be transferred as a percentage of the holding.
Datatype: "PercentageRate" on page 5401
24.4.6.12  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units to be transferred.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 458 May 2026
```

## File page 459

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  461
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 461
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 461
   OrderDate <OrdrDt> [0..1] Date 461
   AcquisitionDate <AcqstnDt> [0..1] Date 461
   CertificateNumber <CertNb> [0..*] Text 461
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 461
   Reference <Ref> [0..1] Text 462
   PriceDetails <PricDtls> [0..1] ± 462
   TransactionOverhead <TxOvrhd> [0..1]  C23,
C34
462
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 464
     TotalFees <TtlFees> [0..1] Amount C1, C10 465
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 465
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 465
     IndividualFee <IndvFee> [0..*]  C6 466
       Type <Tp> [1..1]  466
{Or         Code <Cd> [1..1] CodeSet 467
Or}         Proprietary <Prtry> [1..1] ± 468
       Basis <Bsis> [0..1]  468
{Or         Code <Cd> [1..1] CodeSet 468
Or}         Proprietary <Prtry> [1..1] ± 469
       StandardAmount <StdAmt> [0..1] Amount C1, C10 469
       StandardRate <StdRate> [0..1] Rate 469
       DiscountDetails <DscntDtls> [0..1]  C15 470
         Amount <Amt> [0..1] Amount C1, C10 470
         Rate <Rate> [0..1] Rate 471
         Basis <Bsis> [0..1]  471
{Or           Code <Cd> [1..1] CodeSet 471
Or}           Proprietary <Prtry> [1..1] ± 471
       AppliedAmount <ApldAmt> [0..1] Amount C1, C10 472
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 459 May 2026
```

## File page 460

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 472
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 472
       RecipientIdentification <RcptId> [0..1] ± 472
       InformativeIndicator <InftvInd> [1..1] Indicator 473
     IndividualTax <IndvTax> [0..*] ± 473
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  473
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C24
474
         ISIN <ISIN> [0..1] IdentifierSet 476
         OtherIdentification <OthrId> [0..*]  476
           Identification <Id> [1..1] Text 476
           Suffix <Sfx> [0..1] Text 476
           Type <Tp> [1..1]  476
{Or             Code <Cd> [1..1] CodeSet 477
Or}             Proprietary <Prtry> [1..1] Text 478
         Description <Desc> [0..1] Text 478
       Quantity <Qty> [1..1]  479
{Or         Quantity <Qty> [1..1] ± C14 479
Or}         ProprietaryQuantity <PrtryQty> [1..1]  479
           Quantity <Qty> [1..1] Quantity 480
           QuantityType <QtyTp> [1..1] Text 480
           Issuer <Issr> [1..1] Text 480
           SchemeName <SchmeNm> [0..1] Text 480
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 480
   OtherAmount <OthrAmt> [0..*]  480
     Type <Tp> [1..1]  481
{Or       Code <Cd> [1..1] CodeSet 481
Or}       ProprietaryCode <PrtryCd> [1..1] ± 481
     Amount <Amt> [1..1] Amount C1, C10 481
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 460 May 2026
```

