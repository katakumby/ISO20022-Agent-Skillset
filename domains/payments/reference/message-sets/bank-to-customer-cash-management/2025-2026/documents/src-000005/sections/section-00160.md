---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.1 Card <Card>"]
file_pages: [236]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.1 Card <Card>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 236 to 236.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 236

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AdditionalService <AddtlSvc> [0..1] CodeSet 256
       TransactionCategory <TxCtgy> [0..1] CodeSet 256
       SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 256
       SaleReferenceNumber <SaleRefNb> [0..1] Text 257
       RePresentmentReason <RePresntmntRsn> [0..1] CodeSet 257
       SequenceNumber <SeqNb> [0..1] Text 257
       TransactionIdentification <TxId> [0..1] ± 257
       Product <Pdct> [0..1]  257
         ProductCode <PdctCd> [1..1] Text 258
         UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 258
         ProductQuantity <PdctQty> [0..1] Quantity 259
         UnitPrice <UnitPric> [0..1] Amount 259
         ProductAmount <PdctAmt> [0..1] Amount 259
         TaxType <TaxTp> [0..1] Text 260
         AdditionalProductInformation <AddtlPdctInf> [0..1] Text 260
       ValidationDate <VldtnDt> [0..1] Date 260
       ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 260
   PrePaidAccount <PrePdAcct> [0..1] ± C20,
C18
260
2.4.2.15.18.2.26.1  Card <Card>
Presence: [0..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
236 March 2026
```

