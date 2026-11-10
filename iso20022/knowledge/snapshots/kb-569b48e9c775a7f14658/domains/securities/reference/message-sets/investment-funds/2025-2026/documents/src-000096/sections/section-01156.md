---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.9 Conversion <Convs>", "40.4.15.11.9.1 OriginalSecurity <OrgnlScty>", "40.4.15.11.9.1.1 Identification <Id>", "40.4.15.11.9.1.1.16 OtherProprietaryIdentification <OthrPrtryId>", "40.4.15.11.9.1.1.16.1 Identification <Id>"]
file_pages: [1613, 1614, 1615]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.9.1.1.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1613 to 1615.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1613

```text
40.4.15.11.9.1.1.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
40.4.15.11.9.1.1.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
40.4.15.11.9.1.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
40.4.15.11.9.1.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Financial Instrument Short Name (FISN) expressed in conformance with the ISO 18774
standard.
Datatype: "Max35Text" on page 5403
40.4.15.11.9.2  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the conversion.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
40.4.15.11.10  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1613 May 2026
```

## File page 1614

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  1616
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 1616
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1616
   OrderDate <OrdrDt> [0..1] Date 1616
   AcquisitionDate <AcqstnDt> [0..1] Date 1616
   CertificateNumber <CertNb> [0..*] Text 1616
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1616
   Reference <Ref> [0..1] Text 1617
   PriceDetails <PricDtls> [0..1] ± 1617
   TransactionOverhead <TxOvrhd> [0..1]  C36,
C53
1617
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C18 1619
     TotalFees <TtlFees> [0..1] Amount C1, C18 1620
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C18 1620
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1620
     IndividualFee <IndvFee> [0..*]  C6 1621
       Type <Tp> [1..1]  1621
{Or         Code <Cd> [1..1] CodeSet 1622
Or}         Proprietary <Prtry> [1..1] ± 1623
       Basis <Bsis> [0..1]  1623
{Or         Code <Cd> [1..1] CodeSet 1623
Or}         Proprietary <Prtry> [1..1] ± 1624
       StandardAmount <StdAmt> [0..1] Amount C1, C18 1624
       StandardRate <StdRate> [0..1] Rate 1624
       DiscountDetails <DscntDtls> [0..1]  C24 1625
         Amount <Amt> [0..1] Amount C1, C18 1625
         Rate <Rate> [0..1] Rate 1626
         Basis <Bsis> [0..1]  1626
{Or           Code <Cd> [1..1] CodeSet 1626
Or}           Proprietary <Prtry> [1..1] ± 1626
       AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1627
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1614 May 2026
```

## File page 1615

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 1627
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 1627
       RecipientIdentification <RcptId> [0..1] ± 1627
       InformativeIndicator <InftvInd> [1..1] Indicator 1628
     IndividualTax <IndvTax> [0..*] ± 1628
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  1628
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C21,
C22,
C33,
C34,
C37
1629
         ISIN <ISIN> [0..1] IdentifierSet 1631
         OtherIdentification <OthrId> [0..*]  1631
           Identification <Id> [1..1] Text 1631
           Suffix <Sfx> [0..1] Text 1631
           Type <Tp> [1..1]  1631
{Or             Code <Cd> [1..1] CodeSet 1632
Or}             Proprietary <Prtry> [1..1] Text 1633
         Description <Desc> [0..1] Text 1633
       Quantity <Qty> [1..1]  1634
{Or         Quantity <Qty> [1..1] ± C23 1634
Or}         ProprietaryQuantity <PrtryQty> [1..1]  1634
           Quantity <Qty> [1..1] Quantity 1635
           QuantityType <QtyTp> [1..1] Text 1635
           Issuer <Issr> [1..1] Text 1635
           SchemeName <SchmeNm> [0..1] Text 1635
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1635
   OtherAmount <OthrAmt> [0..*]  1635
     Type <Tp> [1..1]  1636
{Or       Code <Cd> [1..1] CodeSet 1636
Or}       ProprietaryCode <PrtryCd> [1..1] ± 1636
     Amount <Amt> [1..1] Amount C1, C18 1636
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1615 May 2026
```

