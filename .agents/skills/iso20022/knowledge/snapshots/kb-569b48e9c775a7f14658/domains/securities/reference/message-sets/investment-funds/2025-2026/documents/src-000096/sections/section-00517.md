---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.3 PreviousReference <PrvsRef>"]
file_pages: [707, 708, 709, 710, 711]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.3 PreviousReference <PrvsRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 707 to 711.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 707

```text
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
30.4.3 PreviousReference <PrvsRef>
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
30.4.4 RelatedReference <RltdRef>
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
30.4.5 Function <Fctn>
Presence: [0..1]
Definition: Function of the transfer in, that is, whether the transfer in message is used as a confirmation
or as or an advice. The absence of Function indicates the message is a confirmation.
Datatype: "TransferInFunction2Code" on page 5379
CodeName Name Definition
CONF Confirmation The transfer-in is a confirmation (rather
than an advice).
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 707 May 2026
```

## File page 708

```text
CodeName Name Definition
ADVI Advice The transfer-in provides advice about
account information for a transfer.
30.4.6 MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
30.4.7 TransferDetails <TrfDtls>
Presence: [1..*]
Definition: General information related to the transfer of the financial instrument.
Impacted by: C34 "TotalUnitsNumberRule"
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 708 May 2026
```

## File page 709

```text
TransferDetails <TrfDtls> contains the following Transfer38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferConfirmationReference <TrfConfRef> [1..1] Text 712
   TransferReference <TrfRef> [1..1] Text 712
   ClientReference <ClntRef> [0..1] ± 713
   CounterpartyReference <CtrPtyRef> [0..1] ± 713
   BusinessFlowType <BizFlowTp> [0..1] CodeSet 713
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 714
   EffectiveTransferDate <FctvTrfDt> [1..1] ± 714
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 714
   TradeDate <TradDt> [0..1] ± 714
   TransferOrderDateForm <TrfOrdrDtForm> [0..1] Date 714
   TransferReason <TrfRsn> [0..1] ± 715
   HoldingsPlanType <HldgsPlanTp> [0..3] CodeSet 715
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 715
     Identification <Id> [1..1]  717
{Or       ISIN <ISIN> [1..1] IdentifierSet 717
Or       SEDOL <SEDOL> [1..1] IdentifierSet 717
Or       CUSIP <CUSIP> [1..1] IdentifierSet 718
Or       RIC <RIC> [1..1] IdentifierSet 718
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 718
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 718
Or       CTA <CTA> [1..1] IdentifierSet 718
Or       QUICK <QUICK> [1..1] IdentifierSet 718
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 718
Or       Dutch <Dtch> [1..1] IdentifierSet 719
Or       Valoren <Vlrn> [1..1] IdentifierSet 719
Or       Sicovam <SCVM> [1..1] IdentifierSet 719
Or       Belgian <Belgn> [1..1] IdentifierSet 719
Or       Common <Cmon> [1..1] IdentifierSet 719
Or       DTI <DTI> [1..1] IdentifierSet 719
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  719
         Identification <Id> [1..1] Text 720
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 709 May 2026
```

## File page 710

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         IdentificationSource <IdSrc> [1..1] ± 720
     Name <Nm> [0..1] Text 720
     ShortName <ShrtNm> [0..1] Text 720
     SupplementaryIdentification <SplmtryId> [0..1] Text 720
     ClassType <ClssTp> [0..1] Text 720
     SecuritiesForm <SctiesForm> [0..1] CodeSet 721
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 721
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 721
   TotalUnitsNumber <TtlUnitsNb> [1..1]  721
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 722
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 722
   TransferRate <TrfRate> [0..1] Rate 722
   UnitsDetails <UnitsDtls> [0..*]  722
     Units <Units> [1..1]  725
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 725
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 725
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
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 729
       IndividualFee <IndvFee> [0..*]  C6 730
         Type <Tp> [1..1]  730
{Or           Code <Cd> [1..1] CodeSet 731
Or}           Proprietary <Prtry> [1..1] ± 732
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 710 May 2026
```

## File page 711

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Basis <Bsis> [0..1]  732
{Or           Code <Cd> [1..1] CodeSet 732
Or}           Proprietary <Prtry> [1..1] ± 733
         StandardAmount <StdAmt> [0..1] Amount C1, C10 733
         StandardRate <StdRate> [0..1] Rate 733
         DiscountDetails <DscntDtls> [0..1]  C15 734
           Amount <Amt> [0..1] Amount C1, C10 734
           Rate <Rate> [0..1] Rate 735
           Basis <Bsis> [0..1]  735
{Or             Code <Cd> [1..1] CodeSet 735
Or}             Proprietary <Prtry> [1..1] ± 735
         AppliedAmount <ApldAmt> [0..1] Amount C1, C10 736
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
{Or               Code <Cd> [1..1] CodeSet 741
Or}               Proprietary <Prtry> [1..1] Text 742
           Description <Desc> [0..1] Text 742
         Quantity <Qty> [1..1]  743
{Or           Quantity <Qty> [1..1] ± C14 743
Or}           ProprietaryQuantity <PrtryQty> [1..1]  743
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 711 May 2026
```

