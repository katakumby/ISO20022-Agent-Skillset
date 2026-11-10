---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.8 ReversalReasonInformation <RvslRsnInf>", "4.4.3.8.8.2 Reason <Rsn>", "4.4.3.8.8.2.1 Code <Cd>"]
file_pages: [313, 314, 315, 316, 317, 318]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.8.2.1 Code <Cd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 313 to 318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 313

```text
Reason <Rsn> contains one of the following ReversalReason4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 313
Or}   Proprietary <Prtry> [1..1] Text 313
4.4.3.8.8.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the reversal, as published in an external reason code list.
Datatype: "ExternalReversalReason1Code" on page 597
4.4.3.8.8.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the reversal, in a proprietary form.
Datatype: "Max35Text" on page 609
4.4.3.8.8.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the reversal reason.
Datatype: "Max105Text" on page 607
4.4.3.8.9  OriginalTransactionReference <OrgnlTxRef>
Presence: [0..1]
Definition: Key elements used to identify the original transaction that is being referred to.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 313 March 2026
```

## File page 314

```text
OriginalTransactionReference <OrgnlTxRef> contains the following
OriginalTransactionReference47 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] Amount C2, C9 319
   Amount <Amt> [0..1] ± 320
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 320
   RequestedCollectionDate <ReqdColltnDt> [0..1] Date 320
   RequestedExecutionDate <ReqdExctnDt> [0..1] ± 320
   CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 321
   SettlementInformation <SttlmInf> [0..1]  C19,
C20,
C25,
C26,
C27,
C28,
C31,
C32
322
     SettlementMethod <SttlmMtd> [1..1] CodeSet 324
     SettlementAccount <SttlmAcct> [0..1] ± C18,
C17
325
     ClearingSystem <ClrSys> [0..1]  325
{Or       Code <Cd> [1..1] CodeSet 326
Or}       Proprietary <Prtry> [1..1] Text 326
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 326
     InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C18,
C17
327
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 327
     InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C18,
C17
328
     ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 329
     ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C18,
C17
329
   PaymentTypeInformation <PmtTpInf> [0..1] ± 330
   PaymentMethod <PmtMtd> [0..1] CodeSet 331
   MandateRelatedInformation <MndtRltdInf> [0..1]  331
{Or     DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 333
       MandateIdentification <MndtId> [0..1] Text 335
       DateOfSignature <DtOfSgntr> [0..1] Date 335
       AmendmentIndicator <AmdmntInd> [0..1] Indicator 335
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 314 March 2026
```

## File page 315

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AmendmentInformationDetails <AmdmntInfDtls> [0..1]  335
         OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 336
         OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 336
         OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 337
         OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C18,
C17
338
         OriginalDebtor <OrgnlDbtr> [0..1] ± 339
         OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C18,
C17
340
         OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 341
         OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C18,
C17
342
         OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 343
         OriginalFrequency <OrgnlFrqcy> [0..1] ± 343
         OriginalReason <OrgnlRsn> [0..1]  343
{Or           Code <Cd> [1..1] CodeSet 343
Or}           Proprietary <Prtry> [1..1] Text 343
         OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 344
       ElectronicSignature <ElctrncSgntr> [0..1] Text 344
       FirstCollectionDate <FrstColltnDt> [0..1] Date 344
       FinalCollectionDate <FnlColltnDt> [0..1] Date 344
       Frequency <Frqcy> [0..1] ± 344
       Reason <Rsn> [0..1]  344
{Or         Code <Cd> [1..1] CodeSet 345
Or}         Proprietary <Prtry> [1..1] Text 345
       TrackingDays <TrckgDays> [0..1] Text 345
