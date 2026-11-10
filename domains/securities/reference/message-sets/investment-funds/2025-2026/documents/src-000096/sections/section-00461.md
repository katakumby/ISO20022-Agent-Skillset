---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.11 Quantity <Qty>", "28.4.7.11.1 TotalUnitsNumber <TtlUnitsNb>"]
file_pages: [634, 635, 636]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.11.1 TotalUnitsNumber <TtlUnitsNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 634 to 636.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 634

```text
Quantity <Qty> contains one of the following Quantity82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TotalUnitsNumber <TtlUnitsNb> [1..1]  634
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 634
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 634
Or}   TransferRate <TrfRate> [1..1] Rate 634
28.4.7.11.1  TotalUnitsNumber <TtlUnitsNb>
Presence: [1..1]
Definition: Total quantity of securities to be transferred.
TotalUnitsNumber <TtlUnitsNb> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 634
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 634
28.4.7.11.1.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
28.4.7.11.1.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
28.4.7.11.2  TransferRate <TrfRate>
Presence: [1..1]
Definition: Quantity of securities to be transferred as a percentage of the holding.
Datatype: "PercentageRate" on page 5401
28.4.7.12  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units to be transferred.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 634 May 2026
```

## File page 635

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  637
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 637
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 637
   OrderDate <OrdrDt> [0..1] Date 637
   AcquisitionDate <AcqstnDt> [0..1] Date 637
   CertificateNumber <CertNb> [0..*] Text 637
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 637
   Reference <Ref> [0..1] Text 638
   PriceDetails <PricDtls> [0..1] ± 638
   TransactionOverhead <TxOvrhd> [0..1]  C23,
C34
638
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 640
     TotalFees <TtlFees> [0..1] Amount C1, C10 641
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 641
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 641
     IndividualFee <IndvFee> [0..*]  C6 642
       Type <Tp> [1..1]  642
{Or         Code <Cd> [1..1] CodeSet 643
Or}         Proprietary <Prtry> [1..1] ± 644
       Basis <Bsis> [0..1]  644
{Or         Code <Cd> [1..1] CodeSet 644
Or}         Proprietary <Prtry> [1..1] ± 645
       StandardAmount <StdAmt> [0..1] Amount C1, C10 645
       StandardRate <StdRate> [0..1] Rate 645
       DiscountDetails <DscntDtls> [0..1]  C15 646
         Amount <Amt> [0..1] Amount C1, C10 646
         Rate <Rate> [0..1] Rate 647
         Basis <Bsis> [0..1]  647
{Or           Code <Cd> [1..1] CodeSet 647
Or}           Proprietary <Prtry> [1..1] ± 647
       AppliedAmount <ApldAmt> [0..1] Amount C1, C10 648
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 635 May 2026
```

## File page 636

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 648
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 648
       RecipientIdentification <RcptId> [0..1] ± 648
       InformativeIndicator <InftvInd> [1..1] Indicator 649
     IndividualTax <IndvTax> [0..*] ± 649
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  649
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C24
650
         ISIN <ISIN> [0..1] IdentifierSet 652
         OtherIdentification <OthrId> [0..*]  652
           Identification <Id> [1..1] Text 652
           Suffix <Sfx> [0..1] Text 652
           Type <Tp> [1..1]  652
{Or             Code <Cd> [1..1] CodeSet 653
Or}             Proprietary <Prtry> [1..1] Text 654
         Description <Desc> [0..1] Text 654
       Quantity <Qty> [1..1]  655
{Or         Quantity <Qty> [1..1] ± C14 655
Or}         ProprietaryQuantity <PrtryQty> [1..1]  655
           Quantity <Qty> [1..1] Quantity 656
           QuantityType <QtyTp> [1..1] Text 656
           Issuer <Issr> [1..1] Text 656
           SchemeName <SchmeNm> [0..1] Text 656
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 656
   OtherAmount <OthrAmt> [0..*]  656
     Type <Tp> [1..1]  657
{Or       Code <Cd> [1..1] CodeSet 657
Or}       ProprietaryCode <PrtryCd> [1..1] ± 657
     Amount <Amt> [1..1] Amount C1, C10 657
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 636 May 2026
```

