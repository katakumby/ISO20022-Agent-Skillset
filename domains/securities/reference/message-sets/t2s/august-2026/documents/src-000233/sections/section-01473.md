---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.4 Message Building Blocks", "37.4.2 ReportOrError <RptOrErr>", "37.4.2.1 PartyReport <PtyRpt>", "37.4.2.1.2 PartyOrError <PtyOrErr>", "37.4.2.1.2.1 SystemParty <SysPty>", "37.4.2.1.2.1.4 OpeningDate <OpngDt>"]
file_pages: [2091]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.4.2.1.2.1.4 OpeningDate <OpngDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2091 to 2091.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2091

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact14" on page 3080 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 3081
   Name <Nm> [0..1] Text 3081
   PhoneNumber <PhneNb> [0..1] Text 3082
   MobileNumber <MobNb> [0..1] Text 3082
   FaxNumber <FaxNb> [0..1] Text 3082
   URLAddress <URLAdr> [0..1] Text 3082
   EmailAddress <EmailAdr> [0..1] Text 3082
   EmailPurpose <EmailPurp> [0..1] Text 3082
   JobTitle <JobTitl> [0..1] Text 3082
   Responsibility <Rspnsblty> [0..1] Text 3082
   Department <Dept> [0..1] Text 3083
   Other <Othr> [0..*]  3083
     ChannelType <ChanlTp> [1..1] Text 3083
     Identification <Id> [0..1] Text 3083
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 3083
   ValidFrom <VldFr> [0..1] Date 3084
   ValidTo <VldTo> [0..1] Date 3084
37.4.2.1.2.1.4  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Specifies the opening date of the party.
Datatype: "ISODate" on page 3319
37.4.2.1.2.1.5  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Specifies the closing date of the party.
Datatype: "ISODate" on page 3319
37.4.2.1.2.1.6  Type <Tp>
Presence: [0..1]
Definition: Specifies the type classification of the party.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2091 August 2026
```

