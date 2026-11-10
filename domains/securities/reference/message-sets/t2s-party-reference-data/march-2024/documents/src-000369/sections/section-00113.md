---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "10.4.2.1.1.1 AuditTrail <AudtTrl>", "10.4.2.1.1.1.1 Record <Rcrd>", "10.4.2.1.1.1.1.8 Name <Nm>", "10.4.2.1.1.1.1.8.2 New <New>", "10.4.2.1.1.1.1.8.2.1 ValidFrom <VldFr>"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1.1.1.8.2.1 ValidFrom <VldFr>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
Definition: New value after the update.
New <New> contains the following PartyName4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 147
   Name <Nm> [1..1] Text 147
   ShortName <ShrtNm> [0..1] Text 147
10.4.2.1.1.1.1.8.2.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the party name is valid.
Datatype: "ISODate" on page 184
10.4.2.1.1.1.1.8.2.2  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 187
10.4.2.1.1.1.1.8.2.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Specifies the short name of the organisation.
Datatype: "Max35Text" on page 188
10.4.2.1.1.1.1.9  ResidenceType <ResTp>
Presence: [1..1]
Definition: Specifies the type of residence where the party has its permanent home or principal
establishment.
ResidenceType <ResTp> contains the following UpdateLogResidenceType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] CodeSet 147
   New <New> [1..1] CodeSet 148
10.4.2.1.1.1.1.9.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Datatype: "ResidenceType1Code" on page 184
CodeName Name Definition
DMST Domestic Residence is domestic.
FRGN Foreign Residence is foreign.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
147 March 2024
```

