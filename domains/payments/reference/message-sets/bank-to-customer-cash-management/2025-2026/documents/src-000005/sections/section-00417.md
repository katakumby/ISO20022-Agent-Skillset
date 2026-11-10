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
file_pages: [636, 637]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# Continuation at file page 636

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 636 to 637.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 636

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
       Capabilities <Cpblties> [0..1]  760
         CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 760
         CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 761
         OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 761
         DisplayCapabilities <DispCpblties> [0..*]  762
           DisplayType <DispTp> [1..1] CodeSet 762
           NumberOfLines <NbOfLines> [1..1] Text 762
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
636 March 2026
```

## File page 637

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       Aggregated <Aggtd> [1..1]  766
         AdditionalService <AddtlSvc> [0..1] CodeSet 766
         TransactionCategory <TxCtgy> [0..1] CodeSet 767
         SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 767
         SequenceNumberRange <SeqNbRg> [0..1]  767
           FirstTransaction <FrstTx> [0..1] Text 767
           LastTransaction <LastTx> [0..1] Text 767
         TransactionDateRange <TxDtRg> [0..1] ± 768
Or}       Individual <Indv> [1..1]  768
         ICCRelatedData <ICCRltdData> [0..1] Text 770
         PaymentContext <PmtCntxt> [0..1]  770
           CardPresent <CardPres> [0..1] Indicator 770
           CardholderPresent <CrdhldrPres> [0..1] Indicator 770
           OnLineContext <OnLineCntxt> [0..1] Indicator 771
           AttendanceContext <AttndncCntxt> [0..1] CodeSet 771
           TransactionEnvironment <TxEnvt> [0..1] CodeSet 771
           TransactionChannel <TxChanl> [0..1] CodeSet 771
           AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 772
           AttendantLanguage <AttndntLang> [0..1] CodeSet 772
           CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 772
           FallbackIndicator <FllbckInd> [0..1] Indicator 772
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
637 March 2026
```

