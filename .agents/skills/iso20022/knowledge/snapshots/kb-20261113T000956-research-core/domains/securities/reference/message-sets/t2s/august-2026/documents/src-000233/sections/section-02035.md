---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.1 Currency <Ccy>"]
file_pages: [2777]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.1 Currency <Ccy>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2777 to 2777.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2777

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           NumberOfEntries <NbOfNtries> [0..1] Quantity 2827
Constraints
• CounterpartyCSDPresenceRule
Either the CounterpartyCSD or PenaltyPerCounterparty/AccountServicer is informed but not both.
Following Must be True
    /CounterpartyCSD Must be absent
 Or    /PenaltyPerCounterparty[*]/AccountServicer Must be absent
81.4.6.1  Currency <Ccy>
Presence: [1..1]
Definition: Currency of the penalties reported.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
81.4.6.2  Date <Dt>
Presence: [0..1]
Definition: Date where the penalties reported in this block were initially computed.
.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 2914 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
81.4.6.3  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique identification of the party within the system.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2777 August 2026
```

