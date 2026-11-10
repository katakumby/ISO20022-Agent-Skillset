---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.2 Structure"]
file_pages: [1444, 1445, 1446]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1444 to 1446.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1444

```text
39.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctHldgInfReq> [1..1]  C7, C8,
C14,
C15,
C16
   MessageReference <MsgRef> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..1] ± 1450
   RelatedReference <RltdRef> [0..1] ± 1451
   BusinessFlowDirectionType <BizFlowDrctnTp> [0..1] CodeSet 1451
   PrimaryIndividualInvestor <PmryIndvInvstr> [0..1] ± C22 0
   SecondaryIndividualInvestor <ScndryIndvInvstr> [0..1] ± C22 1452
   OtherIndividualInvestor <OthrIndvInvstr> [0..*] ± C22 0
   PrimaryCorporateInvestor <PmryCorpInvstr> [0..1] ± 0
   SecondaryCorporateInvestor <ScndryCorpInvstr> [0..1] ± 0
   OtherCorporateInvestor <OthrCorpInvstr> [0..*] ± 0
   TransferorAccount <TrfrAcct> [1..1] ± 0
   NomineeAccount <NmneeAcct> [0..1] ± 0
   Transferee <Trfee> [1..1] ± 0
   ProductTransfer <PdctTrf> [1..*]  0
     MasterReference <MstrRef> [0..1] Text 1459
     TransferIdentification <TrfId> [1..1] Text 1459
     Portfolio <Prtfl> [0..1]  1460
{Or       TaxEfficientProduct <TaxEffcntPdct> [1..1] ± 1460
Or       GeneralInvestment <GnlInvstmt> [1..1] ± 1461
Or}       Pension <Pnsn> [1..1]  1461
         Identification <Id> [0..1]  1461
           Identifier <Idr> [1..1] Text 1462
           SubIdentifier <SubIdr> [0..1] Text 1462
           AdditionalInformation <AddtlInf> [0..1] ± 1462
         Type <Tp> [0..1]  1462
{Or           Code <Cd> [1..1] CodeSet 1462
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1444 May 2026
```

## File page 1445

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 1463
         TransferScope <TrfScp> [0..1] ± 1464
         TaxReference <TaxRef> [0..*] ± 1464
         DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1464
         NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1464
         AdditionalInformation <AddtlInf> [0..*] ± 1465
     FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> [0..*]  1465
       LineIdentification <LineId> [0..1] Text 1468
       Instrument <Instrm> [1..1]  1468
{Or         Security <Scty> [1..1]  C13 1469
           Identification <Id> [1..1]  1470
{Or             ISIN <ISIN> [1..1] IdentifierSet 1471
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1471
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1472
Or             RIC <RIC> [1..1] IdentifierSet 1472
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1472
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1472
Or             CTA <CTA> [1..1] IdentifierSet 1472
Or             QUICK <QUICK> [1..1] IdentifierSet 1472
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1472
Or             Dutch <Dtch> [1..1] IdentifierSet 1473
Or             Valoren <Vlrn> [1..1] IdentifierSet 1473
Or             Sicovam <SCVM> [1..1] IdentifierSet 1473
Or             Belgian <Belgn> [1..1] IdentifierSet 1473
Or             Common <Cmon> [1..1] IdentifierSet 1473
Or             DTI <DTI> [1..1] IdentifierSet 1473
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1473
               Identification <Id> [1..1] Text 1474
               IdentificationSource <IdSrc> [1..1] ± 1474
           Name <Nm> [0..1] Text 1474
           ShortName <ShrtNm> [0..1] Text 1474
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1445 May 2026
```

## File page 1446

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           ClassificationType <ClssfctnTp> [0..1] ± 1474
Or         CashAsset <CshAsst> [1..1] ± 1474
Or}         OtherAsset <OthrAsst> [1..1] ± 1475
       ClientReference <ClntRef> [0..1] ± 1475
       CounterpartyReference <CtrPtyRef> [0..1] ± 1475
       TransfereeAccount <TrfeeAcct> [0..1]  1476
         OwnerIdentification <OwnrId> [0..1] ± 1476
         AccountIdentification <AcctId> [0..1] Text 1477
         Designation <Dsgnt> [0..1] Text 1477
         AccountName <AcctNm> [0..1] Text 1477
         Servicer <Svcr> [0..1] ± 1477
         SubAccountDetails <SubAcctDtls> [0..1] ± 1477
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1478
       Transferor <Trfr> [0..1]  1478
         OwnerIdentification <OwnrId> [0..1] ± 1478
         AccountIdentification <AcctId> [0..1] Text 1479
         Designation <Dsgnt> [0..1] Text 1479
         AccountName <AcctNm> [0..1] Text 1479
         Servicer <Svcr> [0..1] ± 1479
         SubAccountDetails <SubAcctDtls> [0..1] ± 1480
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1480
       SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  1480
         SafekeepingPlace <SfkpgPlc> [0..1] ± 1481
         TradeTransactionCondition <TradTxCond> [0..*] ± 1482
         SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1482
         SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1482
         ReceivingSideDetails <RcvgSdDtls> [0..1]  C6, C11,
C17,
C18,
C19,
C20,
C21
1482
           Depository <Dpstry> [0..1] ± 1484
           Party1 <Pty1> [0..1] ± 1485
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1446 May 2026
```

