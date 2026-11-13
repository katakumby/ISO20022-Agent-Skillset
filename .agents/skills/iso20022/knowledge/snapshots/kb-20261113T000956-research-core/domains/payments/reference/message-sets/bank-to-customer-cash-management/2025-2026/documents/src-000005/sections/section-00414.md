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
file_pages: [622, 623, 624]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# Continuation at file page 622

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 622 to 624.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 622

```text
Or MessageElement<XML Tag> Mult. Type Constr.
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
622 March 2026
```

## File page 623

```text
Or MessageElement<XML Tag> Mult. Type Constr.
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
{Or         Aggregated <Aggtd> [1..1]  766
           AdditionalService <AddtlSvc> [0..1] CodeSet 766
           TransactionCategory <TxCtgy> [0..1] CodeSet 767
           SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 767
           SequenceNumberRange <SeqNbRg> [0..1]  767
             FirstTransaction <FrstTx> [0..1] Text 767
             LastTransaction <LastTx> [0..1] Text 767
           TransactionDateRange <TxDtRg> [0..1] ± 768
Or}         Individual <Indv> [1..1]  768
           ICCRelatedData <ICCRltdData> [0..1] Text 770
           PaymentContext <PmtCntxt> [0..1]  770
             CardPresent <CardPres> [0..1] Indicator 770
             CardholderPresent <CrdhldrPres> [0..1] Indicator 770
             OnLineContext <OnLineCntxt> [0..1] Indicator 771
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
623 March 2026
```

## File page 624

```text
Or MessageElement<XML Tag> Mult. Type Constr.
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
624 March 2026
```

