---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.6 Date Time", "12.1.6.1 DateFormat65Choice", "12.1.6.1.2 DateCode <DtCd>", "12.1.6.1.2.2 Proprietary <Prtry>"]
file_pages: [389]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.6.1.2.2 Proprietary <Prtry>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 389 to 389.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 389

```text
12.1.6.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
12.1.6.2  DateCode3Choice
Definition: Choice between a code or a proprietary code for a date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 389
Or}   Proprietary <Prtry> [1..1] ± C5 389
12.1.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to indicate the date is unknown.
Datatype: DateType1Code on page 476
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
12.1.6.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Impacted by: C5 CoexistenceIssuerSchemeNameRule
Proprietary <Prtry> contains the following elements (see GenericIdentification20 on page 399 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 399
   Issuer <Issr> [1..1] Text 399
   SchemeName <SchmeNm> [0..1] Text 399
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 389
```

