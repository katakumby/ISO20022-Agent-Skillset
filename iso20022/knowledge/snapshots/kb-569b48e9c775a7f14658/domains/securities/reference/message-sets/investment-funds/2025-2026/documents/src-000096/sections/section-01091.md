---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [1526, 1527, 1528, 1529, 1530]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# Continuation at file page 1526

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1526 to 1530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1526

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 1620
         IndividualFee <IndvFee> [0..*]  C6 1621
           Type <Tp> [1..1]  1621
{Or             Code <Cd> [1..1] CodeSet 1622
Or}             Proprietary <Prtry> [1..1] ± 1623
           Basis <Bsis> [0..1]  1623
{Or             Code <Cd> [1..1] CodeSet 1623
Or}             Proprietary <Prtry> [1..1] ± 1624
           StandardAmount <StdAmt> [0..1] Amount C1, C18 1624
           StandardRate <StdRate> [0..1] Rate 1624
           DiscountDetails <DscntDtls> [0..1]  C24 1625
             Amount <Amt> [0..1] Amount C1, C18 1625
             Rate <Rate> [0..1] Rate 1626
             Basis <Bsis> [0..1]  1626
{Or               Code <Cd> [1..1] CodeSet 1626
Or}               Proprietary <Prtry> [1..1] ± 1626
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
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1526 May 2026
```

## File page 1527

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or                 Code <Cd> [1..1] CodeSet 1632
Or}                 Proprietary <Prtry> [1..1] Text 1633
             Description <Desc> [0..1] Text 1633
           Quantity <Qty> [1..1]  1634
{Or             Quantity <Qty> [1..1] ± C23 1634
Or}             ProprietaryQuantity <PrtryQty> [1..1]  1634
               Quantity <Qty> [1..1] Quantity 1635
               QuantityType <QtyTp> [1..1] Text 1635
               Issuer <Issr> [1..1] Text 1635
               SchemeName <SchmeNm> [0..1] Text 1635
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1635
       OtherAmount <OthrAmt> [0..*]  1635
         Type <Tp> [1..1]  1636
{Or           Code <Cd> [1..1] CodeSet 1636
Or}           ProprietaryCode <PrtryCd> [1..1] ± 1636
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
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1527 May 2026
```

## File page 1528

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1528 May 2026
```

## File page 1529

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1529 May 2026
```

## File page 1530

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1530 May 2026
```

