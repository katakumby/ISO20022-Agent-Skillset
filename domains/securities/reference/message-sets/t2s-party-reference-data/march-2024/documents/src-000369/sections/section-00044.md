---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 reda.017.001.02 PartyReportV02", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 PartyReport <PtyRpt>", "5.4.2.1.2 PartyOrError <PtyOrErr>", "5.4.2.1.2.1 SystemParty <SysPty>", "5.4.2.1.2.1.4 OpeningDate <OpngDt>"]
file_pages: [54]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 5.4.2.1.2.1.4 OpeningDate <OpngDt>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 54 to 54.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 54

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact14" on page 170 for details)
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
5.4.2.1.2.1.4  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Specifies the opening date of the party.
Datatype: "ISODate" on page 184
5.4.2.1.2.1.5  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Specifies the closing date of the party.
Datatype: "ISODate" on page 184
5.4.2.1.2.1.6  Type <Tp>
Presence: [0..1]
Definition: Specifies the type classification of the party.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.017.001.02 PartyReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
54 March 2024
```

