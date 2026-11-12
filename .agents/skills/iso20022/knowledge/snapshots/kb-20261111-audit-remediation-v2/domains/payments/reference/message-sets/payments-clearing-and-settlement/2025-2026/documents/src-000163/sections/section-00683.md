---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.29 Tax <Tax>"]
file_pages: [930, 931]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.29 Tax <Tax>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 930 to 931.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 930

```text
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 1191 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1191
Or}   Proprietary <Prtry> [1..1] Text 1191
7.4.2.40.29  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
930 March 2026
```

## File page 931

```text
Tax <Tax> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 932
   Debtor <Dbtr> [0..1] ± 932
   UltimateDebtor <UltmtDbtr> [0..1] ± 932
   AdministrationZone <AdmstnZone> [0..1] Text 933
   ReferenceNumber <RefNb> [0..1] Text 933
   Method <Mtd> [0..1] Text 933
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 933
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C9 934
   Date <Dt> [0..1] Date 934
   SequenceNumber <SeqNb> [0..1] Quantity 934
   Record <Rcrd> [0..*]  934
     Type <Tp> [0..1] Text 935
     Category <Ctgy> [0..1] Text 935
     CategoryDetails <CtgyDtls> [0..1] Text 935
     DebtorStatus <DbtrSts> [0..1] Text 936
     CertificateIdentification <CertId> [0..1] Text 936
     FormsCode <FrmsCd> [0..1] Text 936
     Period <Prd> [0..1]  936
       Year <Yr> [0..1] Year 936
       Type <Tp> [0..1] CodeSet 936
       FromToDate <FrToDt> [0..1] ± 937
     TaxAmount <TaxAmt> [0..1]  938
       Rate <Rate> [0..1] Rate 938
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 938
       TotalAmount <TtlAmt> [0..1] Amount C2, C9 938
       Details <Dtls> [0..*]  939
         Period <Prd> [0..1]  939
           Year <Yr> [0..1] Year 939
           Type <Tp> [0..1] CodeSet 940
           FromToDate <FrToDt> [0..1] ± 940
         Amount <Amt> [1..1] Amount C2, C9 941
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
931 March 2026
```

