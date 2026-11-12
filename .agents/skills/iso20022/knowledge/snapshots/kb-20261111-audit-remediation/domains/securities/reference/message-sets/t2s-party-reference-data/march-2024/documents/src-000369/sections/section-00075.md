---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.4 Message Building Blocks", "8.4.2 PartyActivity <PtyActvty>", "8.4.2.2 Change <Chng>", "8.4.2.2.2 Record <Rcrd>", "8.4.2.2.2.2 ContactDetails <CtctDtls>", "8.4.2.2.2.2.2 New <New>"]
file_pages: [95]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.4.2.2.2.2.2 New <New>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 95 to 95.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 95

```text
Definition: Old value before change
Old <Od> contains the following elements (see "Contact14" on page 170 for details)
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
8.4.2.2.2.2.2  New <New>
Presence: [1..1]
Definition: New value after change
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
95 March 2024
```

