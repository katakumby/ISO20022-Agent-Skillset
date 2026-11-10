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
file_pages: [1501, 1502, 1503, 1504]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# Continuation at file page 1501

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1501 to 1504.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1501

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
       PaymentDetails <PmtDtls> [0..1]  1645
         Reference <Ref> [0..1] Text 1648
         CreditTransferDetails <CdtTrfDtls> [0..1]  1648
           Debtor <Dbtr> [0..1] ± 1651
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1501 May 2026
```

## File page 1502

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           DebtorAccount <DbtrAcct> [0..1]  1651
             Name <Nm> [0..1] Text 1651
             IBAN <IBAN> [0..1] IdentifierSet C28 1651
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1652
             Other <Othr> [0..1] ± 1652
           DebtorAgent <DbtrAgt> [0..1]  1652
             BICFI <BICFI> [0..1] IdentifierSet C9 1653
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1653
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
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1657
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
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1502 May 2026
```

## File page 1503

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1661
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
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1665
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
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1503 May 2026
```

## File page 1504

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
     AdditionalInformation <AddtlInf> [0..*] ± 1683
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 0
   Extension <Xtnsn> [0..*] ± C26 0
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1504 May 2026
```

