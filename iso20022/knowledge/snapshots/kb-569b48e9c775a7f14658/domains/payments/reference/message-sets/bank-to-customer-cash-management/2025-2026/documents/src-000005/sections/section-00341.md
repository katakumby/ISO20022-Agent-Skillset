---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>"]
file_pages: [493, 494, 495]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26 CardTransaction <CardTx>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 493 to 495.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 493

```text
3.4.2.15.18.2.26  CardTransaction <CardTx>
Presence: [0..1]
Definition: Provides the data related to the card (number, scheme), terminal (number, identification) and
transactional data used to uniquely identify a card transaction.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
493 March 2026
```

## File page 494

```text
CardTransaction <CardTx> contains the following CardTransaction18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Card <Card> [0..1]  496
     PlainCardData <PlainCardData> [0..1]  497
       PAN <PAN> [1..1] Text 498
       CardSequenceNumber <CardSeqNb> [0..1] Text 498
       EffectiveDate <FctvDt> [0..1] YearMonth 498
       ExpiryDate <XpryDt> [1..1] YearMonth 498
       ServiceCode <SvcCd> [0..1] Text 498
       TrackData <TrckData> [0..*]  499
         TrackNumber <TrckNb> [0..1] Text 499
         TrackValue <TrckVal> [1..1] Text 499
       CardSecurityCode <CardSctyCd> [0..1]  499
         CSCManagement <CSCMgmt> [1..1] CodeSet 499
         CSCValue <CSCVal> [0..1] Text 500
     CardCountryCode <CardCtryCd> [0..1] Text 500
     CardBrand <CardBrnd> [0..1] ± 500
     AdditionalCardData <AddtlCardData> [0..1] Text 500
   POI <POI> [0..1]  500
     Identification <Id> [1..1] ± 501
     SystemName <SysNm> [0..1] Text 502
     GroupIdentification <GrpId> [0..1] Text 502
     Capabilities <Cpblties> [0..1]  502
       CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 502
       CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 503
       OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 503
       DisplayCapabilities <DispCpblties> [0..*]  504
         DisplayType <DispTp> [1..1] CodeSet 504
         NumberOfLines <NbOfLines> [1..1] Text 504
         LineWidth <LineWidth> [1..1] Text 504
       PrintLineWidth <PrtLineWidth> [0..1] Text 504
     Component <Cmpnt> [0..*]  504
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
494 March 2026
```

## File page 495

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       POIComponentType <POICmpntTp> [1..1] CodeSet 505
       ManufacturerIdentification <ManfctrId> [0..1] Text 505
       Model <Mdl> [0..1] Text 505
       VersionNumber <VrsnNb> [0..1] Text 505
       SerialNumber <SrlNb> [0..1] Text 506
       ApprovalNumber <ApprvlNb> [0..*] Text 506
   Transaction <Tx> [0..1]  506
{Or     Aggregated <Aggtd> [1..1]  508
       AdditionalService <AddtlSvc> [0..1] CodeSet 508
       TransactionCategory <TxCtgy> [0..1] CodeSet 509
       SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 509
       SequenceNumberRange <SeqNbRg> [0..1]  509
         FirstTransaction <FrstTx> [0..1] Text 509
         LastTransaction <LastTx> [0..1] Text 509
       TransactionDateRange <TxDtRg> [0..1] ± 510
Or}     Individual <Indv> [1..1]  510
       ICCRelatedData <ICCRltdData> [0..1] Text 512
       PaymentContext <PmtCntxt> [0..1]  512
         CardPresent <CardPres> [0..1] Indicator 512
         CardholderPresent <CrdhldrPres> [0..1] Indicator 512
         OnLineContext <OnLineCntxt> [0..1] Indicator 513
         AttendanceContext <AttndncCntxt> [0..1] CodeSet 513
         TransactionEnvironment <TxEnvt> [0..1] CodeSet 513
         TransactionChannel <TxChanl> [0..1] CodeSet 513
         AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 514
         AttendantLanguage <AttndntLang> [0..1] CodeSet 514
         CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 514
         FallbackIndicator <FllbckInd> [0..1] Indicator 514
         AuthenticationMethod <AuthntcnMtd> [0..1]  515
           AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 515
           AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 515
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
495 March 2026
```

