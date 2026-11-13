---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.29 Tax <Tax>"]
file_pages: [477, 478]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.29 Tax <Tax>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 477 to 478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 477

```text
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 1191 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1191
Or}   Proprietary <Prtry> [1..1] Text 1191
4.4.3.27.23.29  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
477 March 2026
```

## File page 478

```text
Tax <Tax> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         Period <Prd> [0..1]  486
           Year <Yr> [0..1] Year 486
           Type <Tp> [0..1] CodeSet 487
           FromToDate <FrToDt> [0..1] ± 487
         Amount <Amt> [1..1] Amount C2, C12 488
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
478 March 2026
```

