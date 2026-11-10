---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.1 ReferredDocumentInformation <RfrdDocInf>", "2.4.2.19.26.2.1.4 LineDetails <LineDtls>", "2.4.2.19.26.2.1.4.3 Amount <Amt>", "2.4.2.19.26.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>", "2.4.2.19.26.2.1.4.3.1.1 Type <Tp>", "2.4.2.19.26.2.1.4.3.1.1.1 Code <Cd>"]
file_pages: [103]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.1.4.3.1.1.1 Code <Cd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 103 to 103.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 103

```text
2.4.2.19.26.2.1.4.3.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the amount type, as published in an external referred amount code set.
Datatype: "ExternalDocumentAmountType1Code" on page 593
2.4.2.19.26.2.1.4.3.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the amount type, in a free-text form.
Datatype: "Max35Text" on page 609
2.4.2.19.26.2.1.4.3.1.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of money for the referred document.
Impacted by: C2 "ActiveOrHistoricCurrency", C19 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 585
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
2.4.2.19.26.2.1.4.3.2  AdjustmentAmountAndReason <AdjstmntAmtAndRsn>
Presence: [0..*]
Definition: Specifies detailed information on the amount and reason of the adjustment.
AdjustmentAmountAndReason <AdjstmntAmtAndRsn> contains the following
DocumentAdjustment1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C19 103
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 104
   Reason <Rsn> [0..1] Text 104
   AdditionalInformation <AddtlInf> [0..1] Text 104
2.4.2.19.26.2.1.4.3.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the document adjustment.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 103 March 2026
```

