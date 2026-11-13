---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Identification Information", "6.1.14.6 GenericIdentification30", "6.1.14.6.1 Identification <Id>"]
file_pages: [842]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.6.1 Identification <Id>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 842 to 842.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 842

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 842
   Issuer <Issr> [1..1] Text 842
   SchemeName <SchmeNm> [0..1] Text 842
6.1.14.6.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 914
6.1.14.6.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 916
6.1.14.6.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 916
6.1.15 Miscellaneous
6.1.15.1  CorporateActionEventType104Choice
Definition: Choice between formats to express the corporate event type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 843
Or}   Proprietary <Prtry> [1..1] ± 843
Constraints
• EventTypeRule
If Code is present, the code OTHR (Other) must only be used if no other corporate action event code
is appropriate.
If Code is present, the code CHAN (Change) must only be used if no other corporate action event
code is appropriate and only for an event which relates to a change.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
842 March 2026
```

