---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "10.4.2.1.1.1 AuditTrail <AudtTrl>", "10.4.2.1.1.1.1 Record <Rcrd>", "10.4.2.1.1.1.1.3 OpeningDate <OpngDt>"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1.1.1.3 OpeningDate <OpngDt>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
New <New> contains the following elements (see "Contact14" on page 170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 171
   Name <Nm> [0..1] Text 171
   PhoneNumber <PhneNb> [0..1] Text 172
   MobileNumber <MobNb> [0..1] Text 172
   FaxNumber <FaxNb> [0..1] Text 172
   URLAddress <URLAdr> [0..1] Text 172
   EmailAddress <EmailAdr> [0..1] Text 172
   EmailPurpose <EmailPurp> [0..1] Text 172
   JobTitle <JobTitl> [0..1] Text 172
   Responsibility <Rspnsblty> [0..1] Text 172
   Department <Dept> [0..1] Text 173
   Other <Othr> [0..*]  173
     ChannelType <ChanlTp> [1..1] Text 173
     Identification <Id> [0..1] Text 173
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 173
   ValidFrom <VldFr> [0..1] Date 174
   ValidTo <VldTo> [0..1] Date 174
10.4.2.1.1.1.1.3  OpeningDate <OpngDt>
Presence: [1..1]
Definition: Specifies the opening date of the party.
OpeningDate <OpngDt> contains the following UpdateLogDate1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] Date 140
   New <New> [1..1] Date 140
10.4.2.1.1.1.1.3.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Datatype: "ISODate" on page 184
10.4.2.1.1.1.1.3.2  New <New>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
140 March 2024
```

