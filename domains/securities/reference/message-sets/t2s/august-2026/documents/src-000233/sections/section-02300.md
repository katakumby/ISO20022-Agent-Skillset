---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.21 Person Identification", "82.1.21.1 Contact14", "82.1.21.1.1 NamePrefix <NmPrfx>"]
file_pages: [3081]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.21.1.1 NamePrefix <NmPrfx>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3081 to 3081.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3081

```text
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
82.1.21.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 3265
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
82.1.21.1.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3081 August 2026
```

