---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.14 Charges <Chrgs>", "2.4.2.15.14.2 Record <Rcrd>", "2.4.2.15.14.2.8 Tax <Tax>", "2.4.2.15.14.2.8.3 Amount <Amt>"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.14.2.8.3 Amount <Amt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
2.4.2.15.14.2.8.3  Amount <Amt>
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
2.4.2.15.15  TechnicalInputChannel <TechInptChanl>
Presence: [0..1]
Definition: Channel used to technically input the instruction related to the entry.
TechnicalInputChannel <TechInptChanl> contains one of the following
TechnicalInputChannel1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 79
Or}   Proprietary <Prtry> [1..1] Text 79
2.4.2.15.15.1  Code <Cd>
Presence: [1..1]
Definition: Technical input channel, as published in an external technical input channel code list.
Datatype: "ExternalTechnicalInputChannel1Code" on page 900
2.4.2.15.15.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Technical channel used to input the instruction, in a proprietary form.
Datatype: "Max35Text" on page 916
2.4.2.15.16  Interest <Intrst>
Presence: [0..1]
Definition: Provides details of the interest amount included in the entry amount.
Usage: This component is used on entry level in the case of batch or aggregate bookings.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
79 March 2026
```

