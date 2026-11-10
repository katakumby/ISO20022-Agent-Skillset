---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.1 AuditTrail <AudtTrl>", "60.4.2.1.1.1.1 Record <Rcrd>", "60.4.2.1.1.1.1.6 TechnicalAddress <TechAdr>", "60.4.2.1.1.1.1.6.2 New <New>", "60.4.2.1.1.1.1.6.2.1 BICFI <BICFI>"]
file_pages: [2321]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.1.1.6.2.1 BICFI <BICFI>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2321 to 2321.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2321

```text
New <New> contains one of the following TechnicalIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 2321
Or}   TechnicalAddress <TechAdr> [1..1] Text 2321
60.4.2.1.1.1.1.6.2.1  BICFI <BICFI>
Presence: [1..1]
Definition: Technical address of the party is defined as a financial institution business identifier code.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 3320
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
60.4.2.1.1.1.1.6.2.2  TechnicalAddress <TechAdr>
Presence: [1..1]
Definition: Technical address of the party is defined in a free text format.
Datatype: "Max256Text" on page 3327
60.4.2.1.1.1.1.7  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [1..1]
Definition: Additional attributes defined by a central security depositary for a party.
MarketSpecificAttribute <MktSpcfcAttr> contains the following
UpdateLogMarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  2321
     Name <Nm> [1..1] Text 2322
     Value <Val> [1..1] Text 2322
   New <New> [1..1]  2322
     Name <Nm> [1..1] Text 2322
     Value <Val> [1..1] Text 2322
60.4.2.1.1.1.1.7.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2321 August 2026
```

