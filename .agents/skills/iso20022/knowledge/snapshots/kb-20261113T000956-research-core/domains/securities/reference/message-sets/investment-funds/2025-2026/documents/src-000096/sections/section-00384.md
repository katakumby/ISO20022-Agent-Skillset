---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.5 MasterReference <MstrRef>"]
file_pages: [531, 532, 533, 534, 535]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.5 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 531 to 535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 531

```text
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
26.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
26.4.4 RelatedReference <RltdRef>
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
26.4.5 MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
26.4.6 TransferDetails <TrfDtls>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 531 May 2026
```

## File page 532

```text
Definition: General information related to the transfer of the financial instrument.
Impacted by: C34 "TotalUnitsNumberRule"
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 532 May 2026
```

## File page 533

```text
TransferDetails <TrfDtls> contains the following Transfer38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferConfirmationReference <TrfConfRef> [1..1] Text 536
   TransferReference <TrfRef> [1..1] Text 536
   ClientReference <ClntRef> [0..1] ± 537
   CounterpartyReference <CtrPtyRef> [0..1] ± 537
   BusinessFlowType <BizFlowTp> [0..1] CodeSet 537
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 538
   EffectiveTransferDate <FctvTrfDt> [1..1] ± 538
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 538
   TradeDate <TradDt> [0..1] ± 538
   TransferOrderDateForm <TrfOrdrDtForm> [0..1] Date 538
   TransferReason <TrfRsn> [0..1] ± 539
   HoldingsPlanType <HldgsPlanTp> [0..3] CodeSet 539
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 539
     Identification <Id> [1..1]  541
{Or       ISIN <ISIN> [1..1] IdentifierSet 541
Or       SEDOL <SEDOL> [1..1] IdentifierSet 541
Or       CUSIP <CUSIP> [1..1] IdentifierSet 542
Or       RIC <RIC> [1..1] IdentifierSet 542
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 542
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 542
Or       CTA <CTA> [1..1] IdentifierSet 542
Or       QUICK <QUICK> [1..1] IdentifierSet 542
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 542
Or       Dutch <Dtch> [1..1] IdentifierSet 543
Or       Valoren <Vlrn> [1..1] IdentifierSet 543
Or       Sicovam <SCVM> [1..1] IdentifierSet 543
Or       Belgian <Belgn> [1..1] IdentifierSet 543
Or       Common <Cmon> [1..1] IdentifierSet 543
Or       DTI <DTI> [1..1] IdentifierSet 543
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  543
         Identification <Id> [1..1] Text 544
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 533 May 2026
```

## File page 534

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         IdentificationSource <IdSrc> [1..1] ± 544
     Name <Nm> [0..1] Text 544
     ShortName <ShrtNm> [0..1] Text 544
     SupplementaryIdentification <SplmtryId> [0..1] Text 544
     ClassType <ClssTp> [0..1] Text 544
     SecuritiesForm <SctiesForm> [0..1] CodeSet 545
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 545
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 545
   TotalUnitsNumber <TtlUnitsNb> [1..1]  545
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 546
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 546
   TransferRate <TrfRate> [0..1] Rate 546
   UnitsDetails <UnitsDtls> [0..*]  546
     Units <Units> [1..1]  549
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 549
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 549
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
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 553
       IndividualFee <IndvFee> [0..*]  C6 554
         Type <Tp> [1..1]  554
{Or           Code <Cd> [1..1] CodeSet 555
Or}           Proprietary <Prtry> [1..1] ± 556
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 534 May 2026
```

## File page 535

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Basis <Bsis> [0..1]  556
{Or           Code <Cd> [1..1] CodeSet 556
Or}           Proprietary <Prtry> [1..1] ± 557
         StandardAmount <StdAmt> [0..1] Amount C1, C10 557
         StandardRate <StdRate> [0..1] Rate 557
         DiscountDetails <DscntDtls> [0..1]  C15 558
           Amount <Amt> [0..1] Amount C1, C10 558
           Rate <Rate> [0..1] Rate 559
           Basis <Bsis> [0..1]  559
{Or             Code <Cd> [1..1] CodeSet 559
Or}             Proprietary <Prtry> [1..1] ± 559
         AppliedAmount <ApldAmt> [0..1] Amount C1, C10 560
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
{Or               Code <Cd> [1..1] CodeSet 565
Or}               Proprietary <Prtry> [1..1] Text 566
           Description <Desc> [0..1] Text 566
         Quantity <Qty> [1..1]  567
{Or           Quantity <Qty> [1..1] ± C14 567
Or}           ProprietaryQuantity <PrtryQty> [1..1]  567
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 535 May 2026
```

