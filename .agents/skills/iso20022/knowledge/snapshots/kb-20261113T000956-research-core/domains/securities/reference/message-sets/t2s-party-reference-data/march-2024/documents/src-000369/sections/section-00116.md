---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "10.4.2.1.1.1 AuditTrail <AudtTrl>", "10.4.2.1.1.1.1 Record <Rcrd>", "10.4.2.1.1.1.1.10 LockStatus <LckSts>", "10.4.2.1.1.1.1.10.2 New <New>", "10.4.2.1.1.1.1.10.2.3 LockReason <LckRsn>"]
file_pages: [150]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1.1.1.10.2.3 LockReason <LckRsn>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 150 to 150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 150

```text
10.4.2.1.1.1.1.10.2.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 188
10.4.2.1.1.1.1.11  Restriction <Rstrctn>
Presence: [1..1]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
Restriction <Rstrctn> contains the following UpdateLogRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  150
     RestrictionType <RstrctnTp> [1..1]  151
{Or       Code <Cd> [1..1] Text 151
Or}       Proprietary <Prtry> [1..1] ± 151
     ValidFrom <VldFr> [1..1] DateTime 151
     ValidUntil <VldUntil> [0..1] DateTime 151
   New <New> [1..1]  151
     RestrictionType <RstrctnTp> [1..1]  152
{Or       Code <Cd> [1..1] Text 152
Or}       Proprietary <Prtry> [1..1] ± 152
     ValidFrom <VldFr> [1..1] DateTime 152
     ValidUntil <VldUntil> [0..1] DateTime 153
10.4.2.1.1.1.1.11.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Old <Od> contains the following Restriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictionType <RstrctnTp> [1..1]  151
{Or     Code <Cd> [1..1] Text 151
Or}     Proprietary <Prtry> [1..1] ± 151
   ValidFrom <VldFr> [1..1] DateTime 151
   ValidUntil <VldUntil> [0..1] DateTime 151
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
150 March 2024
```

