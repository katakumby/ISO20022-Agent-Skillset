---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [360, 361, 362, 363]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# Continuation at file page 360

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 360 to 363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 360

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               RelatedDate <RltdDt> [0..1] Date 502
             Description <Desc> [0..1] Text 502
             Amount <Amt> [0..1]  C59 502
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  503
                 Type <Tp> [1..1]  503
{Or                   Code <Cd> [1..1] CodeSet 504
Or}                   Proprietary <Prtry> [1..1] Text 504
                 Amount <Amt> [1..1] Amount C2, C12 504
               AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  504
                 Amount <Amt> [1..1] Amount C2, C12 504
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 505
                 Reason <Rsn> [0..1] Text 505
                 AdditionalInformation <AddtlInf> [0..1] Text 505
         ReferredDocumentAmount <RfrdDocAmt> [0..1]  C59 505
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  506
             Type <Tp> [1..1]  506
{Or               Code <Cd> [1..1] CodeSet 507
Or}               Proprietary <Prtry> [1..1] Text 507
             Amount <Amt> [1..1] Amount C2, C12 507
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  507
             Amount <Amt> [1..1] Amount C2, C12 507
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 508
             Reason <Rsn> [0..1] Text 508
             AdditionalInformation <AddtlInf> [0..1] Text 508
         CreditorReferenceInformation <CdtrRefInf> [0..1]  508
           Type <Tp> [0..1]  509
             CodeOrProprietary <CdOrPrtry> [1..1]  509
{Or               Code <Cd> [1..1] CodeSet 509
Or}               Proprietary <Prtry> [1..1] Text 509
             Issuer <Issr> [0..1] Text 510
           Reference <Ref> [0..1] Text 510
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
360 March 2026
```

## File page 361

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Invoicer <Invcr> [0..1] ± 510
         Invoicee <Invcee> [0..1] ± 511
         TaxRemittance <TaxRmt> [0..1]  512
           Creditor <Cdtr> [0..1] ± 514
           Debtor <Dbtr> [0..1] ± 514
           UltimateDebtor <UltmtDbtr> [0..1] ± 514
           AdministrationZone <AdmstnZone> [0..1] Text 515
           ReferenceNumber <RefNb> [0..1] Text 515
           Method <Mtd> [0..1] Text 515
           TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 515
           TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 516
           Date <Dt> [0..1] Date 516
           SequenceNumber <SeqNb> [0..1] Quantity 516
           Record <Rcrd> [0..*]  516
             Type <Tp> [0..1] Text 517
             Category <Ctgy> [0..1] Text 517
             CategoryDetails <CtgyDtls> [0..1] Text 517
             DebtorStatus <DbtrSts> [0..1] Text 518
             CertificateIdentification <CertId> [0..1] Text 518
             FormsCode <FrmsCd> [0..1] Text 518
             Period <Prd> [0..1]  518
               Year <Yr> [0..1] Year 518
               Type <Tp> [0..1] CodeSet 518
               FromToDate <FrToDt> [0..1] ± 519
             TaxAmount <TaxAmt> [0..1]  520
               Rate <Rate> [0..1] Rate 520
               TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 520
               TotalAmount <TtlAmt> [0..1] Amount C2, C12 520
               Details <Dtls> [0..*]  521
                 Period <Prd> [0..1]  521
                   Year <Yr> [0..1] Year 521
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
361 March 2026
```

## File page 362

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
                   Type <Tp> [0..1] CodeSet 522
                   FromToDate <FrToDt> [0..1] ± 522
                 Amount <Amt> [1..1] Amount C2, C12 523
             AdditionalInformation <AddtlInf> [0..1] Text 523
         GarnishmentRemittance <GrnshmtRmt> [0..1]  523
           Type <Tp> [1..1]  524
             CodeOrProprietary <CdOrPrtry> [1..1]  524
{Or               Code <Cd> [1..1] CodeSet 525
Or}               Proprietary <Prtry> [1..1] Text 525
             Issuer <Issr> [0..1] Text 525
           Garnishee <Grnshee> [0..1] ± 525
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 526
           ReferenceNumber <RefNb> [0..1] Text 527
           Date <Dt> [0..1] Date 528
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 528
           FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 528
           EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 528
         SecuritiesData <SctiesData> [0..*]  528
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 529
           Amount <Amt> [0..1] Amount C1, C11 529
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 529
     InstructedAmount <InstdAmt> [0..1] Amount C2, C12 529
   UnderlyingFinancialInstitutionCreditTransfer
<UndrlygFICdtTrf>
[0..1]  C10,
C13,
C29,
C30,
C33,
C35,
C38,
C40,
C46,
C51,
C53,
C56,
C58,
C48,
C77,
C79
530
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
362 March 2026
```

## File page 363

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PaymentIdentification <PmtId> [1..1] ± C74 534
     PaymentTypeInformation <PmtTpInf> [0..1] ± 535
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C11 535
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 536
     SettlementPriority <SttlmPrty> [0..1] CodeSet 536
     SettlementTimeIndication <SttlmTmIndctn> [0..1]  536
       DebitDateTime <DbtDtTm> [0..1] DateTime 536
       CreditDateTime <CdtDtTm> [0..1] DateTime 537
     SettlementTimeRequest <SttlmTmReq> [0..1] ± 537
     ExpiryDateTime <XpryDtTm> [0..1] DateTime 537
     PaymentSignature <PmtSgntr> [0..1]  537
{Or       ILPV4 <ILPV4> [1..1] Text 537
Or}       Signature <Sgntr> [1..1] Text 538
     PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 538
     PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C22,
C21
538
     PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 539
     PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C22,
C21
540
     PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 541
     PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C22,
C21
541
     InstructingAgent <InstgAgt> [0..1] ± 542
     InstructedAgent <InstdAgt> [0..1] ± 543
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 544
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C22,
C21
545
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 546
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C22,
C21
546
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 547
     IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C22,
C21
548
     UltimateDebtor <UltmtDbtr> [0..1] ± 549
     Debtor <Dbtr> [1..1] ± 549
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
363 March 2026
```

