---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["14 camt.076.001.01 BillingReportRequestV01", "14.4 Message Building Blocks", "14.4.2 SearchCriteria <SchCrit>", "14.4.2.2 BillingIdentification <BllgId>"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 14.4.2.2 BillingIdentification <BllgId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
14.4.2.2  BillingIdentification <BllgId>
Presence: [0..1]
Definition: Identification of the billing report.
Datatype: "Max35Text" on page 3328
14.4.2.3  BillingPeriod <BllgPrd>
Presence: [0..1]
Definition: General information for each invoice invoicing request or month end billing event is stored.
BillingPeriod <BllgPrd> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
14.4.2.4  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the referenced party (that is, which has a
contractual responsibility for the billed customer).
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
14.4.2.5  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the billed party.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.076.001.01 BillingReportRequestV01
Target2-Securities 237 August 2026
```

