---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.22 Purpose <Purp>"]
file_pages: [446, 447, 448, 449, 450, 451, 452, 453, 454]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.22 Purpose <Purp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 446 to 454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 446

```text
Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on
page 1173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  1174
     BICFI <BICFI> [0..1] IdentifierSet C5 1174
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
     LEI <LEI> [0..1] IdentifierSet 1175
     Name <Nm> [0..1] Text 1175
     PostalAddress <PstlAdr> [0..1] ± 1175
     Other <Othr> [0..1] ± 1176
   BranchIdentification <BrnchId> [0..1]  1177
     Identification <Id> [0..1] Text 1177
     LEI <LEI> [0..1] IdentifierSet 1177
     Name <Nm> [0..1] Text 1177
     PostalAddress <PstlAdr> [0..1] ± 1177
4.4.3.27.22  Purpose <Purp>
Presence: [0..1]
Definition: Underlying reason for the payment transaction.
Usage:
Purpose is used by the end customers, that is initiating party, (ultimate) debtor, (ultimate) creditor to
provide information concerning the nature of the payment. Purpose is a content element, which is not
used for processing by any of the agents involved in the payment chain.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 1191 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1191
Or}   Proprietary <Prtry> [1..1] Text 1191
4.4.3.27.23  UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>
Presence: [0..1]
Definition: Provides information on the underlying customer credit transfer for which cover is provided.
Impacted by: C28 "IntermediaryAgent1AccountRule", C32 "IntermediaryAgent2AccountRule", C34
"IntermediaryAgent2Rule", C37 "IntermediaryAgent3AccountRule", C39 "IntermediaryAgent3Rule", C45
"PreviousInstructingAgent1AccountRule", C50 "PreviousInstructingAgent2AccountRule", C52
"PreviousInstructingAgent2Rule", C55 "PreviousInstructingAgent3AccountRule", C57
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
446 March 2026
```

## File page 447

```text
"PreviousInstructingAgent3Rule", C47 "PreviousInstructingAgent1Guideline", C76
"UltimateCreditorGuideline", C78 "UltimateDebtorGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
447 March 2026
```

## File page 448

```text
UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf> contains the following
CreditTransferTransaction72 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentIdentification <PmtId> [0..1] ± C74 455
   PaymentTypeInformation <PmtTpInf> [0..1] ± 455
   UltimateDebtor <UltmtDbtr> [0..1] ± 456
   InitiatingParty <InitgPty> [0..1] ± 457
   Debtor <Dbtr> [1..1] ± 458
   DebtorAccount <DbtrAcct> [0..1] ± C22,
C21
459
   DebtorAgent <DbtrAgt> [1..1] ± 460
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C22,
C21
461
   PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 462
   PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C22,
C21
462
   PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 463
   PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C22,
C21
464
   PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 465
   PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C22,
C21
465
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 466
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C22,
C21
467
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 468
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C22,
C21
468
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 469
   IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C22,
C21
470
   CreditorAgent <CdtrAgt> [1..1] ± 471
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C22,
C21
471
   Creditor <Cdtr> [1..1] ± 472
   CreditorAccount <CdtrAcct> [0..1] ± C22,
C21
473
   UltimateCreditor <UltmtCdtr> [0..1] ± 474
   InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 475
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
448 March 2026
```

