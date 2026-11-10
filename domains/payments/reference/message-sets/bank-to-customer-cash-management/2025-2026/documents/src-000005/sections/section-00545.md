---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.3 Transaction <Tx>", "4.4.2.14.18.2.26.3.2 Individual <Indv>", "4.4.2.14.18.2.26.3.2.10 Product <Pdct>", "4.4.2.14.18.2.26.3.2.10.6 TaxType <TaxTp>"]
file_pages: [778]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.3.2.10.6 TaxType <TaxTp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 778 to 778.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 778

```text
Definition: Monetary value of purchased product.
Datatype: "ImpliedCurrencyAndAmount" on page 886
4.4.2.14.18.2.26.3.2.10.6  TaxType <TaxTp>
Presence: [0..1]
Definition: Information on tax paid on the product.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.26.3.2.10.7  AdditionalProductInformation <AddtlPdctInf>
Presence: [0..1]
Definition: Additional information related to the product.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.26.3.2.11  ValidationDate <VldtnDt>
Presence: [0..1]
Definition: Date when the deposit was validated by the financial institution that collected the cash.
Datatype: "ISODate" on page 908
4.4.2.14.18.2.26.3.2.12  ValidationSequenceNumber <VldtnSeqNb>
Presence: [0..1]
Definition: Sequential number of the validation of the cash deposit.
Usage: The sequential number is increased incrementally for each transaction.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.26.4  PrePaidAccount <PrePdAcct>
Presence: [0..1]
Definition: Prepaid account for the transfer or loading of an amount of money.
Impacted by: C19 "IdentificationOrProxyPresenceRule", C17 "IdentificationAndProxyGuideline"
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
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
778 March 2026
```

