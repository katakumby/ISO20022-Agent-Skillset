---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "10.4.2.1.1.1 AuditTrail <AudtTrl>", "10.4.2.1.1.1.1 Record <Rcrd>", "10.4.2.1.1.1.1.6 TechnicalAddress <TechAdr>", "10.4.2.1.1.1.1.6.2 New <New>", "10.4.2.1.1.1.1.6.2.1 BICFI <BICFI>"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1.1.1.6.2.1 BICFI <BICFI>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
New <New> contains one of the following TechnicalIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 144
Or}   TechnicalAddress <TechAdr> [1..1] Text 144
10.4.2.1.1.1.1.6.2.1  BICFI <BICFI>
Presence: [1..1]
Definition: Technical address of the party is defined as a financial institution business identifier code.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 185
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
10.4.2.1.1.1.1.6.2.2  TechnicalAddress <TechAdr>
Presence: [1..1]
Definition: Technical address of the party is defined in a free text format.
Datatype: "Max256Text" on page 187
10.4.2.1.1.1.1.7  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [1..1]
Definition: Additional attributes defined by a central security depositary for a party.
MarketSpecificAttribute <MktSpcfcAttr> contains the following
UpdateLogMarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  144
     Name <Nm> [1..1] Text 145
     Value <Val> [1..1] Text 145
   New <New> [1..1]  145
     Name <Nm> [1..1] Text 145
     Value <Val> [1..1] Text 145
10.4.2.1.1.1.1.7.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
144 March 2024
```

