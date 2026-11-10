---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.14 TotalUnitsNumber <TtlUnitsNb>", "30.4.7.14.1 UnitsNumber <UnitsNb>"]
file_pages: [722, 723, 724]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.14.1 UnitsNumber <UnitsNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 722 to 724.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 722

```text
TotalUnitsNumber <TtlUnitsNb> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 722
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 722
30.4.7.14.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
30.4.7.14.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
30.4.7.15  TransferRate <TrfRate>
Presence: [0..1]
Definition: Quantity of securities transferred as a percentage of the holding.
Datatype: "PercentageRate" on page 5401
30.4.7.16  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units transferred.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 722 May 2026
```

## File page 723

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  725
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 725
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 725
   OrderDate <OrdrDt> [0..1] Date 725
   AcquisitionDate <AcqstnDt> [0..1] Date 725
   CertificateNumber <CertNb> [0..*] Text 725
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 725
   Reference <Ref> [0..1] Text 726
   PriceDetails <PricDtls> [0..1] ± 726
   TransactionOverhead <TxOvrhd> [0..1]  C24,
C35
726
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 728
     TotalFees <TtlFees> [0..1] Amount C1, C10 729
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 729
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 729
     IndividualFee <IndvFee> [0..*]  C6 730
       Type <Tp> [1..1]  730
{Or         Code <Cd> [1..1] CodeSet 731
Or}         Proprietary <Prtry> [1..1] ± 732
       Basis <Bsis> [0..1]  732
{Or         Code <Cd> [1..1] CodeSet 732
Or}         Proprietary <Prtry> [1..1] ± 733
       StandardAmount <StdAmt> [0..1] Amount C1, C10 733
       StandardRate <StdRate> [0..1] Rate 733
       DiscountDetails <DscntDtls> [0..1]  C15 734
         Amount <Amt> [0..1] Amount C1, C10 734
         Rate <Rate> [0..1] Rate 735
         Basis <Bsis> [0..1]  735
{Or           Code <Cd> [1..1] CodeSet 735
Or}           Proprietary <Prtry> [1..1] ± 735
       AppliedAmount <ApldAmt> [0..1] Amount C1, C10 736
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 723 May 2026
```

## File page 724

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 736
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 736
       RecipientIdentification <RcptId> [0..1] ± 736
       InformativeIndicator <InftvInd> [1..1] Indicator 737
     IndividualTax <IndvTax> [0..*] ± 737
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  737
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C21,
C22,
C25
738
         ISIN <ISIN> [0..1] IdentifierSet 740
         OtherIdentification <OthrId> [0..*]  740
           Identification <Id> [1..1] Text 740
           Suffix <Sfx> [0..1] Text 740
           Type <Tp> [1..1]  740
{Or             Code <Cd> [1..1] CodeSet 741
Or}             Proprietary <Prtry> [1..1] Text 742
         Description <Desc> [0..1] Text 742
       Quantity <Qty> [1..1]  743
{Or         Quantity <Qty> [1..1] ± C14 743
Or}         ProprietaryQuantity <PrtryQty> [1..1]  743
           Quantity <Qty> [1..1] Quantity 744
           QuantityType <QtyTp> [1..1] Text 744
           Issuer <Issr> [1..1] Text 744
           SchemeName <SchmeNm> [0..1] Text 744
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 744
   OtherAmount <OthrAmt> [0..*]  744
     Type <Tp> [1..1]  745
{Or       Code <Cd> [1..1] CodeSet 745
Or}       ProprietaryCode <PrtryCd> [1..1] ± 745
     Amount <Amt> [1..1] Amount C1, C10 745
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 724 May 2026
```

