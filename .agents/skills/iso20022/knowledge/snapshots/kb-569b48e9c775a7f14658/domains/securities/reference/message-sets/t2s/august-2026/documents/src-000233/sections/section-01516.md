---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["41 reda.021.001.01 SecuritiesAccountReportV01", "41.4 Message Building Blocks", "41.4.3 ReportOrError <RptOrErr>", "41.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "41.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "41.4.3.1.2.1 SecuritiesAccount <SctiesAcct>", "41.4.3.1.2.1.7 PartyType <PtyTp>", "41.4.3.1.2.1.7.2 Proprietary <Prtry>"]
file_pages: [2136]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 41.4.3.1.2.1.7.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2136 to 2136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2136

```text
41.4.3.1.2.1.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System party type, in a proprietary format.
Datatype: "Max35Text" on page 3328
41.4.3.1.2.1.8  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [0..*]
Definition: Additional attributes defined by a central security depositary for a securities account.
MarketSpecificAttribute <MktSpcfcAttr> contains the following MarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 2136
   Value <Val> [1..1] Text 2136
41.4.3.1.2.1.8.1  Name <Nm>
Presence: [1..1]
Definition: Specifies the name of the market-specific attribute.
Datatype: "Max35Text" on page 3328
41.4.3.1.2.1.8.2  Value <Val>
Presence: [1..1]
Definition: Specifies the value of the market-specific attribute.
Datatype: "Max350Text" on page 3328
41.4.3.1.2.1.9  Restriction <Rstrctn>
Presence: [0..*]
Definition: Defines the specific processing characteristics for a securities account to ensure
configurability of specific requirements, as prescribed by national legal and regulatory requirements and
practices.
Restriction <Rstrctn> contains the following SystemRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] DateTime 2136
   ValidTo <VldTo> [0..1] DateTime 2137
   Type <Tp> [1..1] Text 2137
41.4.3.1.2.1.9.1  ValidFrom <VldFr>
Presence: [1..1]
Definition: Specifies the date from which the restriction is valid.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities 2136 August 2026
```

