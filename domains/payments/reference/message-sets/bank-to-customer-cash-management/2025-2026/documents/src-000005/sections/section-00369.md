---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [534, 535, 536, 537, 538, 539]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# Continuation at file page 534

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 534 to 539.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 534

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 716
                     TotalAmount <TtlAmt> [0..1] Amount C2, C6 716
                     Details <Dtls> [0..*]  717
                       Period <Prd> [0..1]  717
                         Year <Yr> [0..1] Year 717
                         Type <Tp> [0..1] CodeSet 718
                         FromToDate <FrToDt> [0..1] ± 718
                       Amount <Amt> [1..1] Amount C2, C6 719
                   AdditionalInformation <AddtlInf> [0..1] Text 719
               GarnishmentRemittance <GrnshmtRmt> [0..1]  719
                 Type <Tp> [1..1]  720
                   CodeOrProprietary <CdOrPrtry> [1..1]  720
{Or                     Code <Cd> [1..1] CodeSet 721
Or}                     Proprietary <Prtry> [1..1] Text 721
                   Issuer <Issr> [0..1] Text 721
                 Garnishee <Grnshee> [0..1] ± 721
                 GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 722
                 ReferenceNumber <RefNb> [0..1] Text 723
                 Date <Dt> [0..1] Date 724
                 RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 724
                 FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 724
                 EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 724
               SecuritiesData <SctiesData> [0..*]  724
                 UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 725
                 Amount <Amt> [0..1] Amount C1, C7 725
               AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 725
           RelatedDates <RltdDts> [0..1]  725
             AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 726
             TradeActivityContractualSettlementDate
<TradActvtyCtrctlSttlmDt>
[0..1] Date 726
             TradeDate <TradDt> [0..1] Date 726
             InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 726
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
534 March 2026
```

## File page 535

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             StartDate <StartDt> [0..1] Date 726
             EndDate <EndDt> [0..1] Date 727
             TransactionDateTime <TxDtTm> [0..1] DateTime 727
             Proprietary <Prtry> [0..*]  727
               Type <Tp> [1..1] Text 727
               Date <Dt> [1..1] ± 727
           RelatedPrice <RltdPric> [0..1]  727
{Or             DealPrice <DealPric> [1..1] ± 728
Or}             Proprietary <Prtry> [1..*]  728
               Type <Tp> [1..1] Text 728
               Price <Pric> [1..1] Amount C2, C6 728
           RelatedQuantities <RltdQties> [0..*]  729
{Or             Quantity <Qty> [1..1] ± C10 729
Or             OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1] ± 730
Or}             Proprietary <Prtry> [1..1]  730
               Type <Tp> [1..1] Text 730
               Quantity <Qty> [1..1] Text 730
           FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C8, C9,
C20,
C21,
C23
730
           Tax <Tax> [0..1]  731
             Creditor <Cdtr> [0..1] ± 733
             Debtor <Dbtr> [0..1] ± 733
             UltimateDebtor <UltmtDbtr> [0..1] ± 733
             AdministrationZone <AdmstnZone> [0..1] Text 734
             ReferenceNumber <RefNb> [0..1] Text 734
             Method <Mtd> [0..1] Text 734
             TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 734
             TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 735
             Date <Dt> [0..1] Date 735
             SequenceNumber <SeqNb> [0..1] Quantity 735
             Record <Rcrd> [0..*]  735
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
535 March 2026
```

## File page 536

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Type <Tp> [0..1] Text 736
               Category <Ctgy> [0..1] Text 736
               CategoryDetails <CtgyDtls> [0..1] Text 736
               DebtorStatus <DbtrSts> [0..1] Text 737
               CertificateIdentification <CertId> [0..1] Text 737
               FormsCode <FrmsCd> [0..1] Text 737
               Period <Prd> [0..1]  737
                 Year <Yr> [0..1] Year 737
                 Type <Tp> [0..1] CodeSet 737
                 FromToDate <FrToDt> [0..1] ± 738
               TaxAmount <TaxAmt> [0..1]  739
                 Rate <Rate> [0..1] Rate 739
                 TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 739
                 TotalAmount <TtlAmt> [0..1] Amount C2, C6 739
                 Details <Dtls> [0..*]  740
                   Period <Prd> [0..1]  740
                     Year <Yr> [0..1] Year 740
                     Type <Tp> [0..1] CodeSet 741
                     FromToDate <FrToDt> [0..1] ± 741
                   Amount <Amt> [1..1] Amount C2, C6 742
               AdditionalInformation <AddtlInf> [0..1] Text 742
           ReturnInformation <RtrInf> [0..1]  C27 742
             OriginalBankTransactionCode <OrgnlBkTxCd> [0..1] ± C11,
