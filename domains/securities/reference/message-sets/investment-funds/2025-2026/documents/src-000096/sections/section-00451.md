---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.5 Function <Fctn>"]
file_pages: [620, 621, 622, 623, 624]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.5 Function <Fctn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 620 to 624.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 620

```text
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
28.4.4 RelatedReference <RltdRef>
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
28.4.5 Function <Fctn>
Presence: [0..1]
Definition: Function of the transfer in, that is, whether the transfer in message is used as an instruction
or an advice and request for information. The absence of Function indicates the message is an
instruction.
Datatype: "TransferInFunction1Code" on page 5379
CodeName Name Definition
ADRE AdviceAndRequest The transfer-in is an advice and request,
that is, the message is used to inform
the receiver to expect an unsolicited
transfer in confirmation and to request
account information for the transfer.
INST Instruction The transfer-in is an instruction.
28.4.6 MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 620 May 2026
```

## File page 621

```text
28.4.7 TransferDetails <TrfDtls>
Presence: [1..*]
Definition: General information related to the transfer of the financial instrument.
Impacted by: C33 "TotalUnitsNumberRule"
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 621 May 2026
```

## File page 622

```text
TransferDetails <TrfDtls> contains the following Transfer39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransferReference <TrfRef> [1..1] Text 625
   ClientReference <ClntRef> [0..1] ± 625
   CounterpartyReference <CtrPtyRef> [0..1] ± 626
   BusinessFlowType <BizFlowTp> [0..1] CodeSet 626
   RequestedTransferDate <ReqdTrfDt> [0..1] ± 626
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 627
   TransferOrderDateForm <TrfOrdrDtForm> [0..1] Date 627
   TransferReason <TrfRsn> [0..1] ± 627
   HoldingsPlanType <HldgsPlanTp> [0..3] CodeSet 627
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C19 628
     Identification <Id> [1..1]  629
{Or       ISIN <ISIN> [1..1] IdentifierSet 629
Or       SEDOL <SEDOL> [1..1] IdentifierSet 630
Or       CUSIP <CUSIP> [1..1] IdentifierSet 630
Or       RIC <RIC> [1..1] IdentifierSet 630
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 630
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 630
Or       CTA <CTA> [1..1] IdentifierSet 630
Or       QUICK <QUICK> [1..1] IdentifierSet 630
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 631
Or       Dutch <Dtch> [1..1] IdentifierSet 631
Or       Valoren <Vlrn> [1..1] IdentifierSet 631
Or       Sicovam <SCVM> [1..1] IdentifierSet 631
Or       Belgian <Belgn> [1..1] IdentifierSet 631
Or       Common <Cmon> [1..1] IdentifierSet 631
Or       DTI <DTI> [1..1] IdentifierSet 631
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  631
         Identification <Id> [1..1] Text 632
         IdentificationSource <IdSrc> [1..1] ± 632
     Name <Nm> [0..1] Text 632
     ShortName <ShrtNm> [0..1] Text 632
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 622 May 2026
```

## File page 623

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SupplementaryIdentification <SplmtryId> [0..1] Text 632
     ClassType <ClssTp> [0..1] Text 632
     SecuritiesForm <SctiesForm> [0..1] CodeSet 633
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 633
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 633
   Quantity <Qty> [1..1]  633
{Or     TotalUnitsNumber <TtlUnitsNb> [1..1]  634
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 634
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 634
Or}     TransferRate <TrfRate> [1..1] Rate 634
   UnitsDetails <UnitsDtls> [0..*]  634
     Units <Units> [1..1]  637
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 637
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 637
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
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 641
       IndividualFee <IndvFee> [0..*]  C6 642
         Type <Tp> [1..1]  642
{Or           Code <Cd> [1..1] CodeSet 643
Or}           Proprietary <Prtry> [1..1] ± 644
         Basis <Bsis> [0..1]  644
{Or           Code <Cd> [1..1] CodeSet 644
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 623 May 2026
```

## File page 624

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 645
         StandardAmount <StdAmt> [0..1] Amount C1, C10 645
         StandardRate <StdRate> [0..1] Rate 645
         DiscountDetails <DscntDtls> [0..1]  C15 646
           Amount <Amt> [0..1] Amount C1, C10 646
           Rate <Rate> [0..1] Rate 647
           Basis <Bsis> [0..1]  647
{Or             Code <Cd> [1..1] CodeSet 647
Or}             Proprietary <Prtry> [1..1] ± 647
         AppliedAmount <ApldAmt> [0..1] Amount C1, C10 648
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
{Or               Code <Cd> [1..1] CodeSet 653
Or}               Proprietary <Prtry> [1..1] Text 654
           Description <Desc> [0..1] Text 654
         Quantity <Qty> [1..1]  655
{Or           Quantity <Qty> [1..1] ± C14 655
Or}           ProprietaryQuantity <PrtryQty> [1..1]  655
             Quantity <Qty> [1..1] Quantity 656
             QuantityType <QtyTp> [1..1] Text 656
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 624 May 2026
```

