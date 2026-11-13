---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.10 PaymentDetails <PmtDtls>", "40.4.15.10.2 CreditTransferDetails <CdtTrfDtls>", "40.4.15.10.2.12 CreditorAccount <CdtrAcct>", "40.4.15.10.2.12.3 BlockChainCashWallet <BlckChainCshWllt>"]
file_pages: [1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.10.2.12.3 BlockChainCashWallet <BlckChainCshWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1588 to 1596.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1588

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
40.4.15.10.2.12.3  BlockChainCashWallet <BlckChainCshWllt>
Presence: [0..1]
Definition: Block Chain Wallet where digital currencies are maintained. This is the equivalent of cash
account for digital currencies.
BlockChainCashWallet <BlckChainCshWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
40.4.15.10.2.12.4  Other <Othr>
Presence: [0..1]
Definition: Unique identification of the account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 4326 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4326
   SchemeName <SchmeNm> [0..1]  4326
{Or     Code <Cd> [1..1] CodeSet 4326
Or}     Proprietary <Prtry> [1..1] Text 4326
   Issuer <Issr> [0..1] Text 4326
40.4.15.11  FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>
Presence: [0..*]
Definition: Asset transferred.
Impacted by: C7 "AssetQuantity1Guideline", C8 "AssetQuantity2Guideline", C13 "Conversion1Rule",
C14 "Conversion2Rule", C25 "EffectiveDatesGuideline"
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1588 May 2026
```

## File page 1589

```text
FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> contains the following
FinancialInstrument112 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LineIdentification <LineId> [0..1] Text 1597
   Instrument <Instrm> [1..1]  1597
{Or     Security <Scty> [1..1]  C29 1598
       Identification <Id> [1..1]  1599
{Or         ISIN <ISIN> [1..1] IdentifierSet 1600
Or         SEDOL <SEDOL> [1..1] IdentifierSet 1600
Or         CUSIP <CUSIP> [1..1] IdentifierSet 1601
Or         RIC <RIC> [1..1] IdentifierSet 1601
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 1601
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 1601
Or         CTA <CTA> [1..1] IdentifierSet 1601
Or         QUICK <QUICK> [1..1] IdentifierSet 1601
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 1601
Or         Dutch <Dtch> [1..1] IdentifierSet 1602
Or         Valoren <Vlrn> [1..1] IdentifierSet 1602
Or         Sicovam <SCVM> [1..1] IdentifierSet 1602
Or         Belgian <Belgn> [1..1] IdentifierSet 1602
Or         Common <Cmon> [1..1] IdentifierSet 1602
Or         DTI <DTI> [1..1] IdentifierSet 1602
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  1602
           Identification <Id> [1..1] Text 1603
           IdentificationSource <IdSrc> [1..1] ± 1603
       Name <Nm> [0..1] Text 1603
       ShortName <ShrtNm> [0..1] Text 1603
       ClassificationType <ClssfctnTp> [0..1] ± 1603
Or     CashAsset <CshAsst> [1..1] ± C27 1603
Or}     OtherAsset <OthrAsst> [1..1] ± 1604
   Quantity <Qty> [0..1]  1604
     Unit <Unit> [0..1]  1605
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 1605
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1589 May 2026
```

## File page 1590

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1605
     PercentageRate <PctgRate> [0..1] Rate 1605
     FaceAmount <FaceAmt> [0..1] Amount 1605
     AmortisedValue <AmtsdVal> [0..1] Amount 1606
     CashAmount <CshAmt> [0..1] Amount C1 1606
     OtherAsset <OthrAsst> [0..1] Text 1606
   PartialInstructedQuantity <PrtlInstdQty> [0..1] Indicator 1606
   OriginalPercentageInstructed <OrgnlPctgInstd> [0..1] Rate 1606
   TransferType <TrfTp> [1..1] ± C46 1606
   AdditionalAsset <AddtlAsst> [0..1] Indicator 1607
   NotAvailable <NotAvlbl> [0..1] Indicator 1607
   Conversion <Convs> [0..1]  1607
     OriginalSecurity <OrgnlScty> [1..1]  C30 1608
       Identification <Id> [1..1]  1609
{Or         ISIN <ISIN> [1..1] IdentifierSet 1610
Or         SEDOL <SEDOL> [1..1] IdentifierSet 1610
Or         CUSIP <CUSIP> [1..1] IdentifierSet 1611
Or         RIC <RIC> [1..1] IdentifierSet 1611
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 1611
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 1611
Or         CTA <CTA> [1..1] IdentifierSet 1611
Or         QUICK <QUICK> [1..1] IdentifierSet 1611
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 1611
Or         Dutch <Dtch> [1..1] IdentifierSet 1612
Or         Valoren <Vlrn> [1..1] IdentifierSet 1612
Or         Sicovam <SCVM> [1..1] IdentifierSet 1612
Or         Belgian <Belgn> [1..1] IdentifierSet 1612
Or         Common <Cmon> [1..1] IdentifierSet 1612
Or         DTI <DTI> [1..1] IdentifierSet 1612
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  1612
           Identification <Id> [1..1] Text 1613
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1590 May 2026
```

## File page 1591

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           IdentificationSource <IdSrc> [1..1] ± 1613
       Name <Nm> [0..1] Text 1613
       ShortName <ShrtNm> [0..1] Text 1613
     AdditionalInformation <AddtlInf> [0..*] ± 1613
   UnitsDetails <UnitsDtls> [0..*]  1613
     Units <Units> [1..1]  1616
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 1616
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1616
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
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 1620
       IndividualFee <IndvFee> [0..*]  C6 1621
         Type <Tp> [1..1]  1621
{Or           Code <Cd> [1..1] CodeSet 1622
Or}           Proprietary <Prtry> [1..1] ± 1623
         Basis <Bsis> [0..1]  1623
{Or           Code <Cd> [1..1] CodeSet 1623
Or}           Proprietary <Prtry> [1..1] ± 1624
         StandardAmount <StdAmt> [0..1] Amount C1, C18 1624
         StandardRate <StdRate> [0..1] Rate 1624
         DiscountDetails <DscntDtls> [0..1]  C24 1625
           Amount <Amt> [0..1] Amount C1, C18 1625
           Rate <Rate> [0..1] Rate 1626
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1591 May 2026
```

## File page 1592

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Basis <Bsis> [0..1]  1626
{Or             Code <Cd> [1..1] CodeSet 1626
Or}             Proprietary <Prtry> [1..1] ± 1626
         AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1627
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
{Or               Code <Cd> [1..1] CodeSet 1632
Or}               Proprietary <Prtry> [1..1] Text 1633
           Description <Desc> [0..1] Text 1633
         Quantity <Qty> [1..1]  1634
{Or           Quantity <Qty> [1..1] ± C23 1634
Or}           ProprietaryQuantity <PrtryQty> [1..1]  1634
             Quantity <Qty> [1..1] Quantity 1635
             QuantityType <QtyTp> [1..1] Text 1635
             Issuer <Issr> [1..1] Text 1635
             SchemeName <SchmeNm> [0..1] Text 1635
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1635
     OtherAmount <OthrAmt> [0..*]  1635
       Type <Tp> [1..1]  1636
{Or         Code <Cd> [1..1] CodeSet 1636
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1592 May 2026
```

## File page 1593

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         ProprietaryCode <PrtryCd> [1..1] ± 1636
       Amount <Amt> [1..1] Amount C1, C18 1636
   ClientReference <ClntRef> [0..1] ± 1637
   CounterpartyReference <CtrPtyRef> [0..1] ± 1637
   BusinessFlowType <BizFlowTp> [0..1] CodeSet 1637
   AverageAcquisitionPrice <AvrgAcqstnPric> [0..1] Amount C1, C18 1638
   TransferCurrency <TrfCcy> [0..1] CodeSet C2 1638
   TotalBookValue <TtlBookVal> [0..1] ± 1638
   OriginalCost <OrgnlCost> [0..1] Amount C1 1639
   LatestValuation <LatstValtn> [0..1] ± 1639
   TransfereeAccount <TrfeeAcct> [0..1]  1639
     OwnerIdentification <OwnrId> [0..1] ± 1640
     AccountIdentification <AcctId> [0..1] Text 1640
     Designation <Dsgnt> [0..1] Text 1640
     AccountName <AcctNm> [0..1] Text 1640
     Servicer <Svcr> [0..1] ± 1641
     SubAccountDetails <SubAcctDtls> [0..1] ± 1641
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1641
   Transferor <Trfr> [0..1]  1642
     OwnerIdentification <OwnrId> [0..1] ± 1642
     AccountIdentification <AcctId> [0..1] Text 1642
     Designation <Dsgnt> [0..1] Text 1642
     AccountName <AcctNm> [0..1] Text 1643
     Servicer <Svcr> [0..1] ± 1643
     SubAccountDetails <SubAcctDtls> [0..1] ± 1643
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1643
   IntermediaryInformation <IntrmyInf> [0..*] ± 1644
   RequestedTradeDate <ReqdTradDt> [0..1] Date 1644
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 1644
   EffectiveTransferDate <FctvTrfDt> [0..1] ± 1644
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 1645
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1593 May 2026
```

## File page 1594

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentDetails <PmtDtls> [0..1]  1645
     Reference <Ref> [0..1] Text 1648
     CreditTransferDetails <CdtTrfDtls> [0..1]  1648
       Debtor <Dbtr> [0..1] ± 1651
       DebtorAccount <DbtrAcct> [0..1]  1651
         Name <Nm> [0..1] Text 1651
         IBAN <IBAN> [0..1] IdentifierSet C28 1651
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1652
         Other <Othr> [0..1] ± 1652
       DebtorAgent <DbtrAgt> [0..1]  1652
         BICFI <BICFI> [0..1] IdentifierSet C9 1653
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1653
         NameAndAddress <NmAndAdr> [0..1] ± 1654
         LEI <LEI> [0..1] IdentifierSet 1654
         ProprietaryIdentification <PrtryId> [0..1] Text 1655
         BranchIdentification <BrnchId> [0..1] ± 1655
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  1655
         Name <Nm> [0..1] Text 1655
         IBAN <IBAN> [0..1] IdentifierSet C28 1655
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1656
         Other <Othr> [0..1] ± 1656
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  1656
         BICFI <BICFI> [0..1] IdentifierSet C9 1657
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1657
         NameAndAddress <NmAndAdr> [0..1] ± 1658
         LEI <LEI> [0..1] IdentifierSet 1658
         ProprietaryIdentification <PrtryId> [0..1] Text 1659
         BranchIdentification <BrnchId> [0..1] ± 1659
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1659
         Name <Nm> [0..1] Text 1659
         IBAN <IBAN> [0..1] IdentifierSet C28 1659
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1594 May 2026
```

## File page 1595

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1660
         Other <Othr> [0..1] ± 1660
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  1660
         BICFI <BICFI> [0..1] IdentifierSet C9 1661
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1661
         NameAndAddress <NmAndAdr> [0..1] ± 1662
         LEI <LEI> [0..1] IdentifierSet 1662
         ProprietaryIdentification <PrtryId> [0..1] Text 1663
         BranchIdentification <BrnchId> [0..1] ± 1663
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1663
         Name <Nm> [0..1] Text 1663
         IBAN <IBAN> [0..1] IdentifierSet C28 1663
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1664
         Other <Othr> [0..1] ± 1664
       CreditorAgent <CdtrAgt> [1..1]  1664
         BICFI <BICFI> [0..1] IdentifierSet C9 1665
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1665
         NameAndAddress <NmAndAdr> [0..1] ± 1666
         LEI <LEI> [0..1] IdentifierSet 1666
         ProprietaryIdentification <PrtryId> [0..1] Text 1667
         BranchIdentification <BrnchId> [0..1] ± 1667
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  1667
         Name <Nm> [0..1] Text 1667
         IBAN <IBAN> [0..1] IdentifierSet C28 1667
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1668
         Other <Othr> [0..1] ± 1668
       Creditor <Cdtr> [0..1] ± 1668
       CreditorAccount <CdtrAcct> [1..1]  1669
         Name <Nm> [0..1] Text 1669
         IBAN <IBAN> [0..1] IdentifierSet C28 1669
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1670
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1595 May 2026
```

## File page 1596

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Other <Othr> [0..1] ± 1670
   CrystallisationDetails <CrstllstnDtls> [0..*] ± 1670
   TaxValuationPoint <TaxValtnPt> [0..1] ± 1671
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  1671
     SafekeepingPlace <SfkpgPlc> [0..1] ± 1672
     TradeTransactionCondition <TradTxCond> [0..*] ± 1673
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1673
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1673
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1674
       Depository <Dpstry> [0..1] ± 1675
       Party1 <Pty1> [0..1] ± 1676
       Party2 <Pty2> [0..1] ± 1676
       Party3 <Pty3> [0..1] ± 1677
       Party4 <Pty4> [0..1] ± 1677
       Party5 <Pty5> [0..1] ± 1678
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1678
       Depository <Dpstry> [0..1] ± 1680
       Party1 <Pty1> [0..1] ± 1681
       Party2 <Pty2> [0..1] ± 1681
       Party3 <Pty3> [0..1] ± 1681
       Party4 <Pty4> [0..1] ± 1682
       Party5 <Pty5> [0..1] ± 1682
   AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1683
   TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1683
   AdditionalInformation <AddtlInf> [0..*] ± 1683
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1596 May 2026
```