C14
743
             Originator <Orgtr> [0..1] ± 744
             Reason <Rsn> [0..1]  745
{Or               Code <Cd> [1..1] CodeSet 746
Or}               Proprietary <Prtry> [1..1] Text 746
             AdditionalInformation <AddtlInf> [0..*] Text 746
           RelatedCorporateAction <RltdCorpActn> [0..1]  746
             EventType <EvtTp> [1..1] ± C12 746
             CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 747
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
536 March 2026
```

## File page 537

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 747
           SafekeepingAccount <SfkpgAcct> [0..1] ± 747
           UnderlyingAllocation <UndrlygAllcn> [0..*]  C30 748
             Amount <Amt> [1..1] Amount C2, C6 748
             CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 748
             Account <Acct> [1..1] ± C19,
C17
749
             Purpose <Purp> [1..1] ± 749
             Reference <Ref> [1..1] Text 750
             RelatedReferences <RltdRefs> [0..*] ± 750
           CashDeposit <CshDpst> [0..*] ± 750
           CardTransaction <CardTx> [0..1]  751
             Card <Card> [0..1]  754
               PlainCardData <PlainCardData> [0..1]  755
                 PAN <PAN> [1..1] Text 756
                 CardSequenceNumber <CardSeqNb> [0..1] Text 756
                 EffectiveDate <FctvDt> [0..1] YearMonth 756
                 ExpiryDate <XpryDt> [1..1] YearMonth 756
                 ServiceCode <SvcCd> [0..1] Text 756
                 TrackData <TrckData> [0..*]  757
                   TrackNumber <TrckNb> [0..1] Text 757
                   TrackValue <TrckVal> [1..1] Text 757
                 CardSecurityCode <CardSctyCd> [0..1]  757
                   CSCManagement <CSCMgmt> [1..1] CodeSet 757
                   CSCValue <CSCVal> [0..1] Text 758
               CardCountryCode <CardCtryCd> [0..1] Text 758
               CardBrand <CardBrnd> [0..1] ± 758
               AdditionalCardData <AddtlCardData> [0..1] Text 758
             POI <POI> [0..1]  758
               Identification <Id> [1..1] ± 759
               SystemName <SysNm> [0..1] Text 760
               GroupIdentification <GrpId> [0..1] Text 760
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
537 March 2026
```

## File page 538

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Capabilities <Cpblties> [0..1]  760
                 CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 760
                 CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 761
                 OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 761
                 DisplayCapabilities <DispCpblties> [0..*]  762
                   DisplayType <DispTp> [1..1] CodeSet 762
                   NumberOfLines <NbOfLines> [1..1] Text 762
                   LineWidth <LineWidth> [1..1] Text 762
                 PrintLineWidth <PrtLineWidth> [0..1] Text 762
               Component <Cmpnt> [0..*]  762
                 POIComponentType <POICmpntTp> [1..1] CodeSet 763
                 ManufacturerIdentification <ManfctrId> [0..1] Text 763
                 Model <Mdl> [0..1] Text 763
                 VersionNumber <VrsnNb> [0..1] Text 763
                 SerialNumber <SrlNb> [0..1] Text 764
                 ApprovalNumber <ApprvlNb> [0..*] Text 764
             Transaction <Tx> [0..1]  764
{Or               Aggregated <Aggtd> [1..1]  766
                 AdditionalService <AddtlSvc> [0..1] CodeSet 766
                 TransactionCategory <TxCtgy> [0..1] CodeSet 767
                 SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 767
                 SequenceNumberRange <SeqNbRg> [0..1]  767
                   FirstTransaction <FrstTx> [0..1] Text 767
                   LastTransaction <LastTx> [0..1] Text 767
                 TransactionDateRange <TxDtRg> [0..1] ± 768
Or}               Individual <Indv> [1..1]  768
                 ICCRelatedData <ICCRltdData> [0..1] Text 770
                 PaymentContext <PmtCntxt> [0..1]  770
                   CardPresent <CardPres> [0..1] Indicator 770
                   CardholderPresent <CrdhldrPres> [0..1] Indicator 770
                   OnLineContext <OnLineCntxt> [0..1] Indicator 771
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
538 March 2026
```

## File page 539

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                   AttendanceContext <AttndncCntxt> [0..1] CodeSet 771
                   TransactionEnvironment <TxEnvt> [0..1] CodeSet 771
                   TransactionChannel <TxChanl> [0..1] CodeSet 771
                   AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 772
                   AttendantLanguage <AttndntLang> [0..1] CodeSet 772
                   CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 772
                   FallbackIndicator <FllbckInd> [0..1] Indicator 772
                   AuthenticationMethod <AuthntcnMtd> [0..1]  773
                     AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 773
                     AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 773
                 AdditionalService <AddtlSvc> [0..1] CodeSet 774
                 TransactionCategory <TxCtgy> [0..1] CodeSet 774
                 SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 774
                 SaleReferenceNumber <SaleRefNb> [0..1] Text 775
                 RePresentmentReason <RePresntmntRsn> [0..1] CodeSet 775
                 SequenceNumber <SeqNb> [0..1] Text 775
                 TransactionIdentification <TxId> [0..1] ± 775
                 Product <Pdct> [0..1]  775
                   ProductCode <PdctCd> [1..1] Text 776
                   UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 776
                   ProductQuantity <PdctQty> [0..1] Quantity 777
                   UnitPrice <UnitPric> [0..1] Amount 777
                   ProductAmount <PdctAmt> [0..1] Amount 777
                   TaxType <TaxTp> [0..1] Text 778
                   AdditionalProductInformation <AddtlPdctInf> [0..1] Text 778
                 ValidationDate <VldtnDt> [0..1] Date 778
                 ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 778
             PrePaidAccount <PrePdAcct> [0..1] ± C19,
C17
778
           InstructionCopy <InstrCpy> [0..1] Text 779
           AdditionalTransactionInformation <AddtlTxInf> [0..1] Text 779
           SupplementaryData <SplmtryData> [0..*] ± C29 779
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
539 March 2026
```

