---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.5 Balance", "6.1.5.3 CashBalance8", "6.1.5.3.2 CreditLine <CdtLine>"]
file_pages: [819]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.5.3.2 CreditLine <CdtLine>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 819 to 819.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 819

```text
Type <Tp> contains the following elements (see "BalanceType13" on page 817 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  817
{Or     Code <Cd> [1..1] CodeSet 817
Or}     Proprietary <Prtry> [1..1] Text 817
   SubType <SubTp> [0..1]  817
{Or     Code <Cd> [1..1] CodeSet 818
Or}     Proprietary <Prtry> [1..1] Text 818
6.1.5.3.2  CreditLine <CdtLine>
Presence: [0..*]
Definition: Set of elements used to provide details on the credit line.
CreditLine <CdtLine> contains the following elements (see "CreditLine3" on page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Included <Incl> [1..1] Indicator 815
   Type <Tp> [0..1]  816
{Or     Code <Cd> [1..1] CodeSet 816
Or}     Proprietary <Prtry> [1..1] Text 816
   Amount <Amt> [0..1] Amount C1, C5 816
   Date <Dt> [0..1] ± 816
6.1.5.3.3  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the cash balance.
Impacted by: C1 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
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
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
819 March 2026
```

