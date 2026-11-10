---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.4 Date Time", "4.1.4.1 DateAndDateTime2Choice", "4.1.4.1.1 Date <Dt>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.4.1.1 Date <Dt>

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
4.1.4.1.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 43
4.1.4.1.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 43
4.1.5 Identification Information
4.1.5.1  GenericIdentification36
Definition: Identification using a proprietary scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 32
   Issuer <Issr> [1..1] Text 32
   SchemeName <SchmeNm> [0..1] Text 32
4.1.5.1.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 46
4.1.5.1.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 46
4.1.5.1.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 46
4.1.6 Miscellaneous
4.1.6.1  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
Message Items Types
Target2-Securities - Limit Utilisation Journal 32 February 2025
```

