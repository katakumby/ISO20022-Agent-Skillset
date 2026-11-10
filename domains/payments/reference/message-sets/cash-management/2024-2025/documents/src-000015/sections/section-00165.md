---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.1 PaymentTo <PmtTo>"]
file_pages: [273]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.1 PaymentTo <PmtTo>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 273 to 273.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 273

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Identification <Id> [0..1] Text 322
       StatementIdentification <StmtId> [0..1] Text 322
       AccountServicerReference <AcctSvcrRef> [0..1] Quantity 322
       AdditionalEntryInformation <AddtlNtryInf> [0..*] Text 322
   SecuritiesTransactionReferences <SctiesTxRefs> [0..1]  322
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 323
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 323
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 323
     ProcessingIdentification <PrcgId> [0..1] Text 323
Constraints
• CreditDebitIndicatorGuideline
The CreditDebitIndicator may be omitted for optimisation reason if the CreditDebitIndicator is used in
the search criteria of the related query.
• TransactionCreditDebitIndicatorRule
If CreditDebitIndicator is present, then AccountEntry/Entry/Amount or Payment/InstructedAmount or
Payment/InterbankSettlementAmount must be present.
If CreditDebitIndicator is not present, then any Message Elements in the list (AccountEntry/Entry/
Amount, Payment/InstructedAmount, Payment/InterbankSettlementAmount) is optional.
On Condition
    /CreditDebitIndicator is present
Following Must be True
    /AccountEntry/Entry/Amount Must be present
 Or    /Payment/InstructedAmount Must be present
 Or    /Payment/InterbankSettlementAmount Must be present
5.4.2.1.3.2.1.1  PaymentTo <PmtTo>
Presence: [0..1]
Definition: Destination of the payment (be it a member or a system or both).
PaymentTo <PmtTo> contains the following System3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 274
   MemberIdentification <MmbId> [0..1] ± 274
   Country <Ctry> [0..1] CodeSet C5 274
   AccountIdentification <AcctId> [0..1] ± 275
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 273 February 2025
```

