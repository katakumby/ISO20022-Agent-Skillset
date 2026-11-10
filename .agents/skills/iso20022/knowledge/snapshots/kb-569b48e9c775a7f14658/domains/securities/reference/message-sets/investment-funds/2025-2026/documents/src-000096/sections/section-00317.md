---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.4 RelatedReference <RltdRef>"]
file_pages: [445, 446, 447, 448]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.4 RelatedReference <RltdRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 445 to 448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 445

```text
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
24.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
24.4.5 MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
24.4.6 TransferDetails <TrfDtls>
Presence: [1..*]
Definition: General information related to the transfer of the financial instrument.
Impacted by: C33 "TotalUnitsNumberRule"
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 445 May 2026
```

## File page 446

```text
TransferDetails <TrfDtls> contains the following Transfer39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferReference <TrfRef> [1..1] Text 449
   ClientReference <ClntRef> [0..1] ± 449
   CounterpartyReference <CtrPtyRef> [0..1] ± 450
   BusinessFlowType <BizFlowTp> [0..1] CodeSet 450
   RequestedTransferDate <ReqdTrfDt> [0..1] ± 450
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 451
   TransferOrderDateForm <TrfOrdrDtForm> [0..1] Date 451
   TransferReason <TrfRsn> [0..1] ± 451
   HoldingsPlanType <HldgsPlanTp> [0..3] CodeSet 451
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C19 452
     Identification <Id> [1..1]  453
{Or       ISIN <ISIN> [1..1] IdentifierSet 453
Or       SEDOL <SEDOL> [1..1] IdentifierSet 454
Or       CUSIP <CUSIP> [1..1] IdentifierSet 454
Or       RIC <RIC> [1..1] IdentifierSet 454
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 454
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 454
Or       CTA <CTA> [1..1] IdentifierSet 454
Or       QUICK <QUICK> [1..1] IdentifierSet 454
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 455
Or       Dutch <Dtch> [1..1] IdentifierSet 455
Or       Valoren <Vlrn> [1..1] IdentifierSet 455
Or       Sicovam <SCVM> [1..1] IdentifierSet 455
Or       Belgian <Belgn> [1..1] IdentifierSet 455
Or       Common <Cmon> [1..1] IdentifierSet 455
Or       DTI <DTI> [1..1] IdentifierSet 455
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  455
         Identification <Id> [1..1] Text 456
         IdentificationSource <IdSrc> [1..1] ± 456
     Name <Nm> [0..1] Text 456
     ShortName <ShrtNm> [0..1] Text 456
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 446 May 2026
```

## File page 447

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SupplementaryIdentification <SplmtryId> [0..1] Text 456
     ClassType <ClssTp> [0..1] Text 456
     SecuritiesForm <SctiesForm> [0..1] CodeSet 457
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 457
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 457
   Quantity <Qty> [1..1]  457
{Or     TotalUnitsNumber <TtlUnitsNb> [1..1]  458
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 458
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 458
Or}     TransferRate <TrfRate> [1..1] Rate 458
   UnitsDetails <UnitsDtls> [0..*]  458
     Units <Units> [1..1]  461
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 461
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 461
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
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 465
       IndividualFee <IndvFee> [0..*]  C6 466
         Type <Tp> [1..1]  466
{Or           Code <Cd> [1..1] CodeSet 467
Or}           Proprietary <Prtry> [1..1] ± 468
         Basis <Bsis> [0..1]  468
{Or           Code <Cd> [1..1] CodeSet 468
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 447 May 2026
```

## File page 448

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 469
         StandardAmount <StdAmt> [0..1] Amount C1, C10 469
         StandardRate <StdRate> [0..1] Rate 469
         DiscountDetails <DscntDtls> [0..1]  C15 470
           Amount <Amt> [0..1] Amount C1, C10 470
           Rate <Rate> [0..1] Rate 471
           Basis <Bsis> [0..1]  471
{Or             Code <Cd> [1..1] CodeSet 471
Or}             Proprietary <Prtry> [1..1] ± 471
         AppliedAmount <ApldAmt> [0..1] Amount C1, C10 472
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
{Or               Code <Cd> [1..1] CodeSet 477
Or}               Proprietary <Prtry> [1..1] Text 478
           Description <Desc> [0..1] Text 478
         Quantity <Qty> [1..1]  479
{Or           Quantity <Qty> [1..1] ± C14 479
Or}           ProprietaryQuantity <PrtryQty> [1..1]  479
             Quantity <Qty> [1..1] Quantity 480
             QuantityType <QtyTp> [1..1] Text 480
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 448 May 2026
```

