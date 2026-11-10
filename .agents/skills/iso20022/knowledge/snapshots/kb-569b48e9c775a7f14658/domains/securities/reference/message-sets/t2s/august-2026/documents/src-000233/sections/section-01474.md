---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.4 Message Building Blocks", "37.4.2 ReportOrError <RptOrErr>", "37.4.2.1 PartyReport <PtyRpt>", "37.4.2.1.2 PartyOrError <PtyOrErr>", "37.4.2.1.2.1 SystemParty <SysPty>", "37.4.2.1.2.1.6 Type <Tp>", "37.4.2.1.2.1.6.1 Code <Cd>"]
file_pages: [2092]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.4.2.1.2.1.6.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2092 to 2092.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2092

```text
Type <Tp> contains one of the following SystemPartyType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2092
Or}   Proprietary <Prtry> [1..1] Text 2092
37.4.2.1.2.1.6.1  Code <Cd>
Presence: [1..1]
Definition: System party type, in a coded format.
Datatype: "ExternalSystemPartyType1Code" on page 3246
37.4.2.1.2.1.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System party type, in a proprietary format.
Datatype: "Max35Text" on page 3328
37.4.2.1.2.1.7  TechnicalAddress <TechAdr>
Presence: [0..*]
Definition: Unique technical address to unambiguously identify a party for receiving messages from the
executing system.
TechnicalAddress <TechAdr> contains one of the following TechnicalIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 2092
Or}   TechnicalAddress <TechAdr> [1..1] Text 2092
37.4.2.1.2.1.7.1  BICFI <BICFI>
Presence: [1..1]
Definition: Technical address of the party is defined as a financial institution business identifier code.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 3320
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
37.4.2.1.2.1.7.2  TechnicalAddress <TechAdr>
Presence: [1..1]
Definition: Technical address of the party is defined in a free text format.
Datatype: "Max256Text" on page 3327
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2092 August 2026
```

