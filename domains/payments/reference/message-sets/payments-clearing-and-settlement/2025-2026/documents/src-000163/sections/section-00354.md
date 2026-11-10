---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.1 Unstructured <Ustrd>"]
file_pages: [492, 493, 494, 495]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.1 Unstructured <Ustrd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 492 to 495.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 492

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 525
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
4.4.3.27.23.30.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 1244
4.4.3.27.23.30.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
492 March 2026
```

## File page 493

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  496
     Type <Tp> [0..1]  498
       CodeOrProprietary <CdOrPrtry> [1..1]  498
{Or         Code <Cd> [1..1] CodeSet 498
Or}         Proprietary <Prtry> [1..1] Text 498
       Issuer <Issr> [0..1] Text 498
     Number <Nb> [0..1] Text 499
     RelatedDate <RltdDt> [0..1]  499
       Type <Tp> [1..1]  499
{Or         Code <Cd> [1..1] CodeSet 499
Or}         Proprietary <Prtry> [1..1] Text 499
       Date <Dt> [1..1] Date 499
     LineDetails <LineDtls> [0..*]  500
       Identification <Id> [1..*]  500
         Type <Tp> [0..1]  501
           CodeOrProprietary <CdOrPrtry> [1..1]  501
{Or             Code <Cd> [1..1] CodeSet 501
Or}             Proprietary <Prtry> [1..1] Text 501
           Issuer <Issr> [0..1] Text 502
         Number <Nb> [0..1] Text 502
         RelatedDate <RltdDt> [0..1] Date 502
       Description <Desc> [0..1] Text 502
       Amount <Amt> [0..1]  C59 502
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  503
           Type <Tp> [1..1]  503
{Or             Code <Cd> [1..1] CodeSet 504
Or}             Proprietary <Prtry> [1..1] Text 504
           Amount <Amt> [1..1] Amount C2, C12 504
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  504
           Amount <Amt> [1..1] Amount C2, C12 504
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
493 March 2026
```

## File page 494

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 505
           Reason <Rsn> [0..1] Text 505
           AdditionalInformation <AddtlInf> [0..1] Text 505
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C59 505
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  506
       Type <Tp> [1..1]  506
{Or         Code <Cd> [1..1] CodeSet 507
Or}         Proprietary <Prtry> [1..1] Text 507
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
{Or         Code <Cd> [1..1] CodeSet 509
Or}         Proprietary <Prtry> [1..1] Text 509
       Issuer <Issr> [0..1] Text 510
     Reference <Ref> [0..1] Text 510
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
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
494 March 2026
```

## File page 495

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
           Amount <Amt> [1..1] Amount C2, C12 523
       AdditionalInformation <AddtlInf> [0..1] Text 523
   GarnishmentRemittance <GrnshmtRmt> [0..1]  523
     Type <Tp> [1..1]  524
       CodeOrProprietary <CdOrPrtry> [1..1]  524
{Or         Code <Cd> [1..1] CodeSet 525
Or}         Proprietary <Prtry> [1..1] Text 525
       Issuer <Issr> [0..1] Text 525
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
495 March 2026
```

