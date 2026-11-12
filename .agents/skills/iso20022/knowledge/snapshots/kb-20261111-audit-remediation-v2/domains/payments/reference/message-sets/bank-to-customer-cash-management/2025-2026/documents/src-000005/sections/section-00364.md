---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.3 Transaction <Tx>", "3.4.2.15.18.2.26.3.2 Individual <Indv>", "3.4.2.15.18.2.26.3.2.10 Product <Pdct>", "3.4.2.15.18.2.26.3.2.10.6 TaxType <TaxTp>"]
file_pages: [520]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.3.2.10.6 TaxType <TaxTp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 520 to 520.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 520

```text
Definition: Monetary value of purchased product.
Datatype: "ImpliedCurrencyAndAmount" on page 886
3.4.2.15.18.2.26.3.2.10.6  TaxType <TaxTp>
Presence: [0..1]
Definition: Information on tax paid on the product.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.26.3.2.10.7  AdditionalProductInformation <AddtlPdctInf>
Presence: [0..1]
Definition: Additional information related to the product.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.26.3.2.11  ValidationDate <VldtnDt>
Presence: [0..1]
Definition: Date when the deposit was validated by the financial institution that collected the cash.
Datatype: "ISODate" on page 908
3.4.2.15.18.2.26.3.2.12  ValidationSequenceNumber <VldtnSeqNb>
Presence: [0..1]
Definition: Sequential number of the validation of the cash deposit.
Usage: The sequential number is increased incrementally for each transaction.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.26.4  PrePaidAccount <PrePdAcct>
Presence: [0..1]
Definition: Prepaid account for the transfer or loading of an amount of money.
Impacted by: C20 "IdentificationOrProxyPresenceRule", C18 "IdentificationAndProxyGuideline"
PrePaidAccount <PrePdAcct> contains the following elements (see "CashAccount40" on page 796
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 796
   Type <Tp> [0..1] ± 796
   Currency <Ccy> [0..1] CodeSet C1 797
   Name <Nm> [0..1] Text 797
   Proxy <Prxy> [0..1] ± 797
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
520 March 2026
```

