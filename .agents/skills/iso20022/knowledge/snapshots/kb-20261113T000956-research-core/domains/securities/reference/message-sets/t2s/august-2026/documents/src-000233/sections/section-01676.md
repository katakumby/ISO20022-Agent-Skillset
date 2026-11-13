---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.1 AuditTrail <AudtTrl>", "60.4.2.1.1.1.1 Record <Rcrd>", "60.4.2.1.1.1.1.8 Name <Nm>", "60.4.2.1.1.1.1.8.2 New <New>", "60.4.2.1.1.1.1.8.2.1 ValidFrom <VldFr>"]
file_pages: [2324]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.1.1.8.2.1 ValidFrom <VldFr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2324 to 2324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2324

```text
Definition: New value after the update.
New <New> contains the following PartyName4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2324
   Name <Nm> [1..1] Text 2324
   ShortName <ShrtNm> [0..1] Text 2324
60.4.2.1.1.1.1.8.2.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the party name is valid.
Datatype: "ISODate" on page 3319
60.4.2.1.1.1.1.8.2.2  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 3328
60.4.2.1.1.1.1.8.2.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Specifies the short name of the organisation.
Datatype: "Max35Text" on page 3328
60.4.2.1.1.1.1.9  ResidenceType <ResTp>
Presence: [1..1]
Definition: Specifies the type of residence where the party has its permanent home or principal
establishment.
ResidenceType <ResTp> contains the following UpdateLogResidenceType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] CodeSet 2324
   New <New> [1..1] CodeSet 2325
60.4.2.1.1.1.1.9.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Datatype: "ResidenceType1Code" on page 3288
CodeName Name Definition
DMST Domestic Residence is domestic.
FRGN Foreign Residence is foreign.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2324 August 2026
```

