---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.4 Message Building Blocks", "58.4.2 PartyActivity <PtyActvty>", "58.4.2.2 Change <Chng>", "58.4.2.2.2 Record <Rcrd>", "58.4.2.2.2.8 Name <Nm>", "58.4.2.2.2.8.1 Old <Od>"]
file_pages: [2279]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 58.4.2.2.2.8.1 Old <Od>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2279 to 2279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2279

```text
Name <Nm> contains the following UpdateLogPartyName1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  2279
     ValidFrom <VldFr> [0..1] Date 2279
     Name <Nm> [1..1] Text 2279
     ShortName <ShrtNm> [0..1] Text 2279
   New <New> [1..1]  2279
     ValidFrom <VldFr> [0..1] Date 2280
     Name <Nm> [1..1] Text 2280
     ShortName <ShrtNm> [0..1] Text 2280
58.4.2.2.2.8.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Old <Od> contains the following PartyName4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2279
   Name <Nm> [1..1] Text 2279
   ShortName <ShrtNm> [0..1] Text 2279
58.4.2.2.2.8.1.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the party name is valid.
Datatype: "ISODate" on page 3319
58.4.2.2.2.8.1.2  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 3328
58.4.2.2.2.8.1.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Specifies the short name of the organisation.
Datatype: "Max35Text" on page 3328
58.4.2.2.2.8.2  New <New>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2279 August 2026
```

