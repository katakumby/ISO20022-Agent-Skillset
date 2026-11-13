---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.20 Tax <Tax>", "4.4.2.14.18.2.20.11 Record <Rcrd>", "4.4.2.14.18.2.20.11.8 TaxAmount <TaxAmt>", "4.4.2.14.18.2.20.11.8.4 Details <Dtls>", "4.4.2.14.18.2.20.11.8.4.2 Amount <Amt>"]
file_pages: [742]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.20.11.8.4.2 Amount <Amt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 742 to 742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 742

```text
Definition: Range of time between a start date and an end date for which the tax report is provided.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 826 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 826
   ToDate <ToDt> [1..1] Date 826
4.4.2.14.18.2.20.11.8.4.2  Amount <Amt>
Presence: [1..1]
Definition: Underlying tax amount related to the specified period.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.4.2.14.18.2.20.11.9  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details of the tax record.
Datatype: "Max140Text" on page 914
4.4.2.14.18.2.21  ReturnInformation <RtrInf>
Presence: [0..1]
Definition: Provides the return information.
Impacted by: C27 "ReturnReasonRule"
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
742 March 2026
```

