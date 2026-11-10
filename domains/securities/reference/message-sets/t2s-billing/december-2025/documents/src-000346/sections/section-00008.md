---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["2 camt.076.001.01 BillingReportRequestV01", "2.4 Message Building Blocks", "2.4.2 SearchCriteria <SchCrit>", "2.4.2.2 BillingIdentification <BllgId>"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 2.4.2.2 BillingIdentification <BllgId>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 143
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
2.4.2.2  BillingIdentification <BllgId>
Presence: [0..1]
Definition: Identification of the billing report.
Datatype: "Max35Text" on page 153
2.4.2.3  BillingPeriod <BllgPrd>
Presence: [0..1]
Definition: General information for each invoice invoicing request or month end billing event is stored.
BillingPeriod <BllgPrd> contains the following elements (see "DatePeriod2" on page 114 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 115
   ToDate <ToDt> [1..1] Date 115
2.4.2.4  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the referenced party (that is, which has a
contractual responsibility for the billed customer).
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 123
   LEI <LEI> [0..1] IdentifierSet 123
2.4.2.5  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the billed party.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.076.001.01 BillingReportRequestV01
Target2-Securities - Billing 8 December 2025
```

