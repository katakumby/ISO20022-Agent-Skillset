---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>"]
file_pages: [233, 234, 235]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26 CardTransaction <CardTx>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 233 to 235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 233

```text
2.4.2.15.18.2.26  CardTransaction <CardTx>
Presence: [0..1]
Definition: Provides the data related to the card (number, scheme), terminal (number, identification) and
transactional data used to uniquely identify a card transaction.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
233 March 2026
```

## File page 234

```text
CardTransaction <CardTx> contains the following CardTransaction18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Card <Card> [0..1]  236
     PlainCardData <PlainCardData> [0..1]  237
       PAN <PAN> [1..1] Text 238
       CardSequenceNumber <CardSeqNb> [0..1] Text 238
       EffectiveDate <FctvDt> [0..1] YearMonth 238
       ExpiryDate <XpryDt> [1..1] YearMonth 238
       ServiceCode <SvcCd> [0..1] Text 238
       TrackData <TrckData> [0..*]  239
         TrackNumber <TrckNb> [0..1] Text 239
         TrackValue <TrckVal> [1..1] Text 239
       CardSecurityCode <CardSctyCd> [0..1]  239
         CSCManagement <CSCMgmt> [1..1] CodeSet 239
         CSCValue <CSCVal> [0..1] Text 240
     CardCountryCode <CardCtryCd> [0..1] Text 240
     CardBrand <CardBrnd> [0..1] ± 240
     AdditionalCardData <AddtlCardData> [0..1] Text 240
   POI <POI> [0..1]  240
     Identification <Id> [1..1] ± 241
     SystemName <SysNm> [0..1] Text 242
     GroupIdentification <GrpId> [0..1] Text 242
     Capabilities <Cpblties> [0..1]  242
       CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 242
       CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 243
       OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 243
       DisplayCapabilities <DispCpblties> [0..*]  244
         DisplayType <DispTp> [1..1] CodeSet 244
         NumberOfLines <NbOfLines> [1..1] Text 244
         LineWidth <LineWidth> [1..1] Text 244
       PrintLineWidth <PrtLineWidth> [0..1] Text 244
     Component <Cmpnt> [0..*]  244
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
234 March 2026
```

## File page 235

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       POIComponentType <POICmpntTp> [1..1] CodeSet 245
       ManufacturerIdentification <ManfctrId> [0..1] Text 245
       Model <Mdl> [0..1] Text 245
       VersionNumber <VrsnNb> [0..1] Text 245
       SerialNumber <SrlNb> [0..1] Text 246
       ApprovalNumber <ApprvlNb> [0..*] Text 246
   Transaction <Tx> [0..1]  246
{Or     Aggregated <Aggtd> [1..1]  248
       AdditionalService <AddtlSvc> [0..1] CodeSet 248
       TransactionCategory <TxCtgy> [0..1] CodeSet 249
       SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 249
       SequenceNumberRange <SeqNbRg> [0..1]  249
         FirstTransaction <FrstTx> [0..1] Text 249
         LastTransaction <LastTx> [0..1] Text 249
       TransactionDateRange <TxDtRg> [0..1] ± 250
Or}     Individual <Indv> [1..1]  250
       ICCRelatedData <ICCRltdData> [0..1] Text 252
       PaymentContext <PmtCntxt> [0..1]  252
         CardPresent <CardPres> [0..1] Indicator 252
         CardholderPresent <CrdhldrPres> [0..1] Indicator 252
         OnLineContext <OnLineCntxt> [0..1] Indicator 253
         AttendanceContext <AttndncCntxt> [0..1] CodeSet 253
         TransactionEnvironment <TxEnvt> [0..1] CodeSet 253
         TransactionChannel <TxChanl> [0..1] CodeSet 253
         AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 254
         AttendantLanguage <AttndntLang> [0..1] CodeSet 254
         CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 254
         FallbackIndicator <FllbckInd> [0..1] Indicator 254
         AuthenticationMethod <AuthntcnMtd> [0..1]  255
           AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 255
           AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 255
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
235 March 2026
```

