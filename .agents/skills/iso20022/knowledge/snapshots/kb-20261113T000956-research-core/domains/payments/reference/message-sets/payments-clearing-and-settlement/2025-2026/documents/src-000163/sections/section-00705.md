---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.2 ReferredDocumentAmount <RfrdDocAmt>", "7.4.2.40.30.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>", "7.4.2.40.30.2.2.1.1 Type <Tp>", "7.4.2.40.30.2.2.1.1.1 Code <Cd>"]
file_pages: [960]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.2.1.1.1 Code <Cd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 960 to 960.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 960

```text
7.4.2.40.30.2.2.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the amount type, as published in an external referred amount code set.
Datatype: "ExternalDocumentAmountType1Code" on page 1229
7.4.2.40.30.2.2.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the amount type, in a free-text form.
Datatype: "Max35Text" on page 1246
7.4.2.40.30.2.2.1.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of money for the referred document.
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.4.2.40.30.2.2.2  AdjustmentAmountAndReason <AdjstmntAmtAndRsn>
Presence: [0..*]
Definition: Specifies detailed information on the amount and reason of the adjustment.
AdjustmentAmountAndReason <AdjstmntAmtAndRsn> contains the following
DocumentAdjustment1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C9 960
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 961
   Reason <Rsn> [0..1] Text 961
   AdditionalInformation <AddtlInf> [0..1] Text 961
7.4.2.40.30.2.2.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the document adjustment.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
960 March 2026
```

