---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.4 UnitsDetails <UnitsDtls>"]
file_pages: [1396, 1397, 1398]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.4 UnitsDetails <UnitsDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1396 to 1398.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1396

```text
Datatype: "Max35Text" on page 5403
38.4.15.8.4  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1396 May 2026
```

## File page 1397

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  1399
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 1399
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1399
   OrderDate <OrdrDt> [0..1] Date 1399
   AcquisitionDate <AcqstnDt> [0..1] Date 1399
   CertificateNumber <CertNb> [0..*] Text 1399
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1399
   Reference <Ref> [0..1] Text 1400
   PriceDetails <PricDtls> [0..1] ± 1400
   TransactionOverhead <TxOvrhd> [0..1]  C30,
C46
1400
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C15 1402
     TotalFees <TtlFees> [0..1] Amount C1, C15 1403
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C15 1403
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1403
     IndividualFee <IndvFee> [0..*]  C6 1404
       Type <Tp> [1..1]  1404
{Or         Code <Cd> [1..1] CodeSet 1405
Or}         Proprietary <Prtry> [1..1] ± 1406
       Basis <Bsis> [0..1]  1406
{Or         Code <Cd> [1..1] CodeSet 1406
Or}         Proprietary <Prtry> [1..1] ± 1407
       StandardAmount <StdAmt> [0..1] Amount C1, C15 1407
       StandardRate <StdRate> [0..1] Rate 1407
       DiscountDetails <DscntDtls> [0..1]  C21 1408
         Amount <Amt> [0..1] Amount C1, C15 1408
         Rate <Rate> [0..1] Rate 1409
         Basis <Bsis> [0..1]  1409
{Or           Code <Cd> [1..1] CodeSet 1409
Or}           Proprietary <Prtry> [1..1] ± 1409
       AppliedAmount <ApldAmt> [0..1] Amount C1, C15 1410
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1397 May 2026
```

## File page 1398

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 1410
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 1410
       RecipientIdentification <RcptId> [0..1] ± 1410
       InformativeIndicator <InftvInd> [1..1] Indicator 1411
     IndividualTax <IndvTax> [0..*] ± 1411
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  1411
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C18,
C19,
C27,
C28,
C31
1412
         ISIN <ISIN> [0..1] IdentifierSet 1414
         OtherIdentification <OthrId> [0..*]  1414
           Identification <Id> [1..1] Text 1414
           Suffix <Sfx> [0..1] Text 1414
           Type <Tp> [1..1]  1414
{Or             Code <Cd> [1..1] CodeSet 1415
Or}             Proprietary <Prtry> [1..1] Text 1416
         Description <Desc> [0..1] Text 1416
       Quantity <Qty> [1..1]  1417
{Or         Quantity <Qty> [1..1] ± C20 1417
Or}         ProprietaryQuantity <PrtryQty> [1..1]  1417
           Quantity <Qty> [1..1] Quantity 1418
           QuantityType <QtyTp> [1..1] Text 1418
           Issuer <Issr> [1..1] Text 1418
           SchemeName <SchmeNm> [0..1] Text 1418
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1418
   OtherAmount <OthrAmt> [0..*]  1418
     Type <Tp> [1..1]  1419
{Or       Code <Cd> [1..1] CodeSet 1419
Or}       ProprietaryCode <PrtryCd> [1..1] ± 1419
     Amount <Amt> [1..1] Amount C1, C15 1419
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1398 May 2026
```

