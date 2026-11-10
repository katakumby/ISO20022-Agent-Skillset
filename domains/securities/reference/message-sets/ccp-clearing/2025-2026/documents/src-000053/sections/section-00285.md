---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.1 Account", "12.1.1.2 GenericAccountIdentification1"]
file_pages: [374]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.1.2 GenericAccountIdentification1

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 374 to 374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 374

```text
12.1.1.2  GenericAccountIdentification1
Definition: Information related to a generic account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 374
   SchemeName <SchmeNm> [0..1]  374
{Or     Code <Cd> [1..1] CodeSet 374
Or}     Proprietary <Prtry> [1..1] Text 374
   Issuer <Issr> [0..1] Text 374
12.1.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: Max34Text on page 493
12.1.1.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following AccountSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 374
Or}   Proprietary <Prtry> [1..1] Text 374
12.1.1.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: ExternalAccountIdentification1Code on page 477
12.1.1.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: Max35Text on page 493
12.1.1.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: Max35Text on page 493
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 374
```

