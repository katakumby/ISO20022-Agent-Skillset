---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.6 TaxRemittance <TaxRmt>", "5.4.3.21.11.2.6.11 Record <Rcrd>", "5.4.3.21.11.2.6.11.4 DebtorStatus <DbtrSts>"]
file_pages: [675]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.6.11.4 DebtorStatus <DbtrSts>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 675 to 675.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 675

```text
Definition: Provides further details of the category tax code.
Datatype: "Max35Text" on page 1246
5.4.3.21.11.2.6.11.4  DebtorStatus <DbtrSts>
Presence: [0..1]
Definition: Code provided by local authority to identify the status of the party that has drawn up the
settlement document.
Datatype: "Max35Text" on page 1246
5.4.3.21.11.2.6.11.5  CertificateIdentification <CertId>
Presence: [0..1]
Definition: Identification number of the tax report as assigned by the taxing authority.
Datatype: "Max35Text" on page 1246
5.4.3.21.11.2.6.11.6  FormsCode <FrmsCd>
Presence: [0..1]
Definition: Identifies, in a coded form, on which template the tax report is to be provided.
Datatype: "Max35Text" on page 1246
5.4.3.21.11.2.6.11.7  Period <Prd>
Presence: [0..1]
Definition: Set of elements used to provide details on the period of time related to the tax payment.
Period <Prd> contains the following TaxPeriod3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Year <Yr> [0..1] Year 675
   Type <Tp> [0..1] CodeSet 675
   FromToDate <FrToDt> [0..1] ± 676
5.4.3.21.11.2.6.11.7.1  Year <Yr>
Presence: [0..1]
Definition: Year related to the tax payment.
Datatype: "ISOYear" on page 1247
5.4.3.21.11.2.6.11.7.2  Type <Tp>
Presence: [0..1]
Definition: Identification of the period related to the tax payment.
Datatype: "TaxRecordPeriod1Code" on page 1238
CodeName Name Definition
MM01 FirstMonth Tax is related to the second month of the
period.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
675 March 2026
```