Or}     CreditTransferMandate <CdtTrfMndt> [1..1] ± 345
   RemittanceInformation <RmtInf> [0..1]  346
     Unstructured <Ustrd> [0..*] Text 350
     Structured <Strd> [0..*]  350
       ReferredDocumentInformation <RfrdDocInf> [0..*]  354
         Type <Tp> [0..1]  356
           CodeOrProprietary <CdOrPrtry> [1..1]  356
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 315 March 2026
```

## File page 316

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 356
Or}             Proprietary <Prtry> [1..1] Text 356
           Issuer <Issr> [0..1] Text 356
         Number <Nb> [0..1] Text 357
         RelatedDate <RltdDt> [0..1]  357
           Type <Tp> [1..1]  357
{Or             Code <Cd> [1..1] CodeSet 357
Or}             Proprietary <Prtry> [1..1] Text 357
           Date <Dt> [1..1] Date 357
         LineDetails <LineDtls> [0..*]  358
           Identification <Id> [1..*]  358
             Type <Tp> [0..1]  359
               CodeOrProprietary <CdOrPrtry> [1..1]  359
{Or                 Code <Cd> [1..1] CodeSet 359
Or}                 Proprietary <Prtry> [1..1] Text 359
               Issuer <Issr> [0..1] Text 360
             Number <Nb> [0..1] Text 360
             RelatedDate <RltdDt> [0..1] Date 360
           Description <Desc> [0..1] Text 360
           Amount <Amt> [0..1]  C24 360
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  361
               Type <Tp> [1..1]  361
{Or                 Code <Cd> [1..1] CodeSet 362
Or}                 Proprietary <Prtry> [1..1] Text 362
               Amount <Amt> [1..1] Amount C2, C9 362
             AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  362
               Amount <Amt> [1..1] Amount C2, C9 362
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 363
               Reason <Rsn> [0..1] Text 363
               AdditionalInformation <AddtlInf> [0..1] Text 363
       ReferredDocumentAmount <RfrdDocAmt> [0..1]  C24 363
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 316 March 2026
```

## File page 317

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  364
           Type <Tp> [1..1]  364
{Or             Code <Cd> [1..1] CodeSet 365
Or}             Proprietary <Prtry> [1..1] Text 365
           Amount <Amt> [1..1] Amount C2, C9 365
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  365
           Amount <Amt> [1..1] Amount C2, C9 365
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 366
           Reason <Rsn> [0..1] Text 366
           AdditionalInformation <AddtlInf> [0..1] Text 366
       CreditorReferenceInformation <CdtrRefInf> [0..1]  366
         Type <Tp> [0..1]  367
           CodeOrProprietary <CdOrPrtry> [1..1]  367
{Or             Code <Cd> [1..1] CodeSet 367
Or}             Proprietary <Prtry> [1..1] Text 367
           Issuer <Issr> [0..1] Text 368
         Reference <Ref> [0..1] Text 368
       Invoicer <Invcr> [0..1] ± 368
       Invoicee <Invcee> [0..1] ± 369
       TaxRemittance <TaxRmt> [0..1]  370
         Creditor <Cdtr> [0..1] ± 372
         Debtor <Dbtr> [0..1] ± 372
         UltimateDebtor <UltmtDbtr> [0..1] ± 372
         AdministrationZone <AdmstnZone> [0..1] Text 373
         ReferenceNumber <RefNb> [0..1] Text 373
         Method <Mtd> [0..1] Text 373
         TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 373
         TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C9 374
         Date <Dt> [0..1] Date 374
         SequenceNumber <SeqNb> [0..1] Quantity 374
         Record <Rcrd> [0..*]  374
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 317 March 2026
```

## File page 318

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Type <Tp> [0..1] Text 375
           Category <Ctgy> [0..1] Text 375
           CategoryDetails <CtgyDtls> [0..1] Text 375
           DebtorStatus <DbtrSts> [0..1] Text 376
           CertificateIdentification <CertId> [0..1] Text 376
           FormsCode <FrmsCd> [0..1] Text 376
           Period <Prd> [0..1]  376
             Year <Yr> [0..1] Year 376
             Type <Tp> [0..1] CodeSet 376
             FromToDate <FrToDt> [0..1] ± 377
           TaxAmount <TaxAmt> [0..1]  378
             Rate <Rate> [0..1] Rate 378
             TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 378
             TotalAmount <TtlAmt> [0..1] Amount C2, C9 378
             Details <Dtls> [0..*]  379
               Period <Prd> [0..1]  379
                 Year <Yr> [0..1] Year 379
                 Type <Tp> [0..1] CodeSet 380
                 FromToDate <FrToDt> [0..1] ± 380
               Amount <Amt> [1..1] Amount C2, C9 381
           AdditionalInformation <AddtlInf> [0..1] Text 381
       GarnishmentRemittance <GrnshmtRmt> [0..1]  381
         Type <Tp> [1..1]  382
           CodeOrProprietary <CdOrPrtry> [1..1]  382
{Or             Code <Cd> [1..1] CodeSet 383
Or}             Proprietary <Prtry> [1..1] Text 383
           Issuer <Issr> [0..1] Text 383
         Garnishee <Grnshee> [0..1] ± 383
         GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 384
         ReferenceNumber <RefNb> [0..1] Text 385
         Date <Dt> [0..1] Date 386
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 318 March 2026
```

