---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.4 Message Building Blocks", "37.4.2 ReportOrError <RptOrErr>", "37.4.2.1 PartyReport <PtyRpt>", "37.4.2.1.2 PartyOrError <PtyOrErr>", "37.4.2.1.2.1 SystemParty <SysPty>", "37.4.2.1.2.1.8 MarketSpecificAttribute <MktSpcfcAttr>"]
file_pages: [2093]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.4.2.1.2.1.8 MarketSpecificAttribute <MktSpcfcAttr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2093 to 2093.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2093

```text
37.4.2.1.2.1.8  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [0..*]
Definition: Additional attributes defined by a central security depositary for a party.
MarketSpecificAttribute <MktSpcfcAttr> contains the following MarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 2093
   Value <Val> [1..1] Text 2093
37.4.2.1.2.1.8.1  Name <Nm>
Presence: [1..1]
Definition: Specifies the name of the market-specific attribute.
Datatype: "Max35Text" on page 3328
37.4.2.1.2.1.8.2  Value <Val>
Presence: [1..1]
Definition: Specifies the value of the market-specific attribute.
Datatype: "Max350Text" on page 3328
37.4.2.1.2.1.9  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Name <Nm> contains the following PartyName4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2093
   Name <Nm> [1..1] Text 2093
   ShortName <ShrtNm> [0..1] Text 2093
37.4.2.1.2.1.9.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the party name is valid.
Datatype: "ISODate" on page 3319
37.4.2.1.2.1.9.2  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 3328
37.4.2.1.2.1.9.3  ShortName <ShrtNm>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2093 August 2026
```

