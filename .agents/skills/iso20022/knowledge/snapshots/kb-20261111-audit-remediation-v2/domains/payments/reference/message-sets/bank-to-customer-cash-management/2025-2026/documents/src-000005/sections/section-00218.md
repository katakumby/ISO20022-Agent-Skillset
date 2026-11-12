---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.14 Charges <Chrgs>", "3.4.2.15.14.2 Record <Rcrd>", "3.4.2.15.14.2.8 Tax <Tax>", "3.4.2.15.14.2.8.3 Amount <Amt>"]
file_pages: [339]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.14.2.8.3 Amount <Amt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 339 to 339.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 339

```text
3.4.2.15.14.2.8.3  Amount <Amt>
Presence: [0..1]
Definition: Amount of money resulting from the calculation of the tax.
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
3.4.2.15.15  TechnicalInputChannel <TechInptChanl>
Presence: [0..1]
Definition: Channel used to technically input the instruction related to the entry.
TechnicalInputChannel <TechInptChanl> contains one of the following
TechnicalInputChannel1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 339
Or}   Proprietary <Prtry> [1..1] Text 339
3.4.2.15.15.1  Code <Cd>
Presence: [1..1]
Definition: Technical input channel, as published in an external technical input channel code list.
Datatype: "ExternalTechnicalInputChannel1Code" on page 900
3.4.2.15.15.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Technical channel used to input the instruction, in a proprietary form.
Datatype: "Max35Text" on page 916
3.4.2.15.16  Interest <Intrst>
Presence: [0..1]
Definition: Provides details of the interest amount included in the entry amount.
Usage: This component is used on entry level in the case of batch or aggregate bookings.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
339 March 2026
```

