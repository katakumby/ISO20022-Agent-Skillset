---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.4 Message Building Blocks", "58.4.2 PartyActivity <PtyActvty>", "58.4.2.2 Change <Chng>", "58.4.2.2.2 Record <Rcrd>", "58.4.2.2.2.2 ContactDetails <CtctDtls>", "58.4.2.2.2.2.2 New <New>"]
file_pages: [2272]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 58.4.2.2.2.2.2 New <New>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2272 to 2272.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2272

```text
Definition: Old value before change
Old <Od> contains the following elements (see "Contact14" on page 3080 for details)
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
58.4.2.2.2.2.2  New <New>
Presence: [1..1]
Definition: New value after change
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2272 August 2026
```

