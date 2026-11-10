---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.53 UnderlyingRisk <UndrlygRsk>", "28.4.2.1.1.2.53.2 Identification <Id>"]
file_pages: [1183]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.53.2 Identification <Id>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1183 to 1183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1183

```text
28.4.2.1.1.2.53.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1183
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1183
28.4.2.1.1.2.53.2.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
28.4.2.1.1.2.53.2.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
28.4.2.1.1.2.53.3  Purpose <Purp>
Presence: [0..1]
Definition: Purpose of the organisation, eg, charity.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1183 August 2026
```

