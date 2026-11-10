---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.20 Tax <Tax>"]
file_pages: [473, 474]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.20 Tax <Tax>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 473 to 474.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 473

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 835
   OtherIdentification <OthrId> [0..*]  836
     Identification <Id> [1..1] Text 836
     Suffix <Sfx> [0..1] Text 836
     Type <Tp> [1..1] ± 836
   Description <Desc> [0..1] Text 836
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
3.4.2.15.18.2.20  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
473 March 2026
```

## File page 474

```text
Tax <Tax> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 475
   Debtor <Dbtr> [0..1] ± 475
   UltimateDebtor <UltmtDbtr> [0..1] ± 475
   AdministrationZone <AdmstnZone> [0..1] Text 476
   ReferenceNumber <RefNb> [0..1] Text 476
   Method <Mtd> [0..1] Text 476
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 476
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 477
   Date <Dt> [0..1] Date 477
   SequenceNumber <SeqNb> [0..1] Quantity 477
   Record <Rcrd> [0..*]  477
     Type <Tp> [0..1] Text 478
     Category <Ctgy> [0..1] Text 478
     CategoryDetails <CtgyDtls> [0..1] Text 478
     DebtorStatus <DbtrSts> [0..1] Text 479
     CertificateIdentification <CertId> [0..1] Text 479
     FormsCode <FrmsCd> [0..1] Text 479
     Period <Prd> [0..1]  479
       Year <Yr> [0..1] Year 479
       Type <Tp> [0..1] CodeSet 479
       FromToDate <FrToDt> [0..1] ± 480
     TaxAmount <TaxAmt> [0..1]  481
       Rate <Rate> [0..1] Rate 481
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 481
       TotalAmount <TtlAmt> [0..1] Amount C2, C6 481
       Details <Dtls> [0..*]  482
         Period <Prd> [0..1]  482
           Year <Yr> [0..1] Year 482
           Type <Tp> [0..1] CodeSet 483
           FromToDate <FrToDt> [0..1] ± 483
         Amount <Amt> [1..1] Amount C2, C6 484
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
474 March 2026
```