## File page 449

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionForNextAgent <InstrForNxtAgt> [0..*]  476
     Code <Cd> [0..1] CodeSet 476
     InstructionInformation <InstrInf> [0..1] Text 476
   Purpose <Purp> [0..1] ± 476
   Tax <Tax> [0..1]  477
     Creditor <Cdtr> [0..1] ± 479
     Debtor <Dbtr> [0..1] ± 479
     UltimateDebtor <UltmtDbtr> [0..1] ± 479
     AdministrationZone <AdmstnZone> [0..1] Text 480
     ReferenceNumber <RefNb> [0..1] Text 480
     Method <Mtd> [0..1] Text 480
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 480
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 481
     Date <Dt> [0..1] Date 481
     SequenceNumber <SeqNb> [0..1] Quantity 481
     Record <Rcrd> [0..*]  481
       Type <Tp> [0..1] Text 482
       Category <Ctgy> [0..1] Text 482
       CategoryDetails <CtgyDtls> [0..1] Text 482
       DebtorStatus <DbtrSts> [0..1] Text 483
       CertificateIdentification <CertId> [0..1] Text 483
       FormsCode <FrmsCd> [0..1] Text 483
       Period <Prd> [0..1]  483
         Year <Yr> [0..1] Year 483
         Type <Tp> [0..1] CodeSet 483
         FromToDate <FrToDt> [0..1] ± 484
       TaxAmount <TaxAmt> [0..1]  485
         Rate <Rate> [0..1] Rate 485
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 485
         TotalAmount <TtlAmt> [0..1] Amount C2, C12 485
         Details <Dtls> [0..*]  486
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
449 March 2026
```

## File page 450

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Period <Prd> [0..1]  486
             Year <Yr> [0..1] Year 486
             Type <Tp> [0..1] CodeSet 487
             FromToDate <FrToDt> [0..1] ± 487
           Amount <Amt> [1..1] Amount C2, C12 488
       AdditionalInformation <AddtlInf> [0..1] Text 488
   RemittanceInformation <RmtInf> [0..1]  488
     Unstructured <Ustrd> [0..*] Text 492
     Structured <Strd> [0..*]  492
       ReferredDocumentInformation <RfrdDocInf> [0..*]  496
         Type <Tp> [0..1]  498
           CodeOrProprietary <CdOrPrtry> [1..1]  498
{Or             Code <Cd> [1..1] CodeSet 498
Or}             Proprietary <Prtry> [1..1] Text 498
           Issuer <Issr> [0..1] Text 498
         Number <Nb> [0..1] Text 499
         RelatedDate <RltdDt> [0..1]  499
           Type <Tp> [1..1]  499
{Or             Code <Cd> [1..1] CodeSet 499
Or}             Proprietary <Prtry> [1..1] Text 499
           Date <Dt> [1..1] Date 499
         LineDetails <LineDtls> [0..*]  500
           Identification <Id> [1..*]  500
             Type <Tp> [0..1]  501
               CodeOrProprietary <CdOrPrtry> [1..1]  501
{Or                 Code <Cd> [1..1] CodeSet 501
Or}                 Proprietary <Prtry> [1..1] Text 501
               Issuer <Issr> [0..1] Text 502
             Number <Nb> [0..1] Text 502
             RelatedDate <RltdDt> [0..1] Date 502
           Description <Desc> [0..1] Text 502
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
450 March 2026
```

## File page 451

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Amount <Amt> [0..1]  C59 502
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  503
               Type <Tp> [1..1]  503
{Or                 Code <Cd> [1..1] CodeSet 504
Or}                 Proprietary <Prtry> [1..1] Text 504
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
{Or             Code <Cd> [1..1] CodeSet 507
Or}             Proprietary <Prtry> [1..1] Text 507
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
{Or             Code <Cd> [1..1] CodeSet 509
Or}             Proprietary <Prtry> [1..1] Text 509
           Issuer <Issr> [0..1] Text 510
         Reference <Ref> [0..1] Text 510
       Invoicer <Invcr> [0..1] ± 510
       Invoicee <Invcee> [0..1] ± 511
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
451 March 2026
```

## File page 452

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
                 Type <Tp> [0..1] CodeSet 522
                 FromToDate <FrToDt> [0..1] ± 522
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
452 March 2026
```

## File page 453

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               Amount <Amt> [1..1] Amount C2, C12 523
           AdditionalInformation <AddtlInf> [0..1] Text 523
       GarnishmentRemittance <GrnshmtRmt> [0..1]  523
         Type <Tp> [1..1]  524
           CodeOrProprietary <CdOrPrtry> [1..1]  524
{Or             Code <Cd> [1..1] CodeSet 525
Or}             Proprietary <Prtry> [1..1] Text 525
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
Constraints
• IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent1 is absent
Following Must be True
    /IntermediaryAgent1Account Must be absent
• IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent2 is absent
Following Must be True
    /IntermediaryAgent2Account Must be absent
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
453 March 2026
```

## File page 454

```text
• IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent2 is present
Following Must be True
    /IntermediaryAgent1 Must be present
• IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
On Condition
    /IntermediaryAgent3 is absent
Following Must be True
    /IntermediaryAgent3Account Must be absent
• IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent3 is present
Following Must be True
    /IntermediaryAgent2 Must be present
• PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be present.
On Condition
    /PreviousInstructingAgent1 is absent
Following Must be True
    /PreviousInstructingAgent1Account Must be absent
• PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the DebtorAgent
in the payment chain.
• PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be present.
On Condition
    /PreviousInstructingAgent2 is absent
Following Must be True
    /PreviousInstructingAgent2Account Must be absent
• PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
On Condition
    /PreviousInstructingAgent2 is present
Following Must be True
    /PreviousInstructingAgent1 Must be present
• PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be present.
On Condition
    /PreviousInstructingAgent3 is absent
Following Must be True
    /PreviousInstructingAgent3Account Must be absent
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
454 March 2026
```

