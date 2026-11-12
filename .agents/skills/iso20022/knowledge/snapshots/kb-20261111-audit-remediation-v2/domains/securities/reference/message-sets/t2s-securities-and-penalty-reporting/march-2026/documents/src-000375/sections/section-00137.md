---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.1 Currency <Ccy>"]
file_pages: [195]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.1 Currency <Ccy>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 195 to 195.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 195

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           NumberOfEntries <NbOfNtries> [0..1] Quantity 245
Constraints
• CounterpartyCSDPresenceRule
Either the CounterpartyCSD or PenaltyPerCounterparty/AccountServicer is informed but not both.
Following Must be True
    /CounterpartyCSD Must be absent
 Or    /PenaltyPerCounterparty[*]/AccountServicer Must be absent
6.4.6.1  Currency <Ccy>
Presence: [1..1]
Definition: Currency of the penalties reported.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 492
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
6.4.6.2  Date <Dt>
Presence: [0..1]
Definition: Date where the penalties reported in this block were initially computed.
.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 321 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
6.4.6.3  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique identification of the party within the system.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 195 March 2026
```

