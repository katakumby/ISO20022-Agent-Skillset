---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.20 Tax <Tax>"]
file_pages: [731, 732]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.20 Tax <Tax>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 731 to 732.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 731

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
4.4.2.14.18.2.20  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
731 March 2026
```

## File page 732

```text
Tax <Tax> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 733
   Debtor <Dbtr> [0..1] ± 733
   UltimateDebtor <UltmtDbtr> [0..1] ± 733
   AdministrationZone <AdmstnZone> [0..1] Text 734
   ReferenceNumber <RefNb> [0..1] Text 734
   Method <Mtd> [0..1] Text 734
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 734
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 735
   Date <Dt> [0..1] Date 735
   SequenceNumber <SeqNb> [0..1] Quantity 735
   Record <Rcrd> [0..*]  735
     Type <Tp> [0..1] Text 736
     Category <Ctgy> [0..1] Text 736
     CategoryDetails <CtgyDtls> [0..1] Text 736
     DebtorStatus <DbtrSts> [0..1] Text 737
     CertificateIdentification <CertId> [0..1] Text 737
     FormsCode <FrmsCd> [0..1] Text 737
     Period <Prd> [0..1]  737
       Year <Yr> [0..1] Year 737
       Type <Tp> [0..1] CodeSet 737
       FromToDate <FrToDt> [0..1] ± 738
     TaxAmount <TaxAmt> [0..1]  739
       Rate <Rate> [0..1] Rate 739
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 739
       TotalAmount <TtlAmt> [0..1] Amount C2, C6 739
       Details <Dtls> [0..*]  740
         Period <Prd> [0..1]  740
           Year <Yr> [0..1] Year 740
           Type <Tp> [0..1] CodeSet 741
           FromToDate <FrToDt> [0..1] ± 741
         Amount <Amt> [1..1] Amount C2, C6 742
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
732 March 2026
```

