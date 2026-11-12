---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.2 Structure"]
file_pages: [1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1491 to 1500.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1491

```text
40.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PrtflTrfCmpltn> [1..1]  C15,
C16,
C31,
C32,
C35
   MessageReference <MsgRef> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 1510
   PreviousReference <PrvsRef> [0..1] ± 0
   RelatedReference <RltdRef> [0..1] ± 1511
   PrimaryIndividualInvestor <PmryIndvInvstr> [0..1] ± C48 1511
   RegisteredHolder <RegdHldr> [0..1] ± C48 0
   SecondaryIndividualInvestor <ScndryIndvInvstr> [0..1] ± C48 1513
   OtherIndividualInvestor <OthrIndvInvstr> [0..*] ± C48 0
   PrimaryCorporateInvestor <PmryCorpInvstr> [0..1] ± 0
   SecondaryCorporateInvestor <ScndryCorpInvstr> [0..1] ± 1514
   OtherCorporateInvestor <OthrCorpInvstr> [0..*] ± 1515
   TransferorAccount <TrfrAcct> [1..1] ± 0
   NomineeAccount <NmneeAcct> [0..1] ± 1516
   Transferee <Trfee> [1..1] ± 1516
   ProductTransfer <PdctTrf> [1..*]  0
     MasterReference <MstrRef> [0..1] Text 1531
     TransferInstructionReference <TrfInstrRef> [1..1] Text 1531
     TransferCompletionIdentification <TrfCmpltnId> [1..1] Text 1531
     ActualTransferDate <ActlTrfDt> [0..1] Date 1531
     Portfolio <Prtfl> [0..1]  1532
{Or       TaxEfficientProduct <TaxEffcntPdct> [1..1]  1536
         TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1538
         CurrentYear <CurYr> [0..1] Indicator 1538
         CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1539
         PreviousYears <PrvsYrs> [0..1]  C49 1539
           PreviousYears <PrvsYrs> [1..1]  1539
{Or             AllPreviousYears <AllPrvsYrs> [1..1] Text 1539
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1491 May 2026
```

## File page 1492

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1540
           CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1540
         PreviousYearSubscriptionAmount <PrvsYrSbcptAmt> [0..1] Amount C1 1540
         PreviousYearsSubscriptionAmount <PrvsYrsSbcptAmt> [0..1] Amount C1 1540
         DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1540
         CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C52 1541
           DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1541
           EquityComponent <EqtyCmpnt> [0..1] Amount C1 1541
           CashComponent <CshCmpnt> [0..1] Amount C1 1541
           TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1542
         BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1542
           TypeOfAmount <TpOfAmt> [1..1]  1543
{Or             Code <Cd> [1..1] CodeSet 1543
Or}             Proprietary <Prtry> [1..1] ± 1543
           Amount <Amt> [0..1] Amount C2 1543
           Reason <Rsn> [0..1]  1544
{Or             Code <Cd> [1..1] CodeSet 1544
Or}             Proprietary <Prtry> [1..1] ± 1544
           UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1544
           Outstanding <Outsdng> [0..1] Indicator 1545
           Reference <Ref> [0..1] Text 1545
           AdditionalInformation <AddtlInf> [0..*] ± 1545
         WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1545
         TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1545
         TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C18 1546
         OtherAmount <OthrAmt> [0..*]  1546
           Type <Tp> [1..1] ± 1546
           Amount <Amt> [1..1] Amount C1, C18 1546
         DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1547
         InvestorTaxReference <InvstrTaxRef> [0..1]  1547
           Type <Tp> [0..1]  1547
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1492 May 2026
```

## File page 1493

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 1547
Or}             Proprietary <Prtry> [1..1] ± 1548
           Reference <Ref> [1..1] Text 1548
         InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1548
         InnovativeFinance <InnvtvFinc> [0..*]  1548
           Type <Tp> [1..1] ± 1549
           Information <Inf> [1..1] Text 1549
         LowestInvestedAmountCurrentYear <LwstInvstdAmtCurYr> [0..1] Amount C1 1549
         TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1549
         UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1550
         CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1550
         EstimatedValue <EstmtdVal> [0..1] ± 1550
         AdditionalInformation <AddtlInf> [0..*] ± 1551
Or       GeneralInvestment <GnlInvstmt> [1..1] ± 1551
Or}       Pension <Pnsn> [1..1]  C10,
C11,
C42,
C43,
C44,
C45,
C50,
C51,
C54
1551
         Identification <Id> [0..1]  1554
           Identifier <Idr> [1..1] Text 1555
           SubIdentifier <SubIdr> [0..1] Text 1555
           AdditionalInformation <AddtlInf> [0..1] ± 1555
         Type <Tp> [1..1]  1555
{Or           Code <Cd> [1..1] CodeSet 1555
Or}           Proprietary <Prtry> [1..1] ± 1556
         TransferScope <TrfScp> [0..1] ± 1557
         TaxReference <TaxRef> [0..*] ± 1557
         DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1557
         DrawdownStatus <DrwdwnSts> [0..1] ± 1557
         DrawdownType <DrwdwnTp> [0..1] ± 1558
         NumberOfDrawdownTranches <NbOfDrwdwnTrnchs> [0..1] Quantity 1558
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1493 May 2026
```

## File page 1494

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         EstimatedValue <EstmtdVal> [0..1] ± 1558
         BlockTransfer <BlckTrf> [0..1] Indicator 1558
         BlockTransferReference <BlckTrfRef> [0..1] Text 1559
         TaxFreeCashProtection <TaxFreeCshPrtcn> [0..1] Indicator 1559
         TaxFreeCashAmount <TaxFreeCshAmt> [0..1] ± 1559
         ValueOfPensionPolicyOrPlanOrScheme
<ValOfPnsnPlcyOrPlanOrSchme>
[0..1] ± 1559
         RetirementAgeProtection <RtrmntAgePrtcn> [0..1] Indicator 1559
         RetirementAge <RtrmntAge> [0..1] Quantity 1560
         Sharing <Shrg> [0..1] Indicator 1560
         LumpSumType <LumpSumTp> [0..*] ± 1560
         PensionOrder <PnsnOrdr> [0..*] ± 1560
         RingFencedDrawdownAssets <RingFncdDrwdwnAssts> [0..1] Indicator 1560
         MoneyPurchaseAnnualAllowance <MnyPurchsAnlAllwnc> [0..1] ± 1561
         SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1561
         NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1561
         LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1561
         ClientLifetimeAllowanceProtection <ClntLftmAllwncPrtcn> [0..1] Indicator 1561
         BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1562
         NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1562
         AdditionalInformation <AddtlInf> [0..*] ± 1562
     AllOtherCash <AllOthrCsh> [0..*] ± 1562
     CashAll <CshAll> [0..*] ± 1563
     ResidualCash <RsdlCsh> [0..*] ± 1563
     TaxDate <TaxDt> [0..1] Date 1563
     PaymentDetails <PmtDtls> [0..1]  1563
       Reference <Ref> [0..1] Text 1566
       CreditTransferDetails <CdtTrfDtls> [0..1]  1566
         Debtor <Dbtr> [0..1] ± 1569
         DebtorAccount <DbtrAcct> [0..1]  1569
           Name <Nm> [0..1] Text 1569
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1494 May 2026
```

## File page 1495

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           IBAN <IBAN> [0..1] IdentifierSet C28 1569
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1570
           Other <Othr> [0..1] ± 1570
         DebtorAgent <DbtrAgt> [0..1]  1570
           BICFI <BICFI> [0..1] IdentifierSet C9 1571
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1571
           NameAndAddress <NmAndAdr> [0..1] ± 1572
           LEI <LEI> [0..1] IdentifierSet 1572
           ProprietaryIdentification <PrtryId> [0..1] Text 1573
           BranchIdentification <BrnchId> [0..1] ± 1573
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  1573
           Name <Nm> [0..1] Text 1573
           IBAN <IBAN> [0..1] IdentifierSet C28 1573
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1574
           Other <Othr> [0..1] ± 1574
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  1574
           BICFI <BICFI> [0..1] IdentifierSet C9 1575
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1575
           NameAndAddress <NmAndAdr> [0..1] ± 1576
           LEI <LEI> [0..1] IdentifierSet 1576
           ProprietaryIdentification <PrtryId> [0..1] Text 1577
           BranchIdentification <BrnchId> [0..1] ± 1577
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1577
           Name <Nm> [0..1] Text 1577
           IBAN <IBAN> [0..1] IdentifierSet C28 1577
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1578
           Other <Othr> [0..1] ± 1578
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  1578
           BICFI <BICFI> [0..1] IdentifierSet C9 1579
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1579
           NameAndAddress <NmAndAdr> [0..1] ± 1580
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1495 May 2026
```

## File page 1496

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           LEI <LEI> [0..1] IdentifierSet 1580
           ProprietaryIdentification <PrtryId> [0..1] Text 1581
           BranchIdentification <BrnchId> [0..1] ± 1581
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1581
           Name <Nm> [0..1] Text 1581
           IBAN <IBAN> [0..1] IdentifierSet C28 1581
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1582
           Other <Othr> [0..1] ± 1582
         CreditorAgent <CdtrAgt> [1..1]  1582
           BICFI <BICFI> [0..1] IdentifierSet C9 1583
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1583
           NameAndAddress <NmAndAdr> [0..1] ± 1584
           LEI <LEI> [0..1] IdentifierSet 1584
           ProprietaryIdentification <PrtryId> [0..1] Text 1585
           BranchIdentification <BrnchId> [0..1] ± 1585
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  1585
           Name <Nm> [0..1] Text 1585
           IBAN <IBAN> [0..1] IdentifierSet C28 1585
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1586
           Other <Othr> [0..1] ± 1586
         Creditor <Cdtr> [0..1] ± 1586
         CreditorAccount <CdtrAcct> [1..1]  1587
           Name <Nm> [0..1] Text 1587
           IBAN <IBAN> [0..1] IdentifierSet C28 1587
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1588
           Other <Othr> [0..1] ± 1588
     FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> [0..*]  C7, C8,
C13,
C14,
C25
1588
       LineIdentification <LineId> [0..1] Text 1597
       Instrument <Instrm> [1..1]  1597
{Or         Security <Scty> [1..1]  C29 1598
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1496 May 2026
```

## File page 1497

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1]  1599
{Or             ISIN <ISIN> [1..1] IdentifierSet 1600
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1600
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1601
Or             RIC <RIC> [1..1] IdentifierSet 1601
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1601
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1601
Or             CTA <CTA> [1..1] IdentifierSet 1601
Or             QUICK <QUICK> [1..1] IdentifierSet 1601
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1601
Or             Dutch <Dtch> [1..1] IdentifierSet 1602
Or             Valoren <Vlrn> [1..1] IdentifierSet 1602
Or             Sicovam <SCVM> [1..1] IdentifierSet 1602
Or             Belgian <Belgn> [1..1] IdentifierSet 1602
Or             Common <Cmon> [1..1] IdentifierSet 1602
Or             DTI <DTI> [1..1] IdentifierSet 1602
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1602
               Identification <Id> [1..1] Text 1603
               IdentificationSource <IdSrc> [1..1] ± 1603
           Name <Nm> [0..1] Text 1603
           ShortName <ShrtNm> [0..1] Text 1603
           ClassificationType <ClssfctnTp> [0..1] ± 1603
Or         CashAsset <CshAsst> [1..1] ± C27 1603
Or}         OtherAsset <OthrAsst> [1..1] ± 1604
       Quantity <Qty> [0..1]  1604
         Unit <Unit> [0..1]  1605
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 1605
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1605
         PercentageRate <PctgRate> [0..1] Rate 1605
         FaceAmount <FaceAmt> [0..1] Amount 1605
         AmortisedValue <AmtsdVal> [0..1] Amount 1606
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1497 May 2026
```

## File page 1498

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
{Or             ISIN <ISIN> [1..1] IdentifierSet 1610
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1610
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1611
Or             RIC <RIC> [1..1] IdentifierSet 1611
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1611
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1611
Or             CTA <CTA> [1..1] IdentifierSet 1611
Or             QUICK <QUICK> [1..1] IdentifierSet 1611
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1611
Or             Dutch <Dtch> [1..1] IdentifierSet 1612
Or             Valoren <Vlrn> [1..1] IdentifierSet 1612
Or             Sicovam <SCVM> [1..1] IdentifierSet 1612
Or             Belgian <Belgn> [1..1] IdentifierSet 1612
Or             Common <Cmon> [1..1] IdentifierSet 1612
Or             DTI <DTI> [1..1] IdentifierSet 1612
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1612
               Identification <Id> [1..1] Text 1613
               IdentificationSource <IdSrc> [1..1] ± 1613
           Name <Nm> [0..1] Text 1613
           ShortName <ShrtNm> [0..1] Text 1613
         AdditionalInformation <AddtlInf> [0..*] ± 1613
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1498 May 2026
```

## File page 1499

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       UnitsDetails <UnitsDtls> [0..*]  1613
         Units <Units> [1..1]  1616
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 1616
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1616
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
{Or               Code <Cd> [1..1] CodeSet 1622
Or}               Proprietary <Prtry> [1..1] ± 1623
             Basis <Bsis> [0..1]  1623
{Or               Code <Cd> [1..1] CodeSet 1623
Or}               Proprietary <Prtry> [1..1] ± 1624
             StandardAmount <StdAmt> [0..1] Amount C1, C18 1624
             StandardRate <StdRate> [0..1] Rate 1624
             DiscountDetails <DscntDtls> [0..1]  C24 1625
               Amount <Amt> [0..1] Amount C1, C18 1625
               Rate <Rate> [0..1] Rate 1626
               Basis <Bsis> [0..1]  1626
{Or                 Code <Cd> [1..1] CodeSet 1626
Or}                 Proprietary <Prtry> [1..1] ± 1626
             AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1627
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1499 May 2026
```

## File page 1500

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
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
{Or                   Code <Cd> [1..1] CodeSet 1632
Or}                   Proprietary <Prtry> [1..1] Text 1633
               Description <Desc> [0..1] Text 1633
             Quantity <Qty> [1..1]  1634
{Or               Quantity <Qty> [1..1] ± C23 1634
Or}               ProprietaryQuantity <PrtryQty> [1..1]  1634
                 Quantity <Qty> [1..1] Quantity 1635
                 QuantityType <QtyTp> [1..1] Text 1635
                 Issuer <Issr> [1..1] Text 1635
                 SchemeName <SchmeNm> [0..1] Text 1635
             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1635
         OtherAmount <OthrAmt> [0..*]  1635
           Type <Tp> [1..1]  1636
{Or             Code <Cd> [1..1] CodeSet 1636
Or}             ProprietaryCode <PrtryCd> [1..1] ± 1636
           Amount <Amt> [1..1] Amount C1, C18 1636
       ClientReference <ClntRef> [0..1] ± 1637
       CounterpartyReference <CtrPtyRef> [0..1] ± 1637
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1500 May 2026
```

