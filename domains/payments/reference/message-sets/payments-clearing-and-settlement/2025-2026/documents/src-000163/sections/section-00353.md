---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.29 Tax <Tax>", "4.4.3.27.23.29.11 Record <Rcrd>", "4.4.3.27.23.29.11.8 TaxAmount <TaxAmt>", "4.4.3.27.23.29.11.8.4 Details <Dtls>", "4.4.3.27.23.29.11.8.4.2 Amount <Amt>"]
file_pages: [488, 489, 490, 491]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.29.11.8.4.2 Amount <Amt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 488 to 491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 488

```text
Definition: Range of time between a start date and an end date for which the tax report is provided.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 1168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 1168
   ToDate <ToDt> [1..1] Date 1168
4.4.3.27.23.29.11.8.4.2  Amount <Amt>
Presence: [1..1]
Definition: Underlying tax amount related to the specified period.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.4.3.27.23.29.11.9  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details of the tax record.
Datatype: "Max140Text" on page 1244
4.4.3.27.23.30  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
488 March 2026
```

## File page 489

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 492
   Structured <Strd> [0..*]  492
     ReferredDocumentInformation <RfrdDocInf> [0..*]  496
       Type <Tp> [0..1]  498
         CodeOrProprietary <CdOrPrtry> [1..1]  498
{Or           Code <Cd> [1..1] CodeSet 498
Or}           Proprietary <Prtry> [1..1] Text 498
         Issuer <Issr> [0..1] Text 498
       Number <Nb> [0..1] Text 499
       RelatedDate <RltdDt> [0..1]  499
         Type <Tp> [1..1]  499
{Or           Code <Cd> [1..1] CodeSet 499
Or}           Proprietary <Prtry> [1..1] Text 499
         Date <Dt> [1..1] Date 499
       LineDetails <LineDtls> [0..*]  500
         Identification <Id> [1..*]  500
           Type <Tp> [0..1]  501
             CodeOrProprietary <CdOrPrtry> [1..1]  501
{Or               Code <Cd> [1..1] CodeSet 501
Or}               Proprietary <Prtry> [1..1] Text 501
             Issuer <Issr> [0..1] Text 502
           Number <Nb> [0..1] Text 502
           RelatedDate <RltdDt> [0..1] Date 502
         Description <Desc> [0..1] Text 502
         Amount <Amt> [0..1]  C59 502
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  503
             Type <Tp> [1..1]  503
{Or               Code <Cd> [1..1] CodeSet 504
Or}               Proprietary <Prtry> [1..1] Text 504
             Amount <Amt> [1..1] Amount C2, C12 504
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
489 March 2026
```

## File page 490

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or           Code <Cd> [1..1] CodeSet 507
Or}           Proprietary <Prtry> [1..1] Text 507
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
{Or           Code <Cd> [1..1] CodeSet 509
Or}           Proprietary <Prtry> [1..1] Text 509
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
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
490 March 2026
```

## File page 491

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
             Amount <Amt> [1..1] Amount C2, C12 523
         AdditionalInformation <AddtlInf> [0..1] Text 523
     GarnishmentRemittance <GrnshmtRmt> [0..1]  523
       Type <Tp> [1..1]  524
         CodeOrProprietary <CdOrPrtry> [1..1]  524
{Or           Code <Cd> [1..1] CodeSet 525
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
491 March 2026
```

